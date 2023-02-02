class ShippingList:

    def __init__(self, logger, config, docking_list):
        self.logger = logger
        self.config = config
        self.docking_list = docking_list

    def list_container_files(self):
        pass

    """
    Things to consider:
    1. Filesystem type.
    2. Transfer protocol.
    3. Network card.
    4. Routing, vlan.
    5. (SATA) controller.
    6. Disk type (hw, fs).
    7. Disk count.
    8. File sizes.
    9. Input structure.
    10. Used tool (other than rsync?)
    """
    def calculate_box_size(self):
        pass

    def repackage_to_boxes(self):
        pass
