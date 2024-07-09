import re
import longResponses as long

def msg_prob(msg, words, single_resp=False, req_words=[]):
    msg_certainity = 0
    has_req_words = True
    for word in msg:
        if word in words:
            msg_certainity += 1
    
    perc = float(msg_certainity) / float(len(words))

    for word in req_words:
        if word not in msg:
            has_req_words = False
            break
    
    if has_req_words or single_resp:
        return int(perc * 100)
    else:
        return 0
    
def check_msg(msg):
    high_prob = {}

    def response(bot_resp, word_list, single_resp=False, req_words=[]):
        nonlocal high_prob
        high_prob[bot_resp] = msg_prob(msg, word_list, single_resp, req_words)
    
    response('Hello! How many I help you', ['hello', 'hi', 'sup', 'hey', 'hola', 'wassup'], single_resp=True)
    response("I'm doing great and what about you?", ['how', 'are', 'you', 'doing', '?'], req_words=['how'])
    response('Thank you bud!', ['i', 'appreciate', 'your', 'work'], req_words=['appreciate', 'work'])
    response(long.R_EATING, ['what', 'you', 'eat'], req_words=['you', 'eat'])
    response(long.R_HOBBIES, ['what', 'are', 'your', 'hobbies'], req_words=['hobbies'])
    response(long.R_WEATHER, ['what', 'is', 'the', 'weather'], req_words=['weather'])
    response(long.R_ORIGIN, ['where', 'are', 'you', 'from'], req_words=['where', 'from'])
    response(long.R_FAVORITE_COLOR, ['what', 'is', 'your', 'favorite', 'color'], req_words=['favorite', 'color'])

    best_match = max(high_prob, key=high_prob.get)

    return long.unknown() if high_prob[best_match] < 1 else best_match

def get_response(user_input):
    split_msg = re.split(r'\s+|[,;?!.-]\s*',user_input.lower())
    response = check_msg(split_msg)
    return response

while True:
    user_input = input("User: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("ChatBot's Response: Goodbye!")
        break
    print("ChatBot's Response:", get_response(user_input))