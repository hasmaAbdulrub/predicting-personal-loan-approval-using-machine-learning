from flask import Flask, render_template, request
import numpy as np
import pickle
app = Flask(__name__)
model = pickle.load(open(r'rdf.pkl', 'rb'))
scale = pickle.load(open)(r'scale1.pkl','rb')
@app.route('/') # rendering the html template
def home():
    return render_template('home.html')
    @app.route('/submit',methods=["POST","GET"])# route to show the predictions in a web UI
    def submit():
        #  reading the inputs given by the user
        input_feature=[int(x) for x in request.form.value() ]
        #input_feature = np.transpose(input_feature)
        input_feature=[np.array(input_featue)]
        print(input_feature)
        names = ['GENDER', 'MARRIED', 'Dependents', 'Education', 'Self_Employed', 'ApplicantIncome', 'CoapplicantIncome', 'Loan_Amount_Term', 'Credit_History', 'Property_Area']
        das.DataFrame(input_feature,columns=names)
        print(data)

        #data_scaled = scale.fit_transform(data)
        #data = pandas.DataFrame(,columns=names)



        #predictions using the loaded model file
        prediction=model.predict(data)
        print(predictions)
        prediction = int(prediction)
        print(type(prediction))

        if (prediction ==0);
            return render_template("output.html",result = "Loan will Not be Approved")
        else:
            return render_template("output.html",result = "Loan will be Approved")
           # showing the prediction results in a UI
           if__name__=="__main":
              #app.run(host='0.0.0.0', port=8000,debug=True)
              port=int(os.environ.get('PORT,5000'))
              app.run(debug=False)