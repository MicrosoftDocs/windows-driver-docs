---
title: OID_DOT11_WFD_STOP_DISCOVERY
author: windows-driver-content
description: OID_DOT11_WFD_STOP_DISCOVERY is used to request the Wi-Fi Direct Device to stop any ongoing P2P discovery operation.
ms.assetid: 3180CE98-E8A0-4505-B2E6-766442A820FD
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_WFD_STOP_DISCOVERY Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_WFD\_STOP\_DISCOVERY


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

OID\_DOT11\_WFD\_STOP\_DISCOVERY is used to request the Wi-Fi Direct Device to stop any ongoing P2P discovery operation. If a discovery request initiated by Windows is in progress, the Wi-Fi Direct device must complete it by issuing [**NDIS\_STATUS\_DOT11\_WFD\_DISCOVER\_COMPLETE**](https://msdn.microsoft.com/library/windows/hardware/hh451704) status indication to Windows.

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


[**NDIS\_STATUS\_DOT11\_WFD\_DISCOVER\_COMPLETE**](https://msdn.microsoft.com/library/windows/hardware/hh451704)

 

 




