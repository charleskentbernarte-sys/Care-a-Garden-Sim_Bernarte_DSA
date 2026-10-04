# 🌿 Garden Simulator (v0.2.1)

An interactive, browser-native simulation game designed to teach **Data Structures and Algorithms (DSA)** through real-time Python execution. Aligned with UN Sustainable Development Goals (SDG 2: Zero Hunger, SDG 13: Climate Action, SDG 15: Life on Land).

---

## 🎮 How the Game Works

### 1. **Core Gameplay Loop**
* **The Garden Bed (5x5 Grid):** The sanctuary consists of 25 interactive plot tiles. Clicking any tile allows you to plant seeds, water crops, or inspect soil moisture states.
* **Day Cycle & Growth:** Clicking **"Advance Day"** increments time. Plants progress through lifecycle stages (`seed` -> `sprout` -> `bloom`). Fully bloomed crops can be harvested for Coins and Hope points.
* **Resource Management:** Keep track of your **Water**, **Solar Power**, **Seeds**, and **Coins**. Planting crops costs water and seeds; harvesting returns coins and XP.

### 2. **Player Level & Plant Taxonomy Tree**
* Earning XP levels up your profile. 
* Higher levels dynamically unlock new species on the **Taxonomy Tree UI** (e.g., Rose 🌹 unlocks at Level 2, Sunflower 🌻 at Level 4, Lotus 🪷 at Level 5).

### 3. **Undo Feature (Stack Mechanics)**
* Made a mistake? Click **"Undo"**. The game uses a **LIFO Stack** to pop your last action, restoring your placed seed and refunding spent coins.

### 4. **Weather Pipeline (Queue Mechanics)**
* Weather events (Rainfall, Drought, Typhoons) queue up automatically. The engine processes incoming events in strict **FIFO order**, impacting your garden's water and soil moisture.

---

## 💻 How the 12 DSA Topics Power the Game

| Topic # | DSA Concept | How It Functions in the Game |
| :---: | :--- | :--- |
| **1** | **Python OOP & Stacks** | Encapsulates plant growth states (`Plant` class) and powers the LIFO multi-level Undo system. |
| **2** | **Queues & Deques** | Manages incoming weather disasters sequentially in FIFO arrival order using `collections.deque`. |
| **3** | **2D Grid Array** | Maps 5x5 plot locations in memory, using math (`row = plot // 5`, `col = plot % 5`) for O(1) click handling. |
| **4** | **Hierarchical Trees** | Models taxonomy species tiers that unlock higher plant nodes as player XP increases. |
| **5** | **Binary Search Tree (BST)** | Organizes numeric crop IDs for binary node lookups and stat insertions. |
| **6** | **Hash Tables** | Uses custom hashing (`hash(key) % size`) and bucket lists for key-value plant metadata storage. |
| **7** | **Graphs** | Represents garden plots as graph nodes connected by edge lines to model irrigation pipe routes. |
| **8** | **QuickSort** | Organizes harvested crop inventories by market value in O(n log n) time. |
| **9** | **Binary Search** | Executes fast O(log n) lookups across sorted seed catalogs. |
| **10** | **Dijkstra's Algorithm** | Uses priority queues (`heapq`) to calculate the shortest irrigation pipe path from pumps to dry plots. |
| **11** | **Dynamic Programming** | Uses 0/1 Knapsack memoization tables to calculate optimal harvest selections under weight capacity limits. |
| **12** | **Seed Bank Storage** | Utilizes Python dictionaries for real-time tracking of seeds, coins, and energy reserves. |

---

## 🚀 How to Run the Application

No local installation, backend server, or `pip install` required!

1. **Clone or Download:** Clone this repository or download the source files.
2. **Open `index.html`:** Open `index.html` directly in any modern web browser (Chrome, Edge, Safari, Firefox).
3. **Pyodide Initialization:** The browser automatically loads **Pyodide WebAssembly (v0.26.1)** from CDN, enabling client-side Python execution directly inside your browser DOM.
4. **Run Code Topics:** Click on any of the 12 DSA tabs in the code console to run and test Python implementations live in the game!

---

## 🛠️ Technical Stack

* **Frontend UI:** HTML5, Tailwind CSS (Glassmorphism design), Vanilla JavaScript ES6+, Lucide Icons.
* **Execution Engine:** Pyodide WebAssembly v0.26.1 (Python 3.11+ runtime).
* **Current Release:** `v0.2.1`
