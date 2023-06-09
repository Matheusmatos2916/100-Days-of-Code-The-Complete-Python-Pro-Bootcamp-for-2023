import PyPDF2
 
from gtts import gTTS
 
import os
 
 
 
def pdf_to_speech(pdf_path, output_path):
 
    # Extract text from the PDF
 
    with open(pdf_path, 'rb') as file:
 
        pdf_reader = PyPDF2.PdfReader(file)
 
        text = ''
 
        for page in pdf_reader.pages:
 
            text += page.extract_text()
 
 
 
    # Convert text to speech
 
    tts = gTTS(text=text, lang='pt-br')
 
 
 
    # Save the speech as an audio file
 
    tts.save(output_path)
 
 
 
    # Play the speech using the default audio player
 
    os.system(f'start {output_path}')
 
 
 
if __name__ == '__main__':
 
    pdf_path = 'teste.pdf'  # Replace with your PDF file path
 
    output_path = 'output.mp3'  # Replace with the desired output path and file name
 
 
 
    pdf_to_speech(pdf_path, output_path)
 
 
 