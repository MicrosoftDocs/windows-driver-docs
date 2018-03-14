---
title: OID_DOT11_MULTICAST_LIST
author: windows-driver-content
description: OID_DOT11_MULTICAST_LIST
ms.assetid: 5a27a01f-57d8-435c-a0a8-6ae671b350e2
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_MULTICAST_LIST Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_MULTICAST\_LIST


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_MULTICAST\_LIST object identifier (OID) requests that the miniport driver set its multicast address list to the specified list.

When queried, this OID requests that the miniport driver return its list of multicast addresses.

The data type for OID\_DOT11\_MULTICAST\_LIST is the [**DOT11\_MAC\_ADDRESS**](https://msdn.microsoft.com/library/windows/hardware/ff548681) structure.

The miniport driver can determine the number of media access control (MAC) addresses in the multicast address list from the **InformationBufferLength** member of the [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function's *OidRequest* parameter:

```
 NumOfMulticastAddresses = (InformationBufferLength / sizeof(DOT11_MAC_ADDRESS)
```

The OID\_DOT11\_MULTICAST\_LIST OID can be set at any time, regardless of the miniport driver's current packet filter. After the packet filter is changed to enable any multicast address filter, the miniport driver must enable filtering on the 802.11 station using the current multicast address list.

For more information about 802.11 packet filters, see [OID\_GEN\_CURRENT\_PACKET\_FILTER](oid-gen-current-packet-filter.md).

The miniport driver must clear its multicast address list and disable multicast address filtering on the 802.11 station if any of the following occur:

-   The miniport driver's [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function is called.

-   A method request of [OID\_DOT11\_RESET\_REQUEST](oid-dot11-reset-request.md) is made to reset the MAC layer of the 802.11 station.

The miniport driver must retain its current multicast address list following a call to its [*MiniportResetEx*](https://msdn.microsoft.com/library/windows/hardware/ff559432) function. The miniport driver must also enable multicast filtering on the 802.11 station if the multicast address list contains one or more MAC addresses.

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

 

 




