#!/usr/bin/env python3
"""Usage: python fix_care_a_garden.py your_file.html"""
import sys, shutil

path = sys.argv[1] if len(sys.argv) > 1 else "index.html"
shutil.copy(path, path + ".bak")
s = open(path, encoding="utf-8").read()

def rep(old, new, label):
    global s
    n = s.count(old)
    if n:
        s = s.replace(old, new)
    print(("fixed   " if n else "SKIPPED ") + label)

# ---------- libraries / icons ----------
rep("https://unpkg.com/lucide@latest", "https://unpkg.com/lucide@0.460.0/dist/umd/lucide.min.js", "pin lucide version")
rep('data-lucide="barn"', 'data-lucide="warehouse"', "missing 'barn' icon")
rep('const icon = document.getElementById("bgm-icon");',
    'const oldIcon = document.getElementById("bgm-icon"); const icon = document.createElement("i"); icon.id = "bgm-icon"; '
    'icon.setAttribute("data-lucide", isAudioMuted ? "volume-x" : "volume-2"); '
    'icon.className = "w-4 h-4 " + (isAudioMuted ? "text-red-400" : "text-emerald-400"); if (oldIcon) oldIcon.replaceWith(icon);',
    "mute icon stops updating after first toggle")

# ---------- 3D engine ----------
rep("let raycaster = new THREE.Raycaster();", "let raycaster = null;", "page crashed if three.js failed to load (1)")
rep("let mouse = new THREE.Vector2();", "let mouse = null;", "page crashed if three.js failed to load (2)")
rep("function init3DEngine() {",
    'function init3DEngine() {\n'
    '            if (typeof THREE === "undefined") { const c = document.getElementById("canvas-container"); '
    'if (c) c.insertAdjacentHTML("beforeend", \'<div class="absolute inset-0 flex items-center justify-center text-xs text-red-300 p-6 text-center">3D engine could not load. Check your internet connection and reload.</div>\'); return; }\n'
    '            raycaster = new THREE.Raycaster(); mouse = new THREE.Vector2();',
    "guard missing three.js")
rep("init3DEngine();", "try { init3DEngine(); } catch (e) { console.error('3D init failed', e); }", "WebGL failure no longer stops startup")
rep("renderer.shadowMap.enabled = true;", "renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));\n            renderer.shadowMap.enabled = true;", "blurry canvas on HiDPI screens")
rep("function on3DWheel(e) {", "let dragStartX = null, dragMoved = false;\n        function on3DWheel(e) {", "drag state")
rep("zoom3DCamera(e.deltaY * 0.01);", "e.preventDefault(); zoom3DCamera(e.deltaY * 0.01);", "page scrolled while zooming")
rep("container.addEventListener('wheel', on3DWheel, { passive: true });",
    "container.addEventListener('wheel', on3DWheel, { passive: false });\n"
    "            container.addEventListener('mousedown', e => { dragStartX = e.clientX; dragMoved = false; });\n"
    "            window.addEventListener('mouseup', () => { dragStartX = null; });\n"
    "            container.addEventListener('mousemove', e => { if (dragStartX !== null && e.buttons === 1) { const dx = e.clientX - dragStartX; if (Math.abs(dx) > 3) { dragMoved = true; rotate3DCamera(dx * 0.01); dragStartX = e.clientX; } } });",
    "drag-to-rotate (the UI promised it)")
rep("function on3DClick(e) {", "function on3DClick(e) {\n            if (dragMoved) { dragMoved = false; return; }", "dragging planted a crop")
rep("function update3DCropsMesh(idx, cropName, stage, dry) {", "function update3DCropsMesh(idx, cropName, stage, dry) {\n            if (!scene) return;", "guard before 3D scene exists")
rep("scene.remove(cropMeshes[idx]);", "scene.remove(cropMeshes[idx]); cropMeshes[idx].geometry.dispose(); cropMeshes[idx].material.dispose();", "memory leak when replacing crop meshes")

# ---------- story + BST ----------
rep("function triggerStoryCutsceneFirst(",
    "function getChapter(l) {\n"
    "            return storyChapters[l] || { tag: `LEVEL ${l} • WHISPERING VALLEY FLOURISHES`, ascii: storyChapters[3].ascii, steps: [\n"
    "                `Level ${l} complete! Your farm grows stronger with every harvest.`,\n"
    "                \"The villagers gather at your gate, amazed at how far the Valley has come.\",\n"
    "                \"Barnaby smiles: 'The land remembers who cares for it. Keep going, farmer!'\" ] };\n"
    "        }\n\n        function triggerStoryCutsceneFirst(", "levels 4-10 replayed the Level 1 story (helper)")
rep("currentCutsceneLevel = storyChapters[level] ? level : 1;", "currentCutsceneLevel = level;", "levels 4-10 story (1)")
rep("const chapter = storyChapters[currentCutsceneLevel] || storyChapters[1];", "const chapter = getChapter(currentCutsceneLevel);", "levels 4-10 story (2)")
rep("const plotPos = val % 25;", "const plotPos = ((val % 25) + 25) % 25;", "negative BST values broke plot index")
rep("const newNode = new BSTNode(val, plotPos);",
    'if (findBSTNodeObj(bstRoot, val)) { document.getElementById("bst-search-feedback").innerText = `⚠ Node ${val} already exists in the BST.`; return; }\n            const newNode = new BSTNode(val, plotPos);',
    "duplicate BST values reported as inserted")

# ---------- Python engine ----------
rep('window.pyodideCdnFailed || typeof loadPyodide === "undefined" || location.protocol === "file:"',
    'window.pyodideCdnFailed || typeof loadPyodide === "undefined"', "Python never ran when opened as a local file")
rep("function initPyodideEngine(maxWaitMs = 7000)", "function initPyodideEngine(maxWaitMs = 45000)", "7s timeout too short to download Python")

a = s.find("window.runPythonCode = async function() {")
b = s.find("window.loadTopic = function() {")
if a != -1 and b > a:
    NEW = r'''const escHtml = t => String(t).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
        function consolePrint(t, cls) {
            const el = document.getElementById("output-console");
            el.innerHTML += `<span class="${cls || "text-emerald-200"}">${escHtml(t)}</span><br>`;
            el.scrollTop = el.scrollHeight;
        }
        let pyOutBound = false;
        function bindPyOutput() {
            if (pyodideInstance && !pyOutBound) {
                pyodideInstance.setStdout({ batched: m => consolePrint(m) });
                pyodideInstance.setStderr({ batched: m => consolePrint(m, "text-red-400") });
                pyOutBound = true;
            }
        }

        window.runPythonCode = async function() {
            initAudioContext();
            playTone(523.25, 'triangle', 0.2, 0.08);
            const el = document.getElementById("output-console");
            el.innerHTML = `<span class="text-amber-400">Running selected topic...</span><br>`;
            const key = document.getElementById("topic-selector").value;
            const ready = await initPyodideEngine(45000);
            if (ready && pyodideInstance) {
                bindPyOutput();
                try {
                    await pyodideInstance.runPythonAsync(document.getElementById("code-editor").value);
                    consolePrint("Topic executed in Python engine!", "text-emerald-400");
                } catch (err) {
                    playTone(200, 'sawtooth', 0.2, 0.05);
                    consolePrint("Error: " + err.message, "text-red-400");
                }
            } else {
                consolePrint(jsSimOutputs[key] || "Topic executed.", "text-emerald-400");
            }
            if (!isGameUnlocked) consolePrint("Tip: run all 12 topics to unlock the 3D farm.", "text-amber-300");
        };

        window.runAllTopicsSequentially = async function() {
            initAudioContext();
            playTone(659.25, 'triangle', 0.25, 0.1);
            switchTab('code');
            document.getElementById("output-console").innerHTML = `<span class="text-amber-400">Executing all 12 topics...</span><br>`;
            const ready = await initPyodideEngine(45000);
            if (ready) bindPyOutput();
            const keys = Object.keys(topicTemplates);
            let failed = 0;
            for (const key of keys) {
                consolePrint(`▶ Running Topic ${key}: ${topicTemplates[key].title}`, "text-emerald-400 font-bold");
                if (ready && pyodideInstance) {
                    try { await pyodideInstance.runPythonAsync(topicTemplates[key].code); }
                    catch (e) { failed++; consolePrint(`Error in Topic ${key}: ${e.message}`, "text-red-400"); }
                } else {
                    consolePrint(jsSimOutputs[key], "text-emerald-300");
                }
            }
            if (failed) {
                playTone(200, 'sawtooth', 0.25, 0.06);
                consolePrint(`✗ ${failed} topic(s) failed. The farm stays locked until all 12 pass.`, "text-red-400");
                showToast("Some topics failed. See the console.");
                return;
            }
            consolePrint("✓ All 12 topics verified! 3D Farm Plot Unlocked.", "text-emerald-300 font-bold");
            unlockGameFunctionality();
            showToast("All topics executed! 3D Farm plot unlocked.");
        };

        '''
    s = s[:a] + NEW + s[b:]
    print("fixed   Python output hidden, errors swallowed, single topic unlocked the farm")
else:
    print("SKIPPED Python run functions")

# ---------- missing / broken game actions ----------
EXTRA = r'''// ---- v0.5.4 fixes: missing buttons, Photosynthesis, real Undo ----
        const undoStack = [];
        const gateMsg = () => showToast("🔒 Run all 12 Code Topics first!");

        window.triggerRainEvent = function() {
            if (!isGameUnlocked) return gateMsg();
            initAudioContext(); playTone(500, 'sine', 0.25, 0.06);
            isCurrentlyRaining = true;
            resourcesState.water = Math.min(200, resourcesState.water + 30);
            gardenGridState.forEach((it, i) => { if (!it) return; const p = it.split("|"); p[4] = "0"; gardenGridState[i] = p.join("|"); });
            pushAction("🌧️ Rain fell: +30L water, all plots watered");
            updateResources(resourcesState);
        };

        window.autoWaterAllPlots = function() {
            if (!isGameUnlocked) return gateMsg();
            initAudioContext();
            let n = 0;
            gardenGridState.forEach((it, i) => {
                if (!it) return;
                const p = it.split("|");
                if (p[4] === "1" && p[2] !== "rotten" && resourcesState.water >= 10) {
                    resourcesState.water -= 10; p[4] = "0"; gardenGridState[i] = p.join("|"); n++;
                }
            });
            if (!n) { showToast("No dry plots need water."); return; }
            playTone(587.33, 'sine', 0.2, 0.08);
            pushAction(`Watered ${n} dry plot(s) (-${n * 10}L)`);
            updateResources(resourcesState);
        };

        window.triggerPhotosynthesis = function() {
            if (!isGameUnlocked) return gateMsg();
            if (resourcesState.energy < 20) { showToast("Not enough Sunlight Energy (need 20 Wh)."); return; }
            initAudioContext();
            resourcesState.energy -= 20;
            gardenGridState.forEach((it, i) => {
                if (!it) return;
                const p = it.split("|");
                if (p[2] === "bloom" || p[2] === "rotten") return;
                const d = parseInt(p[3] || "0") + 1, st = d >= 10 ? "bloom" : d >= 4 ? "sprout" : "seed";
                gardenGridState[i] = [p[0], p[1], st, d, p[4], p[5]].join("|");
                update3DCropsMesh(i, p[0], st, p[4] === "1");
            });
            pushAction("☀️ Photosynthesis: every growing crop gained +1 growth day");
            updateResources(resourcesState);
            showToast("☀️ Photosynthesis active!");
        };

        const undoSnap = () => JSON.stringify({ g: gardenGridState, r: resourcesState, d: currentDay, xp: currentXP, l: currentLevel, q: currentQuestHarvests });
        ["onTileClick", "triggerAdvanceDay", "runSolarWellPump", "triggerPhotosynthesis", "triggerRainEvent", "autoWaterAllPlots"].forEach(name => {
            const orig = window[name];
            window[name] = function(...args) {
                const before = undoSnap();
                const out = orig.apply(this, args);
                if (isGameUnlocked && undoSnap() !== before) { undoStack.push(before); if (undoStack.length > 30) undoStack.shift(); }
                return out;
            };
        });

        window.triggerUndo = function() {
            if (!isGameUnlocked) return;
            initAudioContext();
            const snap = undoStack.pop();
            if (!snap) { showToast("Nothing to undo."); return; }
            const o = JSON.parse(snap);
            gardenGridState = o.g; currentDay = o.d; currentXP = o.xp; currentLevel = o.l; currentQuestHarvests = o.q;
            document.getElementById("day-counter").innerText = currentDay;
            document.getElementById("level-counter").innerText = currentLevel;
            document.getElementById("quest-progress-text").innerText = `Progress: ${currentQuestHarvests} / ${questTarget}`;
            for (let i = 0; i < 25; i++) {
                const it = gardenGridState[i];
                if (it) { const p = it.split("|"); update3DCropsMesh(i, p[0], p[2], p[4] === "1"); } else update3DCropsMesh(i, null, null, false);
            }
            refreshCropSelectorOptions(); updateHierarchicalTreeUI(); updateResources(o.r); updateLevelProgress(0);
            pushAction("Undid last action");
            playTone(300, 'sine', 0.15, 0.05);
        };

        window.onload = () => {'''
rep("window.onload = () => {", EXTRA, "missing Rain/Water All buttons, empty Photosynthesis, fake Undo")

open(path, "w", encoding="utf-8").write(s)
print("\nDone. Open", path, "(backup:", path + ".bak)")
