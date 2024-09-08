import streamlit as st
import requests
import uuid
import os

# Set up the Streamlit interface
page = st.title("Assignment 3 - Build LLMs Playground")
page = st.markdown("""
    Assignment 3 - ProtonX AI for devs
""")

# Generate a random session ID
session_id = str(uuid.uuid4())

# Flask API URL
base_url = "https://03b8-34-87-108-240.ngrok-free.app"

def test_generate_video(image_url, input_question):
    # Endpoint for generating video
    generate_url = f"{base_url}/generate-answer"

    # Sending the POST request with the image URL
    response = requests.post(generate_url, json={
        "image_url": image_url,
        "input_question": input_question
    })

    if response.status_code == 200:
        # Get the video download URL from the response
        answer = response.json().get("answer")
        # st.session_state.video_url = f"{base_url}{video_url}"
        st.success(answer)
    else:
        st.error(f"Failed to generate video: {response.json()}")

# Sidebar settings for model, temperature, and top_p
with st.sidebar:
    st.session_state.selected_model = st.selectbox("Select Model", ["gpt-4o", "gpt-4"])
    st.write("You selected:", st.session_state.selected_model)

    st.session_state.temperature = st.slider("Set Temperature", min_value=0.0, max_value=1.0, step=0.1, value=0.5)
    st.write("Current Temperature:", st.session_state.temperature)

    st.session_state.top_p = st.slider("Set Top p", min_value=0.0, max_value=1.0, step=0.1, value=0.9)
    st.write("Current Top p:", st.session_state.top_p)

    st.image("https://storage.googleapis.com/mle-courses-prod/users/61b6fa1ba83a7e37c8309756/private-files/678dadd0-603b-11ef-b0a7-998b84b38d43-ProtonX_logo_horizontally__1_.png", width=100) 

# Main content
image_url = st.text_input("Enter Image URL", "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/bee.JPG?download=true")
input_question = st.text_input("Enter input_question", "What color is the flower that bee is standing on?")

# Display the image from the image_url
if image_url:
    st.image(image_url, caption="Image from URL", use_column_width=True)

if st.button("Q&A for Video"):
    test_generate_video(image_url, input_question)