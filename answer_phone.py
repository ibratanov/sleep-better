from flask import Flask, render_template
app = Flask(__name__)
app = Flask(__name__)
from sleep_agent import SleepAgent
from Oura.oura_daily_sleep import OuraAgent

@app.route("/")
def index():
    # Instantiate a sleep agent
    sleep_agent = SleepAgent()

    # Instantiate an oura agent
    oura_agent = OuraAgent()

    sleep_data = oura_agent.get_sleep_data()

    response = sleep_agent.get_response(sleep_data)
    print(f"Sleep suggestions: {response}")

    return render_template('index.html', text=response)

if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)
