def solution(phoneBook):
	# 문자열은 첫 글자부터 오름차순으로 정렬됨 ex) '11', '112', '21', '9'
	# 따라서, 어떤 번호가 다른 번호의 접두어라면 이 둘은 정렬했을 때 앞뒤에 위치함
    phoneBook = sorted(phoneBook)

	# i번째와 i+1번째를 zip함수로 짝지어서 확인
    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1): # p2가 p1으로 시작하면 False
            return False
    return True