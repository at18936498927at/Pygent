from base_skill import BaseSkill


class FileReaderSkill(BaseSkill):
    name = "file_reader"
    description = "Provides file reading capabilities."

    def run(self, file_path: str, byte_mode: bool = False) -> str | bytes: # pyright: ignore[reportIncompatibleMethodOverride]
        """
        Reads the content of a file and returns it.

        Args:
            file_path (str): The path to the file to read.
            byte_mode (bool): Whether to return the content as bytes.

        Returns:
            str | bytes: The content of the file.
        """
        try:
            with open(file_path, "r" if not byte_mode else "rb", encoding="utf-8") as file:
                data = file.read()
            return data
        except FileNotFoundError as e:
            return f"Error: The file at {file_path} was not found.Exception: {e!r}"
        except IOError as e:
            return f"Error reading file at {file_path}: {e!r}"
        except Exception as e:
            return f"An unexpected error occurred while reading the file at {file_path}: {e!r}"
