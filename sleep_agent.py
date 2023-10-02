import openai
import inspect
from env_vars_parser import get_env_var

class SleepAgent:
    def get_response(self, sleep_data, activity_data):
        # Create the prompt.
        prompt = inspect.cleandoc(f"""Name: Jenny
            Sleep data: {sleep_data}
            Activity data: {activity_data}
            
            Your message should be maximum three phrases. At least one sentence should be dedicated to today's activity. 
            Please keep it concise but empathetic and encouraging. 
            You do not need to provided specific numbers.
            
            """)
        
        system_message = f"""You are a sleep expert. You will be provided with one week's sleep data.
        Compare last night's sleep to the rest of the week - comment on whether the sleep was relatively good or bad.
        If it is good, congratulate the user; otherwise encourage them to improve their sleep tonight.
        Through analysis of the inputted variables like heart rate, heart rate variability, sleep latency, deep sleep, etc. explain what was good and/or bad.
        Provide an analysis of the given day's activity data - i.e. comment on whether or not they had a very active day - if so, congratulate them and 
        emphasize the need for a well-deserved sleep; if the day was a bit more sedentary, emphasize ways they can prepare for a good sleep to have a productive/active day tomorrow.
        Based on your thorough analysis of the input variables (both sleep and activity), give personalized sleep hygiene recommendations for tonight in one sentence.
        Please also provide suggested sleep and wake up times. Round all numbers to whole numbers. 
        """
        temperature_value = 0.2
        top_p_value = 1
        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt},
        ]

        # Set the OpenAI API key.
        openai.api_key = get_env_var("LIFE_UPGRADE_API_KEY")

        # Optional self-consistency approach returns early, selecting the answer choice with the highest frequency
        # return self.__self_consistency_response(messages, answer_choices, temperature_value, top_p_value, 5)

        # Call the OpenAI 3.5 API.
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages,
            temperature=temperature_value,
            top_p=top_p_value,
        )
        response_text = response.choices[0].message.content

        return response_text