from diagrams import Cluster, Diagram
from diagrams.aws.compute import ECS
from diagrams.aws.database import RDS
from diagrams.aws.network import Route53


def example_one(diagram_name: str, path: str = "diagrams") -> None:
    """Example Diagram from https://diagrams.mingrammer.com/docs/guides/cluster with small changes regarding output

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
        outformat=["png"],
        filename=f"{path}/{diagram_name}",
        graph_attr=graph_attr,
    ):
        dns = Route53("dns")
        web = ECS("service")

        with Cluster("DB Cluster"):
            db_primary = RDS("primary")
            db_primary - [RDS("replica1"), RDS("replica2")]

        dns >> web >> db_primary
