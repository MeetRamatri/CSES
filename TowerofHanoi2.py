def tower_of_hanoi(n, src, helper, dest):
    if n == 1:
        print(src, dest)
        return
    tower_of_hanoi(n - 1, src, dest, helper)
    print(src, dest)
    tower_of_hanoi(n - 1, helper, src, dest)

n = int(input())
tower_of_hanoi(n, "1", "2", "3")