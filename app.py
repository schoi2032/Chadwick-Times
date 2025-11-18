# app.py
from flask import Flask, render_template

app = Flask(__name__)

# Dummy data for articles
# In a real application, this would come from a database
articles = [
    {
        "id": 1,
        "title": "The Rise of AI in Everyday Life",
        "author": "Alice Smith",
        "date": "2023-10-26",
        "content": """
        Artificial intelligence is no longer a futuristic concept but a present reality,
        permeating various aspects of our daily lives. From personalized recommendations
        on streaming services to sophisticated medical diagnostics, AI's influence is
        growing exponentially. This article explores the current impact of AI and
        what we can expect in the coming years.
        <br><br>
        One of the most noticeable applications is in natural language processing (NLP),
        which powers virtual assistants like Siri and Alexa, enabling more intuitive
        human-computer interaction. Machine learning algorithms are also optimizing
        supply chains, improving cybersecurity, and even helping to design new materials.
        The ethical implications and potential societal changes due to AI are also
        critical topics of discussion among researchers and policymakers.
        """
    },
    {
        "id": 2,
        "title": "Understanding Quantum Computing Basics",
        "author": "Bob Johnson",
        "date": "2023-10-20",
        "content": """
        Quantum computing promises to revolutionize computation by leveraging quantum-mechanical
        phenomena such as superposition and entanglement. Unlike classical computers
        that use bits representing 0 or 1, quantum computers use qubits which can be 0, 1,
        or both simultaneously. This fundamental difference allows them to solve
        certain problems exponentially faster than classical computers.
        <br><br>
        Key concepts include:
        <ul>
            <li>**Superposition:** Qubits can exist in multiple states at once.</li>
            <li>**Entanglement:** Two or more qubits become linked,
            such that they cannot be described independently of each other.</li>
            <li>**Quantum Gates:** Operations that manipulate qubits.</li>
        </ul>
        While still in its early stages, quantum computing has the potential to impact fields
        like medicine, materials science, and cryptography significantly.
        """
    },
    {
        "id": 3,
        "title": "Sustainable Living: Tips for a Greener Home",
        "author": "Carol White",
        "date": "2023-10-15",
        "content": """
        Adopting sustainable practices at home can significantly reduce your environmental
        footprint and contribute to a healthier planet. Small changes in daily routines
        can lead to substantial positive impacts over time.
        <br><br>
        Here are some practical tips:
        <ol>
            <li>**Reduce, Reuse, Recycle:** Minimize waste generation.</li>
            <li>**Conserve Energy:** Use energy-efficient appliances, switch off lights, and unplug electronics.</li>
            <li>**Save Water:** Fix leaks, take shorter showers, and use water-saving fixtures.</li>
            <li>**Embrace Renewable Energy:** Consider solar panels or choose a utility provider that uses renewables.</li>
            <li>**Grow Your Own Food:** Start a small garden for fresh produce.</li>
            <li>**Support Local & Sustainable Businesses:** Choose products with minimal environmental impact.</li>
        </ol>
        Making conscious choices about consumption and resources can create a more sustainable lifestyle.
        """
    }
]

@app.route('/')
def home():
    """
    Displays the homepage with a list of all articles.
    """
    return render_template('index.html', articles=articles)

@app.route('/article/<int:article_id>')
def article_detail(article_id):
    """
    Displays the full content of a specific article.
    """
    article = next((a for a in articles if a["id"] == article_id), None)
    if article is None:
        return "Article not found", 404 # Simple error handling for now
    return render_template('article.html', article=article)

if __name__ == '__main__':
    app.run(debug=True) # debug=True allows for auto-reloading and helpful error messages

