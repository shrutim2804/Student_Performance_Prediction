from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load('../Model/xgboost.pkl')
feature_names = joblib.load('../Model/feature_names.pkl')

def map_inputs(form):
    # GPA: entered as percentage, convert to 0-4 scale then normalize 0-1
    gpa_raw = float(form.get('gpa', 0))
    gpa = (gpa_raw / 100) * 4
    gpa_normalized = gpa / 4

    # Absences: entered as number, normalize (max assumed 30)
    absences = float(form.get('absences', 0))
    absences_normalized = min(absences / 30, 1.0)

    # StudyTimeWeekly: entered as hours, normalize (max assumed 20)
    study = float(form.get('study_hours', 0))
    study_normalized = min(study / 20, 1.0)

    # Age: normalize (min 15, max 18)
    age = float(form.get('age', 17))
    age_normalized = (age - 15) / (18 - 15)

    # Categorical inputs
    tutoring     = int(form.get('tutoring', 0))
    parental_sup = int(form.get('parental_support', 0))
    parental_edu = int(form.get('parental_education', 0))
    ethnicity    = int(form.get('ethnicity', 0))

    # Activity score: sum of extracurricular, sports, music, volunteering
    extracurricular = int(form.get('extracurricular', 0))
    sports          = int(form.get('sports', 0))
    music           = int(form.get('music', 0))
    volunteering    = int(form.get('volunteering', 0))
    activity_score  = extracurricular + sports + music + volunteering

    # Engineered features
    support_index    = tutoring + parental_sup
    engagement_ratio = study_normalized / (absences_normalized + 0.001)

    # Build in exact model order
    values = {
        'GPA'               : gpa_normalized,
        'Absences'          : absences_normalized,
        'Engagement_Ratio'  : engagement_ratio,
        'StudyTimeWeekly'   : study_normalized,
        'Support_Index'     : support_index,
        'ParentalEducation' : parental_edu,
        'ParentalSupport'   : parental_sup,
        'Age'               : age_normalized,
        'Ethnicity'         : ethnicity,
        'Activity_Score'    : activity_score
    }

    return [values[f] for f in feature_names], values

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_vals, display_vals = map_inputs(request.form)
        input_array = np.array(input_vals).reshape(1, -1)
        prediction  = model.predict(input_array)[0]
        probability = model.predict_proba(input_array)[0]

        grade_map = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'F'}
        emoji_map = {0: '🟢', 1: '🔵', 2: '🟡', 3: '🟠', 4: '🔴'}
        grade      = grade_map.get(int(prediction), '?')
        emoji      = emoji_map.get(int(prediction), '')
        confidence = round(max(probability) * 100, 2)

        return render_template('result.html',
                               grade=grade,
                               emoji=emoji,
                               confidence=confidence,
                               form_data=request.form)
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)