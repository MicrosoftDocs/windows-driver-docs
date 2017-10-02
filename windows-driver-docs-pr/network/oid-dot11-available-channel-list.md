---
title: OID_DOT11_AVAILABLE_CHANNEL_LIST
author: windows-driver-content
description: OID\_DOT11\_AVAILABLE\_CHANNEL\_LIST
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_DOT11_AVAILABLE_CHANNEL_LIST%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


