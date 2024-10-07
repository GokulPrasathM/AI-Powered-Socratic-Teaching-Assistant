# AI Socratic Tutor for Data Structures & Algorithms (DSA)

This project creates an interactive AI-driven tutor that helps students learn **Data Structures and Algorithms (DSA)** through Socratic questioning. Instead of giving direct answers, the AI guides users by asking strategic questions, helping them discover solutions independently. The application is built using **Gradio** for the user interface and **Google Generative AI (Gemini)** for the AI-powered responses.

---

## Features

- **AI-Socratic Teaching Assistant**: An AI that engages students by asking relevant, thought-provoking questions instead of providing direct answers.
- **Dynamic Conversation**: Maintains conversation history to simulate a continuous learning experience.
- **Example Queries**: Includes a list of common DSA questions for users to explore.
- **Easy-to-use Interface**: Built using **Gradio**, a simple and intuitive UI for real-time interaction with the AI.
- **DSA Focus Areas**: Sorting algorithms, algorithm complexity, Big-O notation, recursion, arrays, linked lists, and more.

---

## How It Works

1. **Google Generative AI Configuration**:
   The model (Gemini-1.5) is initialized with parameters that control the AI's response, such as temperature, top-p, and max token output. The API key is fetched securely using Colab's `userdata`.

2. **Socratic Method**:
   The AI behaves like a Socratic tutor, asking questions instead of giving away solutions. The goal is to help students explore concepts and errors independently.

3. **User Input and AI Response**:
   Users ask questions through the Gradio interface. The AI processes the input, generates a response, and the entire conversation history is displayed to keep context for each query.

---

## Setup Instructions

### Prerequisites

- **Python 3.10+**
- **Google Generative AI API Key**
- **Gradio**

### Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-repository/ai-socratic-dsa-tutor.git
   cd ai-socratic-dsa-tutor
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Securely store your **Google Generative AI API key**:
   Ensure the API key is securely accessible in your environment:
   - If using Google Colab, the key can be fetched using `userdata.get()`.
   - Alternatively, you can set the key using environment variables.

4. Run the application:
   ```bash
   python app.py
   ```

### Example Queries

Explore common questions related to DSA, such as:
- "What does a 'stack overflow' error mean and how do I fix it in recursive functions?"
- "Why am I getting a 'segmentation fault' in my linked list implementation?"
- "What are common errors when implementing binary search algorithms?"

These example queries can be directly selected within the Gradio interface or customized with your own questions.

---

## Usage

1. **Input a Question**: Use the Gradio interface to type a question about DSA concepts or errors.
2. **Get AI Guidance**: The AI will respond by asking guiding questions based on your input.
3. **View Conversation**: The chat history will be displayed in a structured format, showing both your questions and the AI’s responses.

---

## Gradio Interface

The application uses **Gradio Blocks** to create a simple and user-friendly interface:

- **Textbox**: Input your question about DSA.
- **Chatbot Display**: View the ongoing conversation between you and the AI tutor.
- **Submit Button**: Ask the AI and receive guided responses.
- **Example Queries**: Use predefined DSA-related questions for quick interaction.

---

## Socratic Teaching Model

The AI uses a Socratic method to promote critical thinking and problem-solving. Instead of providing answers, it breaks down problems and guides students by asking questions. This method helps learners understand underlying principles and develop their skills.

---

## Contributing

Feel free to contribute to this project by:
- Submitting **bug reports** or **feature requests**.
- Forking the repository and creating **pull requests** to improve the functionality or add new features.

---

## License

This project is licensed under the MIT License.

---

### Developed By

**Team Jaspers**  
- AI-Driven Teaching Assistant to help students master **Data Structures and Algorithms** through intelligent guidance.
