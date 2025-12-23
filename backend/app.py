from flask import Flask, render_template

app = Flask(
    __name__,
    template_folder='../',
    static_folder='../assets/'
)

# --- MAIN ROUTES ---
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/module')
def learn():
    return render_template('module.html')

@app.route('/practice')
def practice():
    return render_template('practice.html')

# --- MODULE ROUTES ---
@app.route('/module/digital-forensic')
def digital_forensic():
    return render_template('module/digital-forensic.html')

@app.route('/module/file-analysis')
def file_analysis():
    return render_template('module/file-analysis.html')

@app.route('/module/network-forensic')
def metadata_investigation():
    return render_template('module/network-forensic.html')

@app.route('/module/digital-footprint-investigation')
def digital_footprint_investigation():
    return render_template('module/digital-footprint.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)