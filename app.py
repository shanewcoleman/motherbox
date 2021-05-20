


class Motherbox(environment_dump):
    """We're gonna need to structure 
    these settings according to item and quantiy
    Additionally, we'll probably need to define what each item
    is dependent on inside of the file structure. 

    IE:

    {
        resource_group: "name",
        "vm":["quantity":1, "depends_on": ["vnet", "nsg"]],
        "vnet": {cidr_range: <ip range>, }
        disks: {"opt":<size>, "tmp":500, "data":250}

    }
    etc. etc. 

    We can have top level elements correspond to resources. This will make it 
    easier to determine each resource's specifications. 
    """

