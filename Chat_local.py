# -*- coding: utf-8 -*-
from ollama import chat
from ollama import ChatResponse


def Deepseek(msg, sys='请按照用户要求回答。'):
    stm_opt = False
    stream = chat(model='deepseek-r1:14b',
        messages=[{'role': 'system', 'content': sys}, {'role': 'user', 'content': msg}],
        stream=stm_opt)
    if stm_opt == True:
        for chunk in stream:
            print(chunk['message']['content'], end='', flush=True)
    return stream['message']['content']


def Deepseek_result(msg, sys='请按照用户要求回答。'):
    def find_second_occurrence(s, char):
        count = 0
        for i, c in enumerate(s):
            if c == char:
                count += 1
                if count == 2:
                    return i
        return -1  # 如果没有找到第2次出现，返回-1
    r_full = Deepseek(msg, sys)
    return r_full[find_second_occurrence(r_full, '>')+1:]


if __name__ == '__main__':
    out = Deepseek_result('请将下列词汇翻译成中文：South Africa; Nigeria; Switzerland')
    print(out)
