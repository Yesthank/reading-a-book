import tkinter as tk
from tkinter import ttk

class BookListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("2024 읽은 책 리스트")
        self.setup_cover_page()

    def setup_cover_page(self):
        """표지 페이지를 설정합니다."""
        self.cover_frame = tk.Frame(self.root)
        self.cover_frame.pack(fill="both", expand=True)
        
        title_label = tk.Label(self.cover_frame, text="2024 읽은 책 리스트", font=("Arial", 24))
        title_label.pack(pady=20)
        
        next_page_button = tk.Button(self.cover_frame, text="→", command=self.setup_book_page)
        next_page_button.pack(side="right", padx=10)

    def setup_book_page(self):
        """읽은 책 목록 페이지를 설정합니다. 이 예제에서는 하나의 책 페이지만 생성합니다."""
        # 기존 표지 프레임을 삭제합니다.
        self.cover_frame.destroy()
        
        # 책 페이지 프레임을 생성합니다.
        self.book_frame = tk.Frame(self.root)
        self.book_frame.pack(fill="both", expand=True)
        
        # 개요 섹션
        overview_frame = tk.Frame(self.book_frame)
        overview_frame.pack(fill="x", expand=True, pady=(20, 0))
        
        title_entry = tk.Entry(overview_frame, font=("Arial", 16))
        title_entry.pack(side="left", fill="x", expand=True, padx=(10, 0))
        title_entry.insert(0, "책 제목 입력")
        
        # 별점 기능과 사진 첨부 기능은 추가 구현이 필요합니다.
        
        # 내용 섹션
        content_text = tk.Text(self.book_frame, height=10)
        content_text.pack(fill="both", expand=True, padx=10, pady=10)
        content_text.insert("1.0", "여기에 읽은 내용을 작성하세요.")

def main():
    root = tk.Tk()
    app = BookListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
