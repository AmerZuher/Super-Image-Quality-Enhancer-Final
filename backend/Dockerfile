FROM continuumio/miniconda3

WORKDIR /app

COPY environment.yml .
RUN conda env create -f environment.yml

# Activate the environment
SHELL ["conda", "run", "-n", "imageenv", "/bin/bash", "-c"]

COPY . .

EXPOSE 8000

CMD ["conda", "run", "--no-capture-output", "-n", "imageenv", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
