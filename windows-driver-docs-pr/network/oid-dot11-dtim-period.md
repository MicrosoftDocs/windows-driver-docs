---
title: OID_DOT11_DTIM_PERIOD
author: windows-driver-content
description: OID_DOT11_DTIM_PERIOD
ms.assetid: 32690679-e806-4644-b163-7e7b6c494e1d
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_DTIM_PERIOD Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_DTIM\_PERIOD


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When queried, the OID\_DOT11\_DTIM\_PERIOD object identifier (OID) requests that the miniport driver return the value of the IEEE 802.11 **dot11DTIMPeriod** management information base (MIB) object for the current PHY type on the 802.11 station.

When set, this OID requests that the miniport driver set the value of **dot11DTIMPeriod**.

The **dot11DTIMPeriod** MIB object specifies the number of beacon intervals between transmissions of beacon frames that contain a TIM element with a DTIM Count field that equals zero. This value is transmitted in the DTIM Period field of beacon frames.

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


[Native 802.11 MIB OIDs](https://msdn.microsoft.com/library/windows/hardware/ff560645)

[Native 802.11 Wireless LAN OIDs](https://msdn.microsoft.com/library/windows/hardware/ff560691)

 

 




