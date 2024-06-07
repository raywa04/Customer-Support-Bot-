
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def customer_support_chatbot(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Example usage
if __name__ == "__main__":
    user_input = "How can I reset my password?"
    print(customer_support_chatbot(user_input))
