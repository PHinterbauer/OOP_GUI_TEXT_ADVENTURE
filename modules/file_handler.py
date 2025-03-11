import json

class Json_Handler():
    def __init__(self, json_file_path):
        self.json_file_path = json_file_path

    def load_json_chapter_text(self, chapter_name: str, sub_chapter_name: str) -> list:
        output: list[str] = []
        try:
            with open(self.json_file_path, "r", encoding = "utf-8") as file:
                data = json.load(file)
            if chapter_name in data:
                if sub_chapter_name in data[chapter_name]:
                    for line in data[chapter_name][sub_chapter_name]:
                        output.append(line)
                else:
                    print(f'Sub Chapter "{sub_chapter_name}" konnte nicht gefunden werden!')
            else:
                print(f'Chapter "{chapter_name}" konnte nicht gefunden werden!')
        except FileNotFoundError:
            print(f'Datei {self.json_file_path} konnte nicht gefunden werden!')
        return output
    
    def load_json_chapter_functions(self, chapter_name: str, sub_chapter_name: str) -> dict:
        output: dict = {}
        try:
            with open(self.json_file_path, "r", encoding = "utf-8") as file:
                data = json.load(file)
            if chapter_name in data:
                if "functions" in data[chapter_name]:
                    if sub_chapter_name in data[chapter_name]["functions"]:
                        for key, value in data[chapter_name]["functions"][sub_chapter_name].items():
                            output[key] = value
        except FileNotFoundError:
            print(f'Datei {self.json_file_path} konnte nicht gefunden werden!')
        return output