'''
엘리베이터가 위치해 있는 층과 버튼의 값을 더한 결과가 0보다 작으면 엘리베이터ㄴ 운행 x
민수는 0층에 있으며 0층이 가장 아래층임

버튼 한번당 마법의 돌 한개를 사용
1. 16층에서 0층으로 가려면 -1이 적힌 버튼을 6번, -10이 적힌 버튼을 1번 눌러 총 마법의 돌 7개 소모
2. +1이 적힌 버튼 4번, -10 버튼 2번을 누르면 돌을 6개만 소모할 수 있음

최소한의 버튼을 눌러서 이동하려한다
민수가 0층으로 가는데 필요한 마법의 돌의 최소 개수를 구해라

 마법의 엘리베이터에는 -1, +1, -10, +10, -100, +100 등과 같이 절댓값이 10c (c ≥ 0 인 정수) 형태인 정수들이 적힌 버튼이 있습니다
 
 10 ** 0 -> 1
 10 ** 1 -> 10
 10 ** 2 -> 100

10**n
'''
def solution(storey):
    answer = 0
    a = str(storey)
    storey_end = int(a[-1])
    
    down_list = [1, 2, 3, 4]
    up_list = [6, 7, 8, 9]
    
    
    if storey_end in up_list:
        print("test 1은 출력돼야함")
        
    elif storey_end in down_list:
        print("test 2 출력돼야함")
    
    return answer