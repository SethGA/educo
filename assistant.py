from openai import OpenAI
import json

client = OpenAI()

# CUSTOM FUNCTIONS
customs = [{
    'name': 'extract_student_info',
    'description': 'Get the university student information from the body of the input text',
    'parameters': {
        'type': 'object',
        'properties': {
            'name': {
                'type': 'string',
                'description': 'Name of the user'
            },
            'major': {
                'type': 'string',
                'description': 'Major subject'
            },
            'school': {
                'type': 'string',
                'description': 'Name of the university'
            },
            'age': {
                'type': 'integer',
                'description': 'Age of the user'
            }
        }
    }
}]

# STABLE FUNCTIONS


def extract_student_info(name, age, major, school):

    """ get the student information"""

    return f"{name} is {age} years old, majoring in {major} at {school}."


# SAMPLE
studentDescription1 = "Seth Grief-Albert is an 18 year-old undergraduate studying Applied Mathematics at Queen's University."
studentDescription2 = "Hey so my name is Seth and I am at Queen's University. I study Applied Mathematics. I'm also 18."

# API CALL
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a university assistant, skilled in parsing student information"},
    {"role": "user", "content": studentDescription2}],
    functions=customs,
    function_call='auto'
)

response = completion.choices[0].message

if hasattr(response, 'function_call'):

    # determine which function call was invoked
    functionCalled = response.function_call.name

    # extract args
    functionArgs = json.loads(response.function_call.arguments)

    # define available functions
    available_functions = {
        "extract_student_info": extract_student_info
    }

    function_to_call = available_functions[functionCalled]
    response = function_to_call(*list(functionArgs.values()))

    # DATA
    with open("data.json", "a") as f:
        # write line by line
        f.write(str(functionArgs) + '\n')

else:
    response = response.content

# LOGS
with open("logs.txt", "a") as f:
    # write line by line
    f.write(str(response) + '\n')
