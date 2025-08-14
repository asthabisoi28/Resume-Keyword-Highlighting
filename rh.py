import fitz  # PyMuPDF

# === Step 1: Read keywords from a text file ===
with open("keywords.txt", "r", encoding="utf-8") as f:
    keywords = [line.strip() for line in f if line.strip()]

# === Step 2: Load the resume PDF ===
input_pdf = "resume.pdf"
output_pdf = "highlighted_resume.pdf"
doc = fitz.open(input_pdf)

# === Step 3: Highlight keywords in each page ===
for page in doc:
    for kw in keywords:
        # Case-insensitive search for each keyword
        text_instances = page.search_for(kw, flags=fitz.TEXT_IGNORECASE)
        for inst in text_instances:
            highlight = page.add_highlight_annot(inst)
            highlight.set_colors(stroke=(1, 1, 0))  # yellow highlight
            highlight.update()

# === Step 4: Save the modified PDF ===
doc.save(output_pdf, garbage=4, deflate=True)
doc.close()

print(f"✅ Highlighted resume saved as '{output_pdf}'")
