from distutils.core import setup

setup(
    name='FasterPay Python SDK',
    version='0.1.0',
    author='Prashant Dabholkar',
    author_email='prashant@paymentwall.com',
    packages=['fasterpay', 'fasterpay.tests'],
    scripts=['bin/payment-demo.py','bin/guestcheckout-demo.py'],
    url='http://pypi.python.org/pypi/FasterPay/',
    license='LICENSE.txt',
    description='FasterPay Python Integration SDK',
    long_description=open('README.txt').read(),
)
