---
title: OID_DOT11_WFD_DEVICE_INFO
author: windows-driver-content
description: When set, the OID_DOT11_WFD_DEVICE_INFO object identifier (OID) provides Wi-Fi Direct device information for setting Peer-to-Peer (P2P) attributes.
ms.assetid: EC526346-D2BB-4C25-A4B7-241CDBF6AD9E
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_WFD_DEVICE_INFO Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_WFD\_DEVICE\_INFO


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_WFD\_DEVICE\_INFO object identifier (OID) provides Wi-Fi Direct device information for setting Peer-to-Peer (P2P) attributes.

The data type for OID\_DOT11\_WFD\_DEVICE\_INFO is the [**DOT11\_WFD\_DEVICE\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh464147) structure.

The miniport retains the attribute information from the [**DOT11\_WFD\_DEVICE\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh464147) structure for use in later response operations.

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


[**DOT11\_WFD\_DEVICE\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh464147)

 

 




