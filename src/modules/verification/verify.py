class Verify:

    def __init__(self):
        pass

    def verify_cargo(self):
        for k, v in self.cargo:
            for box in v["boxes"]:
                for crate in box["crates"]:
                    self.verify_existence(crate)
                for file, size in box["files"]:
                    self.verify_size(file, size)
                self.verify_throughput(box)
        pass

    def verify_existence(self, file_path):
        pass

    def verify_size(self):
        try:
            ""
        except FileNotFoundError:
            raise FileNotFoundError
        pass

    def verify_throughput(self):
        pass
