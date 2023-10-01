import csv
from sleep_agent import SleepAgent

if __name__=="__main__":
    # Instantiate a sleep agent
    agent = SleepAgent()

    sleep_data = {
        "id": "string",
        "contributors": {
            "deep_sleep": 0,
            "efficiency": 0,
            "latency": 0,
            "rem_sleep": 0,
            "restfulness": 0,
            "timing": 0,
            "total_sleep": 0
        },
        "day": "2019-08-24",
        "score": 0,
        "timestamp": "2019-08-24T14:15:22Z"
    }

    response = agent.get_response(sleep_data)
    print(f"Sleep suggestions: {response}")