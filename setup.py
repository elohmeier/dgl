from skbuild import setup

setup(
    cmake_args=[
        "-DBUILD_GRAPHBOLT=OFF",
        "-DBUILD_TYPE=release",
        "-DBUILD_TORCH=ON",
        "-DUSE_CUDA=OFF",
        "-DUSE_OPENMP=OFF",
    ],
)
