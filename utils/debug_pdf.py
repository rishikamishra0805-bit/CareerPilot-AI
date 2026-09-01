import fitz

def test_pdf_extraction(pdf_path):
    """
    PDF extraction test karein
    """
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text += page.get_text()
        doc.close()
        
        print(f"Total pages: {len(doc)}")
        print(f"Total characters extracted: {len(text)}")
        print("\n--- FIRST 500 CHARACTERS ---")
        print(text[:500])
        print("\n--- SKILLS SEARCH ---")
        
        skills = ['python', 'java', 'c++', 'sql', 'react', 'tensorflow', 'aws', 'docker', 'html', 'css']
        found = []
        for skill in skills:
            if skill in text.lower():
                found.append(skill)
        
        print(f"Skills found: {found}")
        
        return text
        
    except Exception as e:
        print(f"Error: {e}")
        return None

# Test your resume
if __name__ == "__main__":
    # Uploaded file ka path dena hoga
    # Example: test_pdf_extraction("C:/Users/Rishika mishra/Desktop/Rishika...99 res.pdf")
    pass