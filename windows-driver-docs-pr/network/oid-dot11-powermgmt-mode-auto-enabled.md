---
title: OID_DOT11_POWER_MGMT_MODE_AUTO_ENABLED
author: windows-driver-content
description: This OID supports Set operation.
ms.assetid: 56817EBC-EF21-4013-8298-92944CD05C11
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_POWER_MGMT_MODE_AUTO_ENABLED Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_POWER\_MGMT\_MODE\_AUTO\_ENABLED


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

This OID supports Set operation. If a miniport driver reports that it supports automatic Power Save Mode (Auto-PSM) capability, then Windows issues this OID when appropriate. For example, when the power policy UX does not set Wi-Fi power to "Maximum Performance". On receipt of this OID, devices should operate intelligently in a power efficient way, and transition in and out of PS mode as appropriate.

![default power save mode example sequence showing calls from ndis to nwifi and then to the miniport driver](images/wifiautopsm.png)

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

 

 




