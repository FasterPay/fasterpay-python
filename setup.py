from distutils.core import setup
setup(
  name='fasterpay-python',
  packages=['fasterpay'],
  version='1.2',
  license='MIT',
  description='Integrate FasterPay into your application using fasterpay-python SDK',
  author='FasterPay Integrations Team',
  author_email='integration@fasterpay.com',
  url='https://github.com/FasterPay/fasterpay-python',
  download_url='https://github.com/FasterPay/fasterpay-python/releases',
  keywords=['FASTERPAY', 'PAYMENTS', 'CARD PROCESSING'],
  install_requires=['requests'],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 2.7',
  ],
)
