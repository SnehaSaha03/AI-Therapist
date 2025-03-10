# Smart AI Therapist

## Overview

The "Smart AI Therapist" is an innovative project aimed at providing accessible and personalized mental health support through the use of Artificial Intelligence (AI). Leveraging deep learning techniques and large language models (LLMs), this system simulates human-like interactions to offer empathetic and tailored therapeutic strategies. It addresses critical challenges in mental health care, such as accessibility and affordability, by providing 24/7 support and reaching underserved populations.

## Features

-   **Depression Prediction:** Utilizes deep learning models to predict the likelihood of depression in users based on their input.
-   **AI-Powered Therapy:** Employs various LLMs to generate optimal therapeutic responses in a friendly and accessible manner.
-   **Colloquial Language Support:** Capable of communicating in native languages (e.g., Hindi) to provide a more personalized experience.
-   **Emergency Support:** In critical situations, the system can send emails to first responders or mental health professionals.

## Project Structure

The project encompasses the following key components:

-   **Language Understanding & Response Generation (LLM-based):**
    -   LLMs generate empathetic, context-aware responses personalized to the user's emotional state and previous interactions.
-   **Emotion & Sentiment Analysis:**
    -   Deep learning models detect user emotions via text, voice, or video, enabling the AI to tailor its therapeutic approach.
-   **Therapeutic Frameworks:**
    -   Integrates Cognitive Behavioral Therapy (CBT), mindfulness, and relaxation techniques, offering structured conversations and self-help activities.
    -   Crisis detection mechanisms trigger escalation to human therapists or hotlines.
-   **User Interaction:**
    -   Multi-modal input (text, voice, video) and interactive tools (journals, mood tracking).
    -   Follow-up on user progress and remind users to practice coping strategies.
-   **Privacy & Ethics:**
    -   Ensures anonymity, data encryption, and ethical, unbiased interactions with clear limits on AI capabilities.

## Architecture

-   **Front-End:** Intuitive app/web interface for users.
-   **Back-End:** Cloud-based infrastructure with LLMs (e.g., GPT), emotion recognition models, and secure storage compliant with privacy laws (e.g., HIPAA).

## Software Requirements

### 1.1 Programming Languages & Frameworks

-   **Python:** Primary language for backend development, machine learning models, and NLP processing.
-   **Streamlit:** Used for the front-end UI, providing an interactive and user-friendly experience.
-   **Flask / FastAPI:** Backend API framework to manage data flow between the front-end and machine learning models.

### 1.2 Machine Learning & NLP Libraries

-   **Scikit-learn:** Implements the Random Forest model for depression prediction.
-   **Composio:** Handles text processing, ensuring clean and structured user inputs.
-   **Sarvam AI:** Manages Text-to-Speech (TTS) conversion for spoken responses.
-   **Hugging Face Transformers:** (Optional) For enhanced conversational abilities using LLM-based chatbot responses.
-   **Beijing University Embedding Model:** Generates vector embeddings from user text input for semantic understanding.

### 1.3 Database & Storage

-   **Vector Database (e.g., Pinecone, FAISS, Weaviate):** Stores vector embeddings of user interactions for efficient information retrieval.
-   **AWS / Google Cloud:** Provides cloud-based storage and hosting for application deployment and data management.

## Installation and Setup

Detailed instructions on how to install and set up the project, including:

1.  Cloning the repository
2.  Installing dependencies (using `pip install -r requirements.txt`)
3.  Setting up the database
4.  Configuring API keys and environment variables

## Usage

Explain how to use the "Smart AI Therapist," including:

1.  Running the application
2.  Interacting with the AI
3.  Understanding the different features and functionalities

## Algorithm Workflow

1.  **User Input Processing:**

    -   The user interacts with the AI through text input on the Streamlit UI.
    -   The Composio framework processes the input, handling:
        -   Sentence tokenization, text cleaning, and formatting.
        -   Removal of noise, slang, and unnecessary characters.
        -   Language identification and translation (if necessary).
    -   The cleaned text is converted into a vector representation using the Beijing University Embedding Model.
    -   This vectorized data is stored in the vector database for fast retrieval and contextual awareness.
2.  **Depression Prediction Using Random Forest:**

    -   The vectorized input is fed into the trained Random Forest model.
    -   The model outputs a probability score indicating the likelihood of depression.
    -   Based on the score, the system determines whether to proceed with standard therapy or escalate to emergency protocols.
3.  **Therapy Generation with LLMs:**

    -   If the user is not classified as high-risk, the system proceeds to generate therapeutic responses.
    -   The system uses pre-trained LLMs (e.g., GPT-3.5, Llama 2) to craft empathetic and personalized messages.
    -   The LLM is fine-tuned to adhere to therapeutic techniques (e.g., CBT, mindfulness).
4.  **Emergency Handling:**

    -   If the depression prediction score is above a critical threshold, the system activates emergency protocols.
    -   An email is automatically sent to pre-configured mental health professionals or first responders, including relevant user information.
    -   The user is prompted with immediate support options and contact information for emergency services.
5.  **Multi-Modal Communication:**

    -   The system supports both text-based and voice-based interactions.
    -   For voice interactions, the Sarvam AI Text-to-Speech (TTS) engine converts the AI’s responses into spoken language.
    -   Users can switch between input methods as needed, enhancing accessibility.
6.  **Contextual Awareness and Personalization:**

    -   The vector database stores all user interactions, allowing the AI to maintain contextual awareness.
    -   The system retrieves relevant past conversations to personalize responses and tailor therapeutic strategies.
    -   User preferences, such as preferred language and communication style, are stored and applied to future interactions.

## Course Outcomes

After successful completion of the mini-project, graduates will be able to:

-   **CO1:** Identify a problem through literature survey and knowledge of contemporary engineering technology.
-   **CO2:** Consolidate the literature search to identify issues/gaps and formulate the engineering problem.
-   **CO3:** Prepare a project schedule for the identified design methodology and engage in budget analysis, and share responsibility for every member in the team.
-   **CO4:** Provide sustainable engineering solutions considering health, safety, legal, cultural issues and also demonstrate concern for the environment.
-   **CO5:** Identify and apply the mathematical concepts, science concepts, engineering and management concepts necessary to implement the identified engineering problem.
-   **CO6:** Select the engineering tools/components required to implement the proposed solution for the identified engineering problem.
-   **CO7:** Analyze, design, and implement optimal design solutions, interpret results of experiments and draw valid conclusions.
-   **CO8:** Demonstrate effective written communication through the project report, the one-page poster presentation, and preparation of the video about the project and the four-page IEEE/Springer/ paper format of the work.
-   **CO9:** Engage in effective oral communication through power point presentation and demonstration of the project work.
-   **CO10:** Demonstrate compliance to the prescribed standards/ safety norms and abide by the norms of professional ethics.
-   **CO11:** Perform in the team, contribute to the team and mentor/lead the team.

## Contributing

Guidelines for contributors, including how to submit bug reports, feature requests, and pull requests.
