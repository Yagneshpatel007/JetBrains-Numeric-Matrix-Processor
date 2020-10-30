
class Metrix_addition:

    def matrixaddition(self):
        m, n = input().split()
        matrix1 = []
        matrix2 = []

        for i in range(int(m)):
            li = list(input().split())
            matrix1.append(li)
        k, l = input().split()
        for i in range(int(k)):
            li1 =list(input().split())
            matrix2.append(li1)
        result = []
        answer = ''
        if m == k and l == n:
            for i in range(len(matrix1)):
                for j in range(len(matrix2)):
                    if i == j:
                        for d in range(len(matrix1[i])):
                            for c in range(len(matrix2[j])):
                                if d == c:
                                    result.append(int(matrix1[i][d]) + int(matrix2[j][c]))

            count = 0
            for i in result:
                if count < int(n):
                    answer += (str(i) + ' ')
                    count += 1
                else:
                    answer += ('\n' + str(i) + ' ')
                    count = 1

        else:
            answer = 'ERROR'
        print(answer)

    def multiplicationbyconstant(self):
        m, n = input().split()
        matrix1 = []
        for i in range(int(m)):
            li = list(input().split())
            matrix1.append(li)
        cons = int(input())
        result = []
        answer = ''
        for i in range(len(matrix1)):
            for j in range(len(matrix1[i])):
                dd = int(matrix1[i][j]) * cons
                result.append(str(dd))
        count = 0
        for i in result:
            if count < int(n):
                answer += (str(i) + ' ')
                count += 1
            else:
                answer += ('\n' + str(i) + ' ')
                count = 1


mat = Metrix_addition()
mat.multiplicationbyconstant()