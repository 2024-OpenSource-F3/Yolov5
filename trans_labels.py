import json
import os

# 처리할 폴더 지정
input_folder_path = '.\\Validation\\소도체_1_라벨_300'
output_folder_path = '.\\Validation\\beef_1_labels'

# 출력 폴더가 존재하지 않으면 생성
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

# 폴더 내 모든 JSON 파일에 대해 반복
for file_name in os.listdir(input_folder_path):
    if file_name.endswith('.json'):
        json_path = os.path.join(input_folder_path, file_name)
        
        # JSON 데이터 불러오기
        with open(json_path, 'r') as f:
            data = json.load(f)

        # 이미지 정보
        image_info = data['label_info']['image']
        image_width = image_info['width']
        image_height = image_info['height']

        # YOLO 포맷으로 변환
        output_lines = []
        for shape in data['label_info']['shapes']:
            label = shape['label']
            points = shape['points']
            x_coords = [p[0] for p in points]
            y_coords = [p[1] for p in points]
            x_min, x_max = min(x_coords), max(x_coords)
            y_min, y_max = min(y_coords), max(y_coords)

            x_center = (x_min + x_max) / 2 / image_width
            y_center = (y_min + y_max) / 2 / image_height
            width = (x_max - x_min) / image_width
            height = (y_max - y_min) / image_height

            class_index = 3  # 'pig'의 클래스 인덱스, 실제 사용하는 인덱스로 변경 필요
            output_lines.append(f"{class_index} {x_center} {y_center} {width} {height}")

        # 출력 파일 이름 설정 (JSON 파일명과 동일한 이름의 TXT 파일)
        txt_file_name = file_name.replace('.json', '.txt')
        txt_path = os.path.join(output_folder_path, txt_file_name)

        # 파일로 저장
        with open(txt_path, 'w') as f:
            for line in output_lines:
                f.write(line + '\n')
