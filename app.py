from src.DimondPricePrediction.pipelines.prediction_pipeline import CustomData,PredictPipeline

from flask import request,Flask,render_template,jsonify

app=Flask(__name__)

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route("/predict",methods=["GET","POST"])

def predict_datapoints():
    if request.method=="GET":
        return render_template("form.html")
    else:
        pass


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80)

