class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        arr=[""]*n
        for index in range(n):
            if not (index+1)%3==0 and not (index+1)%5==0:
                arr[index]=str(index+1)
            if (index+1)%3==0:
                arr[index]="Fizz"
            if (index+1)%5==0:
                arr[index]+="Buzz"
        return arr
