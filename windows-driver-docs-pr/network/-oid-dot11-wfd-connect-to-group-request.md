---
title: OID_DOT11_WFD_CONNECT_TO_GROUP_REQUEST
author: windows-driver-content
description: When set, the OID\_DOT11\_WFD\_CONNECT\_TO\_GROUP\_REQUEST object identifier (OID) requests that the miniport driver perform a connection operation to join a Wi-Fi Direct (WFD) group.
ms.assetid: 67B02FD9-1CB2-424D-989C-11A307070B93
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_WFD_CONNECT_TO_GROUP_REQUEST Network Drivers Starting with Windows Vista
---

#  OID\_DOT11\_WFD\_CONNECT\_TO\_GROUP\_REQUEST


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_WFD\_CONNECT\_TO\_GROUP\_REQUEST object identifier (OID) requests that the miniport driver perform a connection operation to join a Wi-Fi Direct (WFD) group. The operation for this OID is identical to that of an [OID\_DOT11\_CONNECT\_REQUEST](oid-dot11-connect-request.md) request for an Extensible Station (ExtSTA) port. For more information about the connection operation, see [Connection Operations](https://msdn.microsoft.com/library/windows/hardware/ff545185).

No data is associated with this OID.

If the connection operation completes successfully, the miniport driver must transition to the WFD client operational (OP) state. The miniport driver must remain in the WFD client OP state until either a method request of [OID\_DOT11\_RESET\_REQUEST](oid-dot11-reset-request.md) or set request of [OID\_DOT11\_WFD\_DISCONNECT\_FROM\_GROUP\_REQUEST](oid-dot11-wfd-disconnect-from-group-request.md) is made. For more information about this state, see [Extensible Station Operating States](https://msdn.microsoft.com/library/windows/hardware/ff549883).

When OID\_DOT11\_WFD\_CONNECT\_TO\_GROUP\_REQUEST is set, the miniport driver must fail the request by returning **NDIS\_STATUS\_POWER\_STATE\_INVALID** from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function if any of the following are true:

-   All of the PHYs specified through the ExtSTA *msDot11DesiredPhyList* MIB object are turned off through sets of [OID\_DOT11\_NIC\_POWER\_STATE](oid-dot11-nic-power-state.md). For more information about this MIB object, see [OID\_DOT11\_DESIRED\_PHY\_LIST](oid-dot11-desired-phy-list.md).

-   All of the PHYs specified through the ExtSTA *msDot11DesiredPhyList* MIB object are turned off through a hardware switch setting or proprietary software setting.

-   Additional criteria apply for the connection request to fail, as described in [General Connection Operation Guidelines](https://msdn.microsoft.com/library/windows/hardware/ff552458).

When OID\_DOT11\_WFD\_CONNECT\_TO\_GROUP\_REQUEST is set, the miniport driver can do one of the following:

-   Wait for the connection operation to complete before completing the set request.

-   Initiate the connection operation and complete the set request. In this situation, the miniport driver must return **NDIS\_STATUS\_PENDING** from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function after initiating the connection operation. After the reset operation has finished, the miniport driver completes the set request by calling [**NdisMRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563622).

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
<td><p>Versions: Supported in Windows 8.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Windot11.h (include Windot11.h)</td>
</tr>
</tbody>
</table>

## See also


[OID\_DOT11\_CONNECT\_REQUEST](oid-dot11-connect-request.md)

[OID\_DOT11\_RESET\_REQUEST](oid-dot11-reset-request.md)

[OID\_DOT11\_WFD\_DISCONNECT\_FROM\_GROUP\_REQUEST](oid-dot11-wfd-disconnect-from-group-request.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20%20OID_DOT11_WFD_CONNECT_TO_GROUP_REQUEST%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


