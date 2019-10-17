import asyncio
import discord

import datetime

import threading

client = discord.Client()

channel = ''

qigamTime = datetime.datetime.now()+datetime.timedelta(days=365)
gudeTime= datetime.datetime.now()+datetime.timedelta(days=365)
ifTime= datetime.datetime.now()+datetime.timedelta(days=365)
pinyxTime= datetime.datetime.now()+datetime.timedelta(days=365)
mayoTime= datetime.datetime.now()+datetime.timedelta(days=365)
dehugTime= datetime.datetime.now()+datetime.timedelta(days=365)
sedeTime= datetime.datetime.now()+datetime.timedelta(days=365)
sede2Time= datetime.datetime.now()+datetime.timedelta(days=365)
jungdeTime= datetime.datetime.now()+datetime.timedelta(days=365)
dongdeTime= datetime.datetime.now()+datetime.timedelta(days=365)
arTime= datetime.datetime.now()+datetime.timedelta(days=365)
jakTime= datetime.datetime.now()+datetime.timedelta(days=365)
kapaTime= datetime.datetime.now()+datetime.timedelta(days=365)
warmTime= datetime.datetime.now()+datetime.timedelta(days=365)
deathTime= datetime.datetime.now()+datetime.timedelta(days=365)
curchTime= datetime.datetime.now()+datetime.timedelta(days=365)
greenTime= datetime.datetime.now()+datetime.timedelta(days=365)
redTime= datetime.datetime.now()+datetime.timedelta(days=365)
sanduTime= datetime.datetime.now()+datetime.timedelta(days=365)
danduTime= datetime.datetime.now()+datetime.timedelta(days=365)
gedTime= datetime.datetime.now()+datetime.timedelta(days=365)
sigamTime = datetime.datetime.now()+datetime.timedelta(days=365)
digamTime = datetime.datetime.now()+datetime.timedelta(days=365)
figamTime = datetime.datetime.now()+datetime.timedelta(days=365)

tmp_qigamTime = datetime.datetime.now()+datetime.timedelta(days=365)
tmp_gudeTime= datetime.datetime.now()+datetime.timedelta(days=365)
tmp_ifTime= datetime.datetime.now()+datetime.timedelta(days=365)
tmp_pinyxTime= datetime.datetime.now()+datetime.timedelta(days=365)
tmp_mayoTime= datetime.datetime.now()+datetime.timedelta(days=365)
tmp_dehugTime= datetime.datetime.now()+datetime.timedelta(days=365)
tmp_sedeTime= datetime.datetime.now()+datetime.timedelta(days=365)
tmp_sede2Time= datetime.datetime.now()+datetime.timedelta(days=365)
tmp_jungdeTime= datetime.datetime.now()+datetime.timedelta(days=365)
tmp_dongdeTime= datetime.datetime.now()+datetime.timedelta(days=365)
tmp_arTime= datetime.datetime.now()+datetime.timedelta(days=365)
tmp_jakTime= datetime.datetime.now()+datetime.timedelta(days=365)
tmp_kapaTime= datetime.datetime.now()+datetime.timedelta(days=365)
tmp_warmTime= datetime.datetime.now()+datetime.timedelta(days=365)
tmp_deathTime= datetime.datetime.now()+datetime.timedelta(days=365)
tmp_curchTime= datetime.datetime.now()+datetime.timedelta(days=365)
tmp_greenTime= datetime.datetime.now()+datetime.timedelta(days=365)
tmp_redTime= datetime.datetime.now()+datetime.timedelta(days=365)
tmp_sanduTime= datetime.datetime.now()+datetime.timedelta(days=365)
tmp_danduTime= datetime.datetime.now()+datetime.timedelta(days=365)
tmp_gedTime= datetime.datetime.now()+datetime.timedelta(days=365)
tmp_sigamTime = datetime.datetime.now()+datetime.timedelta(days=365)
tmp_digamTime = datetime.datetime.now()+datetime.timedelta(days=365)
tmp_figamTime = datetime.datetime.now()+datetime.timedelta(days=365)

qigamTimeString = '99:99:99'
gudeTimeString = '99:99:99'
ifTimeString = '99:99:99'
mayoTimeString = '99:99:99'
pinyxTimeString = '99:99:99'
dehugTimeString = '99:99:99'
sedeTimeString = '99:99:99'
sede2TimeString = '99:99:99'
jungdeTimeString = '99:99:99'
dongdeTimeString = '99:99:99'
arTimeString = '99:99:99'
jakTimeString = '99:99:99'
kapaTimeString = '99:99:99'
warmTimeString = '99:99:99'
deathTimeString = '99:99:99'
curchTimeString = '99:99:99'
greenTimeString = '99:99:99'
redTimeString = '99:99:99'
sanduTimeString = '99:99:99'
danduTimeString = '99:99:99'
gedTimeString = '99:99:99'
sigamTimeString = '99:99:99'
digamTimeString = '99:99:99'
figamTimeString = '99:99:99'


tmp_qigamTimeString = ''
tmp_gudeTimeString = ''
tmp_ifTimeString = ''
tmp_mayoTimeString = ''
tmp_pinyxTimeString = ''
tmp_dehugTimeString = ''
tmp_sedeTimeString = ''
tmp_sede2TimeString = ''
tmp_jungdeTimeString = ''
tmp_dongdeTimeString = ''
tmp_arTimeString = ''
tmp_jakTimeString = ''
tmp_kapaTimeString = ''
tmp_warmTimeString = ''
tmp_deathTimeString = ''
tmp_curchTimeString = ''
tmp_greenTimeString = ''
tmp_redTimeString = ''
tmp_sanduTimeString = ''
tmp_danduTimeString = ''
tmp_gedTimeString = ''
tmp_sigamTimeString = ''
tmp_digamTimeString = ''
tmp_figamTimeString = ''

qigamFlag = False
gudeFlag = False
ifFlag = False
mayoFlag = False
pinyxFlag = False
dehugFlag = False
sedeFlag = False
sede2Flag = False
jungdeFlag = False
dongdeFlag = False
arFlag = False
jakFlag = False
kapaFlag = False
warmFlag = False
deathFlag = False
curchFlag = False
greenFlag = False
redFlag = False
sanduFlag = False
danduFlag = False
gedFlag = False
sigamFlag = False
digamFlag = False
figamFlag = False

nowTimeString = '1'

# 1-6에서 생성된 토큰을 이곳에 입력해주세요.
token = "NDcxOTMyOTg1MzY1NjI2ODgw.DpRUMA.NYAYhvMtW7ik1nYIzksiA4xweW8"

async def my_background_task():
    await client.wait_until_ready()

    global channel
    global nowTimeString

    global qigamTime
    global gudeTime
    global ifTime
    global mayoTime
    global pinyxTime
    global dehugTime
    global sedeTime
    global sede2Time
    global jungdeTime
    global dongdeTime
    global arTime
    global jakTime
    global kapaTime
    global warmTime
    global deathTime
    global curchTime
    global greenTime
    global redTime
    global sanduTime
    global danduTime
    global gedTime
    global sigamTime
    global digamTime
    global figamTime
    
    global qigamTimeString
    global gudeTimeString
    global ifTimeString
    global mayoTimeString
    global pinyxTimeString
    global dehugTimeString
    global sedeTimeString
    global sede2TimeString
    global jungdeTimeString
    global dongdeTimeString
    global arTimeString
    global jakTimeString
    global kapaTimeString
    global warmTimeString
    global deathTimeString
    global curchTimeString
    global greenTimeString
    global redTimeString
    global sanduTimeString
    global danduTimeString
    global gedTimeString
    global sigamTimeString
    global digamTimeString
    global figamTimeString

    global tmp_gudeTime
    global tmp_ifTime
    global tmp_mayoTime
    global tmp_pinyxTime
    global tmp_warmTime
    global tmp_deathTime
    global tmp_curchTime
    global tmp_greenTime
    global tmp_redTime
    global tmp_danduTime
    global tmp_figamTime

    global tmp_qigamTimeString
    global tmp_gudeTimeString
    global tmp_ifTimeString
    global tmp_mayoTimeString
    global tmp_pinyxTimeString
    global tmp_dehugTimeString
    global tmp_sedeTimeString
    global tmp_sede2TimeString
    global tmp_jungdeTimeString
    global tmp_dongdeTimeString
    global tmp_arTimeString
    global tmp_jakTimeString
    global tmp_kapaTimeString
    global tmp_warmTimeString
    global tmp_deathTimeString
    global tmp_curchTimeString
    global tmp_greenTimeString
    global tmp_redTimeString
    global tmp_sanduTimeString
    global tmp_danduTimeString
    global tmp_gedTimeString
    global tmp_sigamTimeString
    global tmp_digamTimeString
    global tmp_figamTimeString

    global qigamFlag
    global gudeFlag
    global ifFlag
    global mayoFlag
    global pinyxFlag
    global dehugFlag
    global sedeFlag
    global sede2Flag
    global jungdeFlag
    global dongdeFlag
    global arFlag
    global jakFlag
    global kapaFlag
    global warmFlag
    global deathFlag
    global curchFlag
    global greenFlag
    global redFlag
    global sanduFlag
    global danduFlag
    global gedFlag    
    global sigamFlag
    global digamFlag
    global figamFlag

    while not client.is_closed:
        now = datetime.datetime.now()
        priv = now+datetime.timedelta(minutes=1)
        privTimeString = priv.strftime('%H:%M:%S')
        nowTimeString = now.strftime('%H:%M:%S')
        #print('loop check ' + qigamTime.strftime('%H:%M:%S') + ' ' + nowTimeString + ' ' + privTimeString)

        if channel != '':


            
            if qigamTime <= now:
                qigamFlag = False
                tmp_qigamTime = qigamTime
                qigamTimeString = '99:99:99'
                qigamTime = now+datetime.timedelta(days=365)
                await client.send_message(channel, '@everyone 기감 탐 입니다.')
                
            if gudeTime <= now:
                gudeFlag = False
                tmp_gudeTime = gudeTime
                gudeTimeString = '99:99:99'
                gudeTime = now+datetime.timedelta(days=365)
                await client.send_message(channel, '@everyone  거드 탐 입니다.')

            if ifTime <= now:
                ifFlag = False
                tmp_ifTime = ifTime
                ifTimeString = '99:99:99'
                ifTime = now+datetime.timedelta(days=365)
                await client.send_message(channel, '@everyone  이프 탐 입니다.')

            if mayoTime <= now:
                mayoFlag = False
                tmp_mayoTime = mayoTime
                mayoTimeString = '99:99:99'
                mayoTime = now+datetime.timedelta(days=365)
                await client.send_message(channel, '@everyone  마요 탐 입니다.')

            if pinyxTime <= now:
                pinyxFlag = False
                tmp_pinyxTime = pinyxTime
                pinyxTimeString = '99:99:99'
                pinyxTime = now+datetime.timedelta(days=365)
                await client.send_message(channel, '@everyone  피닉 탐 입니다.')

            if dehugTime <= now:
                dehugFlag = False
                tmp_dehugTime = dehugTime
                dehugTimeString = '99:99:99'
                dehugTime = now+datetime.timedelta(days=365)
                await client.send_message(channel, '@everyone  대흑 탐 입니다.')

            if sedeTime <= now:
                sedeFlag = False
                tmp_sedeTime = sedeTime
                sedeTimeString = '99:99:99'
                sedeTime = now+datetime.timedelta(days=365)
                await client.send_message(channel, '@everyone  서드1 탐 입니다.')

            if sede2Time <= now:
                sede2Flag = False
                tmp_sede2Time = sede2Time
                sede2TimeString = '99:99:99'
                sede2Time = now+datetime.timedelta(days=365)
                await client.send_message(channel, '@everyone  서드2 탐 입니다.')

            if jungdeTime <= now:
                jungdeFlag = False
                tmp_jungdeTime = jungdeTime
                jungdeTimeString = '99:99:99'
                jungdeTime = now+datetime.timedelta(days=365)
                await client.send_message(channel, '@everyone  중드 탐 입니다.')

            if dongdeTime <= now:
                dongdeFlag = False
                tmp_dongdeTime = dongdeTime
                dongdeTimeString = '99:99:99'
                dongdeTime = now+datetime.timedelta(days=365)
                await client.send_message(channel, '@everyone  동드 탐 입니다.')

            if arTime <= now:
                arFlag = False
                tmp_arTime = arTime
                arTimeString = '99:99:99'
                arTime = now+datetime.timedelta(days=365)
                await client.send_message(channel, '@everyone  아르 탐 입니다.')

            if jakTime <= now:
                jakFlag = False
                tmp_jakTime = jakTime
                jakTimeString = '99:99:99'
                jakTime = now+datetime.timedelta(days=365)
                await client.send_message(channel, '@everyone  자크 탐 입니다.')

            if kapaTime <= now:
                kapaFlag = False
                tmp_kapaTime = kapaTime
                kapaTimeString = '99:99:99'
                kapaTime = now+datetime.timedelta(days=365)
                await client.send_message(channel, '@everyone  카파 탐 입니다.')

            if warmTime <= now:
                warmFlag = False
                tmp_warmTime = warmTime
                warmTimeString = '99:99:99'
                warmTime = now+datetime.timedelta(days=365)
                await client.send_message(channel, '@everyone  웜 탐 입니다.')

            if deathTime <= now:
                deathFlag = False
                tmp_deathTime = deathTime
                deathTimeString = '99:99:99'
                deathTime = now+datetime.timedelta(days=365)
                await client.send_message(channel, '@everyone  데스* 탐 입니다.')

            if curchTime <= now:
                curchFlag = False
                tmp_curchTime = curchTime
                curchTimeString = '99:99:99'
                curchTime = now+datetime.timedelta(days=365)
                await client.send_message(channel, '@everyone  커츠 탐 입니다.')

            if greenTime <= now:
                greenFlag = False
                tmp_greenTime = greenTime
                greenTimeString = '99:99:99'
                greenTime = now+datetime.timedelta(days=365)
                await client.send_message(channel, '@everyone  질풍 탐 입니다.')

            if redTime <= now:
                redFlag = False
                tmp_redTime = redTime
                redTimeString = '99:99:99'
                redTime = now+datetime.timedelta(days=365)
                await client.send_message(channel, '@everyone  광풍 탐 입니다.')

            if sanduTime <= now:
                sanduFlag = False
                tmp_sanduTime = sanduTime
                sanduTimeString = '99:99:99'
                sanduTime = now+datetime.timedelta(days=365)
                await client.send_message(channel, '@everyone  산두 탐 입니다.')

            if danduTime <= now:
                danduFlag = False
                tmp_danduTime = danduTime
                danduTimeString = '99:99:99'
                danduTime = now+datetime.timedelta(days=365)
                await client.send_message(channel, '@everyone  에자 탐 입니다.')

            if gedTime <= now:
                gedFlag = False
                tmp_gedTime = redTime
                gedTimeString = '99:99:99'
                gedTime = now+datetime.timedelta(days=365)
                await client.send_message(channel, '@everyone  감데 탐 입니다.')

            if sigamTime <= now:
                sigamFlag = False
                tmp_sigamTime = sigamTime
                sigamTimeString = '99:99:99'
                sigamTime = now+datetime.timedelta(days=365)
                await client.send_message(channel, '@everyone 개미 탐 입니다.')

            if digamTime <= now:
                digamFlag = False
                tmp_digamTime = digamTime
                digamTimeString = '99:99:99'
                digamTime = now+datetime.timedelta(days=365)
                await client.send_message(channel, '@everyone 스피 탐 입니다.')

            if figamTime <= now:
                figamFlag = False
                tmp_figamTime = figamTime
                figamTimeString = '99:99:99'
                figamTime = now+datetime.timedelta(days=365)
                await client.send_message(channel, '@everyone 도펠 탐 입니다.')



            if qigamTime <= priv:
                if qigamFlag == False:
                    qigamFlag = True
                    await client.send_message(channel, '기감 1분 전 입니다.')
                
            if gudeTime <= priv:
                if gudeFlag == False:
                    gudeFlag = True
                    await client.send_message(channel, '거드 1분 전 입니다.')

            if ifTime <= priv:
                if ifFlag == False:
                    ifFlag = True
                    await client.send_message(channel, '이프 1분 전 입니다.')

            if mayoTime <= priv:
                if mayoFlag == False:
                    mayoFlag = True
                    await client.send_message(channel, '마요 1분 전 입니다.')

            if pinyxTime <= priv:
                if pinyxFlag == False:
                    pinyxFlag = True
                    await client.send_message(channel, '피닉 1분 전 입니다.')

            if dehugTime <= priv:
                if dehugFlag == False:
                    dehugFlag = True
                    await client.send_message(channel, '대흑 1분 전 입니다.')

            if sedeTime <= priv:
                if sedeFlag == False:
                    sedeFlag = True
                    await client.send_message(channel, '서드1 1분 전 입니다.')

            if sede2Time <= priv:
                if sede2Flag == False:
                    sede2Flag = True
                    await client.send_message(channel, '서드2 1분 전 입니다.')

            if jungdeTime <= priv:
                if jungdeFlag == False:
                    jungdeFlag = True
                    await client.send_message(channel, '중드 1분 전 입니다.')

            if dongdeTime <= priv:
                if dongdeFlag == False:
                    dongdeFlag = True
                    await client.send_message(channel, '동드 1분 전 입니다.')

            if arTime <= priv:
                if arFlag == False:
                    arFlag = True
                    await client.send_message(channel, '아르 1분 전 입니다.')

            if jakTime <= priv:
                if jakFlag == False:
                    jakFlag = True
                    await client.send_message(channel, '자크 1분 전 입니다.')

            if kapaTime <= priv:
                if kapaFlag == False:
                    kapaFlag = True
                    await client.send_message(channel, '카파 1분 전 입니다.')

            if warmTime <= priv:
                if warmFlag == False:
                    warmFlag = True
                    await client.send_message(channel, '웜 1분 전 입니다.')

            if deathTime <= priv:
                if deathFlag == False:
                    deathFlag = True
                    await client.send_message(channel, '데스 1분 전 입니다.')

            if curchTime <= priv:
                if curchFlag == False:
                    curchFlag = True
                    await client.send_message(channel, '커츠 1분 전 입니다.')

            if greenTime <= priv:
                if greenFlag == False:
                    greenFlag = True
                    await client.send_message(channel, '질풍 1분 전 입니다.')

            if redTime <= priv:
                if redFlag == False:
                    redFlag = True
                    await client.send_message(channel, '광풍 1분 전 입니다.')

            if sanduTime <= priv:
                if sanduFlag == False:
                    sanduFlag = True
                    await client.send_message(channel, '산두 1분 전 입니다.')

            if danduTime <= priv:
                if danduFlag == False:
                    danduFlag = True
                    await client.send_message(channel, '에자 1분 전 입니다.')

            if gedTime <= priv:
                if gedFlag == False:
                    gedFlag = True
                    await client.send_message(channel, '감데 1분 전 입니다.')

            if sigamTime <= priv:
                if sigamFlag == False:
                    sigamFlag = True
                    await client.send_message(channel, '개미 1분 전 입니다.')
 
            if digamTime <= priv:
                if digamFlag == False:
                    digamFlag = True
                    await client.send_message(channel, '스피 1분 전 입니다.')
 
            if figamTime <= priv:
                if figamFlag == False:
                    figamFlag = True
                    await client.send_message(channel, '도펠 1분 전 입니다.')
 
                    
            
        await asyncio.sleep(1) # task runs every 60 seconds
        


async def joinVoiceChannel():
    channel = client.get_channel("일반")
    await client.join_voice_channel(channel)
    

# 봇이 구동되었을 때 동작되는 코드입니다.
@client.event
async def on_ready():
    print("Logged in as ") #화면에 봇의 아이디, 닉네임이 출력됩니다.
    print(client.user.name)
    print(client.user.id)
    print("===========")

    #await joinVoiceChannel()
    
    client.loop.create_task(my_background_task())
    
    # 디스코드에는 현재 본인이 어떤 게임을 플레이하는지 보여주는 기능이 있습니다.
    # 이 기능을 사용하여 봇의 상태를 간단하게 출력해줄 수 있습니다.
    await client.change_presence(game=discord.Game(name="반갑습니다 :D", type=1))

    

# 봇이 새로운 메시지를 수신했을때 동작되는 코드입니다.
@client.event
async def on_message(message):
    if message.author.bot: #만약 메시지를 보낸사람이 봇일 경우에는
        return None #동작하지 않고 무시합니다.

    global channel
    global nowTimeString

    global qigamTime
    global gudeTime
    global ifTime
    global mayoTime
    global pinyxTime
    global dehugTime
    global sedeTime
    global sede2Time
    global jungdeTime
    global dongdeTime
    global arTime
    global jakTime
    global kapaTime
    global warmTime
    global deathTime
    global curchTime
    global greenTime
    global redTime
    global sanduTime
    global danduTime
    global gedTime
    global sigamTime
    global digamTime
    global figamTime
    
    global qigamTimeString
    global gudeTimeString
    global ifTimeString
    global mayoTimeString
    global pinyxTimeString
    global dehugTimeString
    global sedeTimeString
    global sede2TimeString
    global jungdeTimeString
    global dongdeTimeString
    global arTimeString
    global jakTimeString
    global kapaTimeString
    global warmTimeString
    global deathTimeString
    global curchTimeString
    global greenTimeString
    global redTimeString
    global sanduTimeString
    global danduTimeString
    global gedTimeString
    global sigamTimeString
    global digamTimeString
    global figamTimeString

    global tmp_gudeTime
    global tmp_ifTime
    global tmp_mayoTime
    global tmp_pinyxTime
    global tmp_warmTime
    global tmp_deathTime
    global tmp_curchTime
    global tmp_greenTime
    global tmp_redTime
    global tmp_danduTime
    global tmp_figamTime

    global tmp_qigamTimeString
    global tmp_gudeTimeString
    global tmp_ifTimeString
    global tmp_mayoTimeString
    global tmp_pinyxTimeString
    global tmp_dehugTimeString
    global tmp_sedeTimeString
    global tmp_sede2TimeString
    global tmp_jungdeTimeString
    global tmp_dongdeTimeString
    global tmp_arTimeString
    global tmp_jakTimeString
    global tmp_kapaTimeString
    global tmp_warmTimeString
    global tmp_deathTimeString
    global tmp_curchTimeString
    global tmp_greenTimeString
    global tmp_redTimeString
    global tmp_sanduTimeString
    global tmp_danduTimeString
    global tmp_gedTimeString
    global tmp_sigamTimeString
    global tmp_digamTimeString
    global tmp_figamTimeString

    global qigamFlag
    global gudeFlag
    global ifFlag
    global mayoFlag
    global pinyxFlag
    global dehugFlag
    global sedeFlag
    global sede2Flag
    global jungdeFlag
    global dongdeFlag
    global arFlag
    global jakFlag
    global kapaFlag
    global warmFlag
    global deathFlag
    global curchFlag
    global greenFlag
    global redFlag
    global sanduFlag
    global danduFlag
    global gedFlag    
    global sigamFlag
    global digamFlag
    global figamFlag


    id = message.author.id #id라는 변수에는 메시지를 보낸사람의 ID를 담습니다.
    channel = message.channel #channel이라는 변수에는 메시지를 받은 채널의 ID를 담습니다.
    #channel = discord.Object(id='496252676598661133')   
    modify = ''
    try:
        hello = message.content
        length = len(hello)     # UTF-8로 인코딩 했을 때 바이트 수를 구함
        print(hello)
        print(length)
    
        if length == 11:
            hours = hello[6:8]
            minutes = hello[9:11]
            now = datetime.datetime.now()
            now = now.replace(hour=int(hours), minute=int(minutes))
        elif length == 12:
            hours = hello[7:9]
            minutes = hello[10:12]
            now = datetime.datetime.now()
            now = now.replace(hour=int(hours), minute=int(minutes))
        elif length == 10:
            hours = hello[5:7]
            minutes = hello[8:10]
            now = datetime.datetime.now()
            now = now.replace(hour=int(hours), minute=int(minutes))
        else :
            now = datetime.datetime.now()
            nowTimeString = now.strftime('%H:%M:%S')
    except:
        print('exception');
        now = datetime.datetime.now()
        nowTimeString = now.strftime('%H:%M:%S')


    if message.content.startswith('!기감 컷'):
        qigamFlag = False
        qigamTime = nextTime = now+datetime.timedelta(hours=1)
        tmp_qigamTimeString = qigamTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 기감 ' + qigamTimeString)
        
    if message.content.startswith('!거드 컷'):
        gudeFlag = False
        gudeTime = nextTime = now+datetime.timedelta(hours=3)
        tmp_gudeTimeString = gudeTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 거드 ' + gudeTimeString)

    if message.content.startswith('!이프 컷'):
        ifFlag = False
        ifTime = nextTime = now+datetime.timedelta(hours=2)
        tmp_ifTimeString = ifTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 이프 ' + ifTimeString)

    if message.content.startswith('!마요 컷'):
        mayoFlag = False
        mayoTime = nextTime = now+datetime.timedelta(hours=3)
        tmp_mayoTimeString = mayoTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 마요 ' + mayoTimeString)

    if message.content.startswith('!피닉 컷'):
        pinyxFlag = False
        pinyxTime = nextTime = now+datetime.timedelta(hours=7)
        tmp_pinyxTimeString = pinyxTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 피닉 ' + pinyxTimeString)

    if message.content.startswith('!대흑 컷'):
        dehugFlag = False
        dehugTime = nextTime = now+datetime.timedelta(hours=3)
        tmp_dehugTimeString = dehugTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 대흑 ' + dehugTimeString)

    if message.content.startswith('!서드1 컷'):
        sedeFlag = False
        sedeTime = nextTime = now+datetime.timedelta(hours=2)
        tmp_sedeTimeString = sedeTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 서드1 ' + sedeTimeString)

    if message.content.startswith('!서드2 컷'):
        sede2Flag = False
        sede2Time = nextTime = now+datetime.timedelta(hours=2)
        tmp_sede2TimeString = sede2TimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 서드2 ' + sede2TimeString)

    if message.content.startswith('!중드 컷'):
        jungdeFlag = False
        jungdeTime = nextTime = now+datetime.timedelta(hours=3)
        tmp_jungdeTimeString = jungdeTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 중드 ' + jungdeTimeString)

    if message.content.startswith('!동드 컷'):
        dongdeFlag = False
        dongdeTime = nextTime = now+datetime.timedelta(hours=3)
        tmp_dongdeTimeString = dongdeTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 동드 ' + dongdeTimeString)

    if message.content.startswith('!아르 컷'):
        arFlag = False
        arTime = nextTime = now+datetime.timedelta(hours=4)
        tmp_arTimeString = arTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 아르 ' + arTimeString)

    if message.content.startswith('!자크 컷'):
        jakFlag = False
        jakTime = nextTime = now+datetime.timedelta(hours=3)
        tmp_jakTimeString = jakTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 자크 ' + jakTimeString)

    if message.content.startswith('!카파 컷'):
        kapaFlag = False
        kapaTime = nextTime = now+datetime.timedelta(hours=2)
        tmp_kapaTimeString = kapaTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 카파 ' + kapaTimeString)

    if message.content.startswith('!웜 컷'):
        warmFlag = False
        warmTime = nextTime = now+datetime.timedelta(hours=2)
        tmp_warmTimeString = warmTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 웜 ' + warmTimeString)

    if message.content.startswith('!데스 컷'):
        deathFlag = False
        deathTime = nextTime = now+datetime.timedelta(hours=7)
        tmp_deathTimeString = deathTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 데스 ' + deathTimeString)

    if message.content.startswith('!커츠 컷'):
        curchFlag = False
        curchTime = nextTime = now+datetime.timedelta(hours=10)
        tmp_curchTimeString = curchTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 커츠 ' + curchTimeString)

    if message.content.startswith('!질풍 컷'):
        greenFlag = False
        greenTime = nextTime = now+datetime.timedelta(hours=2)
        tmp_greenTimeString = greenTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 질풍 ' + greenTimeString)

    if message.content.startswith('!광풍 컷'):
        redFlag = False
        redTime = nextTime = now+datetime.timedelta(hours=2)
        tmp_redTimeString = redTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 광풍 ' + redTimeString)

    if message.content.startswith('!산두 컷'):
        sanduFlag = False
        sanduTime = nextTime = now+datetime.timedelta(hours=3)
        tmp_sanduTimeString = sanduTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 산두 ' + sanduTimeString)

    if message.content.startswith('!에자 컷'):
        danduFlag = False
        danduTime = nextTime = now+datetime.timedelta(hours=5)
        tmp_danduTimeString = danduTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 에자 ' + danduTimeString)

    if message.content.startswith('!감데 컷'):
        gedFlag = False
        gedTime = nextTime = now+datetime.timedelta(hours=6)
        tmp_gedTimeString = gedTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 감데 ' + gedTimeString)

    if message.content.startswith('!개미 컷'):
        sigamFlag = False
        sigamTime = nextTime = now+datetime.timedelta(hours=2)
        tmp_sigamTimeString = sigamTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 개미 ' + sigamTimeString)

    if message.content.startswith('!스피 컷'):
        digamFlag = False
        digamTime = nextTime = now+datetime.timedelta(hours=3)
        tmp_digamTimeString = digamTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 스피 ' + digamTimeString)

    if message.content.startswith('!도펠 컷'):
        figamFlag = False
        figamTime = nextTime = now+datetime.timedelta(hours=4)
        tmp_figamTimeString = figamTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 도펠 ' + figamTimeString)
        


    if message.content.startswith('!기감 젠'):
        qigamFlag = False
        qigamTime = nextTime = now
        tmp_qigamTimeString = qigamTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 기감 ' + qigamTimeString)
        
    if message.content.startswith('!거드 젠'):
        gudeFlag = False
        gudeTime = nextTime = now
        tmp_gudeTimeString = gudeTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 거드 ' + gudeTimeString)

    if message.content.startswith('!이프 젠'):
        ifFlag = False
        ifTime = nextTime = now
        tmp_ifTimeString = ifTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 이프 ' + ifTimeString)

    if message.content.startswith('!마요 젠'):
        mayoFlag = False
        mayoTime = nextTime = now
        tmp_mayoTimeString = mayoTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 마요 ' + mayoTimeString)

    if message.content.startswith('!피닉 젠'):
        pinyxFlag = False
        pinyxTime = nextTime = now
        tmp_pinyxTimeString = pinyxTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 피닉 ' + pinyxTimeString)

    if message.content.startswith('!대흑 젠'):
        dehugFlag = False
        dehugTime = nextTime = now
        tmp_dehugTimeString = dehugTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 대흑 ' + dehugTimeString)

    if message.content.startswith('!서드1 젠'):
        sedeFlag = False
        sedeTime = nextTime = now
        tmp_sedeTimeString = sedeTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 서드1 ' + sedeTimeString)

    if message.content.startswith('!서드2 젠'):
        sede2Flag = False
        sede2Time = nextTime = now
        tmp_sede2TimeString = sede2TimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 서드2 ' + sede2TimeString)

    if message.content.startswith('!중드 젠'):
        jungdeFlag = False
        jungdeTime = nextTime = now
        tmp_jungdeTimeString = jungdeTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 중드 ' + jungdeTimeString)

    if message.content.startswith('!동드 젠'):
        dongdeFlag = False
        dongdeTime = nextTime = now
        tmp_dongdeTimeString = dongdeTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 동드 ' + dongdeTimeString)

    if message.content.startswith('!아르 젠'):
        arFlag = False
        arTime = nextTime = now
        tmp_arTimeString = arTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 아르 ' + arTimeString)

    if message.content.startswith('!자크 젠'):
        jakFlag = False
        jakTime = nextTime = now
        tmp_jakTimeString = jakTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 자크 ' + jakTimeString)

    if message.content.startswith('!카파 젠'):
        kapaFlag = False
        kapaTime = nextTime = now
        tmp_kapaTimeString = kapaTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 카파 ' + kapaTimeString)

    if message.content.startswith('!웜 젠'):
        warmFlag = False
        warmTime = nextTime = now
        tmp_warmTimeString = warmTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 웜 ' + warmTimeString)

    if message.content.startswith('!데스 젠'):
        deathFlag = False
        deathTime = nextTime = now
        tmp_deathTimeString = deathTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 데스 ' + deathTimeString)

    if message.content.startswith('!커츠 젠'):
        curchFlag = False
        curchTime = nextTime = now
        tmp_curchTimeString = curchTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 커츠 ' + curchTimeString)

    if message.content.startswith('!질풍 젠'):
        greenFlag = False
        greenTime = nextTime = now
        tmp_greenTimeString = greenTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 질풍 ' + greenTimeString)

    if message.content.startswith('!광풍 젠'):
        redFlag = False
        redTime = nextTime = now
        tmp_redTimeString = redTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 광풍 ' + redTimeString)
    
    if message.content.startswith('!산두 젠'):
        sanduFlag = False
        sanduTime = nextTime = now
        tmp_sanduTimeString = sanduTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 산두 ' + sanduTimeString)

    if message.content.startswith('!에자 젠'):
        danduFlag = False
        danduTime = nextTime = now
        tmp_danduTimeString = danduTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 에자 ' + danduTimeString)

    if message.content.startswith('!감데 젠'):
        gedFlag = False
        gedTime = nextTime = now
        tmp_gedTimeString = gedTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 감데 ' + gedTimeString)

    if message.content.startswith('!개미 젠'):
        sigamFlag = False
        sigamTime = nextTime = now
        tmp_sigamTimeString = sigamTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 개미 ' + sigamTimeString)

    if message.content.startswith('!스피 젠'):
        digamFlag = False
        digamTime = nextTime = now
        tmp_digamTimeString = digamTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 스피 ' + digamTimeString)

    if message.content.startswith('!도펠 젠'):
        figamFlag = False
        figamTime = nextTime = now
        tmp_figamTimeString = figamTimeString = nextTime.strftime('%H:%M:%S')
        await client.send_message(channel, '다음 도펠 ' + figamTimeString)



    try:
        if message.content.startswith('!거드 멍'):
            gudeFlag = False
            now = tmp_gudeTime
            gudeTime = nextTime = now+datetime.timedelta(hours=3)
            gudeTimeString = gudeTime.strftime('%H:%M:%S')
            await client.send_message(channel, '다음 거드 ' + gudeTimeString)

        if message.content.startswith('!이프 멍'):
            ifFlag = False
            now = tmp_ifTime
            ifTime = nextTime = now+datetime.timedelta(hours=2)
            ifTimeString = ifTime.strftime('%H:%M:%S')
            await client.send_message(channel, '다음 이프 ' + ifTimeString)

        if message.content.startswith('!마요 멍'):
            mayoFlag = False
            now = tmp_mayoTime
            mayoTime = nextTime = now+datetime.timedelta(hours=3)
            mayoTimeString = mayoTime.strftime('%H:%M:%S')
            await client.send_message(channel, '다음 마요 ' + mayoTimeString)

        if message.content.startswith('!피닉 멍'):
            pinyxFlag = False
            now = tmp_pinyxTime
            pinyxTime = nextTime = now+datetime.timedelta(hours=7)
            pinyxTimeString = pinyxTime.strftime('%H:%M:%S')
            await client.send_message(channel, '다음 피닉 ' + pinyxTimeString)

        if message.content.startswith('!웜 멍'):
            warmFlag = False
            now = tmp_warmTime
            warmTime = nextTime = now+datetime.timedelta(hours=2)
            warmTimeString = warmTime.strftime('%H:%M:%S')
            await client.send_message(channel, '다음 웜 ' + warmTimeString)

        if message.content.startswith('!데스 멍'):
            deathFlag = False
            now = tmp_deathTime
            deathTime = nextTime = now+datetime.timedelta(hours=7)
            deathTimeString = deathTime.strftime('%H:%M:%S')
            await client.send_message(channel, '다음 데스 ' + deathTimeString)

        if message.content.startswith('!커츠 멍'):
            curchFlag = False
            now = tmp_curchTime
            curchTime = nextTime = now+datetime.timedelta(hours=10)
            curchTimeString = curchTime.strftime('%H:%M:%S')
            await client.send_message(channel, '다음 커츠 ' + curchTimeString)

        if message.content.startswith('!질풍 멍'):
            greenFlag = False
            now = tmp_greenTime
            greenTime = nextTime = now+datetime.timedelta(hours=2)
            greenTimeString = greenTime.strftime('%H:%M:%S')
            await client.send_message(channel, '다음 질풍 ' + greenTimeString)

        if message.content.startswith('!광풍 멍'):
            redFlag = False
            now = tmp_redTime
            redTime = nextTime = now+datetime.timedelta(hours=2)
            redTimeString = redTime.strftime('%H:%M:%S')
            await client.send_message(channel, '다음 광풍 ' + redTimeString)

        if message.content.startswith('!에자 멍'):
            danduFlag = False
            now = tmp_danduTime
            danduTime = nextTime = now+datetime.timedelta(hours=5)
            danduTimeString = danduTime.strftime('%H:%M:%S')
            await client.send_message(channel, '다음 에자 ' + danduTimeString)

            
        if message.content.startswith('!도펠 멍'):
            figamFlag = False
            now = tmp_figamTime
            figamTime = nextTime = now+datetime.timedelta(hours=4)
            figamTimeString = figamTime.strftime('%H:%M:%S')
            await client.send_message(channel, '다음 도펠 ' + figamTimeString)


    except:
        await client.send_message(channel, '입력 오류 ')

      

    if message.content.startswith('!불러오기'):
        file = open("D:\my_bot.db", 'r')
        
        while True:
            line = file.readline();
            
            if not line: break
            
            #await client.send_message(channel, line)

            if (line.startswith(' - 기감 : ')):
                hours = line[8:10]
                minutes = line[11:13]
                now2 = datetime.datetime.now()
                now2 = now.replace(hour=int(hours), minute=int(minutes))
                qigamTime = now2
                qigamTimeString = qigamTime.strftime('%H:%M:%S')

            if (line.startswith(' - 마요 : ')):
                hours = line[8:10]
                minutes = line[11:13]
                now2 = datetime.datetime.now()
                now2 = now.replace(hour=int(hours), minute=int(minutes))
                mayoTime = now2
                mayoTimeString = mayoTime.strftime('%H:%M:%S')

            if (line.startswith(' - 피닉 : ')):
                hours = line[8:10]
                minutes = line[11:13]
                now2 = datetime.datetime.now()
                now2 = now.replace(hour=int(hours), minute=int(minutes))
                pinyxTime = now2
                pinyxTimeString = pinyxTime.strftime('%H:%M:%S')

            if (line.startswith(' - 중드 : ')):
                hours = line[8:10]
                minutes = line[11:13]
                now2 = datetime.datetime.now()
                now2 = now.replace(hour=int(hours), minute=int(minutes))
                jungdeTime = now2
                jungdeTimeString = jungdeTime.strftime('%H:%M:%S')

            if (line.startswith(' - 동드 : ')):
                hours = line[8:10]
                minutes = line[11:13]
                now2 = datetime.datetime.now()
                now2 = now.replace(hour=int(hours), minute=int(minutes))
                dongdeTime = now2
                dongdeTimeString = dongdeTime.strftime('%H:%M:%S')

            if (line.startswith(' - 아르 : ')):
                hours = line[8:10]
                minutes = line[11:13]
                now2 = datetime.datetime.now()
                now2 = now.replace(hour=int(hours), minute=int(minutes))
                arTime = now2
                arTimeString = arTime.strftime('%H:%M:%S')

            if (line.startswith(' - 자크 : ')):
                hours = line[8:10]
                minutes = line[11:13]
                now2 = datetime.datetime.now()
                now2 = now.replace(hour=int(hours), minute=int(minutes))
                jakTime = now2
                jakTimeString = jakTime.strftime('%H:%M:%S')

            if (line.startswith(' - 카파 : ')):
                hours = line[8:10]
                minutes = line[11:13]
                now2 = datetime.datetime.now()
                now2 = now.replace(hour=int(hours), minute=int(minutes))
                kapaTime = now2
                kapaTimeString = kapaTime.strftime('%H:%M:%S')

            if (line.startswith(' - 웜 : ')):
                hours = line[7:9]
                minutes = line[10:12]
                now2 = datetime.datetime.now()
                now2 = now.replace(hour=int(hours), minute=int(minutes))
                warmTime = now2
                warmTimeString = warmTime.strftime('%H:%M:%S')

            if (line.startswith(' - 데스 : ')):
                hours = line[8:10]
                minutes = line[11:13]
                now2 = datetime.datetime.now()
                now2 = now.replace(hour=int(hours), minute=int(minutes))
                deathTime = now2
                deathTimeString = deathTime.strftime('%H:%M:%S')

            if (line.startswith(' - 광풍 : ')):
                hours = line[8:10]
                minutes = line[11:13]
                now2 = datetime.datetime.now()
                now2 = now.replace(hour=int(hours), minute=int(minutes))
                redTime = now2
                redTimeString = redTime.strftime('%H:%M:%S')

            if (line.startswith(' - 에자 : ')):
                hours = line[8:10]
                minutes = line[11:13]
                now2 = datetime.datetime.now()
                now2 = now.replace(hour=int(hours), minute=int(minutes))
                danduTime = now2
                danduTimeString = danduTime.strftime('%H:%M:%S')

            if (line.startswith(' - 개미 : ')):
                hours = line[8:10]
                minutes = line[11:13]
                now2 = datetime.datetime.now()
                now2 = now.replace(hour=int(hours), minute=int(minutes))
                sigamTime = now2
                sigamTimeString = sigamTime.strftime('%H:%M:%S')            

            if (line.startswith(' - 스피 : ')):
                hours = line[8:10]
                minutes = line[11:13]
                now2 = datetime.datetime.now()
                now2 = now.replace(hour=int(hours), minute=int(minutes))
                digamTime = now2
                digamTimeString = digamTime.strftime('%H:%M:%S')

            if (line.startswith(' - 도펠 : ')):
                hours = line[8:10]
                minutes = line[11:13]
                now2 = datetime.datetime.now()
                now2 = now.replace(hour=int(hours), minute=int(minutes))
                figamTime = now2
                figamTimeString = figamTime.strftime('%H:%M:%S')

            if (line.startswith(' - 거드 : ')):
                hours = line[8:10]
                minutes = line[11:13]
                now2 = datetime.datetime.now()
                now2 = now.replace(hour=int(hours), minute=int(minutes))
                gudeTime = now2
                gudeTimeString = gudeTime.strftime('%H:%M:%S')

            if (line.startswith(' - 이프 : ')):
                hours = line[8:10]
                minutes = line[11:13]
                now2 = datetime.datetime.now()
                now2 = now.replace(hour=int(hours), minute=int(minutes))
                ifTime = now2
                ifTimeString = ifTime.strftime('%H:%M:%S')

            if (line.startswith(' - 피닉 : ')):
                hours = line[8:10]
                minutes = line[11:13]
                now2 = datetime.datetime.now()
                now2 = now.replace(hour=int(hours), minute=int(minutes))
                pinyxTime = now2
                pinyxTimeString = pinyxTime.strftime('%H:%M:%S')

            if (line.startswith(' - 대흑 : ')):
                hours = line[8:10]
                minutes = line[11:13]
                now2 = datetime.datetime.now()
                now2 = now.replace(hour=int(hours), minute=int(minutes))
                dehugTime = now2
                dehugTimeString = dehugTime.strftime('%H:%M:%S')

            if (line.startswith(' - 서드1 : ')):
                hours = line[9:11]
                minutes = line[12:14]
                now2 = datetime.datetime.now()
                now2 = now.replace(hour=int(hours), minute=int(minutes))
                sedeTime = now2
                sedeTimeString = sedeTime.strftime('%H:%M:%S')

            if (line.startswith(' - 서드2 : ')):
                hours = line[9:11]
                minutes = line[12:14]
                now2 = datetime.datetime.now()
                now2 = now.replace(hour=int(hours), minute=int(minutes))
                sede2Time = now2
                sede2TimeString = sede2Time.strftime('%H:%M:%S')

            if (line.startswith(' - 커츠 : ')):
                hours = line[8:10]
                minutes = line[11:13]
                now2 = datetime.datetime.now()
                now2 = now.replace(hour=int(hours), minute=int(minutes))
                curchTime = now2
                curchTimeString = curchTime.strftime('%H:%M:%S')

            if (line.startswith(' - 질풍 : ')):
                hours = line[8:10]
                minutes = line[11:13]
                now2 = datetime.datetime.now()
                now2 = now.replace(hour=int(hours), minute=int(minutes))
                greenTime = now2
                greenTimeString = greenTime.strftime('%H:%M:%S')

            if (line.startswith(' - 산두 : ')):
                hours = line[8:10]
                minutes = line[11:13]
                now2 = datetime.datetime.now()
                now2 = now.replace(hour=int(hours), minute=int(minutes))
                sanduTime = now2
                sanduTimeString = sanduTime.strftime('%H:%M:%S')

            if (line.startswith(' - 감데 : ')):
                hours = line[8:10]
                minutes = line[11:13]
                now2 = datetime.datetime.now()
                now2 = now.replace(hour=int(hours), minute=int(minutes))
                gedTime = now2
                gedTimeString = gedTime.strftime('%H:%M:%S')

            if (line.startswith(' - 개미 : ')):
                hours = line[8:10]
                minutes = line[11:13]
                now2 = datetime.datetime.now()
                now2 = now.replace(hour=int(hours), minute=int(minutes))
                sigamTime = now2
                sigamTimeString = sigamTime.strftime('%H:%M:%S')            

            if (line.startswith(' - 도펠 : ')):
                hours = line[8:10]
                minutes = line[11:13]
                now2 = datetime.datetime.now()
                now2 = now.replace(hour=int(hours), minute=int(minutes))
                figamTime = now2
                figamTimeString = figamTime.strftime('%H:%M:%S')                

            if (line.startswith(' - 중드 : ')):
                hours = line[8:10]
                minutes = line[11:13]
                now2 = datetime.datetime.now()
                now2 = now.replace(hour=int(hours), minute=int(minutes))
                jungdeTime = now2
                jungdeTimeString = jungdeTime.strftime('%H:%M:%S')

            if (line.startswith(' - 자크 : ')):
                hours = line[8:10]
                minutes = line[11:13]
                now2 = datetime.datetime.now()
                now2 = now.replace(hour=int(hours), minute=int(minutes))
                jakTime = now2
                jakTimeString = jakTime.strftime('%H:%M:%S')
                
        file.close()
        await client.send_message(channel, '불러오기 완료')

       


    if message.content.startswith('!보스탐'):

        datelist=[qigamTimeString, gudeTimeString, ifTimeString, mayoTimeString, pinyxTimeString, dehugTimeString,
                  sedeTimeString, sede2TimeString, jungdeTimeString, dongdeTimeString, arTimeString, jakTimeString,
                  kapaTimeString, warmTimeString, deathTimeString, curchTimeString, redTimeString, greenTimeString, sanduTimeString, gedTimeString, danduTimeString,
                  sigamTimeString, digamTimeString, figamTimeString,]

        information = '----- 보스탐 정보 -----\n'
        
        for timestring in sorted(datelist):
            #print(timestring)
        
            if timestring == qigamTimeString:
                if qigamTimeString != '99:99:99':
                    information += ' - 기감 : ' + qigamTimeString + '\n'

            elif timestring == gudeTimeString:
                if gudeTimeString != '99:99:99':
                    information += ' - 거드 : ' + gudeTimeString + '\n'

            elif timestring == ifTimeString:     
                if ifTimeString != '99:99:99':
                    information += ' - 이프 : ' + ifTimeString + '\n'

            elif timestring == mayoTimeString:        
                if mayoTimeString != '99:99:99':
                    information += ' - 마요 : ' + mayoTimeString + '\n'

            elif timestring == pinyxTimeString:        
                if pinyxTimeString != '99:99:99':
                    information += ' - 피닉 : ' + pinyxTimeString + '\n'

            elif timestring == dehugTimeString:       
                if dehugTimeString != '99:99:99':
                    information += ' - 대흑 : ' + dehugTimeString + '\n'

            elif timestring == sedeTimeString:       
                if sedeTimeString != '99:99:99':
                    information += ' - 서드1 : ' + sedeTimeString + '\n'
                    
            elif timestring == sede2TimeString:        
                if sede2TimeString != '99:99:99':
                    information += ' - 서드2 : ' + sede2TimeString + '\n'

            elif timestring == jungdeTimeString:     
                if jungdeTimeString != '99:99:99':
                    information += ' - 중드 : ' + jungdeTimeString + '\n'

            elif timestring == dongdeTimeString: 
                if dongdeTimeString != '99:99:99':
                    information += ' - 동드 : ' + dongdeTimeString + '\n'

            elif timestring == arTimeString: 
                if arTimeString != '99:99:99':
                    information += ' - 아르 : ' + arTimeString + '\n'

            elif timestring == jakTimeString:     
                if jakTimeString != '99:99:99':
                    information += ' - 자크 : ' + jakTimeString + '\n'

            elif timestring == kapaTimeString:     
                if kapaTimeString != '99:99:99':
                    information += ' - 카파 : ' + kapaTimeString + '\n'

            elif timestring == warmTimeString:     
                if warmTimeString != '99:99:99':
                    information += ' - 웜 : ' + warmTimeString + '\n'

            elif timestring == deathTimeString: 
                if deathTimeString != '99:99:99':
                    information += ' - 데스 : ' + deathTimeString + '\n'

            elif timestring == curchTimeString:    
                if curchTimeString != '99:99:99':
                    information += ' - 커츠 : ' + curchTimeString + '\n'

            elif timestring == redTimeString:     
                if redTimeString != '99:99:99':
                    information += ' - 광풍 : ' + redTimeString + '\n'

            elif timestring == greenTimeString:     
                if greenTimeString != '99:99:99':
                    information += ' - 질풍 : ' + greenTimeString + '\n'
                    
            elif timestring == sanduTimeString: 
                if sanduTimeString != '99:99:99':
                    information += ' - 산두 : ' + sanduTimeString + '\n'

            elif timestring == danduTimeString: 
                if danduTimeString != '99:99:99':
                    information += ' - 에자 : ' + danduTimeString + '\n'

            elif timestring == gedTimeString:     
                if gedTimeString != '99:99:99':
                    information += ' - 감데 : ' + gedTimeString + '\n'
        
            elif timestring == sigamTimeString:
                if sigamTimeString != '99:99:99':
                    information += ' - 개미 : ' + sigamTimeString + '\n'
        
            elif timestring == digamTimeString:
                if digamTimeString != '99:99:99':
                    information += ' - 스피 : ' + digamTimeString + '\n'
        
            elif timestring == figamTimeString:
                if figamTimeString != '99:99:99':
                    information += ' - 도펠 : ' + figamTimeString + '\n'                    


        if gudeTimeString == '99:99:99':
            information += ' - 거드 입력 안됨\n'
        if ifTimeString == '99:99:99':
            information += ' - 이프 입력 안됨\n'
        if mayoTimeString == '99:99:99':
            information += ' - 마요 입력 안됨\n'
        if warmTimeString == '99:99:99':
            information += ' - 웜 입력 안됨\n'
        if pinyxTimeString == '99:99:99':
            information += ' - 피닉 입력 안됨\n'
        if curchTimeString == '99:99:99':
            information += ' - 커츠 입력 안됨\n'
        if deathTimeString == '99:99:99':
            information += ' - 데스 입력 안됨\n'
        if danduTimeString == '99:99:99':
            information += ' - 에자 입력 안됨\n'
        if dehugTimeString == '99:99:99':
            information += ' - 대흑 입력 안됨\n'
        if jakTimeString == '99:99:99':
            information += ' - 자크 입력 안됨\n'
        if gedTimeString == '99:99:99':
            information += ' - 감데 입력 안됨\n'
        if greenTimeString == '99:99:99':
            information += ' - 질풍 입력 안됨\n'
        if sanduTimeString == '99:99:99':
            information += ' - 산두 입력 안됨\n'
        if qigamTimeString == '99:99:99':
            information += ' - 기감 입력 안됨\n'
        if sedeTimeString == '99:99:99':
            information += ' - 서드1 입력 안됨\n'        
        if sede2TimeString == '99:99:99':
            information += ' - 서드2 입력 안됨\n'
        if kapaTimeString == '99:99:99':
            information += ' - 카파 입력 안됨\n'
        if redTimeString == '99:99:99':
            information += ' - 광풍 입력 안됨\n'
        if jungdeTimeString == '99:99:99':
            information += ' - 중드 입력 안됨\n'
        if dongdeTimeString == '99:99:99':
            information += ' - 동드 입력 안됨\n'
        if arTimeString == '99:99:99':
            information += ' - 아르 입력 안됨\n'
        if sigamTimeString == '99:99:99':
            information += ' - 개미 입력 안됨\n'
        if digamTimeString == '99:99:99':
            information += ' - 스피 입력 안됨\n'
        if figamTimeString == '99:99:99':
            information += ' - 도펠 입력 안됨\n'


        await client.send_message(channel, information)

        file = open("D:\my_bot.db", 'w')
        file.write(information);
        file.close()


    if message.content.startswith('!현재시간'):
        await client.send_message(channel, datetime.datetime.now().strftime('%H:%M:%S'))

client.run(token)

