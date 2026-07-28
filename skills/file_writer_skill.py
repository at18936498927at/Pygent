from base_skill import BaseSkill


class FileWriterSkill(BaseSkill):
    name = "file_writer"
    description = "Writes content to a specified file."

    def run(self, file_path: str, content: str, add: bool=True) -> str: # pyright: ignore[reportIncompatibleMethodOverride]
        """
        Writes the provided content to the specified file.

        Args:
            file_path (str): The path of the file to write to.
            content (str): The content to write into the file.
            add (bool): Whether to append to the file or overwrite it.

        Returns:
            str: A confirmation message indicating success or failure.
        """
        try:
            with open(file_path, 'w' if not add else 'a') as file:
                file.write(content)
            return f"Content successfully written to {file_path}."
        except Exception as e:
            return f"Error writing to file {file_path}: {e}"

