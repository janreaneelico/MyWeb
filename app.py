import streamlit as st
from PIL import Image

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_icon=":wave:", layout="wide")

# Define your background image URL from GitHub repository (use the direct link to the raw image file)
background_image_url = "https://raw.githubusercontent.com/janreaneelico/MyWeb/main/PC.jpg"

# Apply the background image using custom CSS
background_style = f"""
    <style>
        .stApp {{
            background-image: url('{background_image_url}');
            background-size: cover;
            background-repeat: no-repeat;
        }}
        .css-17eq0hr, .css-1v1k8g1, .css-1be9khp {{
            color: black !important;
        }}
    </style>
"""
st.markdown(background_style, unsafe_allow_html=True)

img = Image.open("Me.jpg")
st.image(img, width=600, channels="RGB")

# Set the title for the webpage
st.title("ELICO'S BLOG")

st.header("Hi, I'm Jan Reane L. Elico and Welcome To my Blog :wave:, \n Here where you'll learn more about me")
st.header("I'm a 1st Year College Student in BSCPE Course")
st.write("I choose this course because it's all about Computer, which is related to my strand when I was in Grade 12 ICT")
st.write("Message me on Facebook [Click here >](https://www.facebook.com/profile.php?id=100094491770218)")

st.write("---")
st.header("About me:")
st.write("##")
st.write(
    """
    - The multifaceted world of programming beckons me with its promise of limitless possibilities. 
    - In my pursuit of knowledge, I intend to immerse myself in various programming languages such as Python, Java, and C++, unraveling their unique syntax and functionalities. 
    - Beyond the syntax, I am eager to comprehend the underlying principles that govern the creation of software solutions. Through hands-on projects and practical applications, I aim to hone my coding skills, fostering a mastery that extends beyond theoretical knowledge.
    - Furthermore, my curiosity extends to the broader landscape of computers. I am intrigued by the intricate interplay of hardware and software, and I am determined to explore the symbiotic relationship between the two. 
    - From the fundamentals of computer architecture to the intricacies of operating systems, my quest for knowledge encompasses the holistic understanding of computers. In essence, my journey in programming and coding is not merely about acquiring skills but about cultivating a profound appreciation for the art and science of computational thinking. 
    - With each line of code written and every algorithm deciphered, I am poised to unravel the vast tapestry that is the world of programming and computers.
    """
)

st.write("---")
st.header("More Info About me:")
st.write("##")
st.write(
    """
    - In my pursuit of knowledge, I intend to immerse myself in various programming languages such as Python, Java, and C++, unraveling their unique syntax and functionalities. 
    - Beyond the syntax, I am eager to comprehend the underlying principles that govern the creation of software solutions. Through hands-on projects and practical applications, I aim to hone my coding skills, fostering a mastery that extends beyond theoretical knowledge.
    - Furthermore, my curiosity extends to the broader landscape of computers. I am intrigued by the intricate interplay of hardware and software, and I am determined to explore the symbiotic relationship between the two. 
    - From the fundamentals of computer architecture to the intricacies of operating systems, my quest for knowledge encompasses the holistic understanding of computers. In essence, my journey in programming and coding is not merely about acquiring skills but about cultivating a profound appreciation for the art and science of computational thinking. 
    - With each line of code written and every algorithm deciphered, I am poised to unravel the vast tapestry that is the world of programming and computers.
    """
)

st.image("https://raw.githubusercontent.com/YourGitHubUsername/YourRepositoryName/main/path/to/your/background_image.jpg", use_column_width=True)
