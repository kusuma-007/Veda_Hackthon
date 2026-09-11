import pandas as pd


# =====================================================
# 1. CROP RECOMMENDATION
# =====================================================

def recommend_crop(soil, ph, water, location):

    scores = {
        "Groundnut": 0,
        "Maize": 0,
        "Paddy": 0,
        "Cotton": 0,
        "Chilli": 0
    }

    reasons = []

    # Soil condition
    if soil == "Loamy":
        scores["Groundnut"] += 30
        scores["Maize"] += 25

        reasons.append(
            "Loamy soil supports good crop growth."
        )

    elif soil == "Clay":
        scores["Paddy"] += 35

        reasons.append(
            "Clay soil has good water retention."
        )

    elif soil == "Black Soil":
        scores["Cotton"] += 35
        scores["Chilli"] += 20

        reasons.append(
            "Black soil is suitable for cotton."
        )

    elif soil == "Red Soil":
        scores["Groundnut"] += 30
        scores["Chilli"] += 25

        reasons.append(
            "Red soil can support groundnut and chilli."
        )

    # Soil pH
    if 6.0 <= ph <= 7.5:

        for crop in scores:
            scores[crop] += 15

        reasons.append(
            "Soil pH is within a generally favorable range."
        )

    # Water availability
    if water == "Low":

        scores["Groundnut"] += 20
        scores["Cotton"] += 15

        reasons.append(
            "Groundnut and cotton can be considered "
            "where water availability is limited."
        )

    elif water == "Medium":

        scores["Groundnut"] += 15
        scores["Maize"] += 15
        scores["Chilli"] += 15

        reasons.append(
            "Medium water availability supports several crops."
        )

    elif water == "High":

        scores["Paddy"] += 25

        reasons.append(
            "High water availability supports water-demanding crops."
        )

    # Find highest score
    best_crop = max(
        scores,
        key=scores.get
    )

    score = min(
        scores[best_crop],
        100
    )

    return {
        "crop": best_crop,
        "score": score,
        "reasons": reasons
    }


# =====================================================
# 2. MARKET ANALYSIS
# =====================================================

def analyze_market(crop):

    data = {

        "Paddy": [
            ["Peddapuram Market", 2450, "18 km"],
            ["Samalkota Market", 2380, "25 km"],
            ["Kakinada Market", 2320, "38 km"]
        ],

        "Groundnut": [
            ["Peddapuram Market", 6100, "18 km"],
            ["Tuni Market", 6250, "45 km"],
            ["Kakinada Market", 6000, "38 km"]
        ],

        "Maize": [
            ["Peddapuram Market", 2250, "18 km"],
            ["Kakinada Market", 2300, "38 km"],
            ["Samalkota Market", 2200, "25 km"]
        ],

        "Cotton": [
            ["Kakinada Market", 7200, "38 km"],
            ["Peddapuram Market", 7050, "18 km"],
            ["Rajahmundry Market", 7150, "60 km"]
        ],

        "Chilli": [
            ["Guntur Market", 18500, "220 km"],
            ["Kakinada Market", 17800, "38 km"],
            ["Samalkota Market", 17500, "25 km"]
        ]
    }

    return [
        {
            "Market": item[0],
            "Price": item[1],
            "Distance": item[2]
        }

        for item in data[crop]
    ]


# =====================================================
# 3. WEATHER RISK
# =====================================================

def weather_risk():

    return {

        "risk": "HIGH",

        "condition": "Heavy rainfall possible",

        "actions": [
            "Check and clear field drainage.",
            "Avoid unnecessary irrigation.",
            "Monitor crop for fungal diseases.",
            "Protect harvested produce from rain."
        ]
    }


# =====================================================
# 4. IRRIGATION ADVICE
# =====================================================

def irrigation_advice(crop, stage, water):

    if water == "Low":

        return (
            "Water availability is LOW. "
            "Prioritize critical crop stages, "
            "use efficient irrigation and monitor "
            "soil moisture before irrigating."
        )

    if crop == "Paddy":

        return (
            f"Paddy at {stage} stage requires careful "
            "water management. Maintain appropriate "
            "field moisture and avoid unnecessary "
            "continuous flooding."
        )

    return (
        f"{crop} at {stage} stage requires moderate "
        "irrigation. Check soil moisture before "
        "the next irrigation."
    )


# =====================================================
# 5. FERTILIZER ADVICE
# =====================================================

def fertilizer_advice(crop, stage, soil):

    return (
        f"For {crop} during the {stage} stage on "
        f"{soil} soil, follow the locally recommended "
        "nutrient schedule. Avoid fertilizer application "
        "immediately before heavy rainfall and use "
        "soil-test recommendations when available."
    )


# =====================================================
# 6. DISEASE ADVICE
# =====================================================

def disease_advice(crop):

    diseases = {

        "Paddy": {

            "disease": "Possible Leaf Blast",

            "confidence": 82,

            "symptoms": [
                "Brown or grey leaf lesions",
                "Leaf discoloration",
                "Reduced plant vigor"
            ],

            "actions": [
                "Inspect additional plants.",
                "Monitor disease spread.",
                "Avoid excessive nitrogen application.",
                "Consult an agricultural expert before treatment."
            ]
        },

        "Groundnut": {

            "disease": "Possible Leaf Spot",

            "confidence": 79,

            "symptoms": [
                "Dark spots on leaves",
                "Yellowing",
                "Premature leaf loss"
            ],

            "actions": [
                "Monitor affected plants.",
                "Improve field monitoring.",
                "Avoid excessive moisture.",
                "Seek expert confirmation."
            ]
        },

        "Maize": {

            "disease": "Possible Leaf Blight",

            "confidence": 76,

            "symptoms": [
                "Long leaf lesions",
                "Leaf yellowing"
            ],

            "actions": [
                "Monitor disease spread.",
                "Inspect nearby plants.",
                "Seek agricultural advisory."
            ]
        },

        "Cotton": {

            "disease": "Possible Leaf Spot",

            "confidence": 75,

            "symptoms": [
                "Spots on leaves",
                "Leaf yellowing"
            ],

            "actions": [
                "Inspect field regularly.",
                "Monitor disease spread.",
                "Consult an expert."
            ]
        },

        "Chilli": {

            "disease": "Possible Leaf Spot",

            "confidence": 74,

            "symptoms": [
                "Small dark spots",
                "Yellowing leaves"
            ],

            "actions": [
                "Improve field sanitation.",
                "Monitor nearby plants.",
                "Seek expert confirmation."
            ]
        }
    }

    return diseases[crop]


# =====================================================
# 7. GOVERNMENT SCHEMES
# =====================================================

def scheme_finder():

    return [

        {
            "name": "PM-KISAN",

            "benefit":
                "Direct income support for eligible farmers.",

            "eligibility":
                "Eligible farmer families subject to scheme rules.",

            "support":
                "Income support",

            "action":
                "Verify eligibility through the official government portal."
        },

        {
            "name": "PMFBY",

            "benefit":
                "Crop insurance support against specified risks.",

            "eligibility":
                "Eligible farmers and notified crops or areas.",

            "support":
                "Crop insurance",

            "action":
                "Check current notification and enrollment window."
        },

        {
            "name": "PMKSY",

            "benefit":
                "Support related to irrigation and water-use efficiency.",

            "eligibility":
                "Depends on the applicable component and state guidelines.",

            "support":
                "Irrigation support",

            "action":
                "Check current agriculture department guidelines."
        }
    ]


# =====================================================
# 8. CROP DEMAND ANALYSIS
# =====================================================

def demand_analysis():

    return [

        {
            "Crop": "Groundnut",
            "Demand Score": 88
        },

        {
            "Crop": "Maize",
            "Demand Score": 82
        },

        {
            "Crop": "Chilli",
            "Demand Score": 91
        },

        {
            "Crop": "Cotton",
            "Demand Score": 78
        },

        {
            "Crop": "Paddy",
            "Demand Score": 74
        }
    ]


# =====================================================
# 9. REGIONAL RISK
# =====================================================

def regional_risk():

    data = [

        [
            "Village A",
            "HIGH",
            "MEDIUM",
            "HIGH",
            "URGENT"
        ],

        [
            "Village B",
            "LOW",
            "HIGH",
            "MEDIUM",
            "HIGH"
        ],

        [
            "Village C",
            "MEDIUM",
            "LOW",
            "LOW",
            "NORMAL"
        ],

        [
            "Village D",
            "HIGH",
            "HIGH",
            "MEDIUM",
            "URGENT"
        ],

        [
            "Village E",
            "LOW",
            "MEDIUM",
            "LOW",
            "NORMAL"
        ]
    ]

    return pd.DataFrame(

        data,

        columns=[
            "Village",
            "Pest Risk",
            "Water Risk",
            "Weather Risk",
            "Priority"
        ]
    )


# =====================================================
# 10. AGRICULTURE OFFICER PRIORITY
# =====================================================

def officer_priority():

    return [

        {
            "village": "Village A",
            "priority": "URGENT",
            "reason": "High pest and weather risk"
        },

        {
            "village": "Village D",
            "priority": "URGENT",
            "reason": "High pest and water shortage risk"
        },

        {
            "village": "Village B",
            "priority": "HIGH",
            "reason": "Water availability requires monitoring"
        }
    ]