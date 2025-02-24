# Project description
  * 파이썬을 배우는 초급자들의 파이썬 소스코드 예제에서 사용할 수 있는 유틸리티 라이브러리입니다. 
  * {코딩스쿨} 런스팀로봇코딩학원에서 사용하는 파이썬기본 교재에서 사용

# 기본 사용법
## install with pip:
```shell
pip install atolibrary
```

## 임포팅하기 
```python
import atolibrary as ato
```

## 예제로 배우기 
### lotto 
* `ato.lotto.get_one_number`: 로또 번호를 하나 생성하는 함수입니다.

```python
import atolibrary as ato

number = ato.lotto.get_one_number()
print("생성된 로또 번호:", number)

# `get_one_set`: 하나의 세트를 생성하는 함수입니다.
def get_one_set():
    """
    하나의 세트를 생성하는 함수입니다.
    """
    # 세트 생성 로직
    return set

# `get_one_set_sorted`: 정렬된 하나의 세트를 생성하는 함수입니다.
def get_one_set_sorted():
    """
    정렬된 하나의 세트를 생성하는 함수입니다.
    """
    # 정렬된 세트 생성 로직
    return sorted_set

# `get_one_set_string`: 문자열로 된 하나의 세트를 생성하는 함수입니다.
def get_one_set_string():
    """
    문자열로 된 하나의 세트를 생성하는 함수입니다.
    """
    # 문자열 세트 생성 로직
    return string_set

# `get_one_set_string_bracket`: 괄호로 된 문자열로 된 하나의 세트를 생성하는 함수입니다.
def get_one_set_string_bracket():
    """
    괄호로 된 문자열로 된 하나의 세트를 생성하는 함수입니다.
    """
    # 괄호 문자열 세트 생성 로직
    return bracket_string_set

# `get_some_sets`: 여러 개의 세트를 생성하는 함수입니다.
def get_some_sets():
    """
    여러 개의 세트를 생성하는 함수입니다.
    """
    # 여러 개의 세트 생성 로직
    return sets
```

예제:

```python
import atolibrary as ato

# `get_one_set` 함수 예제
one_set = ato.get_one_set()
print("하나의 세트:", one_set)

# `get_one_set_sorted` 함수 예제
one_set_sorted = ato.get_one_set_sorted()
print("정렬된 하나의 세트:", one_set_sorted)

# `get_one_set_string` 함수 예제
one_set_string = ato.get_one_set_string()
print("문자열로 된 하나의 세트:", one_set_string)

# `get_one_set_string_bracket` 함수 예제
one_set_string_bracket = ato.get_one_set_string_bracket()
print("괄호로 된 문자열로 된 하나의 세트:", one_set_string_bracket)

# `get_some_sets` 함수 예제
some_sets = ato.get_some_sets()
print("여러 개의 세트:", some_sets)
```
---  
* `ato.names.get_human_name`: 사람 이름을 생성하는 함수입니다.

```python
import atolibrary as ato

name = ato.names.get_human_name()
print("생성된 사람 이름:", name)
```
---  
* `get_social_security_number`: 주민등록번호를 생성하는 함수입니다.
    ```python
    import atolibrary as ato

    ssn = ato.get_social_security_number()
    print("생성된 주민등록번호:", ssn)
    ```
---  
* `get_school_name`: 학교 이름을 생성하는 함수입니다.
    ```python
    import atolibrary as ato

    school_name = ato.get_school_name()
    print("생성된 학교 이름:", school_name)
    ```
---  
* `get_country_name`: 국가 이름을 생성하는 함수입니다.
    ```python
    import atolibrary as ato

    country_name = ato.get_country_name()
    print("생성된 국가 이름:", country_name)
    ```
---  
* `get_robot_name`: 로봇 이름을 생성하는 함수입니다.
    ```python
    import atolibrary as ato

    robot_name = ato.get_robot_name()
    print("생성된 로봇 이름:", robot_name)
    ```
---  
* `get_vehicle_company`: 차량 회사 이름을 생성하는 함수입니다.
    ```python
    import atolibrary as ato

    vehicle_company = ato.get_vehicle_company()
    print("생성된 차량 회사 이름:", vehicle_company)
    ```
---  
* `get_color_name`: 색상 이름을 생성하는 함수입니다.
    ```python
    import atolibrary as ato

    color_name = ato.get_color_name()
    print("생성된 색상 이름:", color_name)
    ```
