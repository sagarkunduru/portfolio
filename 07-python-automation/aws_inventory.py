"""Read-only AWS EC2 inventory example.

Authentication is intentionally external (AWS profile, workload identity, etc.).
No credentials belong in source code.
"""

import boto3


def list_instances(region: str = "us-east-1") -> None:
    ec2 = boto3.client("ec2", region_name=region)
    paginator = ec2.get_paginator("describe_instances")

    for page in paginator.paginate():
        for reservation in page["Reservations"]:
            for instance in reservation["Instances"]:
                tags = {tag["Key"]: tag["Value"] for tag in instance.get("Tags", [])}
                print(
                    {
                        "id": instance["InstanceId"],
                        "state": instance["State"]["Name"],
                        "type": instance["InstanceType"],
                        "name": tags.get("Name", "unnamed"),
                    }
                )


if __name__ == "__main__":
    list_instances()
