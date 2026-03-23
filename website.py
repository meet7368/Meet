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
            body { font-family: Arial; background: #111; color: white; text-align: center; }
            .box { margin-top: 50px; }
            .card { background: #222; padding: 20px; margin: 10px; border-radius: 10px; }
        </style>
    </head>
    <body>

        <div class="box">
            <h1>Meet Zambad</h1>
            <p>Tech Enthusiast | Learner | Creator</p>
        </div>

        <div class="card">
            <h2>About Me</h2>
            <p>I love technology, coding, and creating content.</p>
        </div>

        <div class="card">
            <h2>Projects</h2>
            <p>Coming soon...</p>
        </div>

    </body>
    </html>
    """)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)