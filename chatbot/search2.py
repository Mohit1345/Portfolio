from txtai.pipeline import Similarity
from transformers import AutoTokenizer, AutoModelForQuestionAnswering

# Load the question answering model
model_name = "distilbert-base-uncased-distilled-squad"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForQuestionAnswering.from_pretrained(model_name)

# Define the context and question


context = """This pdf contains all data available in website
Website structure
Home page ( Landing page ) 
-Navbar
•	Home
•	Services
•	Contact
•	Funtime
•	Playground
-Landing page
•	Profile pic
•	Name – Mohit Chawla
•	Explore Ai, Django apps, graphic designs and creativity
-Project wheel
	Contains projects which I have made in different domains which includes
	Domain – webdev with Django
ML4CURE – this is a ml based disease prediction website ,which uses Django as backend to show data from database and dynamically update different things.
Ethfund – a blockchain based crowdfunding app which help startups to get funds through cryptocurrency and in this too we have given backend with djago.
	Domain - AI and automation
– Edict ai – which is a news to video converter – it takes a link of news article as input and convert it into video by web scrapping, news authentication, scripting which involves summarization and keyword extraction, then voice over is generated, and then we divide script into meaningful chunks based on punctuations and find keywords for each chunk and then through google image search api we search images for every chunk, and finally we merge that image to chunk and add voiceover , and video get exported likewise. Also SEO based automatic uploading functionality is added , which can automatically upload video to youtube through youtube v3 api with seo based tags and description.
	Domain – automation
Ppt to video converter – It is a python based automation app, which help us to convert a ppt to video , by making comment as voiceover and script for that particulat slide.
Web scraper pro – this is a revolutionizing project , which dosen’t require any manuall work of finding class of elements whose data we want to extract from any website, it can scrape any news article data just input will be news article link and nothing. So no manual work.

	Domain – Data science
IPL score prediction – we participated in a hackathon oragized by iit madras to predict ipl score of matches.
Youtube analytics – Through youtube api , we can find best tags for our vides, also best title and desctiption for our video, we can amnalyse multiple aspects, throught this.
	Domain – ai 
Chatbot – this chatbot to whom u are chatting now is example , which is trained with a data contained in a pdf, and now its able to chat.

Upcoming projects
1.Advacned fake news detection
2.facial search based image sorter
3.automatic video timestamp creator

SKILLS
	Html, css, bootstrap, javascript, Django , chartjs,python, pytorch, Hugging face and deep learning libraries, 

Recommendations
	Checkout automatic news to video converter
	Checkout automatic ppt to video creator 
	Checkout web scraper with no manual wort of finding class 
"""
question = "What does the fox jump over?"

# Tokenize the inputs
inputs = tokenizer.encode_plus(question, context, return_tensors="pt")

# Get the answer from the model
start_scores, end_scores = model(**inputs)
start_index = torch.argmax(start_scores)
end_index = torch.argmax(end_scores)
answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(inputs["input_ids"][0][start_index:end_index+1]))

# Print the answer
print(answer)