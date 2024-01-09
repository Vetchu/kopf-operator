import shutil
import time

import kopf

from git_ext.git_main import (
    update_and_push_file,
    destination_path,
    repository_url,
    git_clone,
    file_path,
)
from utils.format_file import file_filter
from utils.parse_to_df import parse_to_df

namespace = "default"


@kopf.on.create("v1", "configmaps")
@kopf.on.update("v1", "configmaps")
def configmap_handler(body, **kwargs):
    print(f"ConfigMap {body['metadata']['name']} updated or created.")
    if body["metadata"]["namespace"] != namespace:
        print("not interesting change, exiting")
        return
    content = body["data"]["config.txt"]
    print(content)
    df = parse_to_df(content)
    file_content = file_filter(df)

    print("cloning")
    try:
        shutil.rmtree(destination_path)
    except Exception as e:
        print(e)
    git_clone(repository_url, destination_path)
    print("pushing files")
    current_timestamp = time.time()

    branch_name = f"new_branch_{current_timestamp}"
    update_and_push_file(destination_path, branch_name, file_path, file_content)
    shutil.rmtree(destination_path)
