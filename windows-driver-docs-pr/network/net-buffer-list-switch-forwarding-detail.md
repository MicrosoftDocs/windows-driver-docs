---
title: NET_BUFFER_LIST_SWITCH_FORWARDING_DETAIL macro
author: windows-driver-content
description: Hyper-V extensible switch extensions use the NET_BUFFER_LIST_SWITCH_FORWARDING_DETAIL macro to access the NDIS_SWITCH_FORWARDING_DETAIL_NET_BUFFER_LIST_INFO union in the extensible switch context area in a NET_BUFFER_LIST structure.
ms.assetid: 8E6BE3AA-C4FD-40D8-AF13-5C7D0E7B8080
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NET_BUFFER_LIST_SWITCH_FORWARDING_DETAIL macro Network Drivers Starting with Windows Vista
---

# NET\_BUFFER\_LIST\_SWITCH\_FORWARDING\_DETAIL macro


Hyper-V extensible switch extensions use the **NET\_BUFFER\_LIST\_SWITCH\_FORWARDING\_DETAIL** macro to access the [**NDIS\_SWITCH\_FORWARDING\_DETAIL\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh598211) union in the extensible switch context area in a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

Syntax
------

```ManagedCPlusPlus
PNDIS_SWITCH_FORWARDING_DETAIL_NET_BUFFER_LIST_INFO NET_BUFFER_LIST_SWITCH_FORWARDING_DETAIL(
   NET_BUFFER_LIST _NBL
);
```

Parameters
----------

*\_NBL*   
A pointer to a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

Return value
------------

The **NET\_BUFFER\_LIST\_SWITCH\_FORWARDING\_DETAIL** macro returns a pointer to the [**NDIS\_SWITCH\_FORWARDING\_DETAIL\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh598211) union within the specified [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

**Note**  **NET\_BUFFER\_LIST\_SWITCH\_FORWARDING\_DETAIL** returns **NULL** if the [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure does not contain an [**NDIS\_SWITCH\_FORWARDING\_DETAIL\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh598211) structure.

 

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Target platform</p></td>
<td>Desktop</td>
</tr>
<tr class="even">
<td><p>Version</p></td>
<td><p>Supported in NDIS 6.30 and later.</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Ndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[Adding Extensible Switch Destination Port Data to a Packet](https://msdn.microsoft.com/library/windows/hardware/hh582253)

[Cloning Packet Traffic](https://msdn.microsoft.com/library/windows/hardware/hh582254)

[Excluding Packet Delivery to Extensible Switch Destination Ports](https://msdn.microsoft.com/library/windows/hardware/hh582255)

[Forwarding Extensions](https://msdn.microsoft.com/library/windows/hardware/hh598148)

[Forwarding Packets to Hyper-V Extensible Switch Ports](https://msdn.microsoft.com/library/windows/hardware/hh598152)

[Forwarding Packets to Physical Network Adapters](https://msdn.microsoft.com/library/windows/hardware/hh582257)

[Modifying a Packet's Extensible Switch Source Port Data](https://msdn.microsoft.com/library/windows/hardware/hh582266)

[Overview of the Hyper-V Extensible Switch](https://msdn.microsoft.com/library/windows/hardware/hh582268)

[Packet Management Guidelines for the Extensible Switch Data Path](https://msdn.microsoft.com/library/windows/hardware/hh582270)

[Querying a Packet's Extensible Switch Source Port Data](https://msdn.microsoft.com/library/windows/hardware/hh582272)

[**NDIS\_SWITCH\_FORWARDING\_DETAIL\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh598211)

[**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388)

 

 




