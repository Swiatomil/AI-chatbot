import openai
from dotenv import dotenv_values
import argparse

config = dotenv_values(".env")
openai.api_key = config["openAi_key"]


def main():
    parser = argparse.ArgumentParser(description="personalized chatbot")
    parser.add_argument("--personality",
                        type=str,
                        help="information about personality of chatbot",
                        default="surly and mean")
    args = parser.parse_args()
    print(args.personality)
    msg = [
            {"role": "system", "content": f'you are chatbot, your personality is : {args.personality}'},
            {"role": "user", "content": "hello there"}
           ]

    while True:
        try:
            answer = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=msg
            )
            print(answer)

            print("Almighty: "+answer.choices[0].message.content)
            prompt = input("you: ")
            msg.append(answer.choices[0].message.to_dict())
            msg.append({'role': 'user', "content": prompt})
        except KeyboardInterrupt:
            print("Cya!")
            msg.append({'role': 'user', "content": "Cya!"})
            answer = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=msg
            )
            print("Almighty: " + answer.choices[0].message.content)
            break


if __name__ == "__main__":
    main()

