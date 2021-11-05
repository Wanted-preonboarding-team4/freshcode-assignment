# [Assignment 1] Freshcode  

## 사용한 기술 스택
<p>
<img alt="Python" src = "https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white"/>
<img alt="Python" src = "https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white"/>
</p>

## 팀원  
| **이름** | **Github Link** |
|:------|:-------------|
| 강대훈 |          |
| 김훈태 |https://github.com/kim-hoontae|
| 안다민| |
| 이무현 |https://github.com/PeterLEEEEEE |
| 송빈호 |  |
| 정성헌 |  | 

## 모델링  

![image](https://user-images.githubusercontent.com/32921115/140473198-afb3b2ec-4be3-406d-8c29-ee04015a6a6e.png)


## 구현기능  

### 회원가입, 로그인  
- 회원가입 시 관리자, 사용자 API를 각각 만들어 구현하였습니다. 비밀번호는 ```bcrypt```를 이용해 암호화 시킨 뒤 db에 저장했습니다.  
- 로그인 시 db에 이메일이 있는지 확인 후  ```jwt```를 이용해 토큰을 만들어 클라이언트에 보내게 하였습니다.  
