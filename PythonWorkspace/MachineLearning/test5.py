# 5. 리스트 지우기
List = ['hologram', 'charming', 'approve']  # List라는 이름의 리스트 선언 및 초기화
while 1:                # 리스트 값이 존재하면 무한 반복하는 while문 선언
    if List == []:      # 리스트가 비었는지 검사하는 if문
        break           # if문이 참일 때 while을 나가는 break
    print(List)         # if문이 거짓이면 리스트 List 출력
    delete = input("입력한 문자열이 포함된 단어가 List에서 삭제됩니다. : ") # 변수 delete에 삭제할 문자열을 입력받아 초기화
    for l in List:          # List에서 값을 빼낼 for문 선언
        if delete in l:     # List에서 값을 가져온 변수 l에 삭제할 문자열을 입력받은 변수 delete가 포함되었는지 검사하는 if문
            List.remove(l)  # if문이 참이면 해당 리스트 값 삭제