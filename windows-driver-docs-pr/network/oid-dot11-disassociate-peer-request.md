---
title: OID_DOT11_DISASSOCIATE_PEER_REQUEST
author: windows-driver-content
description: OID_DOT11_DISASSOCIATE_PEER_REQUEST
ms.assetid: d12e6374-bc2f-4302-b0ba-24d0b6687849
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_DISASSOCIATE_PEER_REQUEST Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_DISASSOCIATE\_PEER\_REQUEST


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_DISASSOCIATE\_PEER\_REQUEST object identifier (OID) requests that the miniport driver disassociate the NIC from a specified peer station with which the 802.11 station is associated. If the NIC has an association with the specified peer station, it must disassociate from the peer station as described in [Explicit Disassociation Operations](https://msdn.microsoft.com/library/windows/hardware/ff548876) and return a DOT11\_STATUS\_DISASSOCIATION status indication. If the NIC disassociates from all peer stations (when DOT11\_DISASSOCIATE\_PEER\_REQUEST. **PeerMacAddr** = 0xFF), it can return a single DOT11\_STATUS\_DISASSOCIATION status indication.

**Note**  Support for this OID is mandatory.

 

The data type for this OID is the [**DOT11\_DISASSOCIATE\_PEER\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff547681) structure.

When this OID is set, the NIC must behave as follows:

-   If the Extensible AP is in the INIT state, the NIC must fail the request and return a status indication of NDIS\_STATUS\_INVALID\_STATE.

-   If the Extensible AP is in the OP state, the NIC must complete the request if the peer station is in the association table. The NIC must enforce synchronization because the NIC could receive this request while the NIC is already associating or disassociating with a peer station.

While the NIC is in the process of associating with a peer station, it will not receive this OID, but it can receive the reset request OID, OID\_DOT11\_RESET\_REQUEST.

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
<td><p>Available in Windows 7 and later versions of the Windows operating systems.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Windot11.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**DOT11\_DISASSOCIATE\_PEER\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff547681)

[Native 802.11 Wireless LAN OIDs](https://msdn.microsoft.com/library/windows/hardware/ff560691)

 

 




