---
title: OID_GEN_LINK_STATE
description: As a query, NDIS and overlying drivers use the OID_GEN_LINK_STATE OID to determine the current link state of a miniport adapter.
ms.assetid: 75a30054-8700-4b79-902c-c8382a25c0a2
ms.date: 08/08/2017
keywords: 
 -OID_GEN_LINK_STATE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_GEN\_LINK\_STATE


As a query, NDIS and overlying drivers use the OID\_GEN\_LINK\_STATE OID to determine the current link state of a miniport adapter. The miniport driver receives the link state in an [**NDIS\_LINK\_STATE**](https://msdn.microsoft.com/library/windows/hardware/hh205390) structure.

**Version Information**

<a href="" id="windows-vista-and-later-versions-of-windows"></a>Windows Vista and later versions of Windows  
Supported.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Not requested. (see Remarks section)

Remarks
-------

Miniport drivers supply the link state during initialization and provide updates with status indications.

To specify the link state, set the **MediaConnectState**, **MediaDuplexState**, **XmitLinkSpeed**, **RcvLinkSpeed**, **PauseFunctions**, and **AutoNegotiationFlags** members of the [**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565923) structure that the miniport driver passes to the [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672) function.

If a miniport driver does not support this OID, the driver should return NDIS\_STATUS\_NOT\_SUPPORTED. If the miniport driver supports this OID, it returns the connection state, duplex state, and link speeds in an [**NDIS\_LINK\_STATE**](https://msdn.microsoft.com/library/windows/hardware/hh205390) structure.

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


[**NDIS\_LINK\_STATE**](https://msdn.microsoft.com/library/windows/hardware/hh205390)

[**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565923)

[**NDIS\_OBJECT\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff566588)

[**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672)

[OID\_GEN\_MEDIA\_CONNECT\_STATUS\_EX](oid-gen-media-connect-status-ex.md)

[OID\_GEN\_MEDIA\_DUPLEX\_STATE](oid-gen-media-duplex-state.md)

 

 




