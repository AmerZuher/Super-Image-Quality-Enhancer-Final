# 🌟 Super Image Enhancer

Enhance image quality using luminance channel analysis and super-resolution deep learning.

## ✨ Features

- Upload an image via the frontend.
- Automatically enhances the image using a TensorFlow model (`v10.h5`).
- View and compare the original and enhanced images.
- Backend powered by FastAPI.
- Frontend built with Next.js.
- Supports deployment via Docker or local environments.

---

## 🛠️ Tech Stack

- **Backend**: FastAPI, TensorFlow, PIL, PostgreSQL
- **Frontend**: Next.js
- **Environment**: Conda (for Python dependencies)
- **Database**: PostgreSQL

---

## 🚀 Getting Started

You can run this project either locally or using Docker.

### Option 1: Docker (Recommended)

Make sure you have Docker and Docker Compose installed.

```bash
git clone https://github.com/AmerZuher/Super-Image-Quality-Enhancer-Final.git

cd Super-Image-Quality-Enhancer-Final

docker-compose up --build
```

to stop the containers

```bash
docker-compose down
```
