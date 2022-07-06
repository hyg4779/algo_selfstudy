import sys
sys.stdin = open('sample_input.txt')

def insepect(s):
    gwalho_list = list()
    for i in s:
        if i =='(' or i == '{':
            gwalho_list.append(i)

        elif i ==')':
            if len(gwalho_list) == 0 or gwalho_list.pop(-1) != '(':
                return 0

        elif i == '}':
            if len(gwalho_list) == 0 or gwalho_list.pop(-1) != '{':
                return 0
    else:
        if len(gwalho_list):
            return 0

        else:
            return 1



for tc in range(int(input())):
    print('#{} {}'.format(tc+1, insepect(input())))