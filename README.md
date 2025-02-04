# ComfyUI-V-Prediction-Node
Node to set v-prediction sampling when using SDXL and other models that may not have the necessary metadata to identify it as a v-prediction model.
This is relevant for any quantized models since they lack the necessary metadata.

### The basic workflow
The workflow is simple. Search for 'AddPram' node and connect to the node that loads the model (e.g. unetloader) and it will set it to v_prediction.

### Installation
Use GIT:

cd ComfyUI/custom_nodes

git clone [https://github.com/magekinnarus/ComfyUI-V-Prediction-Node]

Restart ComfyUI after installing!
