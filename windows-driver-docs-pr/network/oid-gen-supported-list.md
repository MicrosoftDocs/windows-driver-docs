---
title: OID_GEN_SUPPORTED_LIST
author: windows-driver-content
description: As a query, the OID_GEN_SUPPORTED_LIST OID specifies an array of OIDs for objects that the miniport driver or a NIC supports.
ms.assetid: 4e663204-eee0-4732-83c9-ec1dacd41034
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_GEN_SUPPORTED_LIST Network Drivers Starting with Windows Vista
---

# OID\_GEN\_SUPPORTED\_LIST


As a query, the OID\_GEN\_SUPPORTED\_LIST OID specifies an array of OIDs for objects that the miniport driver or a NIC supports. Objects include general, media-specific, and implementation-specific objects.

**Version Information**

<a href="" id="windows-vista-and-later-versions-of-windows"></a>Windows Vista and later versions of Windows  
Supported.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Not requested.

<a href="" id="ndis-5-1-miniport-drivers"></a>NDIS 5.1 miniport drivers  
Mandatory. See [OID\_GEN\_SUPPORTED\_LIST (NDIS 5.1)](https://msdn.microsoft.com/library/windows/hardware/ff560258).

<a href="" id="windows-xp"></a>Windows XP  
Supported.

<a href="" id="ndis-5-1-miniport-drivers"></a>NDIS 5.1 miniport drivers  
Mandatory. See [OID\_GEN\_SUPPORTED\_LIST (NDIS 5.1)](https://msdn.microsoft.com/library/windows/hardware/ff560258).

Remarks
-------

NDIS 6.0 and later miniport drivers do not receive this OID request. NDIS handles this OID with a cached value that miniport drivers supply during initialization.

NDIS forwards a subset of the provided list to protocol drivers that make this query. That is, NDIS filters any supported statistics OIDs out of the list because protocol drivers never make statistics queries.

If a miniport driver lists an OID in its supported OIDs list, it must fully support the OID. That is, the miniport driver must return valid data when it responds to a query or set request for the OIDs that it includes in the list. For example, the [OID\_GEN\_STATISTICS](oid-gen-statistics.md) OID is a required OID for NDIS 6.0 and later miniport drivers. If a miniport driver does not support the statistics in hardware or software and returns incorrect statistics information, the driver cannot specify OID\_GEN\_STATISTICS in its supported OIDs list.

Duplicates might appear in the supported OIDs list. Drivers are not required to guarantee that there is only one entry for each OID in the list.

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


[OID\_GEN\_STATISTICS](oid-gen-statistics.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_GEN_SUPPORTED_LIST%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


