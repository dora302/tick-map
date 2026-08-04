import json
import os

# 1. 공인 보건기구(CDC/ECDC/KDCA) 기반 대륙별 진드기 매개 질환 데이터베이스 (ISO3166-1-Alpha-3 기준)
# merge_data.py 상단에 덮어씌울 1순위 핵심 진드기 DB
TICK_DISEASE_DB = {
    # --- [동아시아 / 동남아시아] ---
    "KOR": {
        "primary_tick": "털진드기 (Chigger Mite)",
        "disease": "쯔쯔가무시증 (Scrub Typhus)",
        "risk_level": "HIGH",
        "eschar_likely": True,
        "eschar_desc": "물린 자리에 80% 이상 전형적인 검은 딱지(가피) 형성",
        "incubation": "10~12일"
    },
    "JPN": {
        "primary_tick": "피참진드기 (Haemaphysalis)",
        "disease": "일본 홍반열 (JSF)",
        "risk_level": "HIGH",
        "eschar_likely": True,
        "eschar_desc": "전신 발진 및 물린 부위 진한 가피 형성",
        "incubation": "2~10일"
    },
    "CHN": {
        "primary_tick": "작은소피참진드기 (Haemaphysalis longicornis)",
        "disease": "SFTS (중증열성소판감소증후군)",
        "risk_level": "HIGH",
        "eschar_likely": False,
        "eschar_desc": "가피 관찰 안 됨 (고열 및 혈소판 감소 위주)",
        "incubation": "6~14일"
    },
    "THA": {
        "primary_tick": "털진드기 (Chigger Mite)",
        "disease": "쯔쯔가무시증 (Scrub Typhus)",
        "risk_level": "HIGH",
        "eschar_likely": True,
        "eschar_desc": "트레킹 시 노출 위험, 사타구니/겨드랑이 가피 관찰",
        "incubation": "9~12일"
    },
    "VNM": {
        "primary_tick": "털진드기 (Chigger Mite)",
        "disease": "쯔쯔가무시증 (Scrub Typhus)",
        "risk_level": "HIGH",
        "eschar_likely": True,
        "eschar_desc": "하체 및 피부 접히는 부위에 가피 발생",
        "incubation": "10~12일"
    },

    # --- [유럽 / 러시아] ---
    "ESP": {
        "primary_tick": "구름개진드기 (Brown Dog Tick)",
        "disease": "지중해 반점열 (MSF)",
        "risk_level": "HIGH",
        "eschar_likely": True,
        "eschar_desc": "특징적인 'Tache Noire' (검은 점 모양 가피 1개)",
        "incubation": "3~7일"
    },
    "ITA": {
        "primary_tick": "구름개진드기 (Brown Dog Tick)",
        "disease": "지중해 반점열 (MSF)",
        "risk_level": "HIGH",
        "eschar_likely": True,
        "eschar_desc": "지중해 연안 노출 시 검은 가피 관찰",
        "incubation": "3~7일"
    },
    "DEU": {
        "primary_tick": "산림진드기 (Ixodes ricinus)",
        "disease": "라임병 (Lyme Disease)",
        "risk_level": "MEDIUM",
        "eschar_likely": False,
        "eschar_desc": "가피 없음 (과녁 모양의 붉은 반점/홍반 형성)",
        "incubation": "3~30일"
    },
    "FRA": {
        "primary_tick": "산림진드기 (Ixodes ricinus)",
        "disease": "라임병 (Lyme Disease)",
        "risk_level": "MEDIUM",
        "eschar_likely": False,
        "eschar_desc": "가피 없음 (과녁 모양 유전성 홍반 발생)",
        "incubation": "7~14일"
    },
    "RUS": {
        "primary_tick": "극동진드기 / 산림진드기",
        "disease": "시베리아 진드기 티푸스",
        "risk_level": "HIGH",
        "eschar_likely": True,
        "eschar_desc": "물린 자리에 뚜렷한 가피 및 국소 림프절 부종",
        "incubation": "2~7일"
    },

    # --- [아프리카] ---
    "ZAF": {
        "primary_tick": "아프리카소진드기 (Amblyomma)",
        "disease": "아프리카 진드기열 (ATBF)",
        "risk_level": "HIGH",
        "eschar_likely": True,
        "eschar_desc": "사파리 여행객 다발성 가피(Multiple Eschars) 특징",
        "incubation": "5~10일"
    },
    "KEN": {
        "primary_tick": "아프리카소진드기 (Amblyomma)",
        "disease": "아프리카 진드기열 (ATBF)",
        "risk_level": "HIGH",
        "eschar_likely": True,
        "eschar_desc": "야생 동물 국립공원 트레킹 시 가피 형성 진드기 노출",
        "incubation": "5~10일"
    },

    # --- [아메리카 대륙] ---
    "USA": {
        "primary_tick": "사슴진드기 (Blacklegged Tick / Ixodes)",
        "disease": "라임병 (Lyme Disease)",
        "risk_level": "HIGH",
        "eschar_likely": False,
        "eschar_desc": "가피 없음 (물린 자리를 중심으로 퍼지는 과녁 모양 발진)",
        "incubation": "3~30일"
    },
    "MEX": {
        "primary_tick": "개진드기 (Rhipicephalus)",
        "disease": "바위산 홍반열 (RMSF)",
        "risk_level": "HIGH",
        "eschar_likely": False,
        "eschar_desc": "가피 안 생김 (손발바닥 점상 출혈성 발진 특징)",
        "incubation": "2~14일"
    },

    # --- [오세아니아] ---
    "AUS": {
        "primary_tick": "호주마비진드기 (Ixodes holocyclus)",
        "disease": "퀸즐랜드 진드기 티푸스",
        "risk_level": "MEDIUM",
        "eschar_likely": True,
        "eschar_desc": "가피 형성 및 일부 독소에 의한 국소 마비 증상",
        "incubation": "2~14일"
    }
}

def main():
    # 경로 설정 (필요시 수정)
    input_file = 'data/countries.geojson'
    output_file = 'ticks_countries.geojson'

    if not os.path.exists(input_file):
        print(f"❌ 오류: '{input_file}' 파일을 찾을 수 없습니다.")
        print("data/ 폴더 안에 원본 countries.geojson 파일이 있는지 확인해 주세요.")
        return

    # 1. 원본 GeoJSON 읽기
    with open(input_file, 'r', encoding='utf-8') as f:
        geojson_data = json.load(f)

    merged_count = 0

    # 2. 각 국가(Feature)의 properties에 진드기 데이터 매핑
    for feature in geojson_data['features']:
        props = feature['properties']
        iso_a3 = props.get('ISO3166-1-Alpha-3')

        # 진드기 DB에 있는 국가일 경우
        if iso_a3 in TICK_DISEASE_DB:
            props.update(TICK_DISEASE_DB[iso_a3])
            props['has_tick_data'] = True
            merged_count += 1
        else:
            # DB에 없는 국가 기본값 (Fallback)
            props['has_tick_data'] = False
            props['disease'] = "정보 미등록 국가"
            props['risk_level'] = "LOW"
            props['eschar_likely'] = False
            props['eschar_desc'] = "해당 국가의 정밀 CDC 진드기 데이터베이스가 연동되어 있지 않습니다."
            props['incubation'] = "1~3주 (일반 진드기 기준)"

    # 3. 병합된 결과 저장
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(geojson_data, f, ensure_ascii=False, indent=2)

    print(f"🎉 성공! 총 {merged_count}개 국가의 진드기 데이터가 성공적으로 병합되었습니다.")
    print(f"📁 생성된 파일: {os.path.abspath(output_file)}")

if __name__ == '__main__':
    main()