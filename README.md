# ComfyUI-V-Prediction-Node
Node to set v-prediction sampling when using SDXL and other models that may not have the necessary metadata to identify it as a v-prediction model.
This is relevant for any quantized models since they lack the necessary metadata.

### The basic workflow
The workflow is simple. Search for 'AddPram' node and connect to the node that loads the model (e.g. unetloader) and it will set it to v_prediction.

![Screenshot of AddParam node](images/Workflow01.png)
### Installation
Use GIT:

cd ComfyUI/custom_nodes

git clone https://github.com/magekinnarus/ComfyUI-V-Prediction-Node.git

Restart ComfyUI after installing!

### Acknowledgement
ComfyUI: this node utilizes the modules in the ComfyUI codebase for its functions.
