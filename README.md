# Python-Study

<h1>RFP.py</h1>

<h3>고객 정보 관리 시스템 RFP</h3>

1. 주요 내용
   지금 까지 배운 내용을 토대로 고객의 정보를 관리하는 프로그램을 만듭니다.
   고객의 정보를 관리하는 프로그램에서 사용하는 고객 정보를 저장하는 자료구조는 자신 있는 것을 이용합니다.

2. 요구사항 - 데이타

   - 고객의 정보는 이름, 성별, 이메일, 출생년도 가 있습니다.
   - 고객의 정보를 입력받아 본인이 선택한 자료구조에 저장해야 합니다.
   - 이름은 문자열로 저장하며, 성별은 남자는 M, 여자는 F로 저장합니다.
   - 이메일은 문자열로 저장하며, 태어난 연도는 정수로 저장합니다.

3. 요구사항 - 기능

   - 고객 관리 프로그램은 고객의 정보를 저장, 조회, 수정, 삭제 할 수 있는 기능이 있어야 합니다.

   - 고객 정보를 파일에 저장하는 기능을 구현하지 않아도 됩니다.
   - “ I ”를 눌러 고객의 정보를 입력받도록 하며,
   - 저장된 고객 정보는 “P ” 또는 “ N ”을 눌러 이전 고객정보 또는 다음 고객정보를 조회할 수 있어야 합니다.
   - 조회한 고객 정보는 “ U ”를 눌러 새로운 정보로 수정할 수 있어야 합니다.
   - “ D ”를 누르면 조회한 고객 정보를 삭제해야 합니다.
   - 프로그램의 종료는 “ Q ”를 누릅니다.


<h1>NumberGame.py</h1>
<h3>숫자 맞추기 게임 RFP</h3>

1. 주요 내용
   지금 까지 배운 내용을 토대로 AI 숫자 맞추기 게임을 만듭니다.
   AI가 제시하는 1 ~ 100 사이의 숫자를 추론하여 맞추는 게임 기능을 구현 합니다.
   총 시도 횟수를 기준으로 점수를 구하고 누적 총 합을 구합니다.
   콘솔 모드에서 진행 합니다.

2. 요구사항 - 데이타
   게임 정보는 게임 제목, 게이머 이름, 게임 점수, 총 누적 합 이 있습니다.
   25자 이내의 게임 제목과 게이머 이름을 입력받아 본인이 선택한 자료구조에 저장해야 합니다.
   매 게임의 획득 점수와 총 누적 점수를 저장해야 합니다.

3. 요구사항 - 기능
   게임 정보 입력
   프로그램이 구동되면 "게임의 제목 입력" 이라고 출력됨
   입력하지 않고 엔터를 치면 오류를 출력하고 다시 입력을 요청한다.
   입력한 게임의 제목이 25자를 넘으면 오류를 출력하고 다시 입력을 요청한다
   입력을 받으면 아래처럼 정렬하여 출력
   ''' ================== = 게임 제목 == = v1.0.0 == ================== '''
   게이머의 이름을 입력받는다 (프럼프트:게이머의 이름을 입력하세요)
   입력 안 하면 오류

4. 게임 시작 

   1. (프럼프트:0~99사이의 값으만 AI의 값을 예측하여 입력하세요)

   2. 공백을 넣으면 오류

   3. 숫자가 아니면 오류

   4. 값의 범위를 넘으면 오류

   5. 값이 작으면 작다고 출력하고 다시 입력받음

   6. 값이 크면 크다고 출력하고 다시 입력받음

   7. 시도 횟수를 기록

   8. 최종 값을 맞추면 총 x번 시도만에 맞췄다고 출력하고

   9. 다시 게임을 할것인지 물어본다 다시하면 1번부터 시작
