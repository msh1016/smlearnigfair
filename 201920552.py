# 1. 프로그램 시작 및 소개.
print('당신의 주급과 주휴수당을 계산해 드립니다.')
print()
print('2021년 최저임금은 시간당 8,720원입니다.')
print()
print('복리후생비(식대,교통비 등) 및 시간외 근로수당, 연차수당 등은 반영되지 않은 금액이며 회사규정에 따라 주휴수당도 다르기 때문에 실제 주급과는 차이가 있습니다.')
print()

# 2. 주급 및 주휴수당 계산 위해 입력 받아야 할 값.
# 2-1. 자신의 시급 입력.
while True:
    try :
        hw = int(input('당신의 시급을 입력하세요.(원 단위생략) : ')) # hw : hourly wage(시급)
        while hw < 1 : # 시급은 1이상의 값이기에 1미만의 값을 입력시 재입력 받는다.                                    
            print()
            print('올바른 시급을 입력하세요.')
            print()
            hw = int(input('당신의 시급을 입력하세요.(원 단위생략) : '))
        break
    except ValueError: # 정수가 아닌 값을 입력했을 때에도 값을 재입력 받는다.
        print()
        print('올바른 시급을 입력하세요.')
        print()
print()
print('당신의 시급은 '+str(hw)+'원 입니다.')
# 2-2. 한 주 근무규정 일수 입력.
while True:
    try:
        print()
        print('한 주 근무규정 일수를 선택하세요.')
        print()
        pwd = int(input('1. 1일  2. 2일  3. 3일  4. 4일  5. 5일  6. 6일 : ')) # pwd : promised work days(한주 근무규정 일수)
        print()
        while (pwd > 6) or (pwd < 1) : 
            print('알맞는 보기를 다시 선택하세요.')
            print()
            print('한 주 근무규정 일수를 선택하세요.')
            print()
            pwd = int(input('1. 1일  2. 2일  3. 3일  4. 4일  5. 5일  6. 6일 : '))
            print()
        break
    except ValueError:
        print()
        print('알맞는 보기를 다시 선택하세요.')
print('당신의 한 주 근무규정 일수는 '+str(pwd)+'일 입니다.')

# 2-3. 한 주 근무 일수 입력.  
while True:
    try:
        print()
        print('한 주 실제 근무 일수를 선택하세요.')
        print()
        rwd = int(input('1. 1일  2. 2일  3. 3일  4. 4일  5. 5일  6. 6일  7. 7일 : ')) # rwd : real work days(한주 근무 일수)
        print()
        while (rwd > 7) or (rwd < 1) :
            print('알맞는 보기를 다시 선택하세요.')
            print()
            print('한 주 실제 근무 일수를 선택하세요.')
            print()
            rwd = int(input('1. 1일  2. 2일  3. 3일  4. 4일  5. 5일  6. 6일  7. 7일 : '))
            print()
        break
    except ValueError:
        print()
        print('알맞는 보기를 다시 선택하세요.')
print('당신의 한 주 근무 일수는 '+str(rwd)+'일 입니다.')

# 2-4. 한 주 총 근무시간 입력.
print()
while True:
    try :
        wwt = float(input('당신의 한 주간의 총 근무 시간을 입력하세요.(시간 단위생략 / 1 = 1시간, 0.5 = 30분) : '))
        # 기본적으로 시급으로 계산하기 때문에 기본 단위는 1시간 / 분단위는 소수점으로 환산하여 입력해야 함. ex) 0.5 = 30분
        # wwt : week whole work times(한주 근무 시간)
        while wwt < 0 :                                   
            print()
            print('올바른 근무 시간을 입력하세요.')
            print()
            wwt = float(input('당신의 한 주간 총 근무 시간을 입력하세요. : '))
        break
    except ValueError: # 정수가 아닌 값을 입력했을 때에도 값을 재입력 받는다.
        print()
        print('올바른 근무 시간을 입력하세요.')
        print()
print()
print('당신의 한 주간의 총 근무 시간은 '+str(wwt)+'시간 입니다.')

# 3. 주휴수당 계산 함수 / 주급계산 함수 설정.

def getwla():   # wla : weekly leave allowance (주휴수당)
    wla = wwt/40*8*hw
    return wla

def getww():    # weekly wage (주급) / 주휴수당을 미포함하는 순수한 주급을 계산하는 함수.
    ww = wwt*hw 
    return ww

# 4. 주휴수당 및 주급 계산.

if wwt >= 15 :

    if pwd <= rwd :
        print()
        print('% 한 주 근무 시간이 15시간 이상이며, 근무 규정일수 충족으로 주휴수당이 있습니다. %')
        print()
        wla = getwla()
        ww = getww()
        print('주급 : '+ str(ww) + '원 입니다.')
        print('주휴수당 : '+ str(wla) + '원 입니다.')
        print()
        print('당신의 총 주급은 ' + str(wla+ww) + '원 입니다.')

    else:
        print()
        print('% 한 주 근무 시간이 15시간 이상이지만, 근무 규정일수 미충족으로 주휴수당이 없습니다. %')
        print()
        ww = getww()
        print('주급 : '+ str(ww) + '원 입니다.')
        print('주휴수당 : 없습니다.')
        print()
        print('당신의 총 주급은 ' + str(ww) + '원 입니다.')
        
else :

    if pwd <= rwd :
        print()
        print('% 한 주 근무 규정일수는 충족이지만, 근무 시간이 15시간 미만이므로 주휴수당이 없습니다. %')
        print()
        ww = getww()
        print('주급 : '+ str(ww) + '원 입니다.')
        print('주휴수당 : 없습니다.')
        print()
        print('당신의 총 주급은 ' + str(ww) + '원 입니다.')

    else:
        print()
        print('% 한 주 근무 규정일수 불충족이며, 근무 시간이 15시간 미만이므로 주휴수당이 없습니다. %')
        print()
        ww = getww()
        print('주급 : '+ str(ww))
        print('주휴수당 : 없습니다.')
        print()
        print('당신의 총 주급은 ' + str(ww) + '원 입니다.')

# 5. 프로그램 종료.
print()
print('당신의 주급과 주휴수당 계산 프로그램을 종료합니다.')
    
