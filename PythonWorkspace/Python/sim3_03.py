# 실습예제 3 : 리스트 삭제 & 삽입
# 5명의 학생이 중간고사에서 각 10,25,35,50,70의 점수를 받았다
# 시험 점수를 내림차순 리스트 형식으로 출력
# 3등 학생을 0정 처리하고 내림차순으로 출력
score = [10, 25, 35, 50, 70]
score.sort()
score.reverse()
print("적발 전 성적표 = ", score)
del score[2]
score.append(0)
print("적발 후 성적표 = ", score)