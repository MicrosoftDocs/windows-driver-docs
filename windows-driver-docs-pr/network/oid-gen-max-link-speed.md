---
title: OID_GEN_MAX_LINK_SPEED
description: As a query, NDIS and overlying drivers use the OID_GEN_MAX_LINK_SPEED OID to determine the maximum supported transmit and receive link speeds of a miniport adapter.
ms.assetid: 4009c5c6-57ec-47f5-80d6-d69df797857f
ms.date: 08/08/2017
keywords: 
 -OID_GEN_MAX_LINK_SPEED Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_GEN\_MAX\_LINK\_SPEED


As a query, NDIS and overlying drivers use the OID\_GEN\_MAX\_LINK\_SPEED OID to determine the maximum supported transmit and receive link speeds of a miniport adapter.

**Version Information**

<a href="" id="windows-vista-and-later-versions-of-windows"></a>Windows Vista and later versions of Windows  
Supported.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Not requested. (see Remarks section)

Remarks
-------

The miniport driver supplies the maximum link speed during initialization.

To specify the maximum link speeds, set the **MaxXmitLinkSpeed** and **MaxRcvLinkSpeed** members of the [**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565923) structure that the miniport driver passes to the [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672) function. If a miniport driver does not support this OID, the driver should return NDIS\_STATUS\_NOT\_SUPPORTED. If the miniport driver supports this OID, it returns the maximum link speeds in an [**NDIS\_LINK\_SPEED**](https://msdn.microsoft.com/library/windows/hardware/ff565864) structure.

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


[**NDIS\_LINK\_SPEED**](https://msdn.microsoft.com/library/windows/hardware/ff565864)

[**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565923)

[**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672)

 

 




