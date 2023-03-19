# python3


def build_heap(data):
    swaps = []
    n=len(data)
    
    for i in range((size//2)-1,-1,-1):
        while True:
            x=i;
            left=2*i+1
            right=2*i+2
            
            if left < n and data[left]<data[x]:
                x=left
            if right < n and data[right]<data[x]:
                x=right
            if x!=i:
                swaps.append((i, x))
                (data[i], data[x]) = (data[x], data[i]) 
            
            else:
                break
    return swaps


def main():
    
    text= input("Enter 'I' or 'F' : ")
    if "I" in text:
        n = int(input())
        data=list(map(int, input().split()))
    
    elif "F" in text:
        file_name = input()
        if "a" not in file_name
            with open("tests/" + file_name,'r',encoding='utf-8') as fails:
                n=int(fails.readline())
                data = list(map(int, fails.readline().split()))
    else:
        print("Error")
        return
    
    assert len(data) == n

   
    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
