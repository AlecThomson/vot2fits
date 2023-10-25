#!/usr/bin/env python3
"""Convert VOTable to FITS"""
from pathlib import Path
from typing import List

import click
from astropy.table import Table

VOT_EXTENSIONS = (
    ".vot",
    ".xml",
    ".votable",
)


@click.command()
@click.argument("file_names", nargs=-1)
@click.option(
    "--overwrite",
    "-o",
    is_flag=True,
    help="Overwrite existing files",
)
def main(
    file_names: List[str],
    overwrite: bool = False,
):
    for file_name in file_names:
        file_path = Path(file_name)
        if file_path.suffix not in VOT_EXTENSIONS:
            print(f"Skipping {file_name} as it is not a VOTable")
            continue
        table = Table.read(file_name)
        print(f"Read {file_path}")
        fits_name = file_path.with_suffix(".fits")
        print(f"Writing {fits_name}")
        table.write(fits_name, overwrite=overwrite)
        print(f"Wrote {fits_name}")
    print("Done!")


if __name__ == "__main__":
    main()
