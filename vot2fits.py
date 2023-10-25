#!/usr/bin/env python3
"""Convert VOTable to FITS"""
import click
from astropy.table import Table
from typing import List
from pathlib import Path

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
        fits_name = file_path.with_suffix(".fits")
        table.write(fits_name, overwrite=overwrite)



def cli(file_names, overwrite):
    main(file_names, overwrite=overwrite)


if __name__ == "__main__":
    main()