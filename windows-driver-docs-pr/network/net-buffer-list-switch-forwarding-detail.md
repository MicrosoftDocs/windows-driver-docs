---
title: NET\_BUFFER\_LIST\_SWITCH\_FORWARDING\_DETAIL macro
author: windows-driver-content
description: Hyper-V extensible switch extensions use the NET\_BUFFER\_LIST\_SWITCH\_FORWARDING\_DETAIL macro to access the NDIS\_SWITCH\_FORWARDING\_DETAIL\_NET\_BUFFER\_LIST\_INFO union in the extensible switch context area in a NET\_BUFFER\_LIST structure.
ms.assetid: 8E6BE3AA-C4FD-40D8-AF13-5C7D0E7B8080
ms.author: windowsdriverdev 
ms.date: 0718/2017 
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NET_BUFFER_LIST_SWITCH_FORWARDING_DETAIL%20macro%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


