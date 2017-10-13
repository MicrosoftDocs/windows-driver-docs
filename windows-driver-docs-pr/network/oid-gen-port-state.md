---
title: OID_GEN_PORT_STATE
author: windows-driver-content
description: As a query, overlying drivers use the OID\_GEN\_PORT\_STATE OID to get the current state of the port that is specified in the PortNumber member of the NDIS\_OID\_REQUEST structure.
ms.assetid: e0705b2e-08ea-4ed4-a6df-4c33b934c3dd
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_GEN_PORT_STATE Network Drivers Starting with Windows Vista
---

# OID\_GEN\_PORT\_STATE


As a query, overlying drivers use the OID\_GEN\_PORT\_STATE OID to get the current state of the port that is specified in the **PortNumber** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure.

**Version Information**

<a href="" id="windows-vista-and-later-versions-of-windows"></a>Windows Vista and later versions of Windows  
Supported.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Not requested. (see Remarks section)

Remarks
-------

NDIS handles this OID and miniport drivers do not receive this OID query.

If the query succeeds, NDIS returns NDIS\_STATUS\_SUCCESS and returns the port state information in an [**NDIS\_PORT\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff566800) structure.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710)

[**NDIS\_PORT\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff566800)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_GEN_PORT_STATE%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


