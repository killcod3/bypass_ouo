from setuptools import setup, find_packages

setup(
    name='bypass_ouo',  
    version='0.1',      
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4==4.12.2',
        'curl_cffi==0.5.7',
        'requests==2.31.0'  
    ],
    author='@killcod3',  
    author_email='',  
    description='A Python package to bypass ouo.io URL shortener',  
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',  
    url='https://github.com/killcod3',  
    project_urls={
        'Source': 'https://github.com/killcod3/bypass_ouo',  
        'Bug Tracker': 'https://github.com/killcod3/bypass_ouo/issues',  
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: OS Independent',
        
    ],
    python_requires='>=3.6',  
)
