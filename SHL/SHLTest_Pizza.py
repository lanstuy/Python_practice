from past.builtins import raw_input


def orderPizza(orderPlaced, size):
    result = []
    for i in range(len(orderPlaced) - size + 1):
        window = orderPlaced[i:i+size]
        found = False
        for order in window:
            if order > 0:
                result.append(order)
                found = True
                break
        if not found:
            result.append(0)
    return result


def main():
    # input for orderPlaced
    orderPlaced = []
    orderPlaced_size = int(raw_input())
    orderPlaced = list(map(int, raw_input().split()))
    # input for size
    size = int(raw_input())
    result = orderPizza(orderPlaced, size)
    print(" ".join([str(res) for res in result]))

if __name__ == "__main__":
    main()