from flask import Flask, request
import re
import json
import os
import glob
import inspect


def availableDate(activity, destination):
    available = []
    if activity == '温泉ツアー' and destination == '登別':
        for i in range(1, 31):
            if i % 2 == 0:
                available.append('2022年3月' + str(i) + '日午前')
                available.append('2022年4月' + str(i) + '日午前')
            else:
                available.append('2022年3月'+ str(i) + '日午後')
                available.append('2022年4月'+ str(i) + '日午後')
        available.append('2022年3月31日午後')
    elif activity == '温泉ツアー' and destination == '有馬':
        for i in range(1, 31):
            if i % 2 == 0:
                available.append('2022年3月' + str(i) + '日午後')
                available.append('2022年4月' + str(i) + '日午後')
            else:
                available.append('2022年3月'+ str(i) + '日午前')
                available.append('2022年4月'+ str(i) + '日午前')
        available.append('2022年3月31日午後')
    elif activity == '温泉ツアー' and destination == '別府':
        for i in range(1, 31):
            if i % 2 == 0:
                available.append('2022年3月' + str(i) + '日午前')
                available.append('2022年4月' + str(i) + '日午前')
            else:
                available.append('2022年3月'+ str(i) + '日午後')
                available.append('2022年4月'+ str(i) + '日午後')
        available.append('2022年3月31日午後')
    elif activity == '温泉ツアー' and destination == '草津':
        for i in range(1, 31):
            if i % 2 == 0:
                available.append('2022年3月' + str(i) + '日午前')
                available.append('2022年4月' + str(i) + '日午前')
        available.append('2022年3月31日午後')
    elif activity == '温泉ツアー' and destination == '白浜':
        for i in range(1, 31):
            if i % 2 == 0:
                available.append('2022年3月' + str(i) + '日午後')
                available.append('2022年4月' + str(i) + '日午後')
        available.append('2022年3月31日午後')
    elif activity == '遊園地 ツアー' and destination == 'USJ':
        for i in range(1, 31):
            if i % 7 != 3:
                available.append('2022年3月' + str(i) + '日午前')
                available.append('2022年4月' + str(i) + '日午前')
    elif activity == '遊園地 ツアー' and destination == 'ディズニーランド':
        for i in range(1, 31):
            available.append('2022年4月' + str(i) + '日午前')
    elif activity == '遊園地 ツアー' and destination == 'ディズニーシー':
        for i in range(1, 31):
            available.append('2022年4月' + str(i) + '日午前')
    elif activity == '遊園地 ツアー' and destination == '花やしき':
        for i in range(1, 31):
            if i % 2 == 0:
                available.append('2022年3月' + str(i) + '日午前')
                available.append('2022年4月' + str(i) + '日午前')
            else:
                available.append('2022年3月'+ str(i) + '日午後')
                available.append('2022年4月'+ str(i) + '日午後')
    elif activity == '遊園地 ツアー' and destination == 'ひらかたパーク':
        for i in range(1, 31):
            if i % 2 == 0:
                available.append('2022年3月' + str(i) + '日午前')
                available.append('2022年4月' + str(i) + '日午前')
            else:
                available.append('2022年3月'+ str(i) + '日午後')
                available.append('2022年4月'+ str(i) + '日午後')
    elif activity == 'バスツアー' and destination == '中華街':
        for i in range(1, 31):
            if i % 2 == 0:
                available.append('2022年3月' + str(i) + '日午前')
                available.append('2022年4月' + str(i) + '日午前')
            else:
                available.append('2022年3月'+ str(i) + '日午後')
                available.append('2022年4月'+ str(i) + '日午後')
    elif activity == 'バスツアー' and destination == '黒潮市場':
        for i in range(1, 31):
            if i % 2 == 0:
                available.append('2022年3月' + str(i) + '日午前')
                available.append('2022年4月' + str(i) + '日午前')
            else:
                available.append('2022年3月'+ str(i) + '日午後')
                available.append('2022年4月'+ str(i) + '日午後')
    elif activity == 'バスツアー' and destination == '姫路城':
        for i in range(1, 31):
            if i % 2 == 0:
                available.append('2022年3月' + str(i) + '日午前')
                available.append('2022年4月' + str(i) + '日午前')
            else:
                available.append('2022年3月'+ str(i) + '日午後')
                available.append('2022年4月'+ str(i) + '日午後')
    elif activity == 'バスツアー' and destination == 'ディズニーランド':
        for i in range(1, 31):
            available.append('2022年4月' + str(i) + '日午前')
    elif activity == 'バスツアー' and destination == '有馬':
        for i in range(1, 31):
            if i % 2 == 0:
                available.append('2022年3月' + str(i) + '日午前')
                available.append('2022年4月' + str(i) + '日午前')
            else:
                available.append('2022年3月'+ str(i) + '日午後')
                available.append('2022年4月'+ str(i) + '日午後')
    return available

def aviailableDestination(actNum):
    if actNum == 0:
        candidate = '登別、有馬、別府、草津、白浜'
    elif actNum == 1:
        candidate = 'USJ、ディズニーランド、ディズニーシー、花やしき、ひらかたパーク'
    else:
        candidate = '中華街、黒潮市場、姫路城、ディズニーランド、有馬'
    return candidate

app = Flask(__name__)
@app.route('/', methods=['POST'])
# DialogflowからWebhookリクエストが来るとindex()関数が呼び出される
def index():
    # Google Assistantが聞き取ったメッセージを取得し，input変数に代入
    input = request.json["queryResult"]["parameters"]["any"]
    printV('Received: ' + input)
    dictOfActivity = {'温泉ツアー':0, '遊園地 ツアー':1, 'バスツアー':2}
    place = [{'登別':13, '有馬':5, '別府':10, '草津':7, '白浜':5},
            {'USJ':3, 'ディズニーランド':5, 'ディズニーシー':5, '花やしき':4, 'ひらかたパーク':1},
            {'中華街':1.5, '黒潮市場':1.5, '姫路城':1, 'ディズニーランド':4, '有馬':1}]
    if input == 'バイバイ':     # 会話を終了するメッセージ「バイバイ」を受け取った場合
        message = 'さようなら'
        continueFlag = False
    else:                       # 通常のメッセージを受け取った場合
        message = ''
        # 状態(state)の取得
        data_path = os.getcwd() + '/state.txt'
        data_path1 = os.getcwd() + '/actNum.txt'
        data_path2 = os.getcwd() + '/activity.txt'
        data_path3 = os.getcwd() + '/destination.txt'
        data_path4 = os.getcwd() + '/price.txt'
        data_path5 = os.getcwd() + '/count.txt'
        # state.txtがHerokuサーバ上にあるかチェック
        if glob.glob(data_path): # state.txtが見つかった場合
            printV(data_path + ' is found!')
            with open(data_path, mode='r', encoding='utf-8') as r: # state.txtを読み込む
                # state.txtから状態を取得する
                state = int(r.read())
        else: # state.txtが見つからなかった場合
            printV(data_path + ' is not found!')
            with open(data_path, mode='w', encoding='utf-8') as w: # state.txtを作成
                # state.txtに「1」を書き込む
                w.write('1')
                state = 1
        if glob.glob(data_path1): # actNum.txtが見つかった場合
            printV(data_path1 + ' is found!')
            with open(data_path1, mode='r', encoding='utf-8') as r: # actNum.txtを読み込む
                # actNum.txtから状態を取得する
                actNum = int(r.read())
        else: # actNum.txtが見つからなかった場合
            printV(data_path1 + ' is not found!')
            with open(data_path1, mode='w', encoding='utf-8') as w: # actNum.txtを作成
                # actNum.txtに「0」を書き込む
                w.write('0')
                actNum = 0
        if glob.glob(data_path2): # activity.txtが見つかった場合
            printV(data_path2 + ' is found!')
            with open(data_path2, mode='r', encoding='utf-8') as r: # activity.txtを読み込む
                # activity.txtから状態を取得する
                activity = r.read()
        else: # activity.txtが見つからなかった場合
            printV(data_path2 + ' is not found!')
            with open(data_path2, mode='w', encoding='utf-8') as w: # activity.txtを作成
                # activity.txtに「（空白）」を書き込む
                w.write('')
                activity = ''
        if glob.glob(data_path3): # destination.txtが見つかった場合
            printV(data_path3 + ' is found!')
            with open(data_path3, mode='r', encoding='utf-8') as r: # destination.txtを読み込む
                # destination.txtから状態を取得する
                destination = r.read()
        else: # destination.txtが見つからなかった場合
            printV(data_path3 + ' is not found!')
            with open(data_path3, mode='w', encoding='utf-8') as w: # destination.txtを作成
                # destination.txtに「（空白）」を書き込む
                w.write('')
                destination = ''
        if glob.glob(data_path4): # price.txtが見つかった場合
            printV(data_path4 + ' is found!')
            with open(data_path4, mode='r', encoding='utf-8') as r: # price.txtを読み込む
                # price.txtから状態を取得する
                price = r.read()
        else: # price.txtが見つからなかった場合
            printV(data_path4 + ' is not found!')
            with open(data_path4, mode='w', encoding='utf-8') as w: # price.txtを作成
                # price.txtに「（空白）」を書き込む
                w.write('0')
                price = 0
        if glob.glob(data_path5): # count.txtが見つかった場合
            printV(data_path5 + ' is found!')
            with open(data_path5, mode='r', encoding='utf-8') as r: # count.txtを読み込む
                # count.txtから状態を取得する
                count = int(r.read())
        else: # count.txtが見つからなかった場合
            printV(data_path5 + ' is not found!')
            with open(data_path5, mode='w', encoding='utf-8') as w: # count.txtを作成
                # count.txtに「（空白）」を書き込む
                w.write('0')
                count = 1
        if input == 'リセット':
            with open(data_path, mode='w', encoding='utf-8') as w:
                # state.txtに「1」を上書き 
                w.write('1')
            with open(data_path5, mode='w', encoding='utf-8') as w:
                w.write('1')
            message = '状態をリセットしました。こんにちは。ご希望のアクティビティを教えてください。'
            continueFlag = True
        else:
            # 状態によって異なる応答を生成
            stateFlag = True
            if state == 1:
                res = re.search(r'(遊園地( |)|バス|温泉)ツアー', input)
                if res == None:
                    message = 'そのアクティビティはご用意していません。温泉ツアー、遊園地ツアー、バスツアーの中からいずれか一つをお答えください。'
                    stateFlag = False
                else:
                    activity = res.group()
                    with open(data_path1, mode='w', encoding='utf-8') as w:
                        w.write(str(dictOfActivity[activity]))
                    with open(data_path2, mode='w', encoding='utf-8') as w:
                        w.write(activity)
                    message = activity + 'ですね。次に、ご希望の場所を教えてください。'
            elif state == 2:
                res = re.search(r'(登別|有馬|別府|草津|白浜|USJ|ディズニーランド|ディズニーシー|花やしき|ひらかたパーク|中華街|黒潮市場|姫路城)', input)
                if res == None:
                    message = 'よく聞き取れませんでした。' + aviailableDestination(actNum) + 'の中からいずれか一つをお答えください。'
                    stateFlag = False
                else:
                    destination = res.group()
                    if destination in list(place[actNum].keys()):
                        with open(data_path3, mode='w', encoding='utf-8') as w:
                            w.write(destination)
                        with open(data_path4, mode='w', encoding='utf-8') as w:
                            w.write(str(place[actNum][destination]))
                        message = destination + 'ですね。次に、ご希望の日程とご希望の時間を午前か午後かでお答えください。'
                    else:
                        message = destination + '行きの' + activity + 'はご用意していません。' + aviailableDestination(actNum) + 'の中からいずれか一つをお答えください。'
                        stateFlag = False
            else:
                res1 = re.search(r'2022年', input)
                res2 = re.search(r'(3|4)月', input)
                res3 = re.search(r'(\d{1}|\d{2})日', input)
                res4 = re.search(r'午(前|後)', input)
                if res1 == None:
                    message = '予約する年をよく聞き取れませんでした。2022年3月1日から2022年4月30日の間でもう一度お願いします。'
                    stateFlag = False
                elif res2 == None:
                    message = '予約する月をよく聞き取れませんでした。2022年3月1日から2022年4月30日の間でもう一度お願いします。'
                    stateFlag = False
                elif res3 == None:
                    message = '予約する日をよく聞き取れませんでした。2022年3月1日から2022年4月30日の間でもう一度お願いします。'
                    stateFlag = False
                elif res4 == None:
                    message = '予約する時間が午前か午後かをよく聞き取れませんでした。2022年3月1日から2022年4月30日の間でもう一度お願いします。'
                    stateFlag = False
                else:
                    date = res1.group() + res2.group() + res3.group() + res4.group()
                    if date in availableDate(activity, destination):
                        message = destination + '行きの' + activity + 'の' + date + 'でご予約を承りました。料金は' + price +'万円です。'
                    else:
                        if count >= 4:
                            message = 'ご希望のプランでは予約ができない可能性があります。一度対話を終了します。'
                            with open(data_path, mode='w', encoding='utf-8') as w:
                                w.write('1')
                            count = count + 1
                        else:
                            with open(data_path5, mode='w', encoding='utf-8') as w:
                                w.write(str(count + 1))
                            message = 'その日時は予約できません。他の日時をお答えください。'
            if count >= 5:
                continueFlag = False
            else:
                continueFlag = True
            # 状態の更新
            if stateFlag:
                with open(data_path, mode='w', encoding='utf-8') as w:
                    w.write(str(state + 1))
        printV('state is ' + str(state))

    # Dialogflow(Firebase)へのWebhookレスポンス作成
    response = makeResponse(message, continueFlag)
    # Webhookレスポンス送信
    return json.dumps(response)

# Webhookレスポンスの作成（JSON形式）
# message:Google Homeの発話内容，continueFlag:会話を続けるかどうかのフラグ（続ける：Yes，続けない：No）
def makeResponse(message, continueFlag=True):
    response = {
            "payload": {
                "google": {
                    "expectUserResponse": continueFlag,
                    "richResponse": {
                        "items": [
                            {
                                "simpleResponse": {
                                    "textToSpeech": message
                                }
                            }
                        ]
                    }
                }
            },
            "fulfillmentMessages": [
                {
                    "text": {
                        "text": [
                            message
                        ]
                    }
                }
            ]
        }
    return response

# 詳細情報(Verbose)付き出力
def printV(content):
    frame = inspect.currentframe().f_back
    print(content, end='')
    print(' (file: ' + os.path.basename(frame.f_code.co_filename) + ', function: ' + frame.f_code.co_name + ', line: ' + str(frame.f_lineno) + ')')