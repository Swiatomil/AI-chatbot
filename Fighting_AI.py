import openai
from dotenv import dotenv_values
import argparse

config = dotenv_values(".env")
openai.api_key = config["openAi_key"]


def main():
    parser = argparse.ArgumentParser(description="personalized chatbot")
    parser.add_argument("--personality1",
                        type=str,
                        help="information about personality of chatbot",
                        default="surly and mean")
    parser.add_argument("--personality2",
                        type=str,
                        help="information about personality of chatbot",
                        default="crazy")

    args = parser.parse_args()
    
    topic = input("Some statement that Ai will fight about: ")
    msg1 = [
            {"role": "system", "content": f'Your personality is {args.personality1}.'
                                          f'you answer in two to three'
                                          f'You are a human that love to argue with constructive arguments. '
                                          f'You always disagree with you interlocutor.'},
            {"role": "user", "content": topic}
           ]
    msg2 = [
            {"role": "system", "content": f'Your personality is {args.personality2}.'
                                          f'you answer in two to three sentence'
                                          f'You are a human that love to argue with constructive arguments.'
                                          f'You always disagree with you interlocutor.'},
            {"role": "assistant", "content": topic}
           ]

    while True:
        try:
            answer = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=msg1
            )
            print("\033[91m {}\033[00m" .format("AiOne: ")+answer.choices[0].message.content)
            msg1.append(answer.choices[0].message.to_dict())
            msg2.append({"role": "user", "content": answer.choices[0].message["content"]})

            answer2 = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=msg2
            )
            print("\033[95m{}\033[00m" .format("AiTwo: ") + answer2.choices[0].message.content)
            msg2.append(answer2.choices[0].message.to_dict())
            msg1.append({"role": "user", "content": answer2.choices[0].message["content"]})

        except KeyboardInterrupt:
            answer = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": 'system', 'content': "you are crazy assistant"},
                    {"role": 'user', 'content': 'say something about you wining the argue in one or two sentences and say goodbay in crazy maner'}

                          ]
            )
            print("\033[93m{}\033[00m" .format("  Ai: ") + answer.choices[0].message.content)
            break


if __name__ == "__main__":
    main()

