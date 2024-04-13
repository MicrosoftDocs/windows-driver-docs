---
title: "!ndiskd.compartments"
description: "The !ndiskd.compartments extension displays all network compartments."
keywords: ["!ndiskd.compartments Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- ndiskd.compartments
api_type:
- NA
---

# !ndiskd.compartments


The **!ndiskd.compartments** extension displays all network compartments.

```console
!ndiskd.compartments 
```

## Parameters


This extension has no parameters.

## DLL

Ndiskd.dll

## Remarks

Compartments are a way that NDIS manages interfaces. Third party interface providers only use the primary compartment, as described in the **CompartmentId** member of the [**NDIS\_BIND\_PARAMETERS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_bind_parameters) structure.

## Examples

Run the **!ndiskd.compartments** extension to see a list of all network compartments. In this example, there is only one compartment (the primary one).

```console
3: kd> !ndiskd.compartments
    Compartment        ffffdf80139b9940
    ID                 1
    Loopback Network   ffffdf80139b8900
    Loopback Interface ffffdf80139b6a20
    Networks:
                       ffffdf80139b8900    [Unnamed network]
```

## See also


[Network Driver Design Guide](../network/index.md)

[Windows Vista and Later Networking Reference](/windows-hardware/drivers/ddi/_netvista/)

[Debugging the Network Stack](/shows/defrag-tools/175-debugging-network-stack)

[**NDIS extensions (Ndiskd.dll)**](ndis-extensions--ndiskd-dll-.md)

[**!ndiskd.help**](-ndiskd-help.md)

[**NDIS\_BIND\_PARAMETERS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_bind_parameters)

 


