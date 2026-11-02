#!/usr/bin/env python3
"""Builds index.html for AI-HUB from the approved mockup art. Not shipped: run it, commit the output."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from content import ITEMS, DEMOS, VERSION

A = json.load(open(os.path.join(ROOT, '.build-art.json')))
ART, STARS, MOON, CLOCK_DEFS = A['art'], A['stars'], A['moon'], A['clock_defs']
STARS_HTML_UNUSED = "<i style=\"left:73.0%;top:72.4%;width:2.4px;height:2.4px;--lo:0.21;animation-duration:3.7s;animation-delay:-4.3s\"></i><i style=\"left:82.5%;top:61.6%;width:3.6px;height:3.6px;--lo:0.28;animation-duration:4.2s;animation-delay:-0.9s\"></i><i style=\"left:23.3%;top:12.2%;width:2.8px;height:2.8px;--lo:0.16;animation-duration:4.9s;animation-delay:-3.5s\"></i><i style=\"left:64.0%;top:58.6%;width:3.6px;height:3.6px;--lo:0.34;animation-duration:4.6s;animation-delay:-3.3s\"></i><i style=\"left:85.2%;top:8.8%;width:1.6px;height:1.6px;--lo:0.33;animation-duration:2.3s;animation-delay:-4.4s\"></i><i style=\"left:74.8%;top:42.5%;width:2.4px;height:2.4px;--lo:0.22;animation-duration:4.2s;animation-delay:-1.0s\"></i><i style=\"left:47.7%;top:64.6%;width:1.6px;height:1.6px;--lo:0.23;animation-duration:4.4s;animation-delay:-2.3s\"></i><i style=\"left:88.8%;top:11.4%;width:3.6px;height:3.6px;--lo:0.3;animation-duration:3.0s;animation-delay:-3.8s\"></i><i style=\"left:5.3%;top:9.6%;width:2.8px;height:2.8px;--lo:0.4;animation-duration:4.7s;animation-delay:-2.0s\"></i><i style=\"left:62.4%;top:9.2%;width:1.6px;height:1.6px;--lo:0.21;animation-duration:5.0s;animation-delay:-0.0s\"></i><i style=\"left:9.0%;top:60.9%;width:2.4px;height:2.4px;--lo:0.17;animation-duration:5.4s;animation-delay:-2.0s\"></i><i style=\"left:32.3%;top:35.2%;width:2px;height:2px;--lo:0.44;animation-duration:2.5s;animation-delay:-1.7s\"></i><i style=\"left:19.5%;top:17.9%;width:2px;height:2px;--lo:0.29;animation-duration:4.5s;animation-delay:-0.1s\"></i><i style=\"left:78.5%;top:23.4%;width:3.6px;height:3.6px;--lo:0.21;animation-duration:4.0s;animation-delay:-2.2s\"></i><i style=\"left:21.6%;top:54.4%;width:3.6px;height:3.6px;--lo:0.45;animation-duration:3.5s;animation-delay:-2.0s\"></i><i style=\"left:0.6%;top:35.2%;width:2.8px;height:2.8px;--lo:0.21;animation-duration:3.2s;animation-delay:-4.4s\"></i><i style=\"left:63.7%;top:13.5%;width:1.6px;height:1.6px;--lo:0.23;animation-duration:5.5s;animation-delay:-1.1s\"></i><i style=\"left:98.2%;top:42.8%;width:2px;height:2px;--lo:0.21;animation-duration:3.5s;animation-delay:-0.4s\"></i><i style=\"left:39.5%;top:2.6%;width:2.8px;height:2.8px;--lo:0.19;animation-duration:3.4s;animation-delay:-3.1s\"></i><i style=\"left:94.5%;top:62.6%;width:2.8px;height:2.8px;--lo:0.34;animation-duration:2.6s;animation-delay:-1.9s\"></i><i style=\"left:50.3%;top:29.9%;width:2.8px;height:2.8px;--lo:0.37;animation-duration:3.0s;animation-delay:-0.9s\"></i><i style=\"left:89.2%;top:25.9%;width:3.6px;height:3.6px;--lo:0.33;animation-duration:5.3s;animation-delay:-4.4s\"></i><i style=\"left:68.0%;top:6.8%;width:1.6px;height:1.6px;--lo:0.23;animation-duration:2.6s;animation-delay:-2.6s\"></i><i style=\"left:63.3%;top:33.6%;width:2.4px;height:2.4px;--lo:0.24;animation-duration:4.9s;animation-delay:-3.0s\"></i><i style=\"left:28.7%;top:9.5%;width:2px;height:2px;--lo:0.41;animation-duration:3.0s;animation-delay:-2.8s\"></i><i style=\"left:98.9%;top:10.1%;width:2px;height:2px;--lo:0.37;animation-duration:2.9s;animation-delay:-4.6s\"></i><i style=\"left:11.6%;top:35.1%;width:2.4px;height:2.4px;--lo:0.2;animation-duration:3.7s;animation-delay:-0.3s\"></i><i style=\"left:59.6%;top:68.6%;width:2.8px;height:2.8px;--lo:0.19;animation-duration:5.4s;animation-delay:-0.5s\"></i><i style=\"left:72.7%;top:43.0%;width:3.6px;height:3.6px;--lo:0.43;animation-duration:4.6s;animation-delay:-2.6s\"></i><i style=\"left:95.0%;top:5.1%;width:1.6px;height:1.6px;--lo:0.24;animation-duration:3.8s;animation-delay:-1.8s\"></i><i style=\"left:5.9%;top:3.4%;width:2.8px;height:2.8px;--lo:0.37;animation-duration:4.3s;animation-delay:-2.4s\"></i><i style=\"left:51.6%;top:18.1%;width:1.6px;height:1.6px;--lo:0.37;animation-duration:2.4s;animation-delay:-2.7s\"></i><i style=\"left:21.3%;top:44.4%;width:2px;height:2px;--lo:0.17;animation-duration:2.5s;animation-delay:-2.4s\"></i><i style=\"left:67.3%;top:4.5%;width:2.4px;height:2.4px;--lo:0.26;animation-duration:4.1s;animation-delay:-3.1s\"></i><i style=\"left:93.8%;top:2.2%;width:2.8px;height:2.8px;--lo:0.18;animation-duration:2.4s;animation-delay:-0.5s\"></i><i style=\"left:41.7%;top:54.0%;width:3.6px;height:3.6px;--lo:0.36;animation-duration:3.3s;animation-delay:-4.7s\"></i><i style=\"left:73.8%;top:57.1%;width:2.4px;height:2.4px;--lo:0.38;animation-duration:5.0s;animation-delay:-0.4s\"></i><i style=\"left:5.4%;top:40.4%;width:2.8px;height:2.8px;--lo:0.44;animation-duration:2.5s;animation-delay:-0.1s\"></i><i style=\"left:18.7%;top:64.4%;width:2.8px;height:2.8px;--lo:0.42;animation-duration:4.4s;animation-delay:-2.4s\"></i><i style=\"left:59.5%;top:39.2%;width:2px;height:2px;--lo:0.2;animation-duration:4.4s;animation-delay:-1.0s\"></i><i style=\"left:55.4%;top:57.2%;width:2.4px;height:2.4px;--lo:0.35;animation-duration:5.1s;animation-delay:-1.6s\"></i><i style=\"left:32.3%;top:55.9%;width:2px;height:2px;--lo:0.32;animation-duration:5.1s;animation-delay:-1.9s\"></i><i style=\"left:51.2%;top:27.5%;width:2px;height:2px;--lo:0.42;animation-duration:2.6s;animation-delay:-1.8s\"></i><i style=\"left:7.1%;top:8.9%;width:2px;height:2px;--lo:0.29;animation-duration:4.9s;animation-delay:-0.6s\"></i><i style=\"left:34.8%;top:53.6%;width:2.4px;height:2.4px;--lo:0.24;animation-duration:4.3s;animation-delay:-2.5s\"></i><i style=\"left:73.0%;top:41.8%;width:1.6px;height:1.6px;--lo:0.33;animation-duration:4.9s;animation-delay:-1.4s\"></i><i style=\"left:45.5%;top:73.8%;width:2px;height:2px;--lo:0.16;animation-duration:3.2s;animation-delay:-4.0s\"></i><i style=\"left:22.3%;top:52.5%;width:2.4px;height:2.4px;--lo:0.23;animation-duration:2.8s;animation-delay:-3.8s\"></i><i style=\"left:23.1%;top:6.8%;width:3.6px;height:3.6px;--lo:0.31;animation-duration:2.6s;animation-delay:-0.5s\"></i><i style=\"left:59.6%;top:10.6%;width:3.6px;height:3.6px;--lo:0.23;animation-duration:2.9s;animation-delay:-4.1s\"></i><i style=\"left:2.3%;top:61.1%;width:2.8px;height:2.8px;--lo:0.23;animation-duration:4.6s;animation-delay:-0.9s\"></i><i style=\"left:55.9%;top:69.8%;width:3.6px;height:3.6px;--lo:0.45;animation-duration:5.3s;animation-delay:-2.5s\"></i><i style=\"left:26.1%;top:51.0%;width:3.6px;height:3.6px;--lo:0.43;animation-duration:5.2s;animation-delay:-0.4s\"></i><i style=\"left:62.7%;top:17.4%;width:2.4px;height:2.4px;--lo:0.42;animation-duration:3.7s;animation-delay:-3.1s\"></i><i style=\"left:60.9%;top:71.1%;width:2.8px;height:2.8px;--lo:0.4;animation-duration:4.4s;animation-delay:-2.5s\"></i><i style=\"left:55.5%;top:60.0%;width:2px;height:2px;--lo:0.37;animation-duration:4.3s;animation-delay:-1.0s\"></i><i style=\"left:20.3%;top:28.0%;width:2px;height:2px;--lo:0.44;animation-duration:5.2s;animation-delay:-4.9s\"></i><i style=\"left:86.5%;top:41.8%;width:2px;height:2px;--lo:0.25;animation-duration:5.2s;animation-delay:-4.3s\"></i><i style=\"left:13.8%;top:5.5%;width:2.4px;height:2.4px;--lo:0.23;animation-duration:3.3s;animation-delay:-2.1s\"></i><i style=\"left:5.2%;top:28.6%;width:1.6px;height:1.6px;--lo:0.31;animation-duration:3.6s;animation-delay:-0.2s\"></i><i style=\"left:23.0%;top:60.9%;width:2px;height:2px;--lo:0.31;animation-duration:5.5s;animation-delay:-4.5s\"></i><i style=\"left:71.0%;top:63.8%;width:2.8px;height:2.8px;--lo:0.22;animation-duration:5.3s;animation-delay:-0.4s\"></i><i style=\"left:84.8%;top:72.2%;width:2px;height:2px;--lo:0.2;animation-duration:4.9s;animation-delay:-2.8s\"></i><i style=\"left:82.9%;top:72.4%;width:2px;height:2px;--lo:0.4;animation-duration:3.2s;animation-delay:-1.9s\"></i><i style=\"left:98.1%;top:27.4%;width:2px;height:2px;--lo:0.31;animation-duration:5.0s;animation-delay:-4.8s\"></i><i style=\"left:92.3%;top:64.4%;width:2px;height:2px;--lo:0.15;animation-duration:3.6s;animation-delay:-0.6s\"></i><i style=\"left:60.9%;top:4.2%;width:2.8px;height:2.8px;--lo:0.27;animation-duration:5.4s;animation-delay:-2.6s\"></i><i style=\"left:90.6%;top:16.2%;width:2.4px;height:2.4px;--lo:0.43;animation-duration:2.5s;animation-delay:-0.8s\"></i><i style=\"left:74.0%;top:53.6%;width:2.4px;height:2.4px;--lo:0.19;animation-duration:3.1s;animation-delay:-2.4s\"></i><i style=\"left:70.0%;top:61.6%;width:2.8px;height:2.8px;--lo:0.34;animation-duration:3.2s;animation-delay:-1.0s\"></i><b style=\"left:44.7%;top:19.0%;animation-duration:5.6s;animation-delay:-5.9s\"></b><b style=\"left:8.8%;top:27.2%;animation-duration:4.0s;animation-delay:-0.1s\"></b><b style=\"left:48.5%;top:43.6%;animation-duration:5.7s;animation-delay:-1.5s\"></b><b style=\"left:82.9%;top:15.9%;animation-duration:5.0s;animation-delay:-3.5s\"></b><b style=\"left:84.8%;top:34.5%;animation-duration:5.7s;animation-delay:-4.2s\"></b><b style=\"left:73.0%;top:5.4%;animation-duration:4.6s;animation-delay:-2.5s\"></b><b style=\"left:87.8%;top:22.9%;animation-duration:5.1s;animation-delay:-5.2s\"></b>"

CSS = r"""
:root{--bg:#0B1120;--bg2:#121C33;--frame:#15213A;--rim:#2F4369;--rim-lit:#33476F;--ink:#E6EEF9;--quiet:#8FA3C4;--dim:#5B6E92;--cyan:#5FD4F0;--cyan-lit:#7FE3FF;--amber:#FFD36E;--violet:#B48BFF;--teal:#2BD4A6;color-scheme:dark}
*{box-sizing:border-box}
[hidden]{display:none!important}
html,body{margin:0;min-height:100%;background:var(--bg);color:var(--ink);font-family:'Nunito',system-ui,-apple-system,sans-serif;-webkit-font-smoothing:antialiased;overflow-x:hidden}
body{position:relative;min-height:100svh;display:flex;flex-direction:column}
a{color:var(--cyan-lit)}
button{font:inherit;color:inherit}
:focus-visible{outline:3px solid var(--cyan);outline-offset:3px;border-radius:6px}
.sky{position:fixed;inset:0;z-index:0;pointer-events:none;background:linear-gradient(180deg,#0B1120 0%,#0E1729 55%,#121C33 100%)}
.sky .lines{position:absolute;inset:0;background:repeating-linear-gradient(180deg,rgba(255,255,255,.028) 0,rgba(255,255,255,.028) 1px,transparent 1px,transparent 4px)}
.sky .vig{position:absolute;inset:0;background:radial-gradient(ellipse at 50% 40%,transparent 45%,rgba(4,8,18,.7) 100%)}
.sky .stars{position:absolute;inset:0;width:100%;height:100%}
.twinkles{position:absolute;inset:0;pointer-events:none}
.tw{position:absolute;width:14px;height:14px;margin:-7px 0 0 -7px;background:#fff;clip-path:polygon(50% 0,60% 40%,100% 50%,60% 60%,50% 100%,40% 60%,0 50%,40% 40%);opacity:.3;will-change:opacity,transform;animation:twinkle 3s ease-in-out infinite}
.tw.dot{width:3px;height:3px;margin:-1.5px 0 0 -1.5px;clip-path:none;border-radius:50%;background:#EAF4FF}
@keyframes twinkle{0%,100%{opacity:.2;transform:scale(.7)}50%{opacity:1;transform:scale(1.05)}}
@media (prefers-reduced-motion:reduce){.tw{animation:none;opacity:.5}}}
.sky .moon{position:absolute;right:4%;top:24px;width:120px;height:120px;opacity:.9}
@media (max-width:760px){.sky .moon{width:80px;height:80px;top:14px}}

/* ---------- grid ---------- */
.hub{position:relative;z-index:1;flex:1;display:flex;flex-direction:column;align-items:center;padding:56px 56px 24px}
.track-wrap{width:100%;max-width:1012px;overflow:hidden}
.track{display:flex;transition:transform .45s cubic-bezier(.22,.61,.36,1)}
.page{flex:0 0 100%;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:28px;padding:4px}
@media (max-width:1100px){.page{grid-template-columns:repeat(3,minmax(0,1fr));gap:20px}}
@media (max-width:760px){.hub{padding:48px 16px 16px}.page{grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}}
.slot{position:relative;aspect-ratio:232/140;--d:0s;contain:layout paint style}
.chan{position:relative;display:block;width:100%;height:100%;border-radius:18px;background:var(--frame);border:2px solid var(--rim);box-shadow:inset 0 1px 0 rgba(255,255,255,.06),0 10px 24px rgba(0,0,0,.45);overflow:hidden;text-decoration:none;color:var(--ink);cursor:pointer;padding:0;text-align:left;transition:transform .18s ease,border-color .18s ease,box-shadow .18s ease;-webkit-tap-highlight-color:transparent;user-select:none;-webkit-user-select:none;touch-action:manipulation}
.chan:hover,.chan:focus-visible{border-color:var(--cyan);transform:translateY(-2px);box-shadow:inset 0 1px 0 rgba(255,255,255,.08),0 0 0 3px rgba(95,212,240,.22),0 14px 30px rgba(0,0,0,.5);outline:none}
.chan .art{position:absolute;inset:0;width:100%;height:100%;display:block;transform:translateZ(0)}
.chan .name{position:absolute;left:0;right:0;bottom:0;padding:8px 14px 10px;font-weight:800;font-size:15px;letter-spacing:.2px;text-shadow:0 1px 2px rgba(0,0,0,.6);background:linear-gradient(180deg,rgba(11,17,32,0) 0%,rgba(11,17,32,.78) 100%);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.chan .sub{display:block;font-weight:600;font-size:11.5px;color:#9FB3D3;margin-top:1px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
@media (max-width:760px){.chan .name{font-size:12.5px;padding:6px 10px 8px}.chan .sub{font-size:10px}}
.chan.waiting{opacity:.72;cursor:default}
.empty{width:100%;height:100%;border-radius:18px;background:#0F182B;border:2px dashed #223254;box-shadow:inset 0 0 40px rgba(20,34,62,.6)}
.booting .slot{opacity:0;transform:translateY(10px)}
.booted .slot{animation:rise .5s cubic-bezier(.22,.61,.36,1) var(--d) both}
@keyframes rise{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:none}}

/* page tabs + dots */
.tab{position:absolute;top:50%;transform:translateY(-50%);width:40px;height:112px;background:#16213A;border:2px solid var(--rim-lit);color:#C9D8F2;display:flex;align-items:center;justify-content:center;cursor:pointer;padding:0;z-index:2}
.tab svg{width:20px;height:20px}
.tab-l{left:0;border-left:0;border-radius:0 20px 20px 0}.tab-r{right:0;border-right:0;border-radius:20px 0 0 20px}
.tab[disabled]{opacity:.3;cursor:default}
.tab:not([disabled]):hover{border-color:var(--cyan);color:var(--cyan-lit)}
@media (max-width:760px){.tab{width:28px;height:80px}}
.dots{display:flex;justify-content:center;gap:10px;margin-top:18px;min-height:10px}
.dots i{width:10px;height:10px;border-radius:50%;background:var(--rim);display:block;transition:background .2s}
.dots i.on{background:var(--cyan-lit)}

/* ---------- edit mode ---------- */
.editing .chan{animation:jiggle .32s ease-in-out infinite alternate;cursor:grab}
.editing .slot:nth-child(2n) .chan{animation-delay:-.16s}
.editing .slot:nth-child(3n) .chan{animation-duration:.36s}
@keyframes jiggle{from{transform:rotate(-1.2deg)}to{transform:rotate(1.2deg)}}
.del{position:absolute;left:-8px;top:-8px;width:28px;height:28px;border-radius:50%;background:#1C2A47;border:2px solid #C9D8F2;color:#fff;display:none;align-items:center;justify-content:center;cursor:pointer;padding:0;z-index:3;box-shadow:0 4px 10px rgba(0,0,0,.5)}
.del svg{width:10px;height:10px;stroke:#fff;stroke-width:2;fill:none}
.editing .del{display:flex}
.editing .track{touch-action:none}
.slot.dragging .chan{opacity:.25;animation:none}
.slot.target .chan,.slot.target .empty{border-color:var(--cyan);box-shadow:0 0 0 4px rgba(95,212,240,.25)}
.ghost{position:fixed;z-index:50;pointer-events:none;border-radius:18px;overflow:hidden;box-shadow:0 24px 50px rgba(0,0,0,.6);transform:scale(1.06);opacity:.95}
.editbar{position:fixed;left:50%;bottom:28px;transform:translateX(-50%);z-index:40;display:flex;align-items:center;gap:12px;padding:10px 12px 10px 18px;border-radius:999px;background:#16213A;border:2px solid var(--rim-lit);box-shadow:0 14px 40px rgba(0,0,0,.6);font-weight:700;font-size:13.5px;color:#C9D8F2}
.editbar button{height:38px;padding:0 16px;border-radius:19px;border:2px solid var(--rim-lit);background:#1C2A47;color:#C9D8F2;font-weight:800;cursor:pointer}
.editbar .done{background:var(--cyan);border-color:var(--cyan);color:#07131F}
@media (max-width:760px){.editbar{bottom:14px;font-size:12px;gap:8px}.editbar span{display:none}}

/* ---------- clock ---------- */
.clock-block{position:relative;z-index:1;display:flex;flex-direction:column;align-items:center;gap:6px;padding:12px 16px 36px}
.clock{width:300px;height:80px}
@media (max-width:760px){.clock{width:220px;height:59px}}
.clock .colon{animation:blink 1s steps(1) infinite}
@keyframes blink{50%{opacity:.25}}
.date{font-weight:700;font-size:26px;color:#C9D8F2;letter-spacing:.5px}
@media (max-width:760px){.date{font-size:20px}}
.mute{position:absolute;right:max(16px,calc(50% - 215px));top:28px;width:44px;height:44px;border-radius:50%;background:#16213A;border:2px solid var(--rim-lit);color:#C9D8F2;display:flex;align-items:center;justify-content:center;cursor:pointer;padding:0}
.mute svg{width:22px;height:22px;fill:none;stroke:currentColor;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.mute[aria-pressed="false"] .on{display:none}.mute[aria-pressed="true"] .off{display:none}
.mute:hover{border-color:var(--cyan);color:var(--cyan-lit)}

/* ---------- overlays ---------- */
.scrim{position:fixed;inset:0;z-index:30;background:rgba(5,9,18,.82);opacity:0;transition:opacity .25s}
.scrim.show{opacity:1}
.dialog{position:fixed;z-index:31;left:50%;top:50%;transform:translate(-50%,-50%);width:min(900px,calc(100vw - 32px));max-height:calc(100svh - 32px);overflow:auto;border-radius:24px;background:linear-gradient(180deg,#16223D 0%,#101A30 100%);border:2px solid #3C568A;box-shadow:0 0 0 4px rgba(95,212,240,.12),0 30px 80px rgba(0,0,0,.7);padding:26px 28px 28px;display:flex;flex-direction:column;gap:20px}
.dialog .head{display:flex;align-items:center;justify-content:space-between;gap:16px}
.dialog h2{margin:0;font-size:28px;font-weight:800;letter-spacing:-.5px;color:#EEF4FF}
.dialog .hint{font-size:13.5px;font-weight:600;color:var(--quiet)}
.close{width:48px;height:48px;border-radius:50%;background:#1C2A47;border:2px solid var(--rim-lit);color:#C9D8F2;display:flex;align-items:center;justify-content:center;cursor:pointer;padding:0;flex-shrink:0}
.close svg{width:22px;height:22px;fill:none;stroke:currentColor;stroke-width:2.5;stroke-linecap:round}
.close:hover{border-color:var(--cyan);color:var(--cyan-lit)}
.kids{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px}
@media (max-width:760px){.kids{grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}.dialog{padding:18px;gap:14px}.dialog h2{font-size:22px}}
.kids .slot{aspect-ratio:232/150}
.dialog .foot{font-size:12.5px;font-weight:600;color:#6E82A8;text-align:center}

/* zoom */
.zoom{width:min(800px,calc(100vw - 32px));padding:0;overflow:hidden;gap:0;border-color:var(--cyan);box-shadow:0 0 0 6px rgba(95,212,240,.14),0 40px 100px rgba(0,0,0,.75)}
.zoom .big{position:relative;width:100%;aspect-ratio:800/330;background:#0B1120;overflow:hidden}
.zoom .big svg{position:absolute;left:50%;top:50%;width:100%;height:auto;transform:translate(-50%,-50%) scale(1.72);transform-origin:center}
.zoom .body{display:flex;align-items:center;justify-content:space-between;gap:24px;padding:26px 36px 30px}
@media (max-width:760px){.zoom .body{flex-direction:column;align-items:stretch;padding:18px}}
.zoom h2{font-size:30px}
.zoom p{margin:6px 0 0;font-size:15px;font-weight:600;color:#9FB3D3;max-width:440px}
.zoom .url{display:block;margin-top:6px;font-size:12.5px;font-weight:700;color:var(--cyan);letter-spacing:.4px}
.btns{display:flex;gap:14px;flex-shrink:0}
.btn{display:inline-flex;align-items:center;justify-content:center;min-width:120px;height:56px;padding:0 22px;border-radius:28px;background:#1C2A47;border:2px solid var(--rim-lit);color:#C9D8F2;font-weight:800;font-size:17px;text-decoration:none;cursor:pointer}
.btn.primary{background:var(--cyan);border-color:var(--cyan);color:#07131F;box-shadow:0 0 24px rgba(95,212,240,.45)}
.btn:hover{border-color:var(--cyan)}
.chan.lifting{transition:transform .35s cubic-bezier(.22,.61,.36,1),opacity .35s;z-index:35;position:relative}

/* alert */
.alert{position:fixed;z-index:60;left:50%;top:50%;transform:translate(-50%,-50%);width:min(380px,calc(100vw - 32px));border-radius:20px;background:#16223D;border:2px solid #3C568A;box-shadow:0 30px 80px rgba(0,0,0,.7);padding:22px 22px 18px;text-align:center}
.alert h3{margin:0 0 6px;font-size:18px;font-weight:800}
.alert p{margin:0 0 16px;font-size:14px;font-weight:600;color:var(--quiet)}
.alert .btns{justify-content:center}
.alert .btn{min-width:110px;height:46px;font-size:15px}
.alert .danger{background:#FF7A8A;border-color:#FF7A8A;color:#1A0A0D}

/* boot */
.boot{position:fixed;inset:0;z-index:70;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:28px;background:radial-gradient(ellipse at 50% 40%,#101A30 0%,#070C18 70%);cursor:pointer;transition:opacity .6s ease}
.boot.out{opacity:0;pointer-events:none}
.boot .crescent{width:140px;height:140px;animation:breathe 3.4s ease-in-out infinite}
@keyframes breathe{0%,100%{transform:scale(1);filter:drop-shadow(0 0 18px rgba(159,217,255,.25))}50%{transform:scale(1.06);filter:drop-shadow(0 0 40px rgba(159,217,255,.55))}}
.boot h1{margin:0;font-size:28px;font-weight:800;letter-spacing:-.3px;color:#EEF4FF}
.boot p{margin:0;font-size:14px;font-weight:700;letter-spacing:2.5px;color:var(--quiet);animation:blink 2.2s ease-in-out infinite}

/* demo */
.ribbon{position:fixed;left:20px;top:16px;z-index:5;display:flex;align-items:center;gap:10px;padding:8px 14px 8px 10px;border-radius:999px;background:#16213A;border:2px solid var(--amber);color:#FFE9A8;font-weight:800;font-size:13px;letter-spacing:1.2px}
.ribbon i{width:10px;height:10px;border-radius:50%;background:var(--amber);display:block;box-shadow:0 0 12px var(--amber)}
@media (max-width:760px){.ribbon{font-size:11px;top:10px;left:12px}}
.demo{width:min(1000px,calc(100vw - 32px));height:min(620px,calc(100svh - 32px));padding:0;gap:0;overflow:hidden;flex-direction:row;box-shadow:0 0 0 4px rgba(255,211,110,.14),0 30px 80px rgba(0,0,0,.7)}
.rail{width:290px;flex-shrink:0;padding:26px 20px;background:rgba(7,12,24,.55);border-right:1px solid var(--rim);display:flex;flex-direction:column;gap:16px;overflow:auto}
.rail .tag{font-size:11.5px;font-weight:800;letter-spacing:1.5px;color:var(--amber)}
.rail h2{font-size:24px;margin-top:4px}
.steps{display:flex;flex-direction:column;gap:6px}
.step{display:flex;align-items:center;gap:12px;width:100%;text-align:left;padding:10px 12px;border-radius:12px;cursor:pointer;background:transparent;border:1px solid transparent}
.step.on{border-color:var(--cyan);background:rgba(95,212,240,.12)}
.step b{width:24px;height:24px;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-size:12px;font-weight:800;flex-shrink:0;background:#1C2A47;color:#C9D8F2}
.step.done b{background:var(--rim)}.step.on b{background:var(--cyan);color:#07131F}
.step span{display:flex;flex-direction:column;min-width:0}
.step .k{font-size:10.5px;font-weight:800;letter-spacing:1px;color:var(--quiet)}
.step .t{font-size:13.5px;font-weight:700;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.pane{flex:1;min-width:0;display:flex;flex-direction:column;gap:14px;padding:22px 26px 22px;overflow:auto}
.pane .kind{font-size:12px;font-weight:800;letter-spacing:1.5px;color:var(--cyan-lit)}
.shot{position:relative;border-radius:14px;overflow:hidden;background:#f6f5f1;border:1px solid var(--rim);aspect-ratio:690/372;flex-shrink:0}
.shot img{position:absolute;left:0;top:0;width:100%;height:auto;display:block}
.shot .fade{position:absolute;left:0;right:0;bottom:0;height:36px;background:linear-gradient(180deg,rgba(246,245,241,0),rgba(246,245,241,.9))}
.shot .mark{position:absolute;border-radius:6px;border:2px solid var(--cyan);box-shadow:0 0 0 4px rgba(95,212,240,.22),0 0 26px rgba(95,212,240,.55)}
.shot .badge{position:absolute;width:24px;height:24px;border-radius:50%;background:var(--amber);color:#1A1200;font-size:12px;font-weight:800;display:flex;align-items:center;justify-content:center;box-shadow:0 0 12px rgba(255,211,110,.7)}
.pane h3{margin:0;font-size:24px;font-weight:800;line-height:1.15;letter-spacing:-.3px;color:#EEF4FF}
.pane p{margin:0;font-size:15px;line-height:1.55;font-weight:600;color:#B8C7E2}
.pane .nav{margin-top:auto;display:flex;align-items:center;justify-content:space-between;gap:14px;flex-wrap:wrap}
.pane .nav a{font-size:13.5px;font-weight:800;text-decoration:none}
.pane .btn{min-width:100px;height:46px;font-size:15px}
.pdots{display:flex;gap:6px}.pdots i{display:block;width:10px;height:10px;border-radius:5px;background:var(--rim);transition:width .2s}.pdots i.on{width:28px;background:var(--cyan)}
@media (max-width:760px){.demo{flex-direction:column;height:calc(100svh - 24px)}.rail{width:100%;flex-direction:row;align-items:flex-start;gap:12px;padding:14px;border-right:0;border-bottom:1px solid var(--rim)}.rail h2{font-size:18px}.steps{flex-direction:row;overflow:auto;gap:4px}.step{padding:6px 8px}.step span{display:none}.pane{padding:14px}.pane h3{font-size:19px}.pane p{font-size:14px}}
@media (prefers-reduced-motion:reduce){*,*::before,*::after{animation-duration:.001ms!important;animation-iteration-count:1!important;transition-duration:.001ms!important}}
"""

HTML = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>AI-HUB</title>
<meta name="description" content="Henry McGee's app hub: a night channel grid linking every project.">
<meta name="theme-color" content="#0B1120">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Nunito:wght@600;700;800&family=Kalam:wght@700&display=swap">
<style>__CSS__</style>
</head>
<body class="booting">
<div class="sky" aria-hidden="true">
  <div class="lines"></div>
  <canvas class="stars" id="stars"></canvas>
  <div class="vig"></div>
  <svg class="moon" viewBox="0 0 160 160">__MOON__</svg>
</div>

<div class="boot" id="boot" role="button" tabindex="0" aria-label="Tap to begin">
  <svg class="crescent" viewBox="0 0 160 160" aria-hidden="true">__MOON__</svg>
  <h1>AI-HUB</h1>
  <p>TAP TO BEGIN</p>
</div>

<div class="ribbon" id="ribbon" hidden><i></i>DEMO · TAP ANY CHANNEL FOR A WALKTHROUGH</div>

<main class="hub" aria-label="Channels">
  <button class="tab tab-l" id="prev" aria-label="Previous page"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 5l-7 7 7 7"/></svg></button>
  <div class="track-wrap"><div class="track" id="track"></div></div>
  <button class="tab tab-r" id="next" aria-label="Next page"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 5l7 7-7 7"/></svg></button>
  <div class="dots" id="dots" aria-hidden="true"></div>
</main>

<div class="editbar" id="editbar" hidden><span>Drag to move · tap ⓧ to remove</span><button id="reset" type="button">Reset Layout</button><button id="done" class="done" type="button">Done</button></div>

<footer class="clock-block">
  <svg class="clock" id="clock" viewBox="0 0 300 80" role="img" aria-label=""><defs>__CLOCK_DEFS__</defs><g id="digits"></g><text id="ampm" x="266" y="76" font-family="Nunito, system-ui, sans-serif" font-weight="800" font-size="16" fill="#9FB3D3"></text></svg>
  <button class="mute" id="mute" type="button" aria-pressed="true" aria-label="Music on, tap to mute">
    <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 9v6h4l5 4V5L8 9z"/><path class="on" d="M16 9a4 4 0 0 1 0 6M18.5 6.5a7.5 7.5 0 0 1 0 11"/><path class="off" d="M17 9l4 6M21 9l-4 6"/></svg>
  </button>
  <div class="date" id="date"></div>
</footer>

<div class="scrim" id="scrim" hidden></div>

<div class="dialog" id="folder" role="dialog" aria-modal="true" aria-labelledby="folder-title" hidden>
  <div class="head"><div><h2 id="folder-title"></h2><div class="hint" id="folder-hint"></div></div><button class="close" type="button" data-close aria-label="Close"><svg viewBox="0 0 24 24"><path d="M6 6l12 12M18 6L6 18"/></svg></button></div>
  <div class="kids" id="kids"></div>
  <div class="foot">Esc or tap outside to close</div>
</div>

<div class="dialog zoom" id="zoom" role="dialog" aria-modal="true" aria-labelledby="zoom-title" hidden>
  <div class="big" id="zoom-art"></div>
  <div class="body">
    <div><h2 id="zoom-title"></h2><p id="zoom-desc"></p><span class="url" id="zoom-url"></span></div>
    <div class="btns"><button class="btn" type="button" data-close>Back</button><a class="btn primary" id="zoom-start" href="#" target="_blank" rel="noopener">Start</a></div>
  </div>
</div>

<div class="dialog demo" id="demo" role="dialog" aria-modal="true" aria-labelledby="demo-title" hidden>
  <div class="rail"><div><div class="tag" id="demo-tag"></div><h2 id="demo-title"></h2></div><div class="steps" id="steps"></div></div>
  <div class="pane">
    <div class="head"><div class="kind" id="demo-kind"></div><button class="close" type="button" data-close aria-label="Close the walkthrough" style="width:40px;height:40px"><svg viewBox="0 0 24 24"><path d="M6 6l12 12M18 6L6 18"/></svg></button></div>
    <div class="shot" id="demo-shot" hidden><img id="demo-img" decoding="async" alt=""><div class="fade"></div><div class="mark" id="demo-mark" hidden></div><span class="badge" id="demo-badge" hidden></span></div>
    <h3 id="demo-h"></h3>
    <p id="demo-p"></p>
    <div class="nav">
      <a id="demo-open" href="#" target="_blank" rel="noopener">Open the real app ↗</a>
      <div style="display:flex;align-items:center;gap:12px"><div class="pdots" id="pdots" aria-hidden="true"></div><button class="btn" type="button" id="demo-back">Back</button><button class="btn primary" type="button" id="demo-next">Next</button></div>
    </div>
  </div>
</div>

<div class="alert" id="alert" role="alertdialog" aria-modal="true" aria-labelledby="alert-h" hidden>
  <h3 id="alert-h">Remove channel?</h3>
  <p id="alert-p">You can bring it back anytime with Reset Layout.</p>
  <div class="btns"><button class="btn" type="button" id="alert-cancel">Cancel</button><button class="btn danger" type="button" id="alert-ok">Remove</button></div>
</div>

<script>
(function () {
'use strict';
var VERSION = '__VERSION__';
var ITEMS = __ITEMS__;
var ART = __ART__;
var DEMOS = __DEMOS__;
var DEFAULT = ['crm','watch','jobs','site','jira','github','starr','mars','planner'];
var KEY = 'aihub-layout-v1', MKEY = 'aihub-music', SLOTS = 12;

/* ---------- mode: a local file or localhost is the real hub, anything hosted is the demo ---------- */
function isLocal() { return location.protocol === 'file:' || /^(localhost|127\.0\.0\.1|\[::1\])$/.test(location.hostname); }
var q = new URLSearchParams(location.search);
var MODE = (!isLocal() || q.get('mode') === 'demo') ? 'demo' : 'real';
console.log('AI-HUB v' + VERSION + ' · ' + MODE + ' mode · ' + (isLocal() ? 'local origin' : location.hostname));
if (MODE === 'demo') document.getElementById('ribbon').hidden = false;

var $ = function (s, r) { return (r || document).querySelector(s); };
function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
function art(id) { if (ART[id + '_layers']) return ART[id + '_layers']; return '<svg class="art" viewBox="0 0 232 140" preserveAspectRatio="xMidYMid slice" aria-hidden="true">' + (ART[id] || '') + '</svg>'; }

/* ---------- layout: an ordered list of ids (null = empty slot), padded to whole pages ---------- */
var layout;
function pad(a) { var n = Math.max(SLOTS, Math.ceil(a.length / SLOTS) * SLOTS); while (a.length < n) a.push(null); return a; }
function trim(a) { var b = a.slice(); while (b.length > SLOTS && b.slice(-SLOTS).every(function (x) { return !x; })) b.length -= SLOTS; return pad(b); }
function load() {
  try {
    var s = JSON.parse(localStorage.getItem(KEY));
    if (s && Array.isArray(s.order)) {
      var ok = function (id) { return !id || Object.prototype.hasOwnProperty.call(ITEMS, id); };
      var a = s.order.filter(ok), known = Array.isArray(s.known) ? s.known : [];
      Object.keys(ITEMS).forEach(function (id) { if (known.indexOf(id) < 0 && a.indexOf(id) < 0) { var i = a.indexOf(null); if (i < 0) a.push(id); else a[i] = id; } });
      return trim(a);
    }
  } catch (e) {}
  return pad(DEFAULT.slice());
}
function save() { try { localStorage.setItem(KEY, JSON.stringify({ order: trim(layout), known: Object.keys(ITEMS), v: VERSION })); } catch (e) {} }
layout = load();

/* ---------- render ---------- */
var track = $('#track'), dots = $('#dots'), page = 0;
function slotHTML(id, i) {
  var d = (-Math.random() * 0.28).toFixed(2) + 's';
  if (!id) return '<div class="slot" data-i="' + i + '" style="--d:' + d + '"><div class="empty"></div></div>';
  var it = ITEMS[id], body;
  if (it.kind === 'waiting') body = '<div class="chan waiting" role="note" aria-label="' + esc(it.aria || it.name) + '">' + art(id) + '<span class="name">' + esc(it.name) + '<span class="sub">' + esc(it.sub || '') + '</span></span></div>';
  else body = '<a class="chan" href="' + esc(it.href || '#') + '" target="_blank" rel="noopener" data-id="' + id + '" draggable="false"' + (it.kind === 'folder' ? ' aria-haspopup="dialog"' : '') + '>' + art(id) + '<span class="name">' + esc(it.name) + '<span class="sub">' + esc(it.sub || '') + '</span></span></a>';
  return '<div class="slot" data-i="' + i + '" data-id="' + id + '" style="--d:' + d + '">' + body + '<button class="del" type="button" data-del="' + id + '" aria-label="Remove ' + esc(it.name) + '"><svg viewBox="0 0 10 10"><path d="M2 2l6 6M8 2L2 8"/></svg></button></div>';
}
function render() {
  var pages = layout.length / SLOTS, html = '';
  for (var p = 0; p < pages; p++) { html += '<div class="page" data-page="' + p + '">'; for (var i = 0; i < SLOTS; i++) html += slotHTML(layout[p * SLOTS + i], p * SLOTS + i); html += '</div>'; }
  track.innerHTML = html;
  Array.prototype.forEach.call(track.querySelectorAll('svg'), function (sv) { if (sv.pauseAnimations) sv.pauseAnimations(); });
  dots.innerHTML = pages > 1 ? Array.apply(null, Array(pages)).map(function (_, i) { return '<i' + (i === page ? ' class="on"' : '') + '></i>'; }).join('') : '';
  goPage(Math.min(page, pages - 1), true);
}
function goPage(p, silent) {
  var pages = layout.length / SLOTS; page = Math.max(0, Math.min(p, pages - 1));
  syncAnim();
  track.style.transform = 'translateX(' + (-page * 100) + '%)';
  Array.prototype.forEach.call(dots.children, function (d, i) { d.classList.toggle('on', i === page); });
  $('#prev').disabled = page === 0; $('#next').disabled = page >= pages - 1 && !editing;
  if (!silent) tick();
}
$('#prev').addEventListener('click', function () { goPage(page - 1); });
$('#next').addEventListener('click', function () { if (page >= layout.length / SLOTS - 1 && editing) { layout = pad(layout.concat([null])); render(); } goPage(page + 1); });
render();

/* swipe between pages on touch */
(function () {
  var x0 = null, y0 = null;
  track.addEventListener('touchstart', function (e) { if (editing) return; x0 = e.touches[0].clientX; y0 = e.touches[0].clientY; }, { passive: true });
  track.addEventListener('touchend', function (e) { if (x0 === null || editing) return; var dx = e.changedTouches[0].clientX - x0, dy = e.changedTouches[0].clientY - y0; x0 = null; if (Math.abs(dx) > 60 && Math.abs(dx) > Math.abs(dy) * 1.5) goPage(page + (dx < 0 ? 1 : -1)); }, { passive: true });
})();

/* channel art is SVG with SMIL animations. Left alone, every animated tile repaints 60 times a second,
   which is what made the hub lag. Instead all SVG clocks are paused and one ticker advances only the
   art that can be seen (visible page, or the open dialog) at ANIM_FPS. Nothing runs behind a dialog,
   on a hidden tab, or for people who asked for reduced motion. */
var ANIM_FPS = 15;
var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
var animSet = [], animT0 = performance.now();
function syncAnim() {
  animSet = [];
  if (reduce) return;
  var root = openEl || track.children[page];
  if (!root) return;
  Array.prototype.forEach.call(root.querySelectorAll('svg'), function (sv) {
    if (sv.pauseAnimations && sv.querySelector('animate,animateTransform,animateMotion,set')) animSet.push(sv);
  });
}
function stepAnim() {
  if (document.hidden || !animSet.length) return;
  var t = (performance.now() - animT0) / 1000;
  for (var i = 0; i < animSet.length; i++) { var sv = animSet[i]; if (!sv.animationsPaused()) sv.pauseAnimations(); sv.setCurrentTime(t); }
}
setInterval(stepAnim, Math.round(1000 / ANIM_FPS));
document.addEventListener('visibilitychange', syncAnim);
syncAnim();

/* ---------- dialogs ---------- */
var scrim = $('#scrim'), openEl = null, opener = null;
function openDialog(el, from) {
  closeDialog(true);
  opener = from || document.activeElement; openEl = el;
  scrim.hidden = false; requestAnimationFrame(function () { scrim.classList.add('show'); });
  el.hidden = false;
  var f = el.querySelector('button, a[href], [tabindex="0"]'); if (f) f.focus();
  syncAnim();
}
function closeDialog(quiet) {
  if (!openEl) return;
  openEl.hidden = true; openEl = null;
  scrim.classList.remove('show'); scrim.hidden = true;
  if (opener && document.body.contains(opener)) opener.focus();
  opener = null;
  syncAnim();
  if (!quiet) tick();
}
scrim.addEventListener('click', function () { closeDialog(); });
document.addEventListener('click', function (e) { if (e.target.closest('[data-close]')) closeDialog(); });
document.addEventListener('keydown', function (e) {
  if (e.key === 'Escape') { if (!$('#alert').hidden) closeAlert(); else if (openEl) closeDialog(); else if (editing) exitEdit(); }
  if (openEl === $('#demo')) { if (e.key === 'ArrowRight') demoGo(demoStep + 1); if (e.key === 'ArrowLeft') demoGo(demoStep - 1); }
});

function openFolder(id, from) {
  var it = ITEMS[id];
  $('#folder-title').textContent = it.name;
  $('#folder-hint').textContent = it.kids.length + (it.kidNoun ? ' ' + it.kidNoun : ' items') + ' · pick one to open it in a new tab';
  $('#kids').innerHTML = it.kids.map(function (k) {
    if (k.waiting) return '<div class="slot"><div class="chan waiting" role="note" aria-label="' + esc(k.aria || k.name) + '">' + art(k.art) + '<span class="name">' + esc(k.name) + '<span class="sub">' + esc(k.sub || '') + '</span></span></div></div>';
    return '<div class="slot"><a class="chan" href="' + esc(k.href) + '" target="_blank" rel="noopener">' + art(k.art) + '<span class="name">' + esc(k.name) + '<span class="sub">' + esc(k.sub || '') + '</span></span></a></div>';
  }).join('');
  openDialog($('#folder'), from); blip();
}

function openZoom(id, from) {
  var it = ITEMS[id];
  $('#zoom-art').innerHTML = art(id);
  $('#zoom-title').textContent = it.name; $('#zoom-desc').textContent = it.desc || ''; $('#zoom-url').textContent = (it.href || '').replace(/^https?:\/\//, '');
  $('#zoom-start').href = it.href;
  openDialog($('#zoom'), from); blip();
}

/* channel taps */
track.addEventListener('click', function (e) {
  var a = e.target.closest('.chan[data-id]'); if (!a) return;
  if (editing || suppressClick) { e.preventDefault(); return; }
  var id = a.dataset.id, it = ITEMS[id];
  if (e.metaKey || e.ctrlKey || e.button === 1) return;          // let the browser open the link directly
  e.preventDefault();
  if (MODE === 'demo') { openDemo(id, a); return; }
  if (it.kind === 'folder') openFolder(id, a); else openZoom(id, a);
});
track.addEventListener('mouseover', function (e) { var a = e.target.closest('.chan'); if (a && a !== hovered) { hovered = a; tick(); } });
track.addEventListener('mouseout', function (e) { if (!e.relatedTarget || !e.relatedTarget.closest('.chan')) hovered = null; });
var hovered = null;

/* ---------- edit mode ---------- */
var editing = false, suppressClick = false, pressTimer = null, drag = null;
function enterEdit() { if (editing || MODE === 'demo') return; editing = true; document.body.classList.add('editing'); $('#editbar').hidden = false; closeDialog(true); goPage(page, true); }
function exitEdit() { if (!editing) return; editing = false; document.body.classList.remove('editing'); $('#editbar').hidden = true; layout = trim(layout); save(); render(); }
$('#done').addEventListener('click', exitEdit);
$('#reset').addEventListener('click', function () { layout = pad(DEFAULT.slice()); page = 0; save(); render(); exitEdit(); });

track.addEventListener('pointerdown', function (e) {
  var slot = e.target.closest('.slot'); if (!slot || e.target.closest('.del')) return;
  if (e.pointerType === 'mouse' && e.button !== 0) return;
  if (!editing) {
    var last = e;
    var cancel = function () { clearTimeout(pressTimer); pressTimer = null; window.removeEventListener('pointerup', cancel); window.removeEventListener('pointercancel', cancel); window.removeEventListener('pointermove', move); };
    var move = function (ev) { last = ev; if (Math.abs(ev.clientX - e.clientX) > 8 || Math.abs(ev.clientY - e.clientY) > 8) cancel(); };
    // press and hold, then keep holding to drag in the same gesture
    pressTimer = setTimeout(function () { cancel(); enterEdit(); suppressClick = true; if (slot.dataset.id) { var s2 = track.querySelector('.slot[data-i="' + slot.dataset.i + '"]'); if (s2) startDrag(s2, last); } }, 500);
    window.addEventListener('pointerup', cancel); window.addEventListener('pointercancel', cancel); window.addEventListener('pointermove', move);
    return;
  }
  if (!slot.dataset.id) return;
  e.preventDefault();
  startDrag(slot, e);
});
window.addEventListener('pointerup', function () { setTimeout(function () { suppressClick = false; }, 0); });

function startDrag(slot, e) {
  var r = slot.getBoundingClientRect();
  var ghost = slot.querySelector('.chan').cloneNode(true); ghost.className = 'chan ghost'; ghost.style.width = r.width + 'px'; ghost.style.height = r.height + 'px';
  document.body.appendChild(ghost);
  drag = { slot: slot, from: +slot.dataset.i, ghost: ghost, dx: e.clientX - r.left, dy: e.clientY - r.top, target: null, edge: null, edgeTimer: null };
  slot.classList.add('dragging'); moveDrag(e);
  window.addEventListener('pointermove', moveDrag); window.addEventListener('pointerup', endDrag); window.addEventListener('pointercancel', endDrag);
}
function moveDrag(e) {
  if (!drag) return;
  drag.ghost.style.left = (e.clientX - drag.dx) + 'px'; drag.ghost.style.top = (e.clientY - drag.dy) + 'px';
  var el = document.elementFromPoint(e.clientX, e.clientY), slot = el && el.closest('.slot');
  if (drag.target && drag.target !== slot) drag.target.classList.remove('target');
  drag.target = (slot && slot !== drag.slot && slot.closest('#track')) ? slot : null;
  if (drag.target) drag.target.classList.add('target');
  var wrap = $('.track-wrap').getBoundingClientRect(), edge = e.clientX < wrap.left + 36 ? 'l' : e.clientX > wrap.right - 36 ? 'r' : null;
  if (edge !== drag.edge) { clearTimeout(drag.edgeTimer); drag.edge = edge; if (edge) drag.edgeTimer = setTimeout(function () { if (edge === 'r' && page >= layout.length / SLOTS - 1) { layout = pad(layout.concat([null])); render(); markDragging(); } goPage(page + (edge === 'r' ? 1 : -1)); drag.edge = null; }, 900); }
}
function markDragging() { var s = track.querySelector('.slot[data-i="' + drag.from + '"]'); if (s) { drag.slot = s; s.classList.add('dragging'); } }
function endDrag() {
  window.removeEventListener('pointermove', moveDrag); window.removeEventListener('pointerup', endDrag); window.removeEventListener('pointercancel', endDrag);
  if (!drag) return;
  clearTimeout(drag.edgeTimer); drag.ghost.remove(); drag.slot.classList.remove('dragging');
  if (drag.target) {
    var to = +drag.target.dataset.i, a = layout[drag.from]; layout[drag.from] = layout[to]; layout[to] = a;
    save(); render(); latch();
  }
  drag = null; suppressClick = true;
}

/* remove with an in-page confirm */
var pending = null;
track.addEventListener('click', function (e) { var b = e.target.closest('.del'); if (!b) return; e.preventDefault(); pending = b.dataset.del; $('#alert-h').textContent = 'Remove ' + ITEMS[pending].name + '?'; $('#alert').hidden = false; $('#alert-ok').focus(); });
function closeAlert() { $('#alert').hidden = true; pending = null; }
$('#alert-cancel').addEventListener('click', closeAlert);
$('#alert-ok').addEventListener('click', function () { if (pending) { var i = layout.indexOf(pending); if (i >= 0) layout[i] = null; save(); render(); } closeAlert(); });

/* ---------- stars: the field is painted once on a canvas; only a few twinkles animate, as
   CSS opacity on their own layers (compositor work, not main-thread paint) ---------- */
(function () {
  var cv = $('#stars'), cx = cv.getContext('2d'), stars = [], W = 0, H = 0, seed = 11, sky = cv.parentNode;
  function rnd() { seed = (seed * 16807) % 2147483647; return (seed - 1) / 2147483646; }
  for (var i = 0; i < 70; i++) stars.push({ x: rnd(), y: rnd() * 0.74, r: [0.8, 1, 1, 1.2, 1.4, 1.8][Math.floor(rnd() * 6)], a: 0.3 + rnd() * 0.6 });
  function size() { var d = Math.min(window.devicePixelRatio || 1, 1.5); W = cv.clientWidth; H = cv.clientHeight; cv.width = W * d; cv.height = H * d; cx.setTransform(d, 0, 0, d, 0, 0); }
  function draw() {
    cx.clearRect(0, 0, W, H); cx.fillStyle = '#EAF4FF';
    for (var i = 0; i < stars.length; i++) { var st = stars[i]; cx.globalAlpha = st.a; cx.beginPath(); cx.arc(st.x * W, st.y * H, st.r, 0, 6.2832); cx.fill(); }
    cx.globalAlpha = 1;
  }
  size(); draw(); window.addEventListener('resize', function () { size(); draw(); });
  var tw = '';
  for (var j = 0; j < 7; j++) tw += '<i class="tw" style="left:' + (rnd() * 100).toFixed(1) + '%;top:' + (rnd() * 70).toFixed(1) + '%;animation-duration:' + (2.2 + rnd() * 2.4).toFixed(1) + 's;animation-delay:-' + (rnd() * 4).toFixed(1) + 's"></i>';
  for (var k = 0; k < 10; k++) tw += '<i class="tw dot" style="left:' + (rnd() * 100).toFixed(1) + '%;top:' + (rnd() * 74).toFixed(1) + '%;animation-duration:' + (1.6 + rnd() * 2).toFixed(1) + 's;animation-delay:-' + (rnd() * 3).toFixed(1) + 's"></i>';
  var wrap = document.createElement('div'); wrap.className = 'twinkles'; wrap.innerHTML = tw; sky.insertBefore(wrap, cv.nextSibling);
})();

/* ---------- clock: seven-segment digits ---------- */
var SEG = { 0: 'abcdef', 1: 'bc', 2: 'abdeg', 3: 'abcdg', 4: 'bcfg', 5: 'acdfg', 6: 'acdefg', 7: 'abc', 8: 'abcdefg', 9: 'abcdfg' };
function digit(x, d) {
  var on = SEG[d] || '', s = '<g transform="translate(' + x + ',2)">';
  'abcdefg'.split('').forEach(function (k) { s += '<use href="#s' + k + '" fill="' + (on.indexOf(k) >= 0 ? '#7FE3FF' : '#1C2E4F') + '"/>'; });
  return s + '</g>';
}
function clock() {
  var now = new Date(), h = now.getHours(), m = now.getMinutes(), pm = h >= 12; h = h % 12 || 12;
  var hh = String(h), mm = (m < 10 ? '0' : '') + m, s = '', x = hh.length === 2 ? 0 : 40;
  if (hh.length === 2) s += digit(0, +hh[0]);
  s += digit(hh.length === 2 ? 52 : 40, +hh[hh.length - 1]);
  s += '<g class="colon" fill="#7FE3FF"><rect x="' + (hh.length === 2 ? 108 : 96) + '" y="22" width="8" height="8" rx="2"/><rect x="' + (hh.length === 2 ? 108 : 96) + '" y="50" width="8" height="8" rx="2"/></g>';
  var mx = hh.length === 2 ? 128 : 116;
  s += digit(mx, +mm[0]) + digit(mx + 56, +mm[1]);
  $('#digits').innerHTML = s; $('#ampm').textContent = pm ? 'PM' : 'AM'; $('#ampm').setAttribute('x', mx + 116);
  $('#clock').setAttribute('aria-label', now.toLocaleTimeString([], { hour: 'numeric', minute: '2-digit' }));
  $('#date').textContent = now.toLocaleDateString([], { weekday: 'short' }) + ' ' + (now.getMonth() + 1) + '/' + now.getDate();
}
clock(); setInterval(clock, 30000);

/* ---------- sound: everything synthesized, nothing downloaded ---------- */
var ac = null, master = null, unlocked = false, silent = null;
function audio() {
  if (ac) return ac;
  var AC = window.AudioContext || window.webkitAudioContext; if (!AC) return null;
  ac = new AC(); master = ac.createGain(); master.gain.value = 0.9; master.connect(ac.destination); return ac;
}
function unlockAudio() {
  var c = audio(); if (!c) return;
  if (c.state === 'suspended') c.resume();
  if (!silent) {                        // iPhone Safari: a playing media element moves the page to playback audio, so the ringer switch no longer mutes Web Audio
    silent = document.createElement('audio'); silent.loop = true; silent.setAttribute('playsinline', '');
    silent.src = 'data:audio/wav;base64,UklGRiQAAABXQVZFZm10IBAAAAABAAEAQB8AAIA+AAACABAAZGF0YQAAAAA=';
    silent.volume = 0.01; silent.play().catch(function () {});
  }
  unlocked = true;
}
function env(g, t, a, d, peak) { g.gain.setValueAtTime(0.0001, t); g.gain.exponentialRampToValueAtTime(peak, t + a); g.gain.exponentialRampToValueAtTime(0.0001, t + a + d); }
function tone(freq, type, t, a, d, peak, dest) { var o = ac.createOscillator(), g = ac.createGain(); o.type = type; o.frequency.setValueAtTime(freq, t); env(g, t, a, d, peak); o.connect(g); g.connect(dest || master); o.start(t); o.stop(t + a + d + 0.05); }
var lastTick = 0;
function tick() { if (!unlocked || muted || !ac) return; var t = ac.currentTime; if (t - lastTick < 0.06) return; lastTick = t; tone(1320, 'sine', t, 0.004, 0.05, 0.08); }
function blip() { if (!unlocked || muted || !ac) return; var t = ac.currentTime; tone(880, 'triangle', t, 0.005, 0.1, 0.12); tone(1320, 'triangle', t + 0.07, 0.005, 0.16, 0.12); }
function latch() { if (!unlocked || muted || !ac) return; var t = ac.currentTime; tone(220, 'square', t, 0.002, 0.04, 0.05); tone(660, 'sine', t + 0.03, 0.002, 0.08, 0.06); }
function chime() { if (!unlocked || muted || !ac) return; var t = ac.currentTime; [523.25, 659.25, 783.99, 1046.5].forEach(function (f, i) { tone(f, 'sine', t + i * 0.11, 0.01, 0.9, 0.14); }); }

/* music: an original slow loop, a warm pad on two chords, a sparse music-box line, a soft shaker, 72 bpm */
var muted = false; try { muted = localStorage.getItem(MKEY) === 'off'; } catch (e) {}
var muteBtn = $('#mute');
function paintMute() { muteBtn.setAttribute('aria-pressed', muted ? 'false' : 'true'); muteBtn.setAttribute('aria-label', muted ? 'Music off, tap to unmute' : 'Music on, tap to mute'); }
paintMute();
var musicGain = null, musicTimer = null, nextTime = 0, step = 0, BPM = 72, STEP = 60 / BPM / 2;
var CHORDS = [[48, 55, 60, 64], [45, 52, 57, 60]];                       // C major, A minor
var MELODY = [72, 0, 76, 0, 79, 0, 0, 74, 0, 72, 0, 0, 67, 0, 0, 0, 69, 0, 72, 0, 0, 76, 0, 0, 74, 0, 0, 0, 67, 0, 0, 0];
function hz(m) { return 440 * Math.pow(2, (m - 69) / 12); }
function padChord(t, chord) { chord.forEach(function (m) { var o = ac.createOscillator(), g = ac.createGain(), f = ac.createBiquadFilter(); o.type = 'sawtooth'; o.frequency.value = hz(m); f.type = 'lowpass'; f.frequency.value = 520; g.gain.setValueAtTime(0.0001, t); g.gain.exponentialRampToValueAtTime(0.028, t + 1.4); g.gain.setValueAtTime(0.028, t + STEP * 14); g.gain.exponentialRampToValueAtTime(0.0001, t + STEP * 16); o.connect(f); f.connect(g); g.connect(musicGain); o.start(t); o.stop(t + STEP * 16 + 0.1); }); }
function box(t, m) { var o = ac.createOscillator(), g = ac.createGain(); o.type = 'sine'; o.frequency.value = hz(m); env(g, t, 0.004, 1.1, 0.16); o.connect(g); g.connect(musicGain); o.start(t); o.stop(t + 1.2); var o2 = ac.createOscillator(), g2 = ac.createGain(); o2.type = 'sine'; o2.frequency.value = hz(m) * 3.01; env(g2, t, 0.003, 0.35, 0.03); o2.connect(g2); g2.connect(musicGain); o2.start(t); o2.stop(t + 0.4); }
function shaker(t, v) { var n = ac.createBufferSource(), b = ac.createBuffer(1, 2205, ac.sampleRate), d = b.getChannelData(0); for (var i = 0; i < d.length; i++) d[i] = (Math.random() * 2 - 1) * Math.pow(1 - i / d.length, 3); n.buffer = b; var hp = ac.createBiquadFilter(); hp.type = 'highpass'; hp.frequency.value = 6000; var g = ac.createGain(); g.gain.value = v; n.connect(hp); hp.connect(g); g.connect(musicGain); n.start(t); }
function playStep(i, t) { if (i % 16 === 0) padChord(t, CHORDS[(i / 16) % 2]); var m = MELODY[i % MELODY.length]; if (m) box(t, m); if (i % 4 === 2) shaker(t, 0.05); if (i % 8 === 6) shaker(t + STEP / 2, 0.025); }
function scheduler() { while (nextTime < ac.currentTime + 0.25) { playStep(step, nextTime); nextTime += STEP; step++; } }
function startMusic() { if (muted || musicTimer || !unlocked || !ac) return; if (!musicGain) { musicGain = ac.createGain(); musicGain.connect(master); } var t = ac.currentTime; musicGain.gain.cancelScheduledValues(t); musicGain.gain.setValueAtTime(0.0001, t); musicGain.gain.exponentialRampToValueAtTime(0.5, t + 1.5); nextTime = t + 0.1; step = 0; scheduler(); musicTimer = setInterval(scheduler, 50); }
function stopMusic() { if (!musicTimer) return; clearInterval(musicTimer); musicTimer = null; var t = ac.currentTime; musicGain.gain.cancelScheduledValues(t); musicGain.gain.setValueAtTime(Math.max(musicGain.gain.value, 0.0001), t); musicGain.gain.exponentialRampToValueAtTime(0.0001, t + 0.5); }
muteBtn.addEventListener('click', function () { muted = !muted; paintMute(); try { localStorage.setItem(MKEY, muted ? 'off' : 'on'); } catch (e) {} if (muted) stopMusic(); else { unlockAudio(); startMusic(); } });
['pointerdown', 'keydown', 'touchend'].forEach(function (ev) { document.addEventListener(ev, function () { if (!unlocked) unlockAudio(); if (ac && ac.state === 'suspended') ac.resume(); if (booted) startMusic(); }, { passive: true }); });
document.addEventListener('visibilitychange', function () { if (document.hidden) stopMusic(); else if (booted) startMusic(); });

/* ---------- boot ---------- */
var booted = false, boot = $('#boot');
function begin() {
  if (booted) return; booted = true;
  unlockAudio(); chime();
  boot.classList.add('out'); setTimeout(function () { boot.hidden = true; }, 650);
  document.body.classList.remove('booting'); document.body.classList.add('booted');
  startMusic();
}
boot.addEventListener('click', begin);
boot.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); begin(); } });
if (location.hash === '#full' || q.get('boot') === '0') { boot.hidden = true; booted = true; document.body.classList.remove('booting'); document.body.classList.add('booted'); }

/* ---------- demo walkthroughs ---------- */
var demoId = null, demoStep = 0;
function openDemo(id, from) {
  var d = DEMOS[id]; if (!d) { if (ITEMS[id].kind === 'folder') openFolder(id, from); else openZoom(id, from); return; }
  demoId = id; demoStep = 0;
  $('#demo-tag').textContent = 'DEMO · ' + d.tag.toUpperCase(); $('#demo-title').textContent = ITEMS[id].name; $('#demo-open').href = d.href || ITEMS[id].href;
  $('#steps').innerHTML = d.steps.map(function (s, i) { return '<button class="step" type="button" data-step="' + i + '"><b>' + (i + 1) + '</b><span><span class="k">' + esc(s.kind.toUpperCase()) + '</span><span class="t">' + esc(s.title) + '</span></span></button>'; }).join('');
  $('#pdots').innerHTML = d.steps.map(function () { return '<i></i>'; }).join('');
  openDialog($('#demo'), from); blip(); demoGo(0);
}
function demoGo(i) {
  var d = DEMOS[demoId]; if (!d) return;
  if (i < 0) { closeDialog(); return; }
  if (i >= d.steps.length) { closeDialog(); return; }
  demoStep = i; var s = d.steps[i];
  Array.prototype.forEach.call($('#steps').children, function (b, j) { b.classList.toggle('on', j === i); b.classList.toggle('done', j < i); });
  Array.prototype.forEach.call($('#pdots').children, function (b, j) { b.classList.toggle('on', j === i); });
  $('#demo-kind').textContent = s.kind.toUpperCase() + ' · STEP ' + (i + 1) + ' OF ' + d.steps.length;
  $('#demo-h').textContent = s.title; $('#demo-p').textContent = s.body;
  var shot = $('#demo-shot');
  if (s.img) { shot.hidden = false; $('#demo-img').src = s.img; $('#demo-img').alt = s.alt || ''; var mk = $('#demo-mark'), bd = $('#demo-badge'); if (s.mark) { mk.hidden = false; mk.style.left = s.mark[0] + '%'; mk.style.top = s.mark[1] + '%'; mk.style.width = s.mark[2] + '%'; mk.style.height = s.mark[3] + '%'; bd.hidden = false; bd.textContent = i + 1; bd.style.left = (s.mark[0] + s.mark[2] - 1.5) + '%'; bd.style.top = (s.mark[1] - 4) + '%'; } else { mk.hidden = true; bd.hidden = true; } }
  else shot.hidden = true;
  $('#demo-next').textContent = i === d.steps.length - 1 ? 'Done' : 'Next';
  $('#demo-back').textContent = i === 0 ? 'Close' : 'Back';
}
$('#steps').addEventListener('click', function (e) { var b = e.target.closest('.step'); if (b) { demoGo(+b.dataset.step); tick(); } });
$('#demo-next').addEventListener('click', function () { demoGo(demoStep + 1); tick(); });
$('#demo-back').addEventListener('click', function () { demoGo(demoStep - 1); tick(); });
})();
</script>
</body>
</html>
"""

out = HTML.replace('__CSS__', CSS).replace('__MOON__', MOON).replace('__CLOCK_DEFS__', CLOCK_DEFS)
out = out.replace('__VERSION__', VERSION).replace('__ITEMS__', json.dumps(ITEMS, ensure_ascii=False)).replace('__ART__', json.dumps(ART, ensure_ascii=False)).replace('__DEMOS__', json.dumps(DEMOS, ensure_ascii=False))
open(os.path.join(ROOT, 'index.html'), 'w').write(out)
print('index.html', len(out), 'bytes')
