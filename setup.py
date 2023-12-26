from setuptools import find_packages,setup

setup(
    name='medical_chatbot',
    version='0.0.1',
    author='Vikash Kumar',
    author_email='vikashkumar.evolve@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2","pypdf",
                      "ctransformers","sentence-transformers","pinecone-client","flask"],
    packages=find_packages()
)