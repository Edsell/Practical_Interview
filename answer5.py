import os
import re

def find_uuids_in_json(directory):
    uuids = set()
    uuid_pattern = re.compile(r'\b[0-9a-fA-F]{8}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{12}\b')

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    found_uuids = uuid_pattern.findall(content)
                    uuids.update(found_uuids)

    return list(uuids)

directory_path = '/path/to/Edsell_Muhindo/json_files_directory'
all_uuids = find_uuids_in_json(directory_path)
print(all_uuids)