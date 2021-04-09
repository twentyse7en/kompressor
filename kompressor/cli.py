import sys
import click
from kompressor.kompressor import compress_image, no_of_unique_colors


@click.command()
@click.option('-p', '--path', help='path to image you want to compress', type=str,
              default="")
@click.option('-c', '--colors', help='no of colors in the output file',
              default= 512,type=int)
@click.option('-u', '--unique-colors', help='Disply the no. of colors in image',
              is_flag=True)
def main(path, colors, unique_colors):
    """Compress image using k-means clustering algorithm."""

    if path == "" :
        click.echo("Input a path.")
        click.echo("kompressor --help for more details")
    
    if unique_colors:
        no_of_unique_colors(unique)
    else:
        compress_image(path, colors) 
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
