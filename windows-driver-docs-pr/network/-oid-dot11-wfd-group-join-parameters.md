---
title: OID_DOT11_WFD_GROUP_JOIN_PARAMETERS
author: windows-driver-content
description: When set, the OID_DOT11_WFD_GROUP_JOIN_PARAMETERS object identifier (OID) provides the parameters for a Wi-Fi Direct (WFD) client join request.
ms.assetid: 8BA9DC85-41DA-4021-BFBC-2C64A38146E9
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_WFD_GROUP_JOIN_PARAMETERS Network Drivers Starting with Windows Vista
---

#  OID\_DOT11\_WFD\_GROUP\_JOIN\_PARAMETERS


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_WFD\_GROUP\_JOIN\_PARAMETERS object identifier (OID) provides the parameters for a Wi-Fi Direct (WFD) client join request.

The data type for this OID is the [**DOT11\_WFD\_GROUP\_JOIN\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh406655) structure.

If **bInGroupFormation** == FALSE and **bWaitForWPSReady** == TRUE in the [**DOT11\_WFD\_GROUP\_JOIN\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh406655) structure, the wait time for the GO to set the Selected Registrar attribute may be up to several minutes. For exampe, in the invitation case, the GO waits for the user to enter a PIN at prompt.

Depending on the parameters sent with this OID, the system may issue an [OID\_DOT11\_WFD\_CONNECT\_TO\_GROUP\_REQUEST](-oid-dot11-wfd-connect-to-group-request.md) resetting the port to cancel the connection request.

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
<td><p>Versions: Supported in Windows 8.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Windot11.h (include Windot11.h)</td>
</tr>
</tbody>
</table>

## See also


[**DOT11\_WFD\_GROUP\_JOIN\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh406655)

 

 




