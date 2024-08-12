# 음식 데이터를 정의합니다.
food_data = {
    "김치찌개": {
        "재료": {
            "김치": "200g",
            "돼지고기": "100g",
            "두부": "100g",
            "대파": "1대",
            "양파": "1/2개",
            "고춧가루": "1스푼",
            "참기름": "1스푼",
            "마늘": "2쪽",
            "국간장": "1스푼",
            "물": "2컵"
        },
        "레시피": [
            "1. 돼지고기를 참기름에 볶다가 김치를 넣고 볶아줍니다.",
            "2. 물을 넣고 끓여줍니다.",
            "3. 고춧가루, 마늘, 국간장을 넣고 10분 정도 끓입니다.",
            "4. 두부와 대파, 양파를 넣고 추가로 5분간 더 끓입니다."
        ],
        "영양성분": {
            "칼로리": "350kcal",
            "탄수화물": "15g",
            "단백질": "25g",
            "지방": "20g"
        }
    },
    "비빔밥": {
        "재료": {
            "밥": "1공기",
            "시금치": "50g",
            "고사리": "50g",
            "당근": "50g",
            "애호박": "50g",
            "계란": "1개",
            "고추장": "2스푼",
            "참기름": "1스푼",
            "김": "1장"
        },
        "레시피": [
            "1. 시금치, 고사리, 당근, 애호박을 각각 볶아줍니다.",
            "2. 밥 위에 볶은 재료들을 올려줍니다.",
            "3. 계란후라이를 만들어 밥 위에 올립니다.",
            "4. 고추장과 참기름을 넣고 비벼 먹습니다.",
            "5. 김을 잘라서 곁들입니다."
        ],
        "영양성분": {
            "칼로리": "500kcal",
            "탄수화물": "80g",
            "단백질": "20g",
            "지방": "15g"
        }
    },
    "된장찌개": {
        "재료": {
            "된장": "2스푼",
            "두부": "100g",
            "애호박": "50g",
            "감자": "100g",
            "대파": "1대",
            "마늘": "1쪽",
            "고추": "1개",
            "물": "2컵"
        },
        "레시피": [
            "1. 물에 된장을 풀고 끓입니다.",
            "2. 감자와 애호박을 넣고 끓입니다.",
            "3. 두부와 대파, 고추, 마늘을 넣고 추가로 끓입니다."
        ],
        "영양성분": {
            "칼로리": "200kcal",
            "탄수화물": "25g",
            "단백질": "10g",
            "지방": "8g"
        }
    },
    "불고기": {
        "재료": {
            "소고기": "200g",
            "양파": "1/2개",
            "대파": "1대",
            "간장": "2스푼",
            "설탕": "1스푼",
            "마늘": "2쪽",
            "참기름": "1스푼",
            "깨": "1스푼"
        },
        "레시피": [
            "1. 소고기에 간장, 설탕, 마늘, 참기름을 넣고 재웁니다.",
            "2. 팬에 양파와 대파를 볶다가 고기를 넣고 익힙니다.",
            "3. 고기가 익으면 깨를 뿌려 마무리합니다."
        ],
        "영양성분": {
            "칼로리": "400kcal",
            "탄수화물": "10g",
            "단백질": "30g",
            "지방": "25g"
        }
    },
    "잡채": {
        "재료": {
            "당면": "100g",
            "소고기": "100g",
            "당근": "50g",
            "시금치": "50g",
            "양파": "1/2개",
            "간장": "2스푼",
            "설탕": "1스푼",
            "참기름": "1스푼",
            "깨": "1스푼"
        },
        "레시피": [
            "1. 당면을 삶아 찬물에 헹궈줍니다.",
            "2. 소고기와 야채를 볶습니다.",
            "3. 삶은 당면을 넣고 간장, 설탕으로 간을 맞춥니다.",
            "4. 참기름과 깨를 뿌려 마무리합니다."
        ],
        "영양성분": {
            "칼로리": "450kcal",
            "탄수화물": "70g",
            "단백질": "20g",
            "지방": "15g"
        }
    },
    "떡볶이": {
        "재료": {
            "떡": "200g",
            "어묵": "100g",
            "고추장": "2스푼",
            "고춧가루": "1스푼",
            "설탕": "1스푼",
            "대파": "1대",
            "물": "1컵"
        },
        "레시피": [
            "1. 물에 고추장, 고춧가루, 설탕을 넣고 끓입니다.",
            "2. 떡과 어묵을 넣고 끓여줍니다.",
            "3. 대파를 넣고 마무리합니다."
        ],
        "영양성분": {
            "칼로리": "300kcal",
            "탄수화물": "60g",
            "단백질": "10g",
            "지방": "5g"
        }
    },
    "갈비찜": {
        "재료": {
            "소갈비": "300g",
            "양파": "1개",
            "당근": "50g",
            "감자": "100g",
            "간장": "3스푼",
            "설탕": "2스푼",
            "마늘": "3쪽",
            "참기름": "1스푼"
        },
        "레시피": [
            "1. 소갈비를 물에 데쳐 불순물을 제거합니다.",
            "2. 간장, 설탕, 마늘, 참기름으로 양념을 만들어 갈비를 재웁니다.",
            "3. 양파, 당근, 감자를 넣고 푹 끓입니다."
        ],
        "영양성분": {
            "칼로리": "600kcal",
            "탄수화물": "30g",
            "단백질": "40g",
            "지방": "35g"
        }
    },
    "김밥": {
        "재료": {
            "밥": "1공기",
            "김": "2장",
            "단무지": "50g",
            "오이": "50g",
            "계란": "2개",
            "시금치": "50g",
            "참기름": "1스푼",
            "소금": "약간"
        },
        "레시피": [
            "1. 밥에 참기름과 소금을 넣고 섞어줍니다.",
            "2. 김 위에 밥을 펴고 단무지, 오이, 계란, 시금치를 올립니다.",
            "3. 김밥을 말아줍니다.",
            "4. 먹기 좋은 크기로 자릅니다."
        ],
        "영양성분": {
            "칼로리": "400kcal",
            "탄수화물": "65g",
            "단백질": "12g",
            "지방": "10g"
        }
    },
    "미역국": {
        "재료": {
            "미역": "20g",
            "소고기": "100g",
            "마늘": "2쪽",
            "국간장": "1스푼",
            "참기름": "1스푼",
            "물": "5컵"
        },
        "레시피": [
            "1. 미역을 물에 불려서 잘게 자릅니다.",
            "2. 소고기를 참기름에 볶다가 마늘을 넣고 함께 볶습니다.",
            "3. 불린 미역을 넣고 함께 볶습니다.",
            "4. 물을 넣고 끓입니다.",
            "5. 국간장으로 간을 맞추고, 15분 정도 더 끓입니다."
        ],
        "영양성분": {
            "칼로리": "150kcal",
            "탄수화물": "5g",
            "단백질": "15g",
            "지방": "7g"
        }
    },
    "제육볶음": {
        "재료": {
            "돼지고기": "150g",
            "양파": "1/2개",
            "대파": "1대",
            "고추장": "1.5스푼",
            "고춧가루": "1스푼",
            "간장": "1스푼",
            "설탕": "1스푼",
            "마늘": "2쪽",
            "참기름": "1스푼",
            "깨": "약간"
        },
        "레시피": [
            "1. 돼지고기를 얇게 썰어 고추장, 고춧가루, 간장, 설탕, 마늘로 양념합니다.",
            "2. 양파와 대파를 썰어 준비합니다.",
            "3. 팬에 양념된 고기를 넣고 중간 불에서 볶아줍니다.",
            "4. 고기가 반 정도 익었을 때 양파와 대파를 넣고 함께 볶습니다.",
            "5. 고기가 완전히 익으면 참기름과 깨를 뿌려 마무리합니다."
        ],
        "영양성분": {
            "칼로리": "450kcal",
            "탄수화물": "15g",
            "단백질": "25g",
            "지방": "30g"
        }
    },
    "삼계탕": {
        "재료": {
            "닭": "1마리",
            "찹쌀": "1/2컵",
            "대추": "3개",
            "마늘": "3쪽",
            "인삼": "1뿌리",
            "대파": "1대",
            "물": "5컵"
        },
        "레시피": [
            "1. 닭을 깨끗이 씻고 찹쌀을 닭 안에 넣습니다.",
            "2. 냄비에 물을 넣고 닭과 대추, 마늘, 인삼을 넣고 끓입니다.",
            "3. 닭이 익을 때까지 끓이고 대파를 넣고 마무리합니다."
        ],
        "영양성분": {
            "칼로리": "800kcal",
            "탄수화물": "30g",
            "단백질": "60g",
            "지방": "45g"
        }
    },
    "순두부찌개": {
        "재료": {
            "순두부": "200g",
            "돼지고기": "100g",
            "대파": "1대",
            "양파": "1/2개",
            "애호박": "50g",
            "고추장": "1스푼",
            "고춧가루": "1스푼",
            "참기름": "1스푼",
            "마늘": "2쪽",
            "국간장": "1스푼",
            "계란": "1개",
            "물": "2컵"
        },
        "레시피": [
            "1. 돼지고기를 참기름에 볶다가 양파와 대파를 넣고 볶아줍니다.",
            "2. 고추장과 고춧가루를 넣고 잘 섞어줍니다.",
            "3. 물을 넣고 끓입니다.",
            "4. 애호박과 순두부를 넣고 끓입니다.",
            "5. 국간장과 마늘을 넣고 10분 정도 더 끓입니다.",
            "6. 계란을 넣고 살짝 익힌 후 마무리합니다."
        ],
        "영양성분": {
            "칼로리": "400kcal",
            "탄수화물": "15g",
            "단백질": "25g",
            "지방": "30g"
        }
    },
     "부대찌개": {
        "재료": {
            "햄": "100g",
            "소시지": "50g",
            "두부": "100g",
            "김치": "150g",
            "대파": "1대",
            "양파": "1/2개",
            "고추장": "1스푼",
            "고춧가루": "1스푼",
            "마늘": "2쪽",
            "국간장": "1스푼",
            "물": "3컵",
            "라면사리": "1개"
        },
        "레시피": [
            "1. 냄비에 김치와 햄, 소시지를 넣고 볶아줍니다.",
            "2. 물을 넣고 끓입니다.",
            "3. 고추장, 고춧가루, 마늘, 국간장을 넣고 끓입니다.",
            "4. 두부와 대파, 양파를 넣고 추가로 10분간 끓입니다.",
            "5. 마지막으로 라면사리를 넣고 익혀줍니다."
        ],
        "영양성분": {
            "칼로리": "550kcal",
            "탄수화물": "45g",
            "단백질": "20g",
            "지방": "30g"
        }
    },
    "김치볶음밥": {
        "재료": {
            "밥": "1공기",
            "김치": "100g",
            "돼지고기": "50g",
            "양파": "1/4개",
            "대파": "1대",
            "고춧가루": "1스푼",
            "간장": "1스푼",
            "참기름": "1스푼",
            "계란": "1개"
        },
        "레시피": [
            "1. 돼지고기와 양파, 대파를 함께 볶아줍니다.",
            "2. 김치를 넣고 더 볶습니다.",
            "3. 밥과 고춧가루를 넣고 섞어 볶아줍니다.",
            "4. 간장으로 간을 맞추고, 참기름을 넣어 마무리합니다.",
            "5. 볶음밥 위에 계란후라이를 얹어줍니다."
        ],
        "영양성분": {
            "칼로리": "600kcal",
            "탄수화물": "80g",
            "단백질": "20g",
            "지방": "20g"
        }
    },
    "두부조림": {
        "재료": {
            "두부": "200g",
            "양파": "1/2개",
            "대파": "1대",
            "간장": "2스푼",
            "고춧가루": "1스푼",
            "마늘": "2쪽",
            "물": "1/2컵",
            "참기름": "1스푼",
            "깨": "1스푼"
        },
        "레시피": [
            "1. 두부를 적당한 크기로 잘라줍니다.",
            "2. 팬에 두부를 노릇하게 구워줍니다.",
            "3. 구운 두부 위에 양파와 대파, 마늘을 올려줍니다.",
            "4. 간장, 고춧가루, 물을 섞어 만든 양념장을 붓고 끓입니다.",
            "5. 양념이 자작하게 졸아들면 참기름과 깨를 뿌려 마무리합니다."
        ],
        "영양성분": {
            "칼로리": "250kcal",
            "탄수화물": "10g",
            "단백질": "15g",
            "지방": "15g"
        }
    }
}


# 사용자 입력을 받습니다.
food_name = input("음식 이름을 입력하세요: ")

# 입력한 음식이 데이터에 있는지 확인합니다.
if food_name in food_data:
    print(f"\n{food_name}에 대한 정보")
    
    # 재료 출력
    print("\n재료:")
    for ingredient, amount in food_data[food_name]["재료"].items():
        print(f"- {ingredient}: {amount}")
    
    # 레시피 출력
    print("\n레시피:")
    for step in food_data[food_name]["레시피"]:
        print(step)
    
    # 영양성분 출력
    print("\n영양성분:")
    for nutrient, value in food_data[food_name]["영양성분"].items():
        print(f"- {nutrient}: {value}")
else:
    print("해당 음식에 대한 정보가 없습니다.")


