#! /usr/bin/env python3
import argparse
import subprocess
import sys
import tempfile
from enum import Enum
from pathlib import Path


class NodeType(str, Enum):
    VPS = "vps"
    RPI4 = "rpi4"

    def __str__(self):
        return self.value


class Setup:
    def __init__(self, node_type: NodeType, gpg_keyname: str):
        self.home_path = Path.home()
        self.lab_path = self.home_path / "lab"
        self.node_path = self.lab_path / node_type

        self.gpg_keyname = gpg_keyname

    def setup(self) -> int:
        self._symlink()
        self._import_gpg_key(keyname=self.gpg_keyname)
        # import info from pass?
        # modify the github url to SSH
        return 0

    def _symlink(self) -> None:
        symlinks = {
            self.home_path / ".bash_profile": self.lab_path / "bash_profile",
            self.home_path / "node_bash_profile": self.node_path / "node_bash_profile",
        }
        for src, dst in symlinks.items():
            safe_symlink(src, dst)

    def _import_gpg_key(self, keyname: str) -> None:
        subprocess.run(["gpg", "--import", keyname])


def safe_symlink(src: Path, dst: Path) -> None:
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir) / "tmpfile"
        tmp_path.symlink_to(dst)
        tmp_path.rename(src)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-n",
        "--node-type",
        help="setup the instance as this node type",
        choices=list(NodeType),
        type=NodeType,
        dest="node_type",
        required=True,
    )
    parser.add_argument(
        "--gpg",
        help="filename in the home directory that contains the armored gpg priv file",
        dest="gpg_keyname",
        default="priv.asc",
    )
    args = parser.parse_args()
    s = Setup(node_type=args.node_type, gpg_keyname=args.gpg_keyname)
    sys.exit(s.setup())
