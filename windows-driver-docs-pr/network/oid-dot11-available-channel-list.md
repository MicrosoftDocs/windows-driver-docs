---
title: OID_DOT11_AVAILABLE_CHANNEL_LIST
author: windows-driver-content
description: OID_DOT11_AVAILABLE_CHANNEL_LIST
ms.assetid: 3728261d-ed23-491e-b791-ca3778944939
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_AVAILABLE_CHANNEL_LIST Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_AVAILABLE\_CHANNEL\_LIST


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When queried, the OID\_DOT11\_AVAILABLE\_CHANNEL\_LIST OID requests that the miniport driver return the value of the **msDot11AvailableChannelList** MIB object. The **msDot11AvailableChannelList** MIB object specifies the available operating frequency channel list of the [DSSS, HRDSSS, and ERP PHY configurations](https://msdn.microsoft.com/library/windows/hardware/ff548836) that the NIC can operate with.

**Note**  Support for this OID is mandatory if the NIC reports to the operating system that it supports DSSS, HRDSSS, or ERP PHY configurations.

 

The data type for this OID is the [**DOT11\_AVAILABLE\_CHANNEL\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff547663) structure.

Valid channel numbers are defined in 15.4.6.2 of *IEEE Std. 802.11-1997*. The NIC should return the available frequency channel list based on its own capability and knowledge of the regulatory domain. The NIC must ensure that any entry in this list does not violate the regulatory domain requirements where the NIC is operating.

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


[**DOT11\_AVAILABLE\_CHANNEL\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff547663)

[Native 802.11 Wireless LAN OIDs](https://msdn.microsoft.com/library/windows/hardware/ff560691)

 

 




