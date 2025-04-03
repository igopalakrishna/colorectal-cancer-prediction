import kfp
from kfp import dsl
import kfp.compiler

def data_processing_op():
    return dsl.ContainerOp(
        name="Data Processing",
        image = "igopalakrishna23/ccp-app:latest",
        command = ["python", "src/data_processing.py"]
    )
def model_training_op():
    return dsl.ContainerOp(
        name = "Model Training",
        image = "igopalakrishna23/ccp-app:latest",
        command = ["python", "src/model_training.py"] 
    )

#pipelining

@dsl.pipeline(
    name="kuberflow pipeline",
    description = "Kubeflow Pipeline for Colorectal Cancer Prediction"
)
def kfpipeline():
    data_processing = data_processing_op()
    model_training = model_training_op().after(data_processing)

#run

if __name__ =="__main__":
    kfp.compiler.Compiler().compile(
        kfpipeline, "kfpipeline.yaml"
    )





# import kfp
# from kfp import dsl
# from kfp.dsl import pipeline, component


# @component(base_image="python:3.9")
# def data_processing_op():
#     return dsl.ContainerSpec(
#         image="igopalakrishna23/ccp-app:latest",
#         command=["python", "src/data_preprocessing.py"]
#     )


# @component(base_image="python:3.9")
# def model_training_op():
#     return dsl.ContainerSpec(
#         image="igopalakrishna23/ccp-app:latest",
#         command=["python", "src/model_training.py"]
#     )


# @pipeline(
#     name="Kubeflow Pipeline",
#     description="Kubeflow Pipeline for Colorectal Cancer Prediction"
# )
# def kfpipeline():
#     data_step = data_processing_op()
#     model_step = model_training_op().after(data_step)


# if __name__ == "__main__":
#     kfp.compiler.Compiler().compile(
#         pipeline_func=kfpipeline,
#         package_path="kfpipeline.yaml"
#     )
