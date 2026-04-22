def get_loss(w1, w2, w3, w4):
    try:
        result = w1 // w2
    except ZeroDivisionError:
        return (w1, w2)
    else:
        y = 10 * result - 5 * w2 * w3 + w4
        return y