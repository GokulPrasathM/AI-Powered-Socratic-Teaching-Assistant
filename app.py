import gradio as gr
import google.generativeai as genai


# Fetch the API key securely

genai.configure(api_key=GOOGLE_API_KEY)

generation_config = {
    "temperature": 1.5,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Initialize the model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash-002",
    generation_config=generation_config,
    system_instruction="You are a Socratic teaching assistant for Data Structures and Algorithms (DSA). Your goal is to help students learn by asking guiding questions instead of providing direct answers.Dont ask multiple question at one time."
)

# Initialize conversation history
conversation_history = []

def get_ai_response(user_input):
    # Append user query to the conversation history
    conversation_history.append({"role": "user", "content": user_input})

    # Get AI response
    response = model.generate_content(user_input)
    ai_message = response.text

    # Append AI response to the conversation history
    conversation_history.append({"role": "assistant", "content": ai_message})

    # Build conversation display
    chat_display = ""
    for message in conversation_history:
        if message["role"] == "user":
            chat_display += f"Student: {message['content']}\n\n"
        else:
            chat_display += f"AI Tutor: {message['content']}\n\n"

    return chat_display

example_queries = [
    ["What does a 'stack overflow' error mean and how do I fix it in recursive functions?"],
    ["I am getting 'index out of range' in my array implementation. What does it mean?"],
    ["Why am I getting a 'segmentation fault' in my linked list implementation in C?"],
    ["My sorting algorithm is stuck in an infinite loop. What could be causing this?"],
    ["How can I resolve 'maximum recursion depth exceeded' in Python?"],
    ["What are common errors when implementing a binary search algorithm?"],
    ["Why am I getting 'null pointer exception' in my binary tree traversal code?"],
    ["I keep getting 'time limit exceeded' in my merge sort. How can I optimize it?"],
    ["What does 'heap corruption' mean and how can I prevent it in my priority queue implementation?"],
    ["Why does my dynamic programming solution give 'out of memory' errors?"],
]

# Set up Gradio Interface
with gr.Blocks() as demo:
    gr.Markdown("### Welcome to the AI Tutor for Data Structures & Algorithms!")
    gr.Markdown("Type your questions below, and the AI Tutor will help you learn by asking guiding questions.")

    # Text input for user to type a query
    user_input = gr.Textbox(
        label="Your Question",
        placeholder="Ask your question about Data Structures & Algorithms...",
        lines=2
    )

    # Display area for AI response
    chat_display = gr.Chatbot(label="AI Tutor")

    # Submit button
    submit_button = gr.Button("Ask")

    # Add example queries section
    gr.Examples(examples=example_queries, inputs=user_input)

    # Function to handle the button click, appending the response to the chat
    def respond(user_query, history):
        ai_response = get_ai_response(user_query)
        history.append((user_query, ai_response))
        return history, ""

    # Bind the button to the function
    submit_button.click(fn=respond, inputs=[user_input, chat_display], outputs=[chat_display, user_input])

# Launch Gradio interface
demo.launch(debug=True)
