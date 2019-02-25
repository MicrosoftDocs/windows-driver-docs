---
title: OID_GEN_MEDIA_CONNECT_STATUS
description: As a query, the OID_GEN_MEDIA_CONNECT_STATUS OID requests the connection status of the NIC on the network.
ms.assetid: 3ed26e62-a285-4b78-91c6-7c3cc0963570
ms.date: 08/08/2017
keywords: 
 -OID_GEN_MEDIA_CONNECT_STATUS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_GEN\_MEDIA\_CONNECT\_STATUS


As a query, the OID\_GEN\_MEDIA\_CONNECT\_STATUS OID requests the connection status of the NIC on the network.

**Version Information**

<a href="" id="windows-vista-and-later-versions-of-windows"></a>Windows Vista and later versions of Windows  
Supported.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Not requested.

<a href="" id="ndis-5-1-miniport-drivers"></a>NDIS 5.1 miniport drivers  
Mandatory.

<a href="" id="windows-xp"></a>Windows XP  
Supported.

<a href="" id="ndis-5-1-miniport-drivers"></a>NDIS 5.1 miniport drivers  
Mandatory.

Remarks
-------

NDIS handles this OID for NDIS 6.0 and later miniport drivers.

The OID\_GEN\_MEDIA\_CONNECT\_STATUS OID requests the connection status of the NIC on the network as one of the following system-defined values:

**NdisMediaStateConnected**

**NdisMediaStateDisconnected**

When a miniport driver senses that the network connection has been lost, it must also call the [**NdisMIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563600) or [**NdisMCoIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563562) function with NDIS\_STATUS\_MEDIA\_DISCONNECT (for NDIS 5.1) or NDIS\_STATUS\_LINK\_STATE with **MediaConnectStateDisconnected** in the MediaConnectState property (for NDIS 6.x). When the connection is restored, it must then call **NdisM(Co)IndicateStatus** with NDIS\_STATUS\_MEDIA\_CONNECT (for NDIS 5.1) or NDIS\_STATUS\_LINK\_STATE with **MediaConnectStateConnected** in the MediaConnectState property (for NDIS 6.x).

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


[**NdisMCoIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563562)

[**NdisMIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563600)

 

 




