from pathlib import Path


class FileOrganizer:
    def __init__(self, folder_path):
        self.folder_path = Path(folder_path)

    def scan_files(self):
        files = []

        for item in self.folder_path.iterdir():
            if item.is_file():
                # ignore hidden/system files
                if not item.name.startswith("."):
                    files.append(item)

        return files

    def generate_report(self):
        files = self.scan_files()

        report = {
            "total_files": len(files),
            "files": [file.name for file in files]
        }

        return report


def organize_test():
    organizer = FileOrganizer(".")
    return organizer.generate_report()


if __name__ == "__main__":
    result = organize_test()

    print("📁 File Organizer Report")
    print("-----------------------")
    print(f"Total files: {result['total_files']}")

    for file in result["files"]:
        print(f"- {file}")