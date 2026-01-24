import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import Client
from google.genai import types
from prompts import system_prompt
from call_function import available_functions, call_function


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key == None:
    raise Exception("API key not set")

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

client = genai.Client(api_key=api_key)
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=messages,
    config=types.GenerateContentConfig(
        tools=[available_functions],
        system_instruction=system_prompt)
)

if args.verbose:
    print(f"User prompt: {args.user_prompt}")
    if response.usage_metadata != None:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    else:
        raise Exception("Response has missing usage_metadata")


if response.function_calls:
    print(response.function_calls)
    output = []
    function_call_results = []
    for function_call in response.function_calls:
        # append the function call to the result
        output.append(f"Calling function: {function_call.name}({function_call.args})")
        # actually call the function
        # uv run main.py "read the contents of main.py"
        call_function_result = call_function(function_call, args.verbose)
        if call_function_result.parts == None or len(call_function_result.parts) == 0:
            raise Exception("No parts returned")
        
        if call_function_result.parts[0] == None:
            raise Exception("First part is None")
        
        function_call_results.append(call_function_result.parts[0])
        if args.verbose:
            output.append(f"-> {call_function_result.parts[0].function_response.response}")
        
    print("\n".join(output))
else:
    print(response.text)
