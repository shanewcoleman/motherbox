


class Motherbox(environment_dump):
    """We're gonna need to structure 
    these settings according to item and quantiy
    Additionally, we'll probably need to define what each item
    is dependent on inside of the file structure. 

    IE:

    {
        "vm":["quantity":1, "depends_on":"vnet"]
    }
    etc. etc. 

    We can have top level elements correspond to resources. This will make it 
    easier to determine each resource's specifications. 
    """