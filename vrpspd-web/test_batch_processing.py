"""
Test script for Batch Processing
Kiểm tra tính năng batch processing với nhiều file
"""

from algorithms.batch_processor import process_batch_files, create_batch_summary
from algorithms.batch_excel_export import create_batch_excel_report
import os

def create_sample_test_files():
    """Tạo sample files cho testing (giả lập từ file thật)."""
    # Giả sử ta có các file đã upload
    # Trong test thực tế, bạn sẽ upload files từ folder Others/ hoặc folder khác
    
    # Tìm file .txt trong workspace
    test_files = []
    search_paths = ['d:/GR2-VRP4', 'd:/GR2-VRP4/Others']
    
    for path in search_paths:
        if os.path.exists(path):
            for file in os.listdir(path):
                if file.endswith('.txt'):
                    full_path = os.path.join(path, file)
                    test_files.append({
                        'filename': file,
                        'filepath': full_path
                    })
                    if len(test_files) >= 3:  # Chỉ lấy 3 files để test
                        break
        if len(test_files) >= 3:
            break
    
    return test_files

if __name__ == '__main__':
    print("=" * 60)
    print("Testing Batch Processing")
    print("=" * 60)
    
    # Get test files
    test_files = create_sample_test_files()
    
    if len(test_files) == 0:
        print("❌ Không tìm thấy file .txt nào để test")
        print("Vui lòng đặt file .txt trong folder d:/GR2-VRP4/ hoặc d:/GR2-VRP4/Others/")
        exit(1)
    
    print(f"\n✓ Tìm thấy {len(test_files)} files:")
    for i, f in enumerate(test_files, 1):
        print(f"  {i}. {f['filename']}")
    
    # Test batch processing
    print("\n" + "-" * 60)
    print("Testing process_batch_files()...")
    print("-" * 60)
    
    try:
        algorithms = ['savings', 'vnd']
        batch_results = process_batch_files(test_files, algorithms)
        
        print(f"✓ Batch processing completed!")
        print(f"  - Total files processed: {len(batch_results)}")
        
        successful = sum(1 for r in batch_results if r['success'])
        failed = sum(1 for r in batch_results if not r['success'])
        
        print(f"  - Successful: {successful}")
        print(f"  - Failed: {failed}")
        
        # Show details
        print("\nDetailed Results:")
        for i, result in enumerate(batch_results, 1):
            print(f"\n{i}. {result['filename']}:")
            if result['success']:
                savings_cost = result['results']['savings']['total_cost']
                vnd_cost = result['results']['vnd']['total_cost']
                improvement = result['results']['vnd'].get('improvement', 0)
                
                print(f"   Savings Cost: {savings_cost:.2f}")
                print(f"   VND Cost: {vnd_cost:.2f}")
                print(f"   Improvement: {improvement:.2f}%")
            else:
                print(f"   ❌ Error: {result['error']}")
        
    except Exception as e:
        print(f"❌ Batch processing failed: {e}")
        import traceback
        traceback.print_exc()
        exit(1)
    
    # Test summary
    print("\n" + "-" * 60)
    print("Testing create_batch_summary()...")
    print("-" * 60)
    
    try:
        summary = create_batch_summary(batch_results)
        
        print("✓ Summary created!")
        print(f"  - Total files: {summary['total_files']}")
        print(f"  - Successful: {summary['successful']}")
        print(f"  - Failed: {summary['failed']}")
        print(f"  - Avg Improvement: {summary['avg_improvement']:.2f}%")
        print(f"  - Total Savings Cost: {summary['total_cost_savings']:.2f}")
        print(f"  - Total VND Cost: {summary['total_cost_vnd']:.2f}")
        
    except Exception as e:
        print(f"❌ Summary creation failed: {e}")
        import traceback
        traceback.print_exc()
        exit(1)
    
    # Test Excel export
    print("\n" + "-" * 60)
    print("Testing create_batch_excel_report()...")
    print("-" * 60)
    
    try:
        filepath = create_batch_excel_report(
            batch_results=batch_results,
            summary=summary,
            filename='TEST_Batch_Results.xlsx'
        )
        
        print(f"✓ Batch Excel created successfully!")
        print(f"  - File path: {filepath}")
        
        if os.path.exists(filepath):
            file_size = os.path.getsize(filepath)
            print(f"  - File size: {file_size} bytes")
        
        print(f"\nCheck the file at: {os.path.abspath(filepath)}")
        
    except Exception as e:
        print(f"❌ Batch Excel export failed: {e}")
        import traceback
        traceback.print_exc()
        exit(1)
    
    print("\n" + "=" * 60)
    print("✅ ALL TESTS PASSED!")
    print("=" * 60)
    print("\nBatch processing is ready to use in web app!")
