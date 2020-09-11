
import pyttsx3 #pip install pyttsx3
import PyPDF2 #pip install PyPDF2

story = open('read_this.pdf', 'rb') #replace first argument with the name of your script make sure it's in pdf format
pdfReader = PyPDF2.PdfFileReader(story)
pages = pdfReader.numPages
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) #For male voice change the value for voices[] array subscript to '0'

for num in range(0, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    engine.say(text)
    # Blocks while processing all currently queued commands. Invokes callbacks for engine notifications appropriately.
    engine.runAndWait()