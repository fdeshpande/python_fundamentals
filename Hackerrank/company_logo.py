# s="tctesvgnclzykpmbcqixlonfidpdjbynrcpxsjmucpeyormenrjbibafpzkquminfnnbizgbpxeovefuykjrcebfnntvyamkgykcnvjqxvnprwrarpcgrjoucywgfnbnysgwzymcxyachlpsglosflsubqhvobedbtzuqmvgyvrpeclcsoeemysuyuejpjtahnrzmebztrjtzhhjtqlmhttxdnjilqsqymmhjmlzikkdzasshfktbfsaozyhaduyqcufucqxxuksnfjaiwacvlyiimfrzyxwobrfoalhmowcobbpwuqpwvlstbngxjrebfnckbcagoacmfuzvmqxefiwqkgfwgghxbulvhqiaqewdmmizjfgyymchohejdpsnnpvmtgqzxkesnrikywoolootuuikapycpxhkrplyuhzhndxckbvaynkzreybomwuemxtgmrjxbysarlsemwambppmrumivznuaqskzgpamfsjwwrjvtwyqpainuyyfmwnegjlmanqwvshvpsbpeykfwykdumdgjlkuwoxwqctihfdwvxrefggsxmjtxmpdcigjertcxwennzyamqpahytneybgmdyupusarhemazvozdqurftdvbnavynrsdzxjebjrdatbkoezdgwznplqqzakozjecyewsidawuxfpusmeusantzdglridxnwvbgwjcaofbplnwyxtmwerskdzwhgxfdqbpfhymlgwtvqeehnnhwgklxqkdjgmfxvuxwwpmnqxsaiitfehhbqdyveqfrqjjfnggmhjrgldgctnhzrrqdtbunxxcuwibqkjdickhrtbznevczqoidnfmtaveysysrgbhctwxmevuutrwyriugtuvhuxkqapfjyplczgekxisffoivofobqmipqxzunlrrtcmaivvhbfjvgywwtqubwszqwjtskyuxljhinqrhcgddejurivukcspaazjjwwloreqlreqjifwsv"
# !/bin/python3

import math
import os
import random
import re
import sys

# s ="tctesvgnclzykpmbcqixlonfidpdjbynrcpxsjmucpeyormenrjbibafpzkquminfnnbizgbpxeovefuykjrcebfnntvyamkgykcnvjqxvnprwrarpcgrjoucywgfnbnysgwzymcxyachlpsglosflsubqhvobedbtzuqmvgyvrpeclcsoeemysuyuejpjtahnrzmebztrjtzhhjtqlmhttxdnjilqsqymmhjmlzikkdzasshfktbfsaozyhaduyqcufucqxxuksnfjaiwacvlyiimfrzyxwobrfoalhmowcobbpwuqpwvlstbngxjrebfnckbcagoacmfuzvmqxefiwqkgfwgghxbulvhqiaqewdmmizjfgyymchohejdpsnnpvmtgqzxkesnrikywoolootuuikapycpxhkrplyuhzhndxckbvaynkzreybomwuemxtgmrjxbysarlsemwambppmrumivznuaqskzgpamfsjwwrjvtwyqpainuyyfmwnegjlmanqwvshvpsbpeykfwykdumdgjlkuwoxwqctihfdwvxrefggsxmjtxmpdcigjertcxwennzyamqpahytneybgmdyupusarhemazvozdqurftdvbnavynrsdzxjebjrdatbkoezdgwznplqqzakozjecyewsidawuxfpusmeusantzdglridxnwvbgwjcaofbplnwyxtmwerskdzwhgxfdqbpfhymlgwtvqeehnnhwgklxqkdjgmfxvuxwwpmnqxsaiitfehhbqdyveqfrqjjfnggmhjrgldgctnhzrrqdtbunxxcuwibqkjdickhrtbznevczqoidnfmtaveysysrgbhctwxmevuutrwyriugtuvhuxkqapfjyplczgekxisffoivofobqmipqxzunlrrtcmaivvhbfjvgywwtqubwszqwjtskyuxljhinqrhcgddejurivukcspaazjjwwloreqlreqjifwsv"
s="qwertyuiopasdfghjklzxcvbnm"
if __name__ == '__main__':
    d = {}

    for i in s:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1

    c = 1
    sorted_dict = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

    for i, j in sorted_dict.items():
        if c <= 3:
            print(i, j)
        c += 1