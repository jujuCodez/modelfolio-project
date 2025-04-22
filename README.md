# Modelfolio – A Portfolio Website for Freelance Models 💼📸

Modelfolio is a custom-built portfolio website designed to help freelance models professionally showcase their work, manage client inquiries, and maintain control over their personal branding online.

This web application was developed as a software project using the Django web framework and follows a full-stack development process—from client analysis to final deployment.

---

![Modelfolio UI Preview](https://i.imgur.com/tjBkyHB.png)

---

## 🌟 Project Highlights

- 🎨 Elegant, responsive, and customizable design
- 📷 Dedicated album page for modeling photos
- 📬 Contact form for direct client inquiries
- 🛠️ Admin panel for content management
- 🌐 Live deployment using PythonAnywhere

---

## 🧑‍💼 Client Background

The client is a freelance model seeking to expand their reach and improve client engagement. While they previously relied on social media, they needed a **centralized, professional website** to stand out in a highly competitive market and receive inquiries directly.

---

## 🧩 Problem Statement

- Social media alone is limiting and often perceived as informal.
- High competition makes it difficult to retain viewer attention.
- No direct channel for structured client inquiries.
- Lack of content control without a website backend.

---

## ✅ Our Software Solution

We created **Modelfolio**, a Django-powered portfolio website featuring:

- A **landing page** with an animated hero section
- An **About page** detailing the model's background
- An **Album page** showcasing uploaded projects with hover effects
- A **Contact page** with social media links and a built-in contact form
- A secure **admin panel** to upload/edit/delete photos and view inquiries

---

## 🧠 Design & Development Process

### 1. Planning & Requirements
- Identified project scope and deliverables
- Managed milestones using Trello
- Drafted a full Software Requirements Specification (SRS)

### 2. Prototyping
- Designed a high-fidelity prototype using **Figma**
- 📌 [View our Figma Design Prototype](https://www.figma.com/proto/MAjSWMSR0abjoe3M9iSzXk/Portfolio-WEbsite-UI-UX?node-id=0-1&t=iWvSh3Kl361Qeg9O-1)
- Final layout approved after client consultation

### 3. Tech Stack

| Layer       | Tools Used                     |
|-------------|--------------------------------|
| Frontend    | HTML, CSS (custom + gradients), Figma |
| Backend     | Python, Django                 |
| Database    | SQLite                         |
| Deployment  | PythonAnywhere                 |

### 4. Development
- Built using Django’s MVT structure
- Developed reusable templates and views
- Implemented Django Admin for backend CMS

### 5. Testing & Feedback
- Verified all site features aligned with the SRS
- Ensured successful form submissions and image uploads
- Validated responsiveness and design consistency

### 6. Deployment
- Deployed on PythonAnywhere (free hosting)
- Working to migrate to more flexible hosting due to style limitations

---

## 🔧 Installation Guide (Local Setup)

1. **Clone this repo**
   ```bash
   git clone https://github.com/yourusername/modelfolio.git
   cd modelfolio
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

4. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the server**
   ```bash
   python manage.py runserver
   ```

6. Access at `http://127.0.0.1:8000`

---

## 💡 Features

- Custom **admin interface** for adding/removing content
- Mobile-friendly, responsive layout
- Clean UI with aesthetic visual elements
- Social media integration and dynamic contact form

---

## 📜 License

This project is licensed under the MIT License.  
Feel free to use, modify, and share — just don’t remove attribution.

---

## 👥 Contributors

Developed by a team of Computer Engineering students from De La Salle University:
- Lead Designer & Frontend Developer
- Backend Developer
- Project Manager
- Documentation Specialist

---

## 📬 Contact

Have feedback or suggestions? Open an issue or fork the project!
