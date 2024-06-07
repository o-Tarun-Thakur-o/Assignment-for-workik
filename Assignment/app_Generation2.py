print("Programme is loading, Please Wait...")
import google.generativeai as genai
import Assets

genai.configure(api_key=Assets.api_Key)

#Take input from user -->
print(Assets.line)
fileName = input("Enter your app name : ")
fileFunc = input("What is the function of your app : ")
print(Assets.line)

sendAi = f"Write a python code to {fileFunc}, {Assets.sendAI_Specification}"

def generateResponse(appname, appfunction, username):

    for attempts in range(5):
        generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
        }

        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config=generation_config,
        )

        convo = model.start_chat(
            history=[]
        )

        try:
            response = convo.send_message(f"{appfunction}")
        except Exception as e:
            print(Assets.line,f"Error during generation: ***[{e}]***\n--Retrying...--")
            continue  # Try again in the next iteration

        result = Assets.create_File(fileName, response, username)

    return result

username = Assets.makeDir()
result = generateResponse(fileName, sendAi, username)

if result == True:
    Assets.deleteDir(username)
    print(Assets.line, f"File '{fileName}' created successfully", Assets.line)

else:
    print(Assets.line, "An Error has eccord", Assets.Line)

print(Assets.disclaimer, Assets.line)
input("press 'Enter' to 'Exit' : ")
