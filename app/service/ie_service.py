import ast
import csv
import json
import os
import typing
from io import StringIO

from flask import current_app
from werkzeug.utils import secure_filename

from app.models.media.media import Media


class IEService:
    @staticmethod
    async def export_media_as_csv(cls: type(Media)) -> str:
        file = StringIO()
        writer: typing.Union[csv.DictWriter, None] = None

        first = True
        async for a in cls.find_all():
            entry = json.loads(a.json())

            # add headers
            if first:
                first = False
                header = entry.keys()
                writer = csv.DictWriter(file, fieldnames=header)
                writer.writeheader()
            writer.writerow(entry)

        file_data = file.getvalue()
        file.close()
        return file_data

    @staticmethod
    def _convert_csv_row_to_media(row: dict) -> dict:
        # todo: avoid hardcoding?
        row["title"] = ast.literal_eval(row["title"])
        row["coverImage"] = ast.literal_eval(row["coverImage"])
        row["genres"] = ast.literal_eval(row["genres"])
        row["relations"] = ast.literal_eval(row["relations"])

        return row

    @staticmethod
    async def import_media_from_csv(cls, csv_string) -> list[str]:
        file = StringIO(csv_string)
        imported_data = []

        csv_file = csv.DictReader(file)
        for row in csv_file:
            # prepare data for import
            row = IEService._convert_csv_row_to_media(row)

            # actually import data
            a = cls(**row)
            await a.save()

            imported_data.append(a.json())

        return imported_data

    @staticmethod
    def valid_file_extension(uploaded_file) -> bool:
        filename = secure_filename(uploaded_file.filename)
        if not filename:
            return False

        file_ext = os.path.splitext(filename)[1]
        if file_ext not in current_app.config["UPLOAD_EXTENSIONS"]:
            return False

        return True
