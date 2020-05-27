import ehtim as eh
import numpy as np

def dirtyimage(file, path, npix=256, fovv=150):
    obs = eh.obsdata.load_uvfits(file)
    fov = fovv*eh.RADPERUAS
    dim = obs.dirtyimage(npix, fov)
    dim.save_fits(path + file[:-7] + '.fits')
