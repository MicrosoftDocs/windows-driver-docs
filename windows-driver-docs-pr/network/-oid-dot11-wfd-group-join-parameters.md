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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20%20OID_DOT11_WFD_GROUP_JOIN_PARAMETERS%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


