from cbdf_api import Postprocessor

class MyPostprocessor(Postprocessor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # receives the output as dict in the form
    # [{
    #    "identifier":"w_1231",
    #    "results":{
    #        "class_A":{"prediction":"0.9"},
    #        "class_B": {"prediction": "0.1"}
    #    },
    #   "graphics":{}
    #}]
    def get_postprocessor(self, output):
        # assigns the fitting value to the gender property of each patient based on the identifier
        for patient in output:
            if patient["identifier"].startswith("m"):
                patient["gender"] = "male"
            elif patient["identifier"].startswith("w"):
                patient["gender"] = "female"
            else:
                raise Exception 

        return output
