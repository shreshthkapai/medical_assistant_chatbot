# Medical Assistant Chatbot

This project implements a Medical Assistant Chatbot using OpenAI's GPT-4o mini model. The chatbot provides users with information about medical conditions and offers assistance based on user queries.

## Features

- Responds to user inquiries about medical conditions.
- Provides information on symptoms, causes, treatments, and preventive measures.
- Utilizes OpenAI's GPT-4o-mini model for generating responses.

## Setup and Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/shreshthkapai/medical_assistant_chatbot.git
   cd medical_assistant_chatbot
   ```

2. **Create and Activate a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables:**
   Create a `.env` file in the project root directory and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key
   ```

## Usage

Run the main application:
```bash
python main.py
```

Interact with the chatbot through the command line interface.

## License

This project is licensed under the MIT License.
