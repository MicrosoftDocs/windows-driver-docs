---
title: OID_DOT11_WFD_DEVICE_CAPABILITY
author: windows-driver-content
description: When set, the OID_DOT11_WFD_DEVICE_CAPABILITY object identifier (OID) modifies the Peer-to-Peer (P2P) device functionality that a Wi-Fi Direct (WFD) device supports and advertises in the P2P Capability attribute.
ms.assetid: DAB74B39-A904-4F53-9123-0BBA86EBEEF0
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_WFD_DEVICE_CAPABILITY Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_WFD\_DEVICE\_CAPABILITY


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_WFD\_DEVICE\_CAPABILITY object identifier (OID) modifies the Peer-to-Peer (P2P) device functionality that a Wi-Fi Direct (WFD) device supports and advertises in the P2P Capability attribute.

The data type for this OID is the [**DOT11\_WFD\_DEVICE\_CAPABILITY\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/hh464145) structure.

A miniport retains the updated information from the [**DOT11\_WFD\_DEVICE\_CAPABILITY\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/hh464145) for later use in a response.

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


[**DOT11\_WFD\_DEVICE\_CAPABILITY\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/hh464145)

 

 




