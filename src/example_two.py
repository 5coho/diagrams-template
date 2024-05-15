from diagrams import Cluster, Diagram
from diagrams.aws.compute import ECS, EKS, Lambda
from diagrams.aws.database import Redshift
from diagrams.aws.integration import SQS
from diagrams.aws.storage import S3


def example_two(diagram_name: str, path: str = "diagrams") -> None:
    """Example Diagram from https://diagrams.mingrammer.com/docs/getting-started/examples#event-processing-on-aws with small changes regarding output

    Args:
        diagram_name (str): The name of the diagram
        path (str, optional): File path to where diagrams get sent. Defaults to "diagrams".
    """

    graph_attr = {
        "fontsize": "16",
        "bgcolor": "white",
        "pad": "0.5"
    }

    with Diagram(
        diagram_name,
        show=False,
        outformat=["png", "jpg", "svg"],
        filename=f"{path}/{diagram_name}/{diagram_name}",
        graph_attr=graph_attr,
    ):
        source = EKS("k8s source")

        with Cluster("Event Flows"):
            with Cluster("Event Workers"):
                workers = [ECS("worker1"), ECS("worker2"), ECS("worker3")]

            queue = SQS("event queue")

            with Cluster("Processing"):
                handlers = [Lambda("proc1"), Lambda("proc2"), Lambda("proc3")]

        store = S3("events store")
        dw = Redshift("analytics")

        source >> workers >> queue >> handlers
        handlers >> store
        handlers >> dw
