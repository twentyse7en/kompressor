<p align="center"> 
<img src="https://raw.githubusercontent.com/twentyse7en/kompressor/main/assets/LOGO.png?token=AOHUM65ETBOXUMCKBSPJN7LAOFFKO" height="110">
<br>
</p>


<p align="center">
<img src="https://img.shields.io/badge/release-v0.1.0-blue.svg">
<img src="https://img.shields.io/badge/license-MIT-blue.svg">
<a href="https://img.shields.io/badge/support-Linux%20|%20MacOS%20|%20Windows%20-blue.svg"><img src="https://img.shields.io/badge/support-Linux%20|%20MacOS%20|%20Windows%20-blue.svg"></a>
</p>


<p align="center"> Performs pixel-wise color-quantization using K-Means </p>

<p align="center"> 
<img src="https://raw.githubusercontent.com/twentyse7en/kompressor/main/assets/term.gif?token=AOHUM6ZR6IC5K47VARNER63AOFFKU" />
<p/>

## Installation

```console
# clone the repo
$ git clone https://github.com/twentyse7en/kompressor.git  

# change the working directory to sherlock
$ cd kompressor 

# install the requirements
$ pip install .
```

## Usage

```console
$ kompressor --help

Usage: kompressor [OPTIONS]

  Compress image using k-means clustering algorithm.

Options:
  -p, --path TEXT       path to image you want to compress
  -c, --colors INTEGER  no of colors in the output file
  -u, --unique-colors   Disply the no. of colors in image
  --help                Show this message and exit.
```

Apply color quantization to image. Default 512 colors.

```console
$ kompressor -p path/to/image.jpg
```

Specify no. of colors

```console
$ kompressor -p path/to/image.jpg -c 64
```

To get the no. of colors in the image

```console
$ kompressor -p path/to/image.jpg -u
```
## Example results

<p align="center" />
<img src="" />
<p>
<p align="center" />
<img src="" />
<p>
<p align="center" />
<img src="" />
<p>

## Credits
Inspired by [scikit-learn](https://scikit-learn.org/stable/auto_examples/cluster/plot_color_quantization.html#:~:text=Performs%20a%20pixel%2Dwise%20Vector,preserving%20the%20overall%20appearance%20quality.).



