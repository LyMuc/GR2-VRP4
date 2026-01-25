# VIDEO DEMO CHECKLIST - VRPSPD Web Application
## Build Project Step-by-Step for Video Recording

This checklist will guide you through building the VRPSPD web application from scratch in 4 distinct steps. Use Ctrl+F to search for "STEP X" comments in shared files.

---

## PREPARATION

### 1. Create New Demo Folder
```bash
mkdir vrpspd-demo
cd vrpspd-demo
```

### 2. Create Basic Structure
```bash
mkdir algorithms
mkdir static\css
mkdir static\js
mkdir static\uploads
mkdir templates
```

### 3. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

---

## STEP 1: BASIC FUNCTIONALITY (File Upload + Solve)
**Goal:** Upload file, solve with Savings/VND, display results

### FILES TO CREATE (ĐẶC TRƯNG - Copy entire file):
1. **algorithms/file_parser.py** (80 lines)
   - Full file from: `d:\GR2-VRP4\vrpspd-web\algorithms\file_parser.py`
   - Purpose: Parse VRPSPD data files

2. **algorithms/savings.py** (200 lines)
   - Full file from: `d:\GR2-VRP4\vrpspd-web\algorithms\savings.py`
   - Purpose: Savings-based algorithm (Clarke-Wright)

3. **algorithms/vnd.py** (300 lines)
   - Full file from: `d:\GR2-VRP4\vrpspd-web\algorithms\vnd.py`
   - Purpose: Variable Neighborhood Descent optimization

4. **algorithms/utils.py** (100 lines)
   - Full file from: `d:\GR2-VRP4\vrpspd-web\algorithms\utils.py`
   - Purpose: Helper functions (cost calculation, route conversion)

### FILES TO CREATE (CHUNG - Search for STEP 1):
5. **algorithms/__init__.py**
   - Search: "STEP 1" in `d:\GR2-VRP4\vrpspd-web\algorithms\__init__.py`
   - Copy: STEP 1 sections (imports + exports for core modules only)
   - Lines to copy: Core algorithm imports and __all__ exports

6. **app.py**
   - Search: "STEP 1" in `d:\GR2-VRP4\vrpspd-web\app.py`
   - Copy sections:
     - STEP 1 imports (Flask, core algorithms)
     - Flask app initialization
     - `/` route (index)
     - `/api/upload` route
     - `/api/solve` route (without visualization parts)
   
7. **templates/index.html**
   - Search: "STEP 1" in `d:\GR2-VRP4\vrpspd-web\templates\index.html`
   - Copy sections:
     - HTML structure, head with Bootstrap/FontAwesome
     - Navigation bar
     - Left panel: File upload, problem info, algorithm selection, solve button
     - Right panel: Results card (without visualization)
     - Bootstrap JS, Custom JS scripts

8. **static/js/app.js**
   - Search: "STEP 1" in `d:\GR2-VRP4\vrpspd-web\static\js\app.js`
   - Copy sections:
     - Global variables (basic)
     - DOM elements (basic)
     - Event listeners (file, solve)
     - handleFileUpload()
     - handleSolve() (without visualization)
     - displayResults()
     - showNotification()

9. **static/css/style.css**
   - Search: "STEP 1" in `d:\GR2-VRP4\vrpspd-web\static\css\style.css`
   - Copy sections:
     - Basic styles
     - Comparison table
     - Loading spinner
     - Responsive adjustments
     - Collapse button animation

### INSTALL DEPENDENCIES:
```bash
pip install Flask==3.0.3
pip install numpy==2.1.3
pip install scipy==1.14.1
pip install scikit-learn==1.5.2
```

### DEMO ACTIONS:
1. Start server: `python app.py`
2. Open browser: http://127.0.0.1:5000
3. Upload sample file (e.g., `n23k5_E-n23-k3_09.txt`)
4. Check problem info displays
5. Select Savings algorithm
6. Click "Giải bài toán"
7. Show results: total cost, routes, comparison table
8. Select both algorithms
9. Solve again - show comparison

### VERIFICATION CHECKLIST:
- [ ] File uploads successfully
- [ ] Problem info displays (customers, vehicles, capacity)
- [ ] Savings algorithm runs
- [ ] VND algorithm runs
- [ ] Results table shows correctly
- [ ] Routes display with details
- [ ] Comparison table shows when both algorithms selected

---

## STEP 2: VISUALIZATION (Interactive Plotly Charts)
**Goal:** Add route visualization with fullscreen capability

### FILES TO CREATE (ĐẶC TRƯNG):
1. **algorithms/visualization.py** (250 lines)
   - Full file from: `d:\GR2-VRP4\vrpspd-web\algorithms\visualization.py`
   - Purpose: Generate Plotly visualizations

### FILES TO UPDATE (CHUNG - Search for STEP 2):
2. **algorithms/__init__.py**
   - Search: "STEP 2" 
   - Add: visualization imports

3. **app.py**
   - Search: "STEP 2"
   - Add: Import visualization functions
   - Update: `/api/solve` endpoint to generate visualization

4. **templates/index.html**
   - Search: "STEP 2"
   - Add: Plotly.js CDN in head
   - Add: Visualization card with fullscreen button
   - Add: Fullscreen modal

5. **static/js/app.js**
   - Search: "STEP 2"
   - Add: Visualization variables
   - Add: Visualization DOM elements
   - Add: renderVisualization() function
   - Add: openFullscreen() / closeFullscreen() functions
   - Update: handleSolve() to render visualization

6. **static/css/style.css**
   - Search: "STEP 2"
   - Add: Visualization styles
   - Add: Fullscreen modal styles

### DEMO ACTIONS:
1. Restart server
2. Upload file and solve
3. Show interactive visualization appears
4. Hover over routes to see info
5. Click "Phóng to" button
6. Show fullscreen mode
7. Press ESC or X to close
8. Test with different algorithms

### VERIFICATION CHECKLIST:
- [ ] Plotly visualization renders
- [ ] Routes display with different colors
- [ ] Depot marked clearly
- [ ] Customer points labeled
- [ ] Hover shows route info
- [ ] Fullscreen button works
- [ ] ESC key closes fullscreen
- [ ] Visualization updates when solving again

---

## STEP 3: EXCEL EXPORT (Single File)
**Goal:** Export results to formatted Excel file

### FILES TO CREATE (ĐẶC TRƯNG):
1. **algorithms/excel_export.py** (350 lines)
   - Full file from: `d:\GR2-VRP4\vrpspd-web\algorithms\excel_export.py`
   - Purpose: Generate Excel reports with multiple sheets

### FILES TO UPDATE (CHUNG - Search for STEP 3):
2. **app.py**
   - Search: "STEP 3"
   - Add: Import excel_export functions
   - Add: `/api/export-excel` route

3. **templates/index.html**
   - Search: "STEP 3"
   - Add: Export button

4. **static/js/app.js**
   - Search: "STEP 3"
   - Add: Export DOM elements
   - Add: handleExport() function (single mode)
   - Update: Enable export button after solve

### INSTALL DEPENDENCIES:
```bash
pip install pandas==2.2.3
pip install openpyxl==3.1.5
```

### DEMO ACTIONS:
1. Restart server
2. Upload file and solve
3. Click "Xuất Excel" button
4. Show Excel file downloads
5. Open Excel file:
   - Show Summary sheet
   - Show Savings Results sheet (if ran)
   - Show VND Results sheet (if ran)
   - Show Comparison sheet
6. Highlight formatting, colors, borders

### VERIFICATION CHECKLIST:
- [ ] Export button appears after solving
- [ ] Excel file downloads
- [ ] Summary sheet has problem info
- [ ] Each algorithm has its own sheet
- [ ] Routes formatted correctly
- [ ] Comparison sheet shows side-by-side
- [ ] Improvement % calculated
- [ ] File has timestamp in name

---

## STEP 4: BATCH PROCESSING (Multiple Files)
**Goal:** Process multiple files at once, master Excel report

### FILES TO CREATE (ĐẶC TRƯNG):
1. **algorithms/batch_processor.py** (150 lines)
   - Full file from: `d:\GR2-VRP4\vrpspd-web\algorithms\batch_processor.py`
   - Purpose: Process multiple files in batch

2. **algorithms/batch_excel_export.py** (320 lines)
   - Full file from: `d:\GR2-VRP4\vrpspd-web\algorithms\batch_excel_export.py`
   - Purpose: Generate master Excel with all batch results

### FILES TO UPDATE (CHUNG - Search for STEP 4):
3. **app.py**
   - Search: "STEP 4"
   - Add: Import batch processing functions
   - Add: `/api/batch-upload` route
   - Add: `/api/batch-solve` route
   - Add: `/api/batch-export-excel` route

4. **templates/index.html**
   - Search: "STEP 4"
   - Add: Mode selection (Single/Batch)
   - Add: Batch file upload
   - Add: Batch results section

5. **static/js/app.js**
   - Search: "STEP 4"
   - Add: Batch variables
   - Add: Batch DOM elements
   - Add: handleModeChange()
   - Add: handleBatchFileUpload()
   - Add: displayBatchFileList()
   - Add: handleBatchSolve()
   - Add: displayBatchResults()
   - Add: handleBatchExport()
   - Update: handleSolve() to check mode
   - Update: handleExport() to check mode

6. **static/css/style.css**
   - No additional styles needed (uses Bootstrap classes)

### DEMO ACTIONS:
1. Restart server
2. Toggle to "Batch" mode
3. Select multiple files (e.g., 3-5 sample files)
4. Show file list appears
5. Click "Giải hàng loạt"
6. Show progress indicator
7. Show results table with all files
8. Click "Xuất Master Excel"
9. Open Master Excel file:
   - Show Summary sheet (averages, statistics)
   - Show Comparison sheet (all files side-by-side)
10. Toggle back to Single mode
11. Show UI switches back

### VERIFICATION CHECKLIST:
- [ ] Mode toggle works
- [ ] Multiple files can be selected
- [ ] File list displays
- [ ] Batch processing runs
- [ ] Progress shows (X/Y files)
- [ ] Results table shows all files
- [ ] Summary statistics calculated
- [ ] Master Excel exports
- [ ] Excel has Summary + Comparison sheets
- [ ] All file results in one Excel
- [ ] Computation times shown
- [ ] Average improvement calculated

---

## FINAL DEMO TIPS

### Recording Order:
1. **Introduction** (1-2 min)
   - Project overview
   - Technologies used
   - Show final result first

2. **STEP 1 Demo** (5-7 min)
   - Create files
   - Show code structure
   - Demo basic functionality

3. **STEP 2 Demo** (3-4 min)
   - Add visualization module
   - Update shared files
   - Demo interactive charts

4. **STEP 3 Demo** (3-4 min)
   - Add Excel export
   - Demo single file export
   - Show Excel formatting

5. **STEP 4 Demo** (4-5 min)
   - Add batch processing
   - Demo multiple files
   - Show master Excel

6. **Summary** (1-2 min)
   - Recap 4 steps
   - Show complete features
   - Thank you

### Ctrl+F Search Terms:
- `STEP 1` - Basic functionality
- `STEP 2` - Visualization
- `STEP 3` - Excel export
- `STEP 4` - Batch processing

### Sample Files for Demo:
Use these files from `static/uploads/`:
- Single: `n23k5_E-n23-k3_09.txt` (small, fast)
- Batch: 3-5 files with different sizes

### Common Issues to Avoid:
1. Forgot to activate venv
2. Missing imports in __init__.py
3. Forgot to restart server after changes
4. Sample data files not copied
5. Port 5000 already in use

### Time Estimates:
- STEP 1: 15 minutes (setup + basic features)
- STEP 2: 8 minutes (visualization)
- STEP 3: 8 minutes (Excel export)
- STEP 4: 10 minutes (batch processing)
- **Total Development Time in Video: ~40-45 minutes**
- **With explanations and demos: 60-75 minutes total**

---

## FILE ORGANIZATION FOR VIDEO

### Keep These Windows Open:
1. VS Code - File Explorer
2. VS Code - Current editing file
3. Web Browser - Application UI
4. File Explorer - Sample data folder

### Suggested VS Code Layout:
- Left: Explorer panel (always visible)
- Center: Main editor
- Right: Terminal (for server output)

### Before Recording:
- [ ] Clean demo folder ready
- [ ] All source files accessible
- [ ] Sample data files ready
- [ ] Browser cache cleared
- [ ] VS Code zoom level comfortable
- [ ] Terminal font size readable
- [ ] Recording software tested

---

## POST-PROCESSING CHECKLIST

### Video Editing:
- [ ] Add title cards for each STEP
- [ ] Add timestamps in description
- [ ] Speed up file copying (2x-3x)
- [ ] Zoom in on important code sections
- [ ] Add background music (subtle)
- [ ] Add final demo montage

### YouTube Description Template:
```
VRPSPD Web Application - Build From Scratch

🎯 In this video, I build a complete Vehicle Routing Problem with Simultaneous Pickup and Delivery (VRPSPD) web application in 4 steps.

⏱️ TIMESTAMPS:
0:00 Introduction
2:00 STEP 1: Basic Functionality (Upload + Solve)
9:00 STEP 2: Visualization (Plotly Charts)
13:00 STEP 3: Excel Export
17:00 STEP 4: Batch Processing
22:00 Final Demo & Summary

🛠️ TECHNOLOGIES:
- Backend: Flask 3.0.3, Python 3.13
- Frontend: Bootstrap 5, Plotly.js 2.27.0
- Algorithms: Savings-based, VND
- Data Processing: NumPy, Pandas, SciPy

📂 PROJECT STRUCTURE:
- 8 Algorithm modules (~2,300 lines)
- 1 Flask application (286 lines)
- Responsive Bootstrap UI (198 lines HTML)
- Interactive JavaScript (680 lines)

✨ FEATURES:
✅ File upload & parsing
✅ Savings & VND algorithms
✅ Interactive route visualization
✅ Excel export with formatting
✅ Batch processing multiple files
✅ Master Excel reports

📌 GitHub Repository: [Your Link]
📧 Contact: [Your Email]

#VRPSPD #Flask #Python #WebDevelopment #Algorithms #DataScience
```

---

## BONUS: TROUBLESHOOTING GUIDE

### If Server Won't Start:
```bash
# Check Python version
python --version

# Check if port in use
netstat -ano | findstr :5000

# Kill process if needed
taskkill /PID <PID> /F
```

### If Packages Won't Install:
```bash
# Upgrade pip first
python -m pip install --upgrade pip

# Install with verbose
pip install -v Flask==3.0.3
```

### If Visualization Doesn't Show:
1. Check browser console (F12)
2. Verify Plotly.js CDN loaded
3. Check network tab for API calls
4. Verify JSON structure returned

### If Excel Export Fails:
1. Check openpyxl installed
2. Verify write permissions
3. Check disk space
4. Close any open Excel files

---

**Good luck with your video demo! 🎥🚀**
