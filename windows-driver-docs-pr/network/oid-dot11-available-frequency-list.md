---
title: OID_DOT11_AVAILABLE_FREQUENCY_LIST
author: windows-driver-content
description: OID_DOT11_AVAILABLE_FREQUENCY_LIST
ms.assetid: f4531c27-c818-4eed-bbf5-d8e8032167ac
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_AVAILABLE_FREQUENCY_LIST Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_AVAILABLE\_FREQUENCY\_LIST


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When queried, the OID\_DOT11\_AVAILABLE\_FREQUENCY\_LIST requests that the miniport driver return the value of the **msDot11AvailableFrequencyList** management information base (MIB) object. The **msDot11AvailableFrequencyList** MIB object specifies the list of available frequencies that the NIC can operate with.

**Note**  Support for this OID is mandatory if the NIC reports to the operating system that it supports the [OFDM PHY configuration](https://msdn.microsoft.com/library/windows/hardware/ff568828).

 

The data type for this OID is the [**DOT11\_AVAILABLE\_FREQUENCY\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff547664) structure.

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


[**DOT11\_AVAILABLE\_FREQUENCY\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff547664)

[Native 802.11 Wireless LAN OIDs](https://msdn.microsoft.com/library/windows/hardware/ff560691)

 

 




