import lxml.html
import re
import json
from mln122_keywords import CH_KEYWORDS

CHAPTER_NAMES = {
    1: "Chương 1: Đối tượng, phương pháp nghiên cứu và chức năng của Kinh tế chính trị Mác - Lênin",
    2: "Chương 2: Hàng hóa, thị trường và vai trò của các chủ thể tham gia thị trường",
    3: "Chương 3: Giá trị thặng dư trong nền kinh tế thị trường",
    4: "Chương 4: Cạnh tranh và độc quyền trong nền kinh tế thị trường",
    5: "Chương 5: Kinh tế thị trường định hướng xã hội chủ nghĩa và các quan hệ lợi ích kinh tế ở Việt Nam",
    6: "Chương 6: Công nghiệp hóa, hiện đại hóa và hội nhập kinh tế quốc tế của Việt Nam"
}

def element_to_text(el):
    html_str = lxml.html.tostring(el, encoding='utf-8').decode('utf-8')
    html_str = re.sub(r'<\s*br\s*/?>', '\n', html_str, flags=re.I)
    html_str = re.sub(r'<\s*/p\s*>', '\n', html_str, flags=re.I)
    html_str = re.sub(r'<\s*/div\s*>', '\n', html_str, flags=re.I)
    temp_tree = lxml.html.fromstring(f'<div>{html_str}</div>')
    text = temp_tree.text_content()
    lines = [line.strip() for line in text.split('\n')]
    return '\n'.join([l for l in lines if l])

def clean_noise(text):
    text = re.sub(r'\(?\s*NHUNG\s+HOÀNG\s*\)?', '', text, flags=re.I)
    text = re.sub(r'\(?\s*\d{3}[-\s]?\d{3}[-\s]?\d{4}\s*\)?', '', text)
    return text.strip()

def classify_q(text):
    t = text.lower()
    score = {ch: 0 for ch in CH_KEYWORDS}
    for ch, kws in CH_KEYWORDS.items():
        for kw in kws:
            if kw in t:
                score[ch] += len(kw)
    best = max(score, key=score.get)
    return best if score[best] > 0 else 2

def build_dataset():
    p = r"c:\Users\dathn\Downloads\MLN122 - CHUẨN NHUNG HOÀNG Flashcards _ Quizlet.html"
    with open(p, "r", encoding="utf-8", errors="ignore") as f:
        raw_html = f.read()

    tree = lxml.html.fromstring(raw_html)
    term_elements = tree.xpath('//div[@aria-label="Term" and contains(@class, "SetPageTermsList-term")]')

    questions_data = []

    for idx, el in enumerate(term_elements, 1):
        sides = el.xpath('.//div[@data-testid="set-page-term-card-side"]')
        q_raw = element_to_text(sides[0])
        a_raw = element_to_text(sides[1])

        q_lines = [l.strip() for l in q_raw.split('\n') if l.strip()]
        q_text_parts = []
        options = {}
        
        current_opt = None
        for line in q_lines:
            line_clean = clean_noise(line)
            if not line_clean:
                continue
            opt_match = re.match(r'^([A-Ea-e])\s*[\.\:\)]\s*(.*)$', line_clean)
            if opt_match:
                current_opt = opt_match.group(1).upper()
                options[current_opt] = clean_noise(opt_match.group(2).strip())
            elif current_opt:
                options[current_opt] += " " + line_clean
            else:
                q_text_parts.append(line_clean)
                
        question_text = " ".join(q_text_parts).strip()
        
        a_lines = [clean_noise(l) for l in a_raw.split('\n') if clean_noise(l)]
        first_a_line = a_lines[0] if a_lines else ""
        ans_extra = "\n".join(a_lines[1:]) if len(a_lines) > 1 else ""
        
        ans_key = ""
        m_multi = re.match(r'^([A-Ea-e,\s]+)', first_a_line)
        if m_multi:
            letters = re.findall(r'[A-Ea-e]', m_multi.group(1))
            seen = []
            for let in letters:
                u = let.upper()
                if u not in seen and u in 'ABCDE':
                    seen.append(u)
            if seen:
                ans_key = "".join(seen)
                
        if not ans_key:
            letters = re.findall(r'\b([A-E])\b', first_a_line.upper())
            if letters:
                ans_key = letters[0]

        # Build ans_text
        if len(ans_key) > 1:
            ans_parts = [f"{k}. {options[k]}" if k in options else k for k in ans_key]
            ans_text = " | ".join(ans_parts)
        elif len(ans_key) == 1:
            k = ans_key
            ans_text = f"{k}. {options[k]}" if k in options else k
        else:
            ans_text = first_a_line

        ch_num = classify_q(q_raw + "\n" + a_raw)
        chapter_title = CHAPTER_NAMES[ch_num]

        questions_data.append({
            "id": idx,
            "chapter": chapter_title,
            "question": question_text,
            "options": options,
            "ans_key": ans_key,
            "ans_text": ans_text,
            "ans_extra": ans_extra
        })

    return questions_data

if __name__ == "__main__":
    data = build_dataset()
    print(f"Built {len(data)} questions.")
    
    # Save MLN122_540_Cau_Hoi_Va_Dap_An.json
    out_540 = r"c:\Users\dathn\Downloads\MLN111\MLN122_540_Cau_Hoi_Va_Dap_An.json"
    with open(out_540, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # Save to MLN122_133_Cau_Hoi_Va_Dap_An.json for backwards compatibility
    out_133 = r"c:\Users\dathn\Downloads\MLN111\MLN122_133_Cau_Hoi_Va_Dap_An.json"
    with open(out_133, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # Generate Markdown
    md = ["# NGÂN HÀNG 540 CÂU HỎI TRẮC NGHIỆM & ĐÁP ÁN KINH TẾ CHÍNH TRỊ MÁC - LÊNIN (MLN122)\n"]
    for item in data:
        md.append(f"### Câu {item['id']}: {item['question']}\n*{item['chapter']}*\n")
        for k in sorted(item["options"].keys()):
            md.append(f"- **{k}.** {item['options'][k]}")
        md.append(f"\n👉 **Đáp án đúng:** {item['ans_text']}")
        if item["ans_extra"]:
            md.append(f"💡 *Ghi chú:* {item['ans_extra']}")
        md.append("\n---\n")

    md_str = "\n".join(md)
    for path in [
        r"c:\Users\dathn\Downloads\MLN111\MLN122_540_Cau_Hoi_Va_Dap_An.md",
        r"c:\Users\dathn\Downloads\MLN111\MLN122_133_Cau_Hoi_Va_Dap_An.md"
    ]:
        with open(path, "w", encoding="utf-8") as f:
            f.write(md_str)
    print("Files written successfully.")
