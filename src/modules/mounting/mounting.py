import os

from ..checks.healthchecks import HealthCheck
from json import loads
import subprocess


class Docked:

    forbidden_mounts = ["/boot", "/boot/efi", "[SWAP]", "/", "/var/log", "/local"]

    def __init__(self, device_path, include, exclude, config):
        self.forbidden_devices = self.get_forbidden_devices()
        self.device_path = device_path
        self.mount_path = config["mount_path"]
        self.include_list = include
        self.exclude_list = exclude

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

    def get_all_devices(self, device_path: str):
        devices = {}
        for device in os.listdir(device_path):
            if device.startswith("sd") and device not in self.forbidden_devices:
                serial = self.pre_check_container()
                if serial:
                    devices[serial] = device

        if devices:
            return devices
        else:
            raise IndexError("No devices detected")

    def get_docking_list(self):
        docking_list = {}
        approaching = self.get_all_devices(self.device_path)
        if self.include_list:
            docking_list = self.include_list
        else:
            for serial, device in approaching.items():
                if serial not in self.exclude_list:
                    docking_list[serial] = device

        return docking_list

    @staticmethod
    def pre_check_container(device_path: str):
        try:
            disk_debug = subprocess.run(["smartctl", "-a", device_path], stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
            return disk_debug.serial
        except Exception as exc:
            raise exc

    def create_mount_path(self, serial):
        mount_dir = os.path.join(self.mount_path, serial)
        try:
            os.mkdir(mount_dir)
        except Exception as exc:
            pass

    @staticmethod
    def mount_device(device_path: str, mount_path: str):
        try:
            mount = subprocess.run(["mount", device_path, mount_path], stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        except Exception as exc:
            raise exc

    def dock_container(self):


    def return_docking_list(self):
        pass
