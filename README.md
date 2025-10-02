- 👋 Hi, I’m MUHAMMAD UZAIR
- 
- 🌱 Computer Engineer | web developer frontend | python developer
-
- 📫 you can reach me through my mail mu3355232@gmail.com
- 😄 Pronouns: ...
-  🚀 **Let's build something amazing together!**

<h2 align="left">Hi 👋! My name is ... and I'm a ..., from ....</h2>

###

<div align="center">
 <img align="right" height="150" src="https://cdn-icons-png.flaticon.com/512/1055/1055687.png" alt="developer illustration" />
<img align="right" height="150" src="https://cdn-icons-png.flaticon.com/512/921/921071.png" alt="developer illustration" />

  <img src="https://github-readme-stats.vercel.app/api/top-langs?username=maurodesouza&locale=en&hide_title=false&layout=compact&card_width=320&langs_count=5&theme=dracula&hide_border=false" height="150" alt="languages graph"  />
</div>

###
<!-- <img align="right" height="150" src="https://i.imgflip.com/65efzo.gif"  /> -->
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<title>Live Coding Demo</title>
<style>
  :root{
    --bg:#0b1220;
    --editor:#0f1724;
    --gutter:#0b1220;
    --text:#dbeafe;
    --muted:#94a3b8;
    --accent:#7c3aed;
    --cursor:#94e2a6;
    --shadow: rgba(2,6,23,0.6);
    font-family: "Fira Code", "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace;
  }
  html,body{height:100%;margin:0;background:linear-gradient(180deg,#071024 0%, #071a2b 100%);display:flex;align-items:center;justify-content:center}
  .card{
    width:880px; max-width:95vw;
    background:var(--editor);
    border-radius:12px;
    box-shadow: 0 10px 30px var(--shadow);
    padding:20px;
    color:var(--text);
  }

  /* header bar (dots) */
  .titlebar{display:flex;align-items:center;gap:8px;margin-bottom:8px}
  .dot{width:12px;height:12px;border-radius:50%}
  .dot.red{background:#ff5f56}
  .dot.yellow{background:#ffbd2e}
  .dot.green{background:#27c93f}
  .file-name{margin-left:12px;color:var(--muted);font-size:13px}

  .editor{
    display:flex;
    border-radius:8px;
    overflow:hidden;
    background:linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));
  }

  .gutter{
    width:60px;
    background:linear-gradient(180deg, rgba(0,0,0,0.06), rgba(255,255,255,0.01));
    padding:14px 8px;
    color:var(--muted);
    font-size:13px;
    text-align:right;
    user-select:none;
  }

  pre.code{
    margin:0; padding:14px 18px; min-height:320px; width:100%;
    overflow:hidden; white-space:pre-wrap;
    font-size:14px; line-height:1.6;
  }

  .cursor{
    display:inline-block;
    width:10px;
    background:var(--cursor);
    margin-left:2px;
    animation:blink 1s steps(2, start) infinite;
    vertical-align:bottom;
    height:1.2em;
    transform-origin:left;
  }
  @keyframes blink{50%{opacity:0}}

  /* simple highlight */
  .kw{color:#7dd3fc} /* keywords */
  .fn{color:#fca5a5} /* function/ident */
  .num{color:#fbbf24}
  .str{color:#a7f3d0}
  .comment{color:#64748b;font-style:italic}

  /* caption */
  .caption{color:var(--muted);font-size:13px;margin-top:10px}
</style>
</head>
<body>
  <div class="card" role="main">
    <div class="titlebar">
      <span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span>
      <div class="file-name">app.py — demo/live-coding</div>
    </div>

    <div class="editor" aria-hidden="true">
      <div class="gutter" id="gutter"></div>
      <pre class="code" id="codeArea"></pre>
    </div>

    <div class="caption">Recording tip: crop the browser to the card area for a clean GIF.</div>
  </div>

<script>
/*
  Simple typing engine.
  - lines: array of strings (can include simple markup tags for coloring)
  - The engine types each char, then pauses, then continues.
*/
const lines = [
  "<span class='comment'># Simple flask-like server demo</span>",
  "<span class='kw'>from</span> <span class='fn'>http</span> <span class='kw'>import</span> Server",
  "",
  "<span class='kw'>def</span> <span class='fn'>hello</span>(req):",
  "    <span class='comment'># respond with a friendly message</span>",
  "    return { 'status': 200, 'body': 'Hello, world!' }",
  "",
  "<span class='kw'>if</span> __name__ == '__main__':",
  "    server = Server(port=<span class='num'>8080</span>, handler=<span class='fn'>hello</span>)",
  "    server.start()",
  "",
  "<span class='comment'># watch files and auto-reload (pseudo)</span>",
  "    server.watch('./src')",
];

const area = document.getElementById("codeArea");
const gutter = document.getElementById("gutter");
let lineIndex = 0;
let charIndex = 0;
let typingSpeed = 20; // ms per char (faster feels more 'live')
let pauseAfterLine = 400; // ms pause after finishing a line

// Fill gutter numbers
function fillGutter(n){
  let out = "";
  for(let i=1;i<=n;i++){
    out += i + "\\n";
  }
  gutter.textContent = out;
}
fillGutter(lines.length + 2);

// Escape HTML already present (we use lines with HTML markup, so don't escape!)
function setContent(text){
  area.innerHTML = text + "<span class='cursor' aria-hidden='true'></span>";
}

// typing loop
function typeNext(){
  if(lineIndex >= lines.length) {
    // optionally loop: clear and restart
    setTimeout(()=>{ lineIndex = 0; charIndex = 0; setContent(""); }, 1200);
    setTimeout(runTyping, 1400);
    return;
  }

  const current = lines[lineIndex];
  // We treat current as HTML fragment; reveal it char-by-char safely by slicing raw string.
  if(charIndex <= current.length){
    const visible = current.slice(0,charIndex);
    // join all previous lines
    const previous = lines.slice(0,lineIndex).join("\\n");
    setContent(previous + (previous ? "\\n" : "") + visible);
    charIndex++;
    setTimeout(typeNext, typingSpeed);
  } else {
    // finished this line
    charIndex = 0;
    lineIndex++;
    setTimeout(typeNext, pauseAfterLine);
  }
}

function runTyping(){
  setContent("");
  lineIndex = 0; charIndex = 0;
  typeNext();
}

// start after small delay
setTimeout(runTyping, 600);

/* Accessibility: let users pause/resume with spacebar (useful while recording) */
let paused = false;
document.addEventListener('keydown', (e)=>{
  if(e.code === 'Space'){ e.preventDefault(); paused = !paused;
    if(!paused) runTyping();
  }
});
</script>
</body>
</html>



###

<div align="left">
</div>

###

<div align="left">
<img src="https://img.shields.io/static/v1?message=GitHub&logo=github&label=&color=181717&logoColor=white&labelColor=&style=for-the-badge" height="35" alt="github logo" />
<img src="https://img.shields.io/static/v1?message=Stack%20Overflow&logo=stackoverflow&label=&color=F48024&logoColor=white&labelColor=&style=for-the-badge" height="35" alt="stackoverflow logo" />
<img src="https://img.shields.io/static/v1?message=LeetCode&logo=leetcode&label=&color=FFA116&logoColor=white&labelColor=&style=for-the-badge" height="35" alt="leetcode logo" />
<img src="https://img.shields.io/static/v1?message=HackerRank&logo=hackerrank&label=&color=2EC866&logoColor=white&labelColor=&style=for-the-badge" height="35" alt="hackerrank logo" />
<img src="https://img.shields.io/static/v1?message=Codeforces&logo=codeforces&label=&color=1F8ACB&logoColor=white&labelColor=&style=for-the-badge" height="35" alt="codeforces logo" />
<img src="https://img.shields.io/static/v1?message=LinkedIn&logo=linkedin&label=&color=0077B5&logoColor=white&labelColor=&style=for-the-badge" height="35" alt="linkedin logo" />


</div>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![C++](https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white)
![Verilog](https://img.shields.io/badge/Verilog-8B0000?style=for-the-badge&logo=verilog&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=oracle&logoColor=white)
![HTML](https://img.shields.io/badge/HTML-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS-1572B6?style=for-the-badge&logo=css3&logoColor=white)

