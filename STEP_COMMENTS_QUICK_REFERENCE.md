# QUICK REFERENCE - STEP Comments Guide

## How to Use This Guide

When recording your video, use **Ctrl+F** to search for these terms in each file:

---

## FILE: app.py

### Search Terms:
- `STEP 1` → Core imports + basic routes (upload, solve)
- `STEP 2` → Visualization import + render in solve endpoint
- `STEP 3` → Excel export import + export route
- `STEP 4` → Batch imports + batch routes

### Key Sections:
1. **Lines 1-22**: Imports (all 4 steps marked)
2. **Lines 25-45**: Index & Upload routes (STEP 1)
3. **Lines 48-120**: Solve endpoint (STEP 1 + STEP 2)
4. **Lines 200-225**: Excel export endpoint (STEP 3)
5. **Lines 230-286**: Batch endpoints (STEP 4)

---

## FILE: templates/index.html

### Search Terms:
- `STEP 1` → Bootstrap, basic layout, file upload, results
- `STEP 2` → Plotly.js, visualization card, fullscreen modal
- `STEP 3` → Export button
- `STEP 4` → Mode selection, batch upload, batch results

### Key Sections:
1. **Lines 1-15**: Head section (STEP 1: Bootstrap, STEP 2: Plotly.js)
2. **Lines 30-50**: Mode selection (STEP 4)
3. **Lines 55-85**: File upload sections (STEP 1 single, STEP 4 batch)
4. **Lines 98-120**: Algorithm selection + buttons (STEP 1 + STEP 3)
5. **Lines 140-175**: Results + visualization card (STEP 1 + STEP 2)
6. **Lines 180-200**: Batch results (STEP 4)
7. **Lines 205-220**: Fullscreen modal (STEP 2)

---

## FILE: static/js/app.js

### Search Terms:
- `STEP 1` → Basic variables, upload, solve, display
- `STEP 2` → Visualization variables, render functions
- `STEP 3` → Export function
- `STEP 4` → Batch variables, batch functions, mode change

### Key Sections:
1. **Lines 1-85**: Variables, DOM elements, Event listeners (all steps marked)
2. **Lines 88-130**: File upload handler (STEP 1)
3. **Lines 133-200**: Solve handler (STEP 1 main, STEP 2 viz, STEP 3 enable export, STEP 4 mode check)
4. **Lines 203-280**: Display results (STEP 1)
5. **Lines 310-370**: Export handler (STEP 3 single, STEP 4 batch check)
6. **Lines 373-420**: Batch export (STEP 4)
7. **Lines 440-490**: Visualization rendering (STEP 2)
8. **Lines 493-530**: Fullscreen functions (STEP 2)
9. **Lines 533-565**: Mode change handler (STEP 4)
10. **Lines 568-650**: Batch upload, solve, display (STEP 4)

---

## FILE: static/css/style.css

### Search Terms:
- `STEP 1` → Basic styles, comparison table, loading
- `STEP 2` → Visualization styles, fullscreen modal

### Key Sections:
1. **Lines 1-90**: Basic styles (STEP 1)
2. **Lines 95-180**: Fullscreen modal (STEP 2)

---

## FILE: algorithms/__init__.py

### Search Terms:
- `STEP 1` → Core algorithm imports + exports
- `STEP 2` → Visualization imports

### Key Sections:
1. **Lines 5-17**: Imports (STEP 1 core, STEP 2 viz)
2. **Lines 20-44**: __all__ exports (marked by step)

---

## STANDALONE FILES (Copy Entire File)

### STEP 1:
- ✅ `algorithms/file_parser.py` (80 lines)
- ✅ `algorithms/savings.py` (200 lines)
- ✅ `algorithms/vnd.py` (300 lines)
- ✅ `algorithms/utils.py` (100 lines)

### STEP 2:
- ✅ `algorithms/visualization.py` (250 lines)

### STEP 3:
- ✅ `algorithms/excel_export.py` (350 lines)

### STEP 4:
- ✅ `algorithms/batch_processor.py` (150 lines)
- ✅ `algorithms/batch_excel_export.py` (320 lines)

---

## DEPENDENCIES BY STEP

### STEP 1:
```bash
pip install Flask==3.0.3 numpy==2.1.3 scipy==1.14.1 scikit-learn==1.5.2
```

### STEP 2:
No new dependencies (uses Plotly.js via CDN)

### STEP 3:
```bash
pip install pandas==2.2.3 openpyxl==3.1.5
```

### STEP 4:
No new dependencies (uses existing modules)

---

## CODE LINE COUNTS BY STEP

### STEP 1: ~1,100 lines
- file_parser.py: 80
- savings.py: 200
- vnd.py: 300
- utils.py: 100
- app.py: ~120 (STEP 1 parts)
- index.html: ~100 (STEP 1 parts)
- app.js: ~180 (STEP 1 parts)
- style.css: ~80 (STEP 1 parts)
- __init__.py: ~15 (STEP 1 parts)

### STEP 2: ~450 lines
- visualization.py: 250
- app.py: ~30 (STEP 2 additions)
- index.html: ~50 (STEP 2 additions)
- app.js: ~80 (STEP 2 additions)
- style.css: ~90 (STEP 2 additions)
- __init__.py: ~5 (STEP 2 additions)

### STEP 3: ~450 lines
- excel_export.py: 350
- app.py: ~35 (STEP 3 additions)
- index.html: ~10 (STEP 3 additions)
- app.js: ~60 (STEP 3 additions)

### STEP 4: ~650 lines
- batch_processor.py: 150
- batch_excel_export.py: 320
- app.py: ~55 (STEP 4 additions)
- index.html: ~55 (STEP 4 additions)
- app.js: ~120 (STEP 4 additions)

### TOTAL: ~2,650 lines of code

---

## RECORDING TIPS

### Ctrl+F Workflow:
1. Open file in VS Code
2. Press **Ctrl+F**
3. Type: `STEP 1` (or 2, 3, 4)
4. Press **Enter** to jump to next match
5. **F3** = Next match
6. **Shift+F3** = Previous match

### VS Code Settings for Recording:
```json
{
  "editor.fontSize": 16,
  "editor.lineHeight": 24,
  "terminal.integrated.fontSize": 14,
  "workbench.colorTheme": "Default Light+"
}
```

### Browser Zoom:
- Recommended: **110%** for better visibility on video

### Terminal Commands to Copy-Paste:
```bash
# Create structure
mkdir algorithms static\css static\js static\uploads templates

# Activate venv
venv\Scripts\activate

# Install STEP 1
pip install Flask==3.0.3 numpy==2.1.3 scipy==1.14.1 scikit-learn==1.5.2

# Install STEP 3
pip install pandas==2.2.3 openpyxl==3.1.5

# Run server
python app.py
```

---

## DEMO FILE RECOMMENDATIONS

### Single File Demo (STEP 1-3):
- **n23k5_E-n23-k3_09.txt** (23 customers, 5 vehicles)
  - Fast execution (~1 second)
  - Clear visualization
  - Good for demo

### Batch Demo (STEP 4):
Select 3-5 files:
1. Small: n23k5_E-n23-k3_09.txt
2. Medium: n30k5_E-n30-k4_10.txt  
3. Medium: n33k5_E-n33-k4_01.txt

---

## COMMON MISTAKES TO AVOID

### ❌ Forgot to add STEP 1 imports to __init__.py
**Fix:** Search for `STEP 1` in algorithms/__init__.py

### ❌ Forgot Plotly.js CDN link
**Fix:** Search for `STEP 2` in index.html head section

### ❌ Export button doesn't appear
**Fix:** Check if exportBtn.disabled = false in handleSolve()

### ❌ Batch mode UI doesn't switch
**Fix:** Check handleModeChange() function exists and is called

### ❌ Visualization doesn't render
**Fix:** 
1. Check browser console (F12)
2. Verify Plotly.js loaded
3. Check API returns visualization JSON

---

## VERIFICATION AFTER EACH STEP

### After STEP 1:
```bash
✅ Server starts without errors
✅ Can upload file
✅ Problem info displays
✅ Can solve with Savings
✅ Can solve with VND
✅ Results table shows
✅ Routes display correctly
```

### After STEP 2:
```bash
✅ Plotly chart appears
✅ Routes show different colors
✅ Hover shows route info
✅ Fullscreen button works
✅ ESC closes fullscreen
```

### After STEP 3:
```bash
✅ Export button appears
✅ Excel downloads
✅ Has Summary sheet
✅ Has algorithm sheets
✅ Has Comparison sheet
✅ Formatting looks good
```

### After STEP 4:
```bash
✅ Mode toggle works
✅ Can select multiple files
✅ Batch processing runs
✅ Shows progress
✅ Results table displays
✅ Master Excel exports
✅ Summary statistics correct
```

---

## KEYBOARD SHORTCUTS FOR VIDEO EDITING

### VS Code:
- **Ctrl+P**: Quick file open
- **Ctrl+Shift+F**: Search across all files
- **Ctrl+B**: Toggle sidebar
- **Ctrl+J**: Toggle terminal
- **Ctrl+`**: Toggle terminal
- **Alt+Shift+F**: Format document

### Chrome DevTools:
- **F12**: Open DevTools
- **Ctrl+Shift+C**: Inspect element
- **Ctrl+Shift+J**: Console
- **Ctrl+R**: Refresh page

---

**This guide is designed for quick reference during video recording. Keep it open on a second monitor! 📺✨**
