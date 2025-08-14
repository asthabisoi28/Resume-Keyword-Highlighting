import fitz  # PyMuPDF
import re

# Function to extract text from PDF
def extract_text_from_pdf(path):
    doc = fitz.open(path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Function to highlight keywords in text (case-insensitive, word boundaries)
def highlight_keywords(text, keywords):
    for kw in keywords:
        # Regex matches whole words, ignoring case
        pattern = re.compile(r'(?i)(?<!\w)(' + re.escape(kw) + r')(?!\w)')
        text = pattern.sub(r'<mark>\1</mark>', text)
    return text

# Read keywords from keywords.txt file
with open("keywords.txt", "r", encoding="utf-8") as f:
    keywords = [line.strip() for line in f if line.strip()]

# Extract resume text from your PDF (replace with your PDF filename)
resume_text = extract_text_from_pdf("Astha_resume.pdf")
resume_text = resume_text.replace('\n', ' ')  # Remove newlines for better matching

# Highlight keywords in the resume text
highlighted_text = highlight_keywords(resume_text, keywords)

# Prepare HTML content with CSS to highlight keywords in yellow
# ... after highlight_keywords call ...

html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Highlighted Resume</title>
<style>
  body {{
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background-color: #f9f9f9;
    padding: 30px;
    color: #333;
  }}
  .container {{
    max-width: 800px;
    margin: auto;
    background: white;
    padding: 25px 40px;
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  }}
  h1 {{
    text-align: center;
    color: #444;
    margin-bottom: 30px;
  }}
  p {{
    line-height: 1.6;
    margin-bottom: 16px;
  }}
  mark {{
    background-color: #fff176; /* softer yellow */
    padding: 0 3px;
    border-radius: 3px;
  }}
</style>
</head>
<body>
  <div class="container">
    <h1>Resume Keyword Highlighting</h1>
    <p>{highlighted_text}</p>
  </div>
</body>
</html>
"""

with open("highlighted_resume.html", "w", encoding="utf-8") as f:
    f.write(html_content)


print("✅ Resume highlighting complete! Open 'highlighted_resume.html' in your browser.")
