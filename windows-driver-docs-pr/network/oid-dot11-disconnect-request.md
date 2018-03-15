---
title: OID_DOT11_DISCONNECT_REQUEST
author: windows-driver-content
description: OID_DOT11_DISCONNECT_REQUEST
ms.assetid: 89f46c68-1057-4998-86ee-b568eddfe8c2
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_DISCONNECT_REQUEST Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_DISCONNECT\_REQUEST


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_DISCONNECT\_REQUEST object identifier (OID) requests that the miniport driver perform a disconnection operation from the basic service set (BSS) network with which it is connected.

No data is associated with this OID.

When OID\_DOT11\_DISCONNECT\_REQUEST is set, the miniport driver must do the following:

-   If the 802.11 station is not connected to a BSS, fail the set request by returning NDIS\_STATUS\_INVALID\_STATE from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

-   If the 802.11 station is performing a connection operation initiated through a set request of [OID\_DOT11\_CONNECT\_REQUEST](oid-dot11-connect-request.md), fail the set request by returning NDIS\_STATUS\_INVALID\_STATE from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function. For more information about the connection operation, see [Connection Operations](https://msdn.microsoft.com/library/windows/hardware/ff545185).

-   If the 802.11 station is connected to a BSS network, perform a disconnection operation from the BSS network. For more information about the disconnection operation, see [Disconnection Operations](https://msdn.microsoft.com/library/windows/hardware/ff546447).

-   The 802.11 station must not power the radio off.

-   The miniport driver must transition to the INIT state of the Extensible Station (ExtSTA) operation mode. For more information about operation modes and related states, see [Extensible Station Operation Mode](https://msdn.microsoft.com/library/windows/hardware/ff549887).

-   The 802.11 station must stay disconnected from any BSS network until the next set request of [OID\_DOT11\_CONNECT\_REQUEST](oid-dot11-connect-request.md).

When OID\_DOT11\_DISCONNECT\_REQUEST is set, the miniport driver can do one of the following:

-   Wait for the disconnection operation to complete before completing the set request.

-   Initiate the disconnection operation and complete the set request. The miniport driver must return NDIS\_STATUS\_PENDING from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function after initiating the disconnection operation. After the disconnection operation has finished, the miniport driver completes the set request by calling [**NdisMRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563622).The miniport driver also makes the NDIS\_STATUS\_DOT11\_CONNECTION\_COMPLETION asynchronously after the set request.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Available in Windows Vista and later versions of the Windows operating systems.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Windot11.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[Native 802.11 Wireless LAN OIDs](https://msdn.microsoft.com/library/windows/hardware/ff560691)

 

 




