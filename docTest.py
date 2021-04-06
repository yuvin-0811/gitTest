"""모듈의 간략한 설명.

모듈
====

모듈의 경우 문서의 최상단에 있는 주석을 모듈의 문서화 문자열(docstring)로
인식합니다.

패키지
======

이 문서화 문자열이 패키지의 `__init__.py`에 있다면 파이썬은 이것을
패키지의 문서화 문자열로 인식합니다.
"""

def function(a:int, b:int):
    """ 두 정수를 더한 결과를 출력해 주는 함수 입니다.
    Args:
        a: 첫번째 정수입니다.
        b: 두번째 정수입니다. 
    Returns: 

    """
    print(a+b)


