# Academic & Technical Projects

This repository collects **eleven** of my academic/technical projects.
Each subfolder contains its own README with features, how to run, and lessons learned.

## Projects
1. **Digital Logic Design Labs (CMPEN 270)** — Verilog circuits for ALU, FSM, and register files.
2. **Binary Search Tree (Python)** — Recursive & iterative traversals with simple visualization.
3. **Course Scheduler (Java + SQL)** — Models courses, prerequisites, conflicts; DAO layer + schema.
4. **Matrix & Determinant Simulator (Python)** — Determinants, inverses, step-by-step operations.
5. **Cache Simulation System** — Multi-level cache with traces, stats, and AMAT reporting.
6. **Vending Machine Simulator (Java)** — Finite-state machine with tests and CLI runner.
7. **PipelineCPU (Verilog on Zybo)** — Pipelined CPU with hazards, forwarding, and testbenches.
8. **Advanced Calculator (Python)** - Solves basic alebra using stacks, also solves polynomials
9. **Course Scheduler (Python)** — Hardcode of PennStates' Schedule Builder
10. **Binary Heaps (Python)** - Plays with Binary heaps, giving min_heap, max_heap
11. **Linked List Simulator (Python)** - Singly and Doubly Linked List functionality

## Usage
- Add your **actual source code** into each `src/` folder (placeholders are included).
- Commit incrementally with clear messages.
- Consider adding CI (e.g., GitHub Actions) to build/test Java/C projects.

## Suggested .gitignore
Create a `.gitignore` to avoid committing build artifacts:
```
# macOS
.DS_Store

# Java
target/
*.class

# Python
__pycache__/
*.pyc

# Vivado/EDA (very verbose; keep only HDL and key reports/images)
*.jou
*.log
*.str
*.cache/
*.ipr
*.iopl
*.runs/
*.hw/
*.sim/
*.xpr
*.xsa

# Other
build/
dist/
```
