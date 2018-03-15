---
title: OID_DOT11_WFD_FLUSH_DEVICE_LIST
author: windows-driver-content
description: When set, the OID_DOT11_WFD_FLUSH_DEVICE_LIST object identifier (OID) requests that the miniport driver clear the device list cached in the Wi-Fi Direct (WFD) device.
ms.assetid: B9A281B8-331B-47D3-BB00-36BFC7948DE0
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_WFD_FLUSH_DEVICE_LIST Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_WFD\_FLUSH\_DEVICE\_LIST


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_WFD\_FLUSH\_DEVICE\_LIST object identifier (OID) requests that the miniport driver clear the device list cached in the Wi-Fi Direct (WFD) device. The miniport must flush the list of WFD devices and Group Owners (GOs) when it receives this OID.

The miniport may also flush the list of infrastructure access points and discovered adhoc networks when it receives this OID.

No data is sent with this OID.

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

 

 




