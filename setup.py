from setuptools import setup, find_packages

setup(
    name='codepal',
    version='1.0.0',
    description='AI-powered code reviewer and mentor',
    author='mehrshud',
    author_email='mehrshud@example.com',
    packages=find_packages(),
    install_requires=[
        # add dependencies here
    ],
    entry_points={
        'console_scripts': [
            'codepal=codepal.main:main',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    keywords='code reviewer mentor ai',
    project_urls={
        'Documentation': 'https://codepal.readthedocs.io/en/latest/',
        'Source Code': 'https://github.com/mehrshud/codepal',
    },
)
