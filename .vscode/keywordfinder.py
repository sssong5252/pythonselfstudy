import tkinter as tk
from tkinter import messagebox

def summarize_chat():
    text = text_box.get("1.0", "end-1c")
    keywords = keyword_entry.get().strip().split(',')

    if text and keywords:
        summaries = []
        separated_sentences = text.split('. ')

        for sentence in separated_sentences:
            if any(keyword in sentence for keyword in keywords):
                summaries.append(sentence)

        if summaries:
            summary_text = '\n'.join(summaries)
            messagebox.showinfo("채팅 요약", f"키워드를 포함한 문장:\n{summary_text}")
        else:
            messagebox.showinfo("채팅 요약", "채팅 내에서 일치하는 키워드를 포함한 문장을 찾을 수 없습니다.")
    else:
        messagebox.showinfo("채팅 요약", "채팅 텍스트와 키워드를 모두 입력해주세요.")

# tkinter 창 생성
window = tk.Tk()
window.title("채팅 요약기")

# 텍스트 박스 생성
text_box = tk.Text(window, height=10, width=50)
text_box.pack()

# 붙여넣기 기능 추가
text_box.bind("<Command-v>", lambda e: text_box.event_generate("<<Paste>>"))

# 키워드 입력 필드 생성
keyword_label = tk.Label(window, text="키워드 입력 (쉼표로 구분):")
keyword_label.pack()
keyword_entry = tk.Entry(window)
keyword_entry.pack()

# 요약 버튼 생성
summarize_button = tk.Button(window, text="채팅 요약하기", command=summarize_chat)
summarize_button.pack()

# tkinter 창 실행
window.mainloop()