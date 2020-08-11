#! /usr/bin/env python3
import argparse
from enum import Enum
from pathlib import Path


class NodeType(str, Enum):
    VPS = "vps"
    RPI4 = "rpi4"

    def __str__(self):
        return self.value


class Setup:

    def __init__(self, node_type: NodeType, gpg_keyname: str = "priv.asc"):
        self.home_path = Path.home()
        self.lab_path = self.home_path / 'lab'
        self.node_path = self.lab_path / node_type

        self.gpg_keyname = gpg_keyname


    def setup(self) -> int:
        self._symlink()
        self._import_gpg_key(keyname=self.gpg_keyname)
        # import info from pass?
        # modify the github url to SSH

    def _symlink(self) -> None:
        (self.home_path / '.bash_profile').symlink_to(self.lab_path / 'bash_profile')
        (self.home_path / 'node_bash_profile').symlink_to(self.node_path / 'node_bash_profile')

    def _import_gpg_key(self, keyname: str) -> None:
        subprocess.run(["gpg", "--import", key_path])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-n", "--node-type",
        help="setup the instance as this node type",
        choices=list(NodeType),
        type=NodeType,
        dest="node_type",
        required=True
    )
    args = parser.parse_args()
    s = Setup(node_type=args.node_type)
    sys.exit(s.setup())
