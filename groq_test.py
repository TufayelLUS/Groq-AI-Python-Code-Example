from groq import Groq

api_key = "place api key here from groq"


# This function is used to get the response from the Groq API
def get_response(prompt):
    client = Groq(api_key=api_key)
    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message.content


if __name__ == "__main__":
    prompt = input("Enter your prompt: ")
    response = get_response(prompt)
    print(response)
