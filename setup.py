from distutils.core import setup
setup(
  name = 'FasterPay Python SDK',
  packages = ['fasterpay'],
  version = '1.0',
  license='MIT',
  description = 'FasterPay Python SDK enables you to integrate the FasterPay’s Checkout Page seamlessly without having the hassle of integrating everything from Scratch. Once your customer is ready to pay, FasterPay will take care of the payment, notify your system about the payment and return the customer back to your Thank You page.',
  author = 'FasterPay Integrations Team',
  author_email = 'integration@fasterpay.com',
  url = 'https://github.com/FasterPay/fasterpay-python',
  download_url = 'https://github.com/FasterPay/fasterpay-python/releases',
  keywords = ['FASTERPAY', 'PAYMENTS', 'CARD PROCESSING'],
  install_requires=['requests']
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Payment Gateway',
    'License :: MIT License',
    'Programming Language :: Python :: 2.7',
  ],
)
