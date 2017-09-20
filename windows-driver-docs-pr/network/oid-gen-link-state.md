---
title: OID\_GEN\_LINK\_STATE
author: windows-driver-content
description: As a query, NDIS and overlying drivers use the OID\_GEN\_LINK\_STATE OID to determine the current link state of a miniport adapter.
ms.assetid: 75a30054-8700-4b79-902c-c8382a25c0a2
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_GEN_LINK_STATE Network Drivers Starting with Windows Vista
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_GEN_LINK_STATE%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


