---
title: OID_DOT11_SUPPORTED_RX_ANTENNA
author: windows-driver-content
description: OID_DOT11_SUPPORTED_RX_ANTENNA
ms.assetid: 03159f85-e69b-4510-b429-507d1a2f517b
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_SUPPORTED_RX_ANTENNA Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_SUPPORTED\_RX\_ANTENNA


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When queried, the OID\_DOT11\_SUPPORTED\_RX\_ANTENNA object identifier (OID) requests that the miniport driver return the list of antennas on the 802.11 station that support receive (RX) operations.

The data type for this OID is the [**DOT11\_SUPPORTED\_ANTENNA\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff548788) structure.

When this OID is queried, the miniport driver must verify that the **InformationBuffer** member of the [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function's *OidRequest* parameter is large enough to return the list of supported receive antennas. For more information about this procedure, see [**DOT11\_SUPPORTED\_ANTENNA\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff548788).

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

 

 




