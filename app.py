from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Meet Portfolio</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #1e1e2f, #121212);
                color: white;
                text-align: center;
            }
            .container {
                padding: 50px 20px;
            }
            h1 {
                font-size: 48px;
                margin-bottom: 10px;
            }
            p {
                color: #bbb;
            }
            .btn {
                display: inline-block;
                margin-top: 20px;
                padding: 12px 25px;
                background: #4CAF50;
                color: white;
                border-radius: 25px;
                text-decoration: none;
            }
            .section {
                margin-top: 50px;
            }
            .cards {
                display: flex;
                justify-content: center;
                gap: 20px;
                flex-wrap: wrap;
                margin-top: 20px;
            }
            .card {
                background: #1f1f1f;
                padding: 20px;
                border-radius: 15px;
                width: 250px;
            }
        </style>
    </head>
    <body>

        <div class="container">
            <h1>Meet Zambad</h1>
            <p>Tech Enthusiast • Creator • Learner</p>
            <a href="mailto:meetzambad1@email.com" class="btn">Contact Me</a>
            <div class="section">
                <h2>About Me</h2>
                <p>I love technology, coding, and creating useful content.</p>
            </div>

            <div class="section">
                <h2>Skills</h2>
                <div class="cards">
                    <div class="card">Web Development</div>
                    <div class="card">Tech Reviews</div>
                    <div class="card">Content Creation</div>
                </div>
            </div>

            <div class="section">
                <h2>Projects</h2>
                <div class="cards">
                    <div class="card">Portfolio Website</div>
                    <div class="card">Coming Soon</div>
                </div>
            </div>
        </div>

    </body>
    </html>
    """)

if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))