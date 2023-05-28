import tkinter as tk

def analyze_text():
    text = text_box.get("1.0", "end-1c")

    if text:
        separated_words = text.split()
        word_count = {}
        
        for word in separated_words:
            # Count occurrences of each word
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        # Print the word count with duplicates represented as 'word (count)'
        for word, count in word_count.items():
            if count > 1:
                print(f"{word} ({count})")
            else:
                print(word)
    else:
        print("No text entered.")

# Tkinter 창 생성
window = tk.Tk()
window.title("Text Analyzer")

# 텍스트 박스 생성
text_box = tk.Text(window, height=10, width=50)
text_box.pack()

# 분석 버튼 생성
analyze_button = tk.Button(window, text="Analyze Text", command=analyze_text)
analyze_button.pack()

# Tkinter 창 실행
window.mainloop()