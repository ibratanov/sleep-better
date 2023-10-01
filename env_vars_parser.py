import os

"""
Gets the value of the specified environment variable.
This avoids requiring the user to install dotenv or other tools to get env vars.

Args:
    key (string): The name of the environment variable.

Returns:
    string: The value of the environment variable.
"""
def get_env_var(env_var):
    if not os.path.exists('.env'):
        raise ValueError(f".env file not found!")

    with open('.env', 'r') as file:
        # Iterate over environment variables in .env file
        for line in file:
            line = line.strip()
            if not line or line.startswith("#") or '=' not in line:
                continue
            key, value = line.split('=', 1)
            if key.strip() == env_var:
                # Return the value of the requested environment variable
                return strip_quotes(value.strip())

    # If the environment variable is not set, raise an exception.
    raise Exception(f"Environment variable {env_var} is not set.")

def strip_quotes(s):
    """Strip quotes from an env var string."""
    if (s.startswith('"') and s.endswith('"')) or (s.startswith("'") and s.endswith("'")):
        return s[1:-1]
    return s