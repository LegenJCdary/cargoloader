from ..checks.healthchecks import HealthCheck
from json import loads
import subprocess


class Docked:

    forbidden_mounts = ["/boot", "/boot/efi", "[SWAP]", "/", "/var/log", "/local"]

    def __init__(self):
        self.forbidden_devices = self.get_forbidden_devices()

    def get_forbidden_devices(self):
        forbidden = []
        try:
            lsblk = subprocess.run(["lsblk", "-J"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            all_disks = loads(lsblk.stdout)
        except Exception as exc:
            error_msg = log_to_debug(all_disks.stderr, logger)
            logger.error('Unable to list disks due to: "{}".'.format(error_msg))

        for device in all_disks["blockdevices"]:
            child = ""
            if child in self.forbidden_mounts:
                forbidden.append(device)

        return forbidden
