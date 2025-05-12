# Cyberly-backend

**Cyberly** is a collaborative, developer-led company focused on building creative and meaningful technology. We’re driven by ownership, innovation, and a shared goal to build solutions that matter—while putting people and the planet first.

This project provides a RESTful API platform that enables users to manage professional profiles, including availability, language proficiency, categories of expertise, and media resources such as profile photos.

---

## 🚀 Getting Started

### Requirements

- Docker
- Docker Compose

---

## ⚙️ Run the Project

1. **Clone the repository**

```bash
git clone https://github.com/your-org/cyberly.git
cd cyberly


2. Create a .env file
DB_NAME=cyberly
DB_USER=proxyuser
DB_PASSWORD=yourpassword
DB_ROOT_PASSWORD=rootpassword
DB_HOST=db


3. Run the app
docker-compose up --build


# 📘 Cyberly API Documentation

This document outlines the available REST API endpoints for managing user profiles on Cyberly.

Cyberly allows users to manage professional profiles including:

- Personal details (name, gender, phone, email)
- Categories of expertise
- Language proficiency
- Availability for work
- Profile photo

---

## 🔐 Base URL

http://localhost:8000/api/


---

## 🔄 Authentication

Currently, all endpoints are **open for demo purposes**. Future versions will require token-based authentication.

---

## 📇 Profiles

### 🔹 Create Profile

**POST** `/profiles/`

Creates a new profile, including nested categories, languages, availabilities, and profile photo.

#### ✅ Request Body

```json
{
  "first_name": "Emma",
  "last_name": "Taylor",
  "email": "emma.taylor@example.com",
  "phone_number": "+15550999",
  "gender": "F",
  "profile_photo": {
    "thumbnail_url": "https://randomuser.me/api/portraits/women/10.jpg"
  },
  "profile_categories": [
    { "category": 3, "years_of_experience": 4 }
  ],
  "profile_languages": [
    { "language": 1, "proficiency": "fluent", "is_native": true }
  ],
  "availabilities": [
    {
      "availability_type": "w",
      "time_start": "10:00:00",
      "time_end": "18:00:00"
    }
  ]
}

🔁 Response (201 Created)

{
  "id": 12,
  "first_name": "Emma",
  "last_name": "Taylor",
  "email": "emma.taylor@example.com",
  "phone_number": "+15550999",
  "gender": "F",
  "online": false,
  "profile_photo_url": "https://randomuser.me/api/portraits/women/10.jpg"
}

🔹 Get All Profiles

GET /profiles/

Returns a list of all profiles (paginated if configured).
🔹 Get Profile by ID

GET /profiles/{id}/

Returns full details of a single profile.
🔹 Update Profile

PUT or PATCH /profiles/{id}/

Update all or partial fields of a profile, including nested data.
🔹 Delete Profile

DELETE /profiles/{id}/

Removes the profile and all related data.
🔍 Filtering Profiles

You can filter profiles using query parameters on the /profiles/ endpoint.
🧾 Available Query Parameters
Parameter	Description	Example
gender	Filter by gender (F, M, NB, O)	gender=F
online	Filter by online status	online=true
languages	Filter by language ID	languages=1
categories	Filter by category ID	categories=4
experience	Minimum years of experience (≥)	experience=3
availability_date	Date user is available (YYYY-MM-DD)	availability_date=2025-06-01
availability_time	Time user is available (HH:MM)	availability_time=14:00
🧪 Example Request

GET /profiles/?gender=F&online=true&languages=2&categories=4&experience=2&availability_time=16:00

