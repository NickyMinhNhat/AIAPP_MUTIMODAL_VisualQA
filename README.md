# MultiModal Model for Image-Question Answering

This project is a MultiModal model for answering questions based on input images using the **PaliGemma** vision-language architecture. The system integrates advanced image and text processing capabilities through a user-friendly interface.

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Technologies](#technologies)
6. [License](#license)

## Overview
The application utilizes the **PaliGemma** vision-language model for processing and interpreting images to generate relevant text-based responses. The model combines **SigLIP-So400m** as the image encoder and **Gemma-2B** as the text decoder, leveraging pre-trained image-text pairs for enhanced performance in tasks like image captioning and segmentation.

## Features
- **Image-based Question Answering**: Users can upload images and input questions to receive context-based answers.
- **Image Captioning**: Automatically generates captions based on the uploaded images.
- **Image Segmentation**: Fine-tuned for visual segmentation tasks to better understand and describe image content.
- **Streamlit UI**: Provides an intuitive interface for users to upload images and input text prompts.
- **Flask Backend**: Handles interactions between the UI and the model, running on **Google Colab** for efficient processing.
- **Generated Responses**: Displays captions and answers in the app interface.

## Installation

To set up the project locally, follow these steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/username/paligemma-multimodal.git](https://github.com/NickyMinhNhat/AIAPP_MUTIMODAL_VisualQA.git

## Usage

1. Run file Backend (jupyter notebook) in Google Colab with GPU >= L4
2. Run file Client
   ```bash
   cd AIAPP_MUTIMODAL_VisualQA
   streamlit run client_protonX_Project3_streamlit_QAtoVideo.py


## Technologies
- Python, PaliGemma (SigLIP-So400m Gemma-2B), Streamlit, Flask, Google Colab, Ngrok.
   
