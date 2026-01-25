# ✅ VRPSPD Testing Checklist

## 📋 Pre-Testing Setup

### Environment Setup
- [ ] Python 3.8+ installed
- [ ] Virtual environment activated (optional but recommended)
- [ ] Dependencies installed: `pip install -r requirements.txt`
- [ ] Working directory: `cd vrpspd-web`

### File Structure Check
- [ ] `algorithms/` folder exists with all modules
- [ ] `static/uploads/` folder exists (auto-created)
- [ ] `templates/index.html` exists
- [ ] `app.py` exists
- [ ] Test files created: `test_complete_scenarios.py`, `VRPSPD_TEST_SCENARIOS.md`

---

## 🧪 Testing Checklist

### Phase 1: Unit Tests (Automated)

#### TC001: Module Import ✅
- [ ] Run: `python test_complete_scenarios.py --unit`
- [ ] All modules imported without errors
- [ ] No missing dependencies

#### TC002: File Parser ✅
- [ ] Standard test file parsed correctly
- [ ] Cost matrix: 4x4
- [ ] Customers: 3
- [ ] Demands: [1200, 1700, 1500]
- [ ] Pickups: [0, 1200, 1700]
- [ ] Capacity: 6000

#### TC003: Savings Algorithm ✅
- [ ] Algorithm completes successfully
- [ ] Total cost > 0
- [ ] Routes generated
- [ ] All customers visited
- [ ] Capacity constraints satisfied
- [ ] Computation time recorded

#### TC004: VND Algorithm ✅
- [ ] VND runs successfully
- [ ] Final cost ≤ Initial cost
- [ ] Improvement % calculated
- [ ] Routes remain valid
- [ ] Capacity constraints maintained

#### TC005: Visualization ✅
- [ ] Plotly data generated
- [ ] Coordinates created for all nodes
- [ ] Depot coordinates set
- [ ] Routes paths created
- [ ] JSON figure exportable
- [ ] File saved: `test_results/test_viz.json`

#### TC006: Excel Export (Single) ✅
- [ ] Excel file created successfully
- [ ] File: `test_results.xlsx` exists
- [ ] File size > 0
- [ ] Contains Summary sheet
- [ ] Contains Routes sheet
- [ ] Contains Comparison sheet (if both algorithms)
- [ ] File opens in Excel/LibreOffice

#### TC007: Batch Processing ✅
- [ ] Multiple files processed
- [ ] Success count correct
- [ ] Failed count correct (if any)
- [ ] Each file has results or error
- [ ] Parallel processing works

#### TC008: Batch Excel Export ✅
- [ ] Master Excel created
- [ ] File: `test_batch_results.xlsx` exists
- [ ] Overview sheet present
- [ ] Individual instance sheets present
- [ ] Summary statistics correct

#### TC015: Error Handling ✅
- [ ] Invalid file format caught
- [ ] Empty file caught
- [ ] Missing data caught
- [ ] Zero capacity caught
- [ ] Non-existent file caught
- [ ] Error messages clear

---

### Phase 2: Performance Tests

#### TC016: Large Instance Performance ✅
- [ ] Run: `python test_complete_scenarios.py --performance`
- [ ] 50-customer instance created
- [ ] Savings completes < 5 seconds
- [ ] VND completes < 60 seconds
- [ ] No memory issues
- [ ] No crashes

---

### Phase 3: Manual Web App Tests

#### TC009: Upload Single File 🔧 (Manual)
**Steps:**
1. [ ] Start server: `python app.py`
2. [ ] Open browser: `http://localhost:5000`
3. [ ] Click "Choose File"
4. [ ] Select test file from `static/uploads/test_data/standard_test.txt`
5. [ ] Click Upload or wait for auto-upload

**Expected:**
- [ ] Success message shown
- [ ] File info displayed (3 customers, 1 vehicle, capacity 6000)
- [ ] No errors in console

#### TC010: Solve with Algorithms 🔧 (Manual)
**Steps:**
1. [ ] After upload, check "Savings" checkbox
2. [ ] Check "VND" checkbox
3. [ ] Click "Giải bài toán" (Solve)
4. [ ] Wait for results

**Expected:**
- [ ] Progress indicator shows
- [ ] Results displayed
- [ ] Savings cost shown
- [ ] VND cost shown
- [ ] Improvement % shown
- [ ] Visualization appears (if implemented)

#### TC011: Export Excel 🔧 (Manual)
**Steps:**
1. [ ] After solving, find "Export Excel" button
2. [ ] Click button
3. [ ] Save file

**Expected:**
- [ ] File downloads: `VRPSPD_Results.xlsx`
- [ ] File opens correctly
- [ ] All sheets present
- [ ] Data matches web results

#### TC012: Batch Upload 🔧 (Manual)
**Steps:**
1. [ ] Reload page or click "New Problem"
2. [ ] Find "Batch Upload" section
3. [ ] Select multiple files (3-5 files)
4. [ ] Upload

**Expected:**
- [ ] All files uploaded
- [ ] File count shown
- [ ] File list displayed

#### TC013: Batch Solve 🔧 (Manual)
**Steps:**
1. [ ] After batch upload, select algorithms
2. [ ] Click "Batch Solve"
3. [ ] Wait for completion

**Expected:**
- [ ] Progress for each file shown
- [ ] Results table displayed
- [ ] Summary statistics shown
- [ ] Success/Failed counts correct

#### TC014: Batch Excel Export 🔧 (Manual)
**Steps:**
1. [ ] After batch solve, click "Export Batch Excel"
2. [ ] Save file

**Expected:**
- [ ] Master Excel downloads
- [ ] Overview sheet with summary
- [ ] Sheet for each instance
- [ ] Data correct

---

### Phase 4: End-to-End Workflow Test

#### TC018: Complete Workflow 🎯 (Manual)
**Steps:**
1. [ ] **Start Fresh:** Close all browsers, restart server
2. [ ] **Open App:** Navigate to `http://localhost:5000`
3. [ ] **Upload:** Upload `standard_test.txt`
4. [ ] **Verify Upload:** Check file info displayed correctly
5. [ ] **Select Algorithms:** Check both Savings and VND
6. [ ] **Solve:** Click solve button
7. [ ] **View Results:** Verify all results shown
8. [ ] **Check Visualization:** Routes displayed on map/graph
9. [ ] **Export Excel:** Download and open Excel file
10. [ ] **Verify Excel:** Check all sheets and data
11. [ ] **Try Batch:** Upload 3 files for batch processing
12. [ ] **Batch Solve:** Run batch solve
13. [ ] **Batch Export:** Export batch Excel
14. [ ] **Final Check:** Open batch Excel and verify

**Success Criteria:**
- [ ] All steps complete without errors
- [ ] Results are consistent
- [ ] Excel files open and contain correct data
- [ ] No console errors
- [ ] No broken UI elements

---

## 🐛 Error Scenarios Testing

### Edge Cases
- [ ] Upload very large file (>10MB) → Should reject
- [ ] Upload .pdf file → Should reject with message
- [ ] Upload file with negative costs → Should handle or error
- [ ] Upload file with 0 vehicles → Should error
- [ ] Solve without uploading file → Should error
- [ ] Click solve multiple times rapidly → Should handle gracefully

### Browser Compatibility
- [ ] Chrome ✅
- [ ] Firefox ✅
- [ ] Edge ✅
- [ ] Safari ✅ (if Mac available)

### Network Issues
- [ ] Slow connection simulation
- [ ] Server restart during solve
- [ ] Upload interrupted

---

## 📊 Test Results Recording

### Automated Tests

| Test ID | Name | Status | Duration | Notes |
|---------|------|--------|----------|-------|
| TC001 | Module Import | ⬜ | | |
| TC002 | File Parser | ⬜ | | |
| TC003 | Savings | ⬜ | | |
| TC004 | VND | ⬜ | | |
| TC005 | Visualization | ⬜ | | |
| TC006 | Excel Export | ⬜ | | |
| TC007 | Batch Processing | ⬜ | | |
| TC008 | Batch Excel | ⬜ | | |
| TC015 | Error Handling | ⬜ | | |
| TC016 | Performance | ⬜ | | |

### Manual Tests

| Test ID | Name | Status | Browser | Notes |
|---------|------|--------|---------|-------|
| TC009 | Upload Single | ⬜ | | |
| TC010 | Solve | ⬜ | | |
| TC011 | Export Excel | ⬜ | | |
| TC012 | Batch Upload | ⬜ | | |
| TC013 | Batch Solve | ⬜ | | |
| TC014 | Batch Excel Export | ⬜ | | |
| TC018 | End-to-End | ⬜ | | |

**Legend:**
- ⬜ Not Started
- ✅ Passed
- ❌ Failed
- ⚠️ Partial/Warning

---

## 📝 Test Session Log

**Date:** _________________  
**Tester:** _________________  
**Environment:** _________________

### Pre-Test
- [ ] Environment setup complete
- [ ] All dependencies installed
- [ ] Server can start successfully

### During Test
**Issues Found:**
1. _____________________________________________________________
2. _____________________________________________________________
3. _____________________________________________________________

**Notes:**
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________

### Post-Test
- [ ] All critical tests passed
- [ ] Test report generated
- [ ] Issues documented
- [ ] Excel exports verified
- [ ] Code coverage acceptable

---

## 🚀 Quick Test Commands

```bash
# Full test suite
python test_complete_scenarios.py --all

# Only unit tests
python test_complete_scenarios.py --unit

# Only performance tests
python test_complete_scenarios.py --performance

# Start web server for manual tests
python app.py

# Quick smoke test
python test_all.py
```

---

## ✅ Sign-Off

**Automated Tests:**
- [ ] All unit tests PASSED
- [ ] Performance tests PASSED
- [ ] Test report reviewed: `test_results/test_report_*.txt`

**Manual Tests:**
- [ ] Web UI functional
- [ ] All workflows complete successfully
- [ ] Excel exports verified
- [ ] No critical bugs found

**Final Approval:**
- [ ] Ready for demo
- [ ] Ready for production use
- [ ] Documentation complete

**Tester Signature:** _________________  
**Date:** _________________  
**Status:** [ ] APPROVED  [ ] REJECTED

---

## 📞 Support Contacts

**Technical Issues:**
- Developer Team: dev@vrpspd.com
- QA Team: qa@vrpspd.com

**Documentation:**
- `VRPSPD_TEST_SCENARIOS.md` - Detailed test scenarios
- `README_TESTING.md` - Testing guide
- `README.md` - App documentation

---

**Checklist Version:** 1.0  
**Last Updated:** 25/01/2026
