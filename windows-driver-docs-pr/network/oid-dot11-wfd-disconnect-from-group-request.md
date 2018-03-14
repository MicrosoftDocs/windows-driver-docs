---
title: OID_DOT11_WFD_DISCONNECT_FROM_GROUP_REQUEST
author: windows-driver-content
ms.assetid: C0AE95DB-8186-4B89-8115-B6B300FD8D73
description: 
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_WFD_DISCONNECT_FROM_GROUP_REQUEST Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_WFD\_DISCONNECT\_FROM\_GROUP\_REQUEST


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_WFD\_DISCONNECT\_FROM\_GROUP\_REQUEST object identifier (OID) requests that a Wi-Fi Direct (WFD) client perform a disconnection operation from the WFD group it joined previously. The operation for this OID is identical to that of an [OID\_DOT11\_DISCONNECT\_REQUEST](oid-dot11-disconnect-request.md) request for an Extensible Station (ExtSTA) port.

No data is associated with this OID.

When OID\_DOT11\_WFD\_DISCONNECT\_FROM\_GROUP\_REQUEST is set, the miniport driver must do the following:

-   If the WFD client is not joined to a group, fail the set request by returning **NDIS\_STATUS\_INVALID\_STATE** from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

-   If the WFD client is performing a connection operation initiated through a set request of [OID\_DOT11\_WFD\_CONNECT\_TO\_GROUP\_REQUEST](-oid-dot11-wfd-connect-to-group-request.md), fail the set request by returning **NDIS\_STATUS\_INVALID\_STATE** from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function. For more information about the connection operation, see [Connection Operations](https://msdn.microsoft.com/library/windows/hardware/ff545185).

-   If the WFD client station is joined to a group, perform a disconnection operation from the WFD group. For more information about the disconnection operation, see [Disconnection Operations](https://msdn.microsoft.com/library/windows/hardware/ff546447).

-   The WFD client must not power the radio off.

-   The miniport driver must transition to the INIT state of the WFD client port operation mode. For more information about operation modes and related states, see [Extensible Station Operation Mode](https://msdn.microsoft.com/library/windows/hardware/ff549887).

-   The WFD client must stay disconnected from any WFD group until the next set request of [OID\_DOT11\_WFD\_CONNECT\_TO\_GROUP\_REQUEST](-oid-dot11-wfd-connect-to-group-request.md).

When OID\_DOT11\_WFD\_DISCONNECT\_FROM\_GROUP\_REQUESTis set, the miniport driver can do one of the following:

-   Wait for the disconnection operation to complete before completing the set request.

-   Initiate the disconnection operation and complete the set request. The miniport driver must return **NDIS\_STATUS\_PENDING** from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function after initiating the disconnection operation. After the disconnection operation has finished, the miniport driver completes the set request by calling [**NdisMRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563622).The miniport driver also makes the [**NDIS\_STATUS\_DOT11\_CONNECTION\_COMPLETION**](ndis-status-dot11-connection-completion.md) asynchronously after the set request.

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
<td><p>Supported starting with Windows 8.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Windot11.h (include Windot11.h)</td>
</tr>
</tbody>
</table>

## See also


[OID\_DOT11\_DISCONNECT\_REQUEST](oid-dot11-disconnect-request.md)

[OID\_DOT11\_WFD\_CONNECT\_TO\_GROUP\_REQUEST](-oid-dot11-wfd-connect-to-group-request.md)

 

 




