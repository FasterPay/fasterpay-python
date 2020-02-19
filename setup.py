from distutils.core import setup
setup(
  name='FasterPay Python SDK',
  packages=['fasterpay'],
  version='1.1',
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
    'Topic :: Software Development :: Payment Gateway',
    'License :: MIT License',
    'Programming Language :: Python :: 2.7',
  ],
)
