from setuptools import setup

setup(
    name='pretrained',
    version='0.1.1',
    license='HZDR',
    description='Tool to query tensorflowhub and pytorch hub and other repos for pretrained weights for a given architecture or keyword',
    long_description=open('README.md').read(),
    install_requires=['click', 'requests', 'torch', 'torchvision'],
    url='https://gitlab.hzdr.de/haicu/pretrained/tree/master',
    author='Erdem Unal',
    author_email='erdem.unal96@gmail.com'
)