import glob
import tqdm
from conda_forge_tick.lazy_json_backends import dump, loads


all_nodes = glob.glob("./version_pr_info/**/*.json", recursive=True)

for node_path in tqdm.tqdm(all_nodes, desc="fixing version pr info"):
    with open(node_path, "r") as fp:
        attrs = loads(fp.read())

    attrs["bad"] = False
    attrs["new_version_attempt_ts"] = {}
    attrs["new_version_attempts"] = {}
    attrs["new_version_errors"] = {}

    with open(node_path, "w") as fp:
        dump(attrs, fp)

all_nodes = glob.glob("./pr_info/**/*.json", recursive=True)

for node_path in tqdm.tqdm(all_nodes, desc="fixing pr info"):
    with open(node_path, "r") as fp:
        attrs = loads(fp.read())

    attrs["bad"] = False
    attrs["pre_pr_migrator_attempt_ts"] = {}
    attrs["pre_pr_migrator_attempts"] = {}
    attrs["pre_pr_migrator_status"] = {}

    with open(node_path, "w") as fp:
        dump(attrs, fp)


all_nodes = glob.glob("./node_attrs/**/*.json", recursive=True)

for node_path in tqdm.tqdm(all_nodes, desc="fixing node attrs"):
    with open(node_path, "r") as fp:
        attrs = loads(fp.read())

    attrs["parsing_error"] = False

    with open(node_path, "w") as fp:
        dump(attrs, fp)
