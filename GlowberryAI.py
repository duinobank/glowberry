from openai import OpenAI
import linecache 

client = OpenAI(
    api_key="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"    
)

prompt = "What are the top 40 non-fiction books that we study?"
print(prompt)
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role":"user",
            "content":prompt
        }
    ],
    model="gpt-3.5-turbo"
)

print(chat_completion.choices[0].message.content)
response = chat_completion.choices[0].message.content

f = open("1.txt", "w")
f.write(response)


text_count = "B"
counter = 1

for i in range(1,25):
    f = open("1.txt", "r")
    with open("1.txt", 'r') as fp:
        # lines to read
        line_numbers = [counter]
        # To store lines
        lines = []
        for b, line in enumerate(fp):
            # read line 4 and 7
            if b in line_numbers:
                lines.append(line.strip())
            elif b > 7:
                break
    print(lines)
    lines = str(lines)
    lines = lines[4:]
    lines = lines[:-2]
    print(lines)
    prompt_new_1 = ("write a 2000 word essay on "+lines)
    print(prompt_new_1)
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role":"user",
                "content":prompt_new_1
            }
        ],
        model="gpt-3.5-turbo"
    )

    text_count = (text_count,'A')
    print(chat_completion.choices[0].message.content)
    response_essay = chat_completion.choices[0].message.content
    counter = counter+1
    f = open(f"{text_count}.txt", "w")
    f.write(response_essay)
    f.close()



