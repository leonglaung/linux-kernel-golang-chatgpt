import os
import openai
openai.api_key = "apikey"
def completion(prompt):
    completions = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
    )
    message = completions.choices[0].text
    return message
path = "linux_suorce_code20230214\\block\\bfq-cgroup.c"
topath = "linux_go_20230214\\block\\bfq-cgroup.go"
ctext = open(path,"r").read()
#print(ctext)
gotext = completion("请把 "+ctext+" 翻译成 golang语言版本")
f=open(topath,"w")
f.write(gotext)
f.close()