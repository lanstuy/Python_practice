from collections import deque
import sys
from past.builtins import raw_input


def orderPizza():
    """
    Solves the pizza order display problem using a sliding window and a deque.
    This function contains the core logic as requested.
    """
    # Read input values
    N = int(raw_input())
    orderPlaced = list(map(int, raw_input().split()))
    K = int(raw_input())

    n = N
    k = K
    result = []

    # Handle the special case where the display size is 0.
    # The screen never displays any orders, so it never displays a meat order.
    # The first meat order on the screen is always effectively 0.
    # Based on the problem asking for the output "each time an order is delivered",
    # and potentially including the initial state, the most consistent interpretation
    # when K=0 (and N>=0) is N+1 outputs of 0.
    # If N=0, K=0, the range is 0+1=1, result is [0]. Correct.
    # If N>0, K=0, the range is N+1, result is N+1 zeros.
    if k == 0:
        for _ in range(n + 1):
            result.append(0)
        print(" ".join(map(str, result)))
        return

    # Use a deque to store indices of negative numbers (meat pizzas)
    # that are currently within the sliding display window.
    # The deque stores indices in increasing order, which helps in finding
    # the first negative number efficiently (always at neg_indices[0]).
    neg_indices = deque()

    # Process the first display window.
    # The initial window contains the first min(N, K) orders.
    # This loop populates the deque for the initial window [0 ... min(n, k) - 1].
    for i in range(min(n, k)):
        # If the current order is a meat pizza (negative number), add its index to the deque.
        if orderPlaced[i] < 0:
            neg_indices.append(i)


    # Record the output for the first display window (starting at index 0).
    # If the deque is not empty, the first element is the index of the first meat pizza.
    if neg_indices:
        result.append(orderPlaced[neg_indices[0]])
    else:
        # If the deque is empty, there are no meat pizzas in the current window.
        result.append(0)

    # Slide the window through the remaining orders.
    # The outputs are recorded for windows starting at index 0, 1, ..., N-K.
    # The window starting at index `j` ends at index `j + K - 1`.
    # The loop iterates through the indices `i` from K to N-1.
    # When the element at index `i` enters the window, the window now ends at `i`
    # and starts at `i - K + 1`.
    # The element that was at index `i - K` is now leaving the window.
    for i in range(k, n):
        # Remove indices from the left of the deque that are outside the current window.
        # The window currently ends at index `i` and starts at `i - K + 1`.
        # Any index `j` in the deque where `j < i - K + 1` is now outside the window.
        # Since indices in the deque are increasing, we only need to check the leftmost one.
        # If the leftmost index is `i - K`, it's the element that just left the window.
        if neg_indices and neg_indices[0] == i - k:
            neg_indices.popleft()

        # Add the index of the new element entering the window (index i) if it's negative.
        if orderPlaced[i] < 0:
            neg_indices.append(i)

        # Record the output for the current window (the one ending at index i, starting at i-k+1).
        # If the deque is not empty, the first element is the index of the first meat pizza
        # in the current window.
        if neg_indices:
            result.append(orderPlaced[neg_indices[0]])
        else:
            # If the deque is empty, there are no meat pizzas in the current window.
            result.append(0)

    # Print the results space-separated.
    print(" ".join(map(str, result)))


def main():
    orderPlaced = []
    orderPlaced_size = int(raw_input)
    orderPlaced = list(map(int, raw_input().split()))
    size = int(raw_input())

    result = orderPizza(orderPlaced, size)
    print(" ".join(str(res) for res in result))


if __name__ == "__main__":
    orderPizza()
