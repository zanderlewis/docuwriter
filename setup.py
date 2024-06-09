from setuptools import setup, find_packages

setup(
    name='docuwriter',
    version='0.0.5',
    description='Open Source alternative to Jetbrains Writerside.',
    author='Zander Lewis',
    author_email='wolfthedev@gmail.com',
    url='https://github.com/zanderlewis/docuwriter',
    packages=find_packages(),
    install_requires=[
        'markdown',
        'beautifulsoup4',
        'pygments'
    ],
    entry_points={
        'console_scripts': [
            'docuwriter=docuwriter.core:main',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)