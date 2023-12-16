V = int(input())
P1 = int(input())
P2 = int(input())
H = float(input())

V1 = P1 * H
V2 = P2 * H

V_real = V1 + V2

if V_real <= V:
    print(f'The pool is {(V_real / V) * 100:.2f}% full. Pipe 1: { (V1 / V_real) * 100:.2f}%. \
Pipe 2: {(V2 / V_real) * 100:.2f}%.')

elif V_real > V:
    print(f'For {H:.2f} hours the pool overflows with {V_real - V:.2f} liters.')



