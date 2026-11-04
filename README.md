# 🌾 Care a Garden - A Cozy Farming Adventure

**Care a Garden** is an interactive, browser-based 3D cozy farming simulation game combined with an educational Data Structures & Algorithms (DSA) Code Lab. Restore Grandpa's farm, help save Whispering Valley from corporate expansion, and unlock interactive 3D plots through programming challenges.

---

## 🚀 Features

* **3D Sanctuary Farm**: Built with Three.js featuring dynamic lighting, plant ecosystem growth stages, weather effects (rain, sun), interactive soil grids, and dedicated on-screen camera controls (zoom, rotate, reset).
* **Complete 12-Topic DSA Code Lab**: Complete interactive Data Structures & Algorithms modules (Topics 1 through 12) in Python/JS via Pyodide WebAssembly to unlock farm features and ecosystem tiers.
* **Interactive BST Search Visualizer**: Topic 5 features a dynamic graphical Binary Search Tree (BST) visualizer with node search highlighting, SVG connecting lines, and automatic $val \pmod{25}$ mapping directly to 3D garden plot coordinates.
* **Plant Ecosystem Tree**: Unlock up to 12 species of flora across 10 farm level tiers as you gain XP and restore valley health.
* **Dynamic Weather & Events**: FIFO queue-based climate event system affecting soil moisture, well water reserves, and crop health.
* **Crop Rotting Lifecycle**: Harvest fully bloomed crops before they decay after 3 days of neglect!
* **Rich Narrative Cutscenes**: Enjoy story progression with custom ASCII art cutscenes tracking your journey against corporate expansion.
* **Audio & Atmosphere**: Ambient web audio soundscapes with dynamic background music, level-up celebration tunes, and interactive SFX.

---

## 📝 Changelog

### [0.5.4] - 2026-11-04
* **Dynamic BST Search Visualizer & Plot Mapping**: Implemented a graphical canvas renderer for Topic 5 (Binary Search Tree). Inserting and searching BST node values recalculates node coordinates, draws SVG connecting lines, and highlights corresponding 3D soil plots via $val \pmod{25}$ mapping.
* **Advance Season Day Engine Fix**: Fixed DOM reference handling inside `triggerAdvanceDay()` to accurately progress day counters, apply rain watering effects, age growing crops, and decay unharvested bloomed plants into a rotted state after 3 days.
* **ASCII Story Cutscene Engine**: Updated cutscenes ("Old Barnaby • The Valley Storyteller") to focus on interactive visual ASCII graphics and step-by-step narrative text progression across level-up transitions.
* **3D Camera & Viewport Controls**: Added dedicated UI buttons for Zoom (+/-), Orbit Rotation, and Viewport Reset alongside scroll wheel zooming.
* **Expanded Plant Taxonomy**: Expanded ecosystem progression up to Level 10 with celebration reward popups unlocking rare ancient and cosmic flora (e.g., Lotus, Celestial Lily, Tree of Life).

### [0.3.2] - 2026-10-19
* **DSA Topics Completed**: Completed all 12 Data Structures & Algorithms curriculum topics (progressed from Topic 4 to all 12 completed).
* **Version Update**: Updated application version to 0.3.2 across code headers and UI elements.
* **Cozy Loading Screen**: Added a garden-themed startup loading screen with progress bar and tip carousel.
* **Audio Optimization**: Fixed audio context initialization on loading screen entry for instant BGM & SFX playback.
* **Crop Rotting Mechanic**: Introduced crop rotting where unharvested bloomed plants decay after 3 days.

---

## 🛠️ Tech Stack

* **Frontend**: HTML5, CSS3, Tailwind CSS
* **3D Rendering**: Three.js (WebGL)
* **Code Execution**: Pyodide (WebAssembly Python 3.11+ runtime)
* **Audio System**: Web Audio API
* **Icons & Typography**: Lucide Icons, Plus Jakarta Sans, Playfair Display, JetBrains Mono

---

## 🎮 How to Play

1. **Launch**: Open `index.html` in your web browser.
2. **Unlock the Plot**: Head to the **Code Lab** tab and click **"Run All Topics"** to run all 12 topics and initialize the 3D grid.
3. **Plant & Nurture**: Select seeds from your pouch, plant them in fertile soil, water dry plots, and advance season days.
4. **Search Nodes & Plots**: Switch to the **BST Search Visualizer** tab to search nodes, insert new plant values, and pinpoint plot coordinates.
5. **Harvest & Level Up**: Gather mature crops to earn Gold, XP, and Town Hope to unlock rare ancient flora!

---

## 👨‍💻 Authors & Developer

Developed and maintained by **[Charles Kent Bernarte / Charles09]**.

---
