import re
import argparse
import os

def extract_markdown_links(input_file, output_file):
    """
    Trích xuất tất cả các đường link từ tệp Markdown và lưu vào tệp đầu ra.

    :param input_file: Đường dẫn đến tệp Markdown đầu vào.
    :param output_file: Đường dẫn đến tệp văn bản để lưu các link.
    """
    # Biểu thức chính quy để tìm các link trong cú pháp Markdown: [text](link)
    link_pattern = re.compile(r'\[.*?\]\((.*?)\)')

    try:
        # Đảm bảo tệp đầu vào tồn tại
        if not os.path.exists(input_file):
            print(f"Lỗi: Tệp đầu vào '{input_file}' không tồn tại.")
            return

        with open(input_file, 'r', encoding='utf-8') as f_in, \
             open(output_file, 'w', encoding='utf-8') as f_out:
            
            content = f_in.read()
            links = link_pattern.findall(content)

            if not links:
                print(f"Thông báo: Không tìm thấy đường link nào trong '{input_file}'.")
                # Vẫn tạo tệp đầu ra nhưng để trống
                return

            for link in links:
                f_out.write(link + '\n')
            
            print(f"✅ Hoàn tất! Đã trích xuất {len(links)} link và lưu vào tệp '{output_file}'.")

    except Exception as e:
        print(f"Đã xảy ra lỗi không mong muốn: {e}")

def main():
    # --- Thiết lập trình phân tích đối số dòng lệnh ---
    parser = argparse.ArgumentParser(
        description="Một công cụ CLI để trích xuất toàn bộ link từ tệp Markdown.",
        epilog="Ví dụ: python extract_links.py my_document.md my_links.txt"
    )
    
    # Đối số bắt buộc: tệp đầu vào
    parser.add_argument("input_file", help="Đường dẫn đến tệp Markdown nguồn.")
    
    # Đối số tùy chọn: tệp đầu ra
    # nargs='?' có nghĩa là đối số này có thể có hoặc không.
    parser.add_argument("output_file", nargs='?', default=None, help="(Tùy chọn) Tên tệp để lưu kết quả.")
    
    args = parser.parse_args()
    
    # --- Xử lý logic tên tệp ---
    input_filename = args.input_file
    output_filename = args.output_file
    
    # Nếu người dùng không cung cấp tên tệp đầu ra
    if output_filename is None:
        # Lấy tên tệp gốc (không bao gồm đuôi) và thêm đuôi .txt
        base_name = os.path.splitext(input_filename)[0]
        output_filename = f"{base_name}.txt"
        print(f"Tên tệp đầu ra không được cung cấp. Tự động sử dụng: '{output_filename}'")

    # Gọi hàm xử lý chính
    extract_markdown_links(input_filename, output_filename)

# --- Điểm bắt đầu của chương trình ---
if __name__ == "__main__":
    main()