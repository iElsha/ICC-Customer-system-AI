from setuptools import setup

setup(
    name='customerPredictionCustomerReview',
    version='0.1',
    scripts=['predictor.py'],
    install_requires=["tqdm>=4.27.0", "transformers>=4.2.2"],
)
