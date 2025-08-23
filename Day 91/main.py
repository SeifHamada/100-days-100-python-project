import PyPDF2
from gtts import gTTS

def pdf_to_audiobook(pdf_file, output_file="audiobook.mp3", language="en"):
  
    with open(pdf_file, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + " "


    if text.strip():
        tts = gTTS(text=text, lang=language, slow=False)
        tts.save(output_file)
        print(f"✅ Audiobook created successfully: {output_file}")
    else:
        print("⚠️ No text could be extracted from the PDF.")


pdf_to_audiobook("sample.pdf", "my_audiobook.mp3")
