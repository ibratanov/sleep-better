import openai
import inspect
from env_vars_parser import get_env_var

class SleepAgent:
    def get_response(self, sleep_data):
        """
        Calls the OpenAI 3.5 API to generate a response to the question.
        The response is then matched to one of the answer choices and the index of the
        matching answer choice is returned. If the response does not match any answer choice,
        -1 is returned.

        Args:
            question (string): The question to be asked.
            answer_choices (list of strings): A list of answer choices.

        Returns:
            int: The index of the answer choice that matches the response, or -1 if the response
            does not match any answer choice.
        """

        # Create the prompt.
        prompt = inspect.cleandoc(f"""
            Q: {sleep_data}
            A: 
            """)
        
        system_message = "You are a multiple choice question answering system. Please use deductive logical reasoning to answer the given question."
        temperature_value = 0.2
        top_p_value = 1
        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt},
        ]

        # Set the OpenAI API key.
        openai.api_key = get_env_var("MY_OPENAI_API_KEY")

        # Optional self-consistency approach returns early, selecting the answer choice with the highest frequency
        # return self.__self_consistency_response(messages, answer_choices, temperature_value, top_p_value, 5)

        # Call the OpenAI 3.5 API.
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=temperature_value,
            top_p=top_p_value,
        )
        response_text = response.choices[0].message.content

        return response_text