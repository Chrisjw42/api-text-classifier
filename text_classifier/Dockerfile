FROM frolvlad/alpine-miniconda3:python3.7

# COPY /app /app

# Set up conda environment to allow usage of uvicorn and other package requirements
# Use conda forge
RUN conda config --add channels conda-forge \
    && conda install --file requirements.txt -c conda-forge 

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
