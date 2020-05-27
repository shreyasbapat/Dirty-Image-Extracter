import matplotlib.pyplot as plt
from astropy.utils.data import get_pkg_data_filename
from astropy.io import fits

def convert(file, png=False):
    image_file = get_pkg_data_filename(file)
    image_data = fits.getdata(image_file, ext=0)
    plt.figure()
    if png:
        form = 'png'
    else:
        form = 'jpg'
    plt.imsave(fname=path, arr=image_data, cmap='gray', format=form)
