subject = {"DBMS":{"joints":{
    "wht are tjoint":"ganja",
    "wht are hjoint":"ganja",
    "wht are ljoint":"ganja",
    "wht are ojoint":"ganja",
    "wht are ijoint":"ganja",
    "wht are ujoint":"ganja",
    "wht are ejoint":"ganja",
    "wht are fjoint":"ganja",
    "wht are njoint":"ganja",
}}}

chatgptsend = "theese are the question i need answer for \n subject:DBMS "

print(subject["DBMS"])

for x in subject["DBMS"]:
    topic = "\n topic: " + x + "\n"
    chatgptsend += topic
    print(x)

for y in subject["DBMS"][x]:
    question = "\n question: " + y + "\n"
    chatgptsend += question
    print(y)

print(chatgptsend)