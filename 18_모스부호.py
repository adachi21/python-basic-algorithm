# 모스 부호는 ・과 －로 이루어진다.
# A의 모스부호는 ・－이다.
# A의 모스부호 한글표현은 따따~ 이다.
# 각 알파벳의 모스부호 한글표현은 다음과 같다.
# B(따~따따따), C(따~따따~따)), D(따~따따), E(따), F(따따따~따)
# G(따~따~따), H(따따따따), I(따따), J(따따~따~따~), K(따~따따~)
# L(따따~따따), M(따~따~), N(따~따), O(따~따~따~), P(따따~따~따)
# Q(따~따~따따~), R(따따~따), S(따따따), T(따~), U(따따따~)
# V(따따따따~), W(따따~따~), X(따~따따따~), Y(따~따따~따~), Z(따~따~따따)
# "SOS" 문자열을 입력하면 "따따따 따~따~따~ 따따따"를 리턴하시오.

def solution(text):
    morse={'A':'따따~', 'S':'따따따', 'O':'따~따~따~'}
    for s in text:
        print(morse[s],end=' ')
    
solution('SOS')