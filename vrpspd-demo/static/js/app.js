// ============================================
// STEP 1: Global Variables
// ============================================
let currentFilepath = null;
let currentResults = null;
let currentProblemInfo = null; // Store problem info for export

let currentVisualization = null;

// STEP 4: Batch Processing Variables
let currentMode = 'single'; // 'single' or 'batch'
let batchFiles = []; // Store batch uploaded files
let batchResults = null; // Store batch results

const fileInput = document.getElementById('fileInput');
const solveBtn = document.getElementById('solveBtn');
const solveBtnText = document.getElementById('solveBtnText');
const loadingIndicator = document.getElementById('loadingIndicator');
const resultsContainer = document.getElementById('resultsContainer');
const problemInfo = document.getElementById('problemInfo');
const singleModeResults = document.getElementById('singleModeResults');

const fullscreenBtn = document.getElementById('fullscreenBtn');
const fullscreenModal = document.getElementById('fullscreenModal');
const closeFullscreenBtn = document.getElementById('closeFullscreenBtn');

const exportBtn = document.getElementById('exportBtn');
const exportBtnText = document.getElementById('exportBtnText');

const batchFileInput = document.getElementById('batchFileInput');
const modeSingle = document.getElementById('modeSingle');
const modeBatch = document.getElementById('modeBatch');
const singleFileUpload = document.getElementById('singleFileUpload');
const batchFileUpload = document.getElementById('batchFileUpload');
const batchFileList = document.getElementById('batchFileList');
const batchResultsDiv = document.getElementById('batchResults');
const batchResultsContainer = document.getElementById('batchResultsContainer');
const batchLoadingIndicator = document.getElementById('batchLoadingIndicator');
const batchProgress = document.getElementById('batchProgress');

fileInput.addEventListener('change', handleFileUpload);
solveBtn.addEventListener('click', handleSolve);

fullscreenBtn.addEventListener('click', openFullscreen);
closeFullscreenBtn.addEventListener('click', closeFullscreen);

exportBtn.addEventListener('click', handleExport);

batchFileInput.addEventListener('change', handleBatchFileUpload);
modeSingle.addEventListener('change', handleModeChange);
modeBatch.addEventListener('change', handleModeChange);

// ESC key to close fullscreen
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && fullscreenModal.classList.contains('show')) {
        closeFullscreen();
    }
});

async function handleFileUpload(event) {
    const file = event.target.files[0];
    if (!file) return;

    const formData = new FormData();
    formData.append('file', file);

    loadingIndicator.style.display = 'block';
    solveBtn.disabled = true;

    try {
        const response = await fetch('/api/upload', {
            method: 'POST',
            body: formData
        });

        const result = await response.json();

        if (result.success) {
            currentFilepath = result.filepath;
            
            // Display problem info
            document.getElementById('numCustomers').textContent = result.data.num_customers;
            document.getElementById('numVehicles').textContent = result.data.num_vehicles;
            document.getElementById('capacity').textContent = result.data.capacity;
            problemInfo.style.display = 'block';

            // Enable solve button
            solveBtn.disabled = false;

            showNotification('File uploaded successfully!', 'success');
        } else {
            showNotification('Error: ' + result.error, 'danger');
        }
    } catch (error) {
        showNotification('Upload failed: ' + error.message, 'danger');
    } finally {
        loadingIndicator.style.display = 'none';
    }
}

async function handleSolve() {

    // STEP 4: Check mode
    if (currentMode === 'batch') {
        await handleBatchSolve();
        return;
    }

    // STEP 1: Single mode
    if (!currentFilepath) {
        showNotification('Please upload a file first', 'warning');
        return;
    }

    // STEP 1: Get selected algorithms
    const algorithms = [];
    if (document.getElementById('algoSavings').checked) {
        algorithms.push('savings');
    }
    if (document.getElementById('algoVND').checked) {
        algorithms.push('vnd');
    }

    if (algorithms.length === 0) {
        showNotification('Please select at least one algorithm', 'warning');
        return;
    }

    loadingIndicator.style.display = 'block';
    solveBtn.disabled = true;

    try {
        const response = await fetch('/api/solve', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                filepath: currentFilepath,
                algorithms: algorithms
            })
        });

        const result = await response.json();

        if (result.success) {
            // STEP 1: Store results and display
            currentResults = result.results;
            currentProblemInfo = result.problem_info; // Store problem info
            displayResults(result.results, result.problem_info);

            // STEP 2: Render visualization if available
            if (result.visualization) {
                currentVisualization = result.visualization;
                renderVisualization(result.visualization);
                fullscreenBtn.style.display = 'inline-block'; // Show fullscreen button
            }

            // STEP 3: Enable export button
            exportBtn.disabled = false;
            showNotification('Solved successfully!', 'success');
        } else {
            showNotification('Solve failed: ' + result.error, 'danger');
            console.error(result.traceback);
        }
    } catch (error) {
        showNotification('Solve failed: ' + error.message, 'danger');
    } finally {
        loadingIndicator.style.display = 'none';
        solveBtn.disabled = false;
    }
}

function displayResults(results, problemInfo) {
    let html = '';

    // Comparison Table
    if (results.savings && results.vnd) {
        html += `
            <h5>So sánh thuật toán</h5>
            <table class="table table-bordered comparison-table">
                <thead>
                    <tr>
                        <th>Thuật toán</th>
                        <th>Chi phí</th>
                        <th>Số tuyến</th>
                        <th>Thời gian (s)</th>
                        <th>Cải thiện</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>Savings</strong></td>
                        <td>${results.savings.total_cost}</td>
                        <td>${results.savings.num_routes}</td>
                        <td>${results.savings.computation_time}</td>
                        <td>-</td>
                    </tr>
                    <tr class="table-success">
                        <td><strong>Savings + VND</strong></td>
                        <td><strong>${results.vnd.total_cost}</strong></td>
                        <td>${results.vnd.num_routes}</td>
                        <td>${results.vnd.computation_time}</td>
                        <td>
                            <span class="badge bg-success badge-improvement">
                                ${results.vnd.improvement}%
                            </span>
                        </td>
                    </tr>
                </tbody>
            </table>
        `;
    } else if (results.savings) {
        html += `
            <h5>Kết quả Savings Algorithm</h5>
            <table class="table table-bordered">
                <tr><th>Chi phí tối ưu</th><td>${results.savings.total_cost}</td></tr>
                <tr><th>Số tuyến</th><td>${results.savings.num_routes}</td></tr>
                <tr><th>Thời gian tính toán</th><td>${results.savings.computation_time} s</td></tr>
            </table>
        `;
    } else if (results.vnd) {
        html += `
            <h5>Kết quả VND Algorithm</h5>
            <table class="table table-bordered">
                <tr><th>Chi phí tối ưu</th><td>${results.vnd.total_cost}</td></tr>
                <tr><th>Số tuyến</th><td>${results.vnd.num_routes}</td></tr>
                <tr><th>Thời gian tính toán</th><td>${results.vnd.computation_time} s</td></tr>
            </table>
        `;
    }

    // Route Details (use best result) - Collapsible
    const bestResult = results.vnd || results.savings;
    if (bestResult) {
        html += `
            <div class="mt-4">
                <div class="d-flex justify-content-between align-items-center mb-2">
                    <h5 class="mb-0">Chi tiết các tuyến</h5>
                    <button class="btn btn-sm btn-outline-primary" type="button" data-bs-toggle="collapse" data-bs-target="#routeDetailsCollapse">
                        <i class="fas fa-chevron-down"></i> Xem chi tiết
                    </button>
                </div>
                <div class="collapse" id="routeDetailsCollapse">
        `;
        
        bestResult.route_details.forEach(route => {
            html += `
                <div class="route-detail">
                    <h6>Route ${route.route_number}</h6>
                    <p><strong>Tuyến:</strong> ${route.route_with_depot.join(' → ')}</p>
                    <p><strong>Khoảng cách:</strong> ${route.distance}</p>
                    <p><strong>Giao hàng:</strong> ${route.total_delivery} | <strong>Nhận hàng:</strong> ${route.total_pickup}</p>
                </div>
            `;
        });
        
        html += `
                </div>
            </div>
        `;
    }

    resultsContainer.innerHTML = html;

    // Add event listener for collapse button
    const collapseButton = document.querySelector('[data-bs-target="#routeDetailsCollapse"]');
    if (collapseButton) {
        const collapseElement = document.getElementById('routeDetailsCollapse');
        collapseElement.addEventListener('show.bs.collapse', function () {
            collapseButton.innerHTML = '<i class="fas fa-chevron-up"></i> Thu gọn';
        });
        collapseElement.addEventListener('hide.bs.collapse', function () {
            collapseButton.innerHTML = '<i class="fas fa-chevron-down"></i> Xem chi tiết';
        });
    }

    // TODO: Render visualization
    // renderVisualization(bestResult);
}

async function handleBatchExport() {
    if (!batchResults) {
        showNotification('No batch results to export', 'warning');
        return;
    }
    
    try {
        exportBtn.disabled = true;
        showNotification('Đang tạo Master Excel...', 'info');
        
        // Generate filename with timestamp
        const timestamp = new Date().toISOString().replace(/[-:]/g, '').split('.')[0];
        const filename = `VRPSPD_Batch_Results_${timestamp}.xlsx`;
        
        const response = await fetch('/api/batch-export-excel', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                batch_results: batchResults.batch_results,
                summary: batchResults.summary,
                filename: filename
            })
        });
        
        if (response.ok) {
            // Download file
            const blob = await response.blob();
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = filename;
            document.body.appendChild(a);
            a.click();
            window.URL.revokeObjectURL(url);
            document.body.removeChild(a);
            
            showNotification('Master Excel đã được tải xuống!', 'success');
        } else {
            const error = await response.json();
            showNotification('Batch export failed: ' + error.error, 'danger');
        }
    } catch (error) {
        showNotification('Batch export failed: ' + error.message, 'danger');
    } finally {
        exportBtn.disabled = false;
    }
}

function showNotification(message, type = 'info') {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type} alert-dismissible fade show position-fixed top-0 start-50 translate-middle-x mt-3`;
    alertDiv.style.zIndex = '9999';
    alertDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    document.body.appendChild(alertDiv);

    setTimeout(() => {
        alertDiv.remove();
    }, 5000);
}

async function handleExport() {
    // STEP 4: Check mode
    if (currentMode === 'batch') {
        await handleBatchExport();
        return;
    }
    
    // STEP 3: Single mode
    if (!currentResults) {
        showNotification('No results to export', 'warning');
        return;
    }

    try {
        exportBtn.disabled = true;
        showNotification('Đang tạo file Excel...', 'info');

        // Generate filename with timestamp
        const timestamp = new Date().toISOString().replace(/[-:]/g, '').split('.')[0];
        const filename = `VRPSPD_Results_${timestamp}.xlsx`;

        const response = await fetch('/api/export-excel', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                results: currentResults,
                problem_info: currentProblemInfo || {},
                filename: filename
            })
        });

        if (response.ok) {
            // Download file
            const blob = await response.blob();
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = filename;
            document.body.appendChild(a);
            a.click();
            window.URL.revokeObjectURL(url);
            document.body.removeChild(a);

            showNotification('File Excel đã được tải xuống!', 'success');
        } else {
            const error = await response.json();
            showNotification('Export failed: ' + error.error, 'danger');
        }
    } catch (error) {
        showNotification('Export failed: ' + error.message, 'danger');
    } finally {
        exportBtn.disabled = false;
    }
}

// ============================================
// STEP 2: Visualization with Plotly
// ============================================
function renderVisualization(plotlyFigure) {
    const plotContainer = document.getElementById('plotContainer');
    
    if (!plotlyFigure || !plotlyFigure.data) {
        plotContainer.innerHTML = '<p class="text-muted text-center mt-5">No visualization data available</p>';
        return;
    }
    
    // Clear container
    plotContainer.innerHTML = '';
    
    // Configure Plotly
    const config = {
        responsive: true,
        displayModeBar: true,
        modeBarButtonsToRemove: ['lasso2d', 'select2d'],
        displaylogo: false
    };
    
    // Create plot
    Plotly.newPlot('plotContainer', plotlyFigure.data, plotlyFigure.layout, config)
        .then(() => {
            console.log('Visualization rendered successfully');
        })
        .catch(error => {
            console.error('Error rendering visualization:', error);
            plotContainer.innerHTML = '<p class="text-danger text-center">Error rendering visualization</p>';
        });
}

// ============================================
// STEP 2: Fullscreen Functions
// ============================================
function openFullscreen() {
    if (!currentVisualization) {
        showNotification('No visualization to display', 'warning');
        return;
    }
    
    fullscreenModal.classList.add('show');
    document.body.style.overflow = 'hidden'; // Prevent scrolling
    
    // Render in fullscreen container with larger size
    const config = {
        responsive: true,
        displayModeBar: true,
        modeBarButtonsToRemove: ['lasso2d', 'select2d'],
        displaylogo: false
    };
    
    // Update layout for fullscreen
    const fullscreenLayout = {
        ...currentVisualization.layout,
        width: null,  // Auto-size to container
        height: null,
        autosize: true
    };
    
    setTimeout(() => {
        Plotly.newPlot('plotContainerFullscreen', currentVisualization.data, fullscreenLayout, config)
            .then(() => {
                console.log('Fullscreen visualization rendered');
            })
            .catch(error => {
                console.error('Error rendering fullscreen:', error);
            });
    }, 100);
}

function closeFullscreen() {
    fullscreenModal.classList.remove('show');
    document.body.style.overflow = ''; // Restore scrolling
    
    // Clear fullscreen plot
    const fullscreenContainer = document.getElementById('plotContainerFullscreen');
    if (fullscreenContainer) {
        Plotly.purge('plotContainerFullscreen');
    }
}

function handleModeChange() {
    currentMode = modeSingle.checked ? 'single' : 'batch';
    
    if (currentMode === 'single') {
        // Switch to single mode
        singleFileUpload.style.display = 'block';
        batchFileUpload.style.display = 'none';
        singleModeResults.style.display = 'block';
        batchResultsDiv.style.display = 'none';
        solveBtnText.textContent = 'Giải bài toán';
        exportBtnText.textContent = 'Xuất Excel';
        
        // Reset
        solveBtn.disabled = !currentFilepath;
        exportBtn.disabled = !currentResults;
    } else {
        // Switch to batch mode
        singleFileUpload.style.display = 'none';
        batchFileUpload.style.display = 'block';
        singleModeResults.style.display = 'none';
        batchResultsDiv.style.display = 'block';
        solveBtnText.textContent = 'Giải hàng loạt';
        exportBtnText.textContent = 'Xuất Master Excel';
        
        // Reset
        solveBtn.disabled = batchFiles.length === 0;
        exportBtn.disabled = !batchResults;
    }
}

// ============================================
// STEP 4: Batch File Upload Handler
// ============================================
async function handleBatchFileUpload(event) {
    const files = event.target.files;
    if (!files || files.length === 0) return;
    
    const formData = new FormData();
    for (let file of files) {
        formData.append('files[]', file);
    }
    
    try {
        showNotification('Đang upload files...', 'info');
        
        const response = await fetch('/api/batch-upload', {
            method: 'POST',
            body: formData
        });
        
        const result = await response.json();
        
        if (result.success) {
            batchFiles = result.files;
            displayBatchFileList(batchFiles);
            solveBtn.disabled = false;
            showNotification(`Đã upload ${result.count} files!`, 'success');
        } else {
            showNotification('Upload failed: ' + result.error, 'danger');
        }
    } catch (error) {
        showNotification('Upload failed: ' + error.message, 'danger');
    }
}

// ============================================
// STEP 4: Display Batch File List
// ============================================
function displayBatchFileList(files) {
    if (files.length === 0) {
        batchFileList.innerHTML = '';
        return;
    }
    
    let html = '<div class="alert alert-info mt-2"><strong>Files đã chọn:</strong><ul class="mb-0 mt-2">';
    files.forEach((file, index) => {
        html += `<li>${index + 1}. ${file.filename}</li>`;
    });
    html += '</ul></div>';
    
    batchFileList.innerHTML = html;
}

// ============================================
// STEP 4: Batch Solve Handler
// ============================================
async function handleBatchSolve() {
    if (batchFiles.length === 0) {
        showNotification('Chưa có file nào để xử lý', 'warning');
        return;
    }
    
    // Get selected algorithms
    const algorithms = [];
    if (document.getElementById('algoSavings').checked) algorithms.push('savings');
    if (document.getElementById('algoVND').checked) algorithms.push('vnd');
    
    if (algorithms.length === 0) {
        showNotification('Vui lòng chọn ít nhất một thuật toán', 'warning');
        return;
    }
    
    try {
        solveBtn.disabled = true;
        batchLoadingIndicator.style.display = 'block';
        batchProgress.textContent = `0/${batchFiles.length}`;
        
        const response = await fetch('/api/batch-solve', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                files: batchFiles,
                algorithms: algorithms
            })
        });
        
        const result = await response.json();
        
        if (result.success) {
            batchResults = result;
            displayBatchResults(result.batch_results, result.summary);
            exportBtn.disabled = false;
            showNotification('Batch processing hoàn tất!', 'success');
        } else {
            showNotification('Batch solve failed: ' + result.error, 'danger');
            console.error(result.traceback);
        }
    } catch (error) {
        showNotification('Batch solve failed: ' + error.message, 'danger');
    } finally {
        batchLoadingIndicator.style.display = 'none';
        solveBtn.disabled = false;
    }
}

// ============================================
// STEP 4: Display Batch Results
// ============================================
function displayBatchResults(results, summary) {
    let html = '';
    
    // Summary Card
    html += `
        <div class="alert alert-success">
            <h5><i class="fas fa-info-circle"></i> Tổng hợp</h5>
            <ul class="mb-0">
                <li>Tổng số file: ${summary.total_files}</li>
                <li>Thành công: ${summary.successful}</li>
                <li>Thất bại: ${summary.failed}</li>
                ${summary.avg_improvement > 0 ? `<li>Cải thiện trung bình: <strong>${summary.avg_improvement.toFixed(2)}%</strong></li>` : ''}
            </ul>
        </div>
    `;
    
    // Results Table
    html += `
        <table class="table table-bordered table-hover table-sm">
            <thead class="table-primary">
                <tr>
                    <th>#</th>
                    <th>File</th>
                    <th>Customers</th>
                    <th>Savings Cost</th>
                    <th>Savings Time (s)</th>
                    <th>VND Cost</th>
                    <th>VND Time (s)</th>
                    <th>Improvement</th>
                    <th>Status</th>
                </tr>
            </thead>
            <tbody>
    `;
    
    results.forEach((result, index) => {
        if (result.success) {
            const savings = result.results.savings || {};
            const vnd = result.results.vnd || {};
            const improvement = vnd.improvement || 0;
            
            html += `
                <tr>
                    <td>${index + 1}</td>
                    <td><small>${result.filename}</small></td>
                    <td>${result.problem_info.num_customers}</td>
                    <td>${savings.total_cost ? savings.total_cost.toFixed(2) : '-'}</td>
                    <td><small>${savings.computation_time ? savings.computation_time.toFixed(3) : '-'}</small></td>
                    <td>${vnd.total_cost ? vnd.total_cost.toFixed(2) : '-'}</td>
                    <td><small>${vnd.computation_time ? vnd.computation_time.toFixed(3) : '-'}</small></td>
                    <td class="${improvement > 0 ? 'text-success fw-bold' : ''}">${improvement > 0 ? improvement.toFixed(2) + '%' : '-'}</td>
                    <td><span class="badge bg-success">Success</span></td>
                </tr>
            `;
        } else {
            html += `
                <tr>
                    <td>${index + 1}</td>
                    <td><small>${result.filename}</small></td>
                    <td colspan="6"><span class="text-danger">${result.error}</span></td>
                    <td><span class="badge bg-danger">Failed</span></td>
                </tr>
            `;
        }
    });
    
    html += `
            </tbody>
        </table>
    `;
    
    batchResultsContainer.innerHTML = html;
}