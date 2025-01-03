'''
Given an array of integers nums and an integer threshold, we will choose a positive integer divisor, divide all the array by it, and sum the division's result. Find the smallest divisor such that the result mentioned above is less than or equal to threshold.

Each result of the division is rounded to the nearest integer greater than or equal to that element. (For example: 7/3 = 3 and 10/2 = 5).

The test cases are generated so that there will be an answer.
'''
def smallestDivisor(nums, threshold):

    divisor = 1 
    while True: 
        lista = []
        for numero in nums:
            x = (numero / divisor) 
            if x != int(x): 
                x = (numero // divisor) + 1
            else:
                x = int(x)  
            lista.append(x)
        m = sum(lista)
        if m <= threshold: 
            return divisor
        divisor += 1

print(smallestDivisor([44,22,33,11,1], 5))

#oppure 

def smallestDivisor(self, nums, threshold):

        def compute_sum(divisor):
            return sum((num + divisor - 1) // divisor for num in nums)

        left, right = 1, max(nums)  # Limiti per la ricerca binaria
        while left < right:
            mid = (left + right) // 2
            if compute_sum(mid) <= threshold:
                right = mid  # Cerca verso sinistra
            else:
                left = mid + 1  # Cerca verso destra
        return left