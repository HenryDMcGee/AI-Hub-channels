import re, random, json, sys
random.seed(2027)
s = open('real.html', encoding='utf-8').read()
i0 = s.index('<script>'); head, script = s[:i0], s[i0:]

# ---- 1. professors -> fictional names (same mapping everywhere in the data) ----
profs = set(re.findall(r'p:"([^"]+?)(?: \(\'\d\d\))?"', script))
rm_block = script[script.index('const RM={'):script.index('};', script.index('const RM={'))]
profs |= set(re.findall(r'^"([^"]+)":\[', rm_block, re.M))
f24_block = script[script.index('const F24='):script.index('\n', script.index('const F24='))]
profs |= set(re.findall(r'\["[^"]*", "([^"]+)", ', f24_block))
profs = sorted(p for p in profs if p not in ('—', '-', '') and re.search(r'[A-Za-z]', p))
SUR = """Abbott Alvarez Archer Bell Blake Bowen Brandt Caldwell Carver Castillo Chandler Cho Collier Cortez Dalton Delgado Doyle Duarte
Ellison Emery Farrow Fenwick Fischer Fleming Foster Gallo Garner Gentry Gill Hale Hardin Harlow Hayes Hollis Hoyt Ibarra Ingram Iverson
Jarvis Juarez Kane Keller Kendrick Kirby Lam Larkin Lowe Lund Maddox Marlow Mercer Molina Monroe Nakamura Navarro Nolan Novak Oakley
Ortega Osei Park Pace Pruitt Quinlan Rao Reyes Rhodes Rios Royce Salas Sato Sawyer Shah Sinclair Sloan Soto Stroud Sutton Tate Thorne
Tran Upton Vance Varga Voss Wade Walsh Wells Whitaker Winslow Wolfe Xu Yates Yoon Zeller Zhou Abe Bishop Crane Drake Ellis Frost Grant
Hart Irwin Jensen Knox Lyle Mays Nash Orr Penn Quill Ross Stone Tull Vail Webb York Zane Ames Boyd Cruz Dunn Eaton Ford Gage Hunt""".split()
random.shuffle(SUR)
INIT = 'ABCDEFGHJKLMNPRSTW'
fake = {}
for k, p in enumerate(profs):
    fake[p] = f"{SUR[k % len(SUR)]}{'' if k < len(SUR) else '-' + SUR[(k*7) % len(SUR)]}, {random.choice(INIT)}"
def swap_names(text):
    for real, f in sorted(fake.items(), key=lambda kv: -len(kv[0])):
        text = re.sub(r'"' + re.escape(real) + r'((?: \(\'\d\d\))?)"', lambda m: '"' + f + m.group(1) + '"', text)
    return text
script = swap_names(script)

# ---- 2. ratings -> made up, no profile links ----
def fake_rm(m):
    name = m.group(1)
    r = None if random.random() < .12 else round(random.uniform(2.4, 5.0), 1)
    n = 0 if r is None else random.randint(2, 70)
    return f'"{name}":[{"null" if r is None else r},{n},""],'
a = script.index('const RM={'); b = script.index('};', a)
script = script[:a] + re.sub(r'^"([^"]+)":\[[^\]]*\],?', fake_rm, script[a:b], flags=re.M) + script[b:]
script = script.replace(
  "function rmpCell(p){",
  "function rmpCell(p){ /* demo: made-up ratings, no profile links */\n  const m0=RM[normP(p)]; if(m0){const tier=m0[0]==null?'':m0[0]>=4?' hi':m0[0]>=3?' mid':' lo'; return `<span class=\"rmp${tier}\" title=\"Sample rating (demo)\">★ ${m0[0]==null?'—':m0[0].toFixed(1)} <span class=\"n\">(${m0[1]})</span></span>`;}", 1)

# ---- 3. bid history -> jittered numbers ----
def jit(v):
    if v in ('null',): return v
    x = float(v)
    if x == 0: return '0'
    y = x * random.uniform(.55, 1.45)
    return str(round(y, 1)) if x < 20 else str(int(round(y / 5) * 5))
a = script.index('const ST={'); b = script.index('};', a)
script = script[:a] + re.sub(r'\[([\d.]+|null),([\d.]+|null),([\d.]+|null)\]',
    lambda m: '[' + ','.join(jit(g) for g in m.groups()) + ']', script[a:b]) + script[b:]
a = script.index('const F24='); b = script.index('\n', a)
script = script[:a] + re.sub(r'(", )(\d+(?:\.\d+)?), (\d+(?:\.\d+)?)\]',
    lambda m: m.group(1) + jit(m.group(2)) + ', ' + jit(m.group(3)) + ']', script[a:b]) + script[b:]

# ---- 4. nothing persists: an in-memory store stands in for localStorage and the shared db ----
seed = {}
script = script.replace('<script>', '<script>\n/* DEMO: in-memory storage, seeded with a sample plan; nothing is saved */\nconst DEMO_STORE=(()=>{const m=new Map(Object.entries(__SEED__));return {getItem:k=>m.has(k)?m.get(k):null,setItem:(k,v)=>m.set(k,String(v)),removeItem:k=>m.delete(k)};})();', 1)
script = re.sub(r'\blocalStorage\b', 'DEMO_STORE', script)
script = script.replace("const db=await window.claude?.use?.('db');", "const db=null; /* demo: no shared db */")
assert "window.claude" not in script

# sample plan: a handful of Spring '27 courses with points, plus notes
def u_of(code, title_part=None, sess=None):
    for m in re.finditer(r'\{u:"([^"]+)",d:"[^"]*",c:"([^"]+)",t:"([^"]+)",[^}]*?se:"([^"]*)"', script):
        u, c, t, se = m.groups()
        if c == code and (title_part is None or title_part in t) and (sess is None or se == sess) and not u.startswith(('F24', 'AB')):
            return u
    raise SystemExit('no section for ' + code)
plan = [(u_of('FIN 286', sess='S1'), 120, 'SP27'), (u_of('BGS 380E'), 60, 'SP27'), (u_of('FIN 394.5'), 250, 'SP27'),
        (u_of('ACC 380K.7'), 300, 'SP27'), (u_of('I B 385E', 'Italy'), 200, 'SP27')]
seed['plan2027'] = json.dumps([p[0] for p in plan])
seed['plan2027pts'] = json.dumps({p[0]: p[1] for p in plan})
seed['plan2027sems'] = json.dumps({p[0]: p[2] for p in plan})
seed['plan2027notes'] = "Sample notes (demo):\n- Valuation I in Spring 1 clears near 0 in round 1, so bid low.\n- Fintech is the one to protect, so put the most points there.\n- Backup for Global Connections: the S Korea section."
script = script.replace('__SEED__', json.dumps(seed), 1)

# ---- 5. page chrome: demo bar, sources note ----
head = head.replace('<title>McCombs Spring 2027</title>', '<title>McCombs Course Planner · demo</title>')
bar = ('<div style="position:sticky;top:0;z-index:50;display:flex;align-items:center;gap:10px;margin:-10px -16px 8px;padding:7px 16px;'
       'background:#16213a;color:#ffe9a8;font:600 12.5px/1.4 system-ui,sans-serif" role="note"><i style="width:8px;height:8px;border-radius:50%;background:#f2b33d;flex:none"></i>'
       'DEMO <span style="opacity:.8;font-weight:500">· sample data: professor names, ratings, bid results and the plan are made up, and nothing is saved</span></div>')
head = re.sub(r'(<body[^>]*>)', r'\1' + bar, head, count=1)
head = head.replace('Items you supplied are marked "from Henry"; web sources link out;',
                    'Items Henry supplied are marked "from Henry"; web sources link out. In this demo the professor names, ratings and bid numbers are made up;')
for real, f in fake.items():
    sur = real.split(',')[0].strip()
    if sur in ('Hall',) or sur == real and ' ' not in real: continue
    head = re.sub(r'\b' + re.escape(sur) + r'\b', f.split(',')[0], head)
out = head + script
assert out.count('ratemyprofessors.com/professor') == 0, out.count('ratemyprofessors.com/professor')
open(sys.argv[1], 'w', encoding='utf-8').write(out)
print('profs', len(profs))
