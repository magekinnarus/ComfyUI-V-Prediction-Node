import torch
import comfy.model_management
import comfy.model_sampling

class AddParam:
    parameterization_options = ["epsilon", "v_prediction"]  # Both options in the dropdown

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model": ("MODEL",),
                "parameterization": (s.parameterization_options,),  # Required input
            }
        }

    RETURN_TYPES = ("MODEL",)
    FUNCTION = "add_parameterization"

    CATEGORY = "advanced/model"

    def add_parameterization(self, model, parameterization):
        m = model.clone()

        if parameterization == "v_prediction":
            internal_parameterization = "v"  # Set internal value to "v"
            setattr(m.model, "parameterization", internal_parameterization)
            from comfy.model_sampling import V_PREDICTION, ModelSamplingDiscrete
            class ModelSamplingAdvanced(ModelSamplingDiscrete, V_PREDICTION):
                pass
            m.add_object_patch("model_sampling", ModelSamplingAdvanced(m.model.model_config))
        # No 'elif' for epsilon - this is the key for the bypass

        return (m,)  # Return the (potentially modified) model