---
title: OID\_DOT11\_WFD\_DEVICE\_CAPABILITY
author: windows-driver-content
description: When set, the OID\_DOT11\_WFD\_DEVICE\_CAPABILITY object identifier (OID) modifies the Peer-to-Peer (P2P) device functionality that a Wi-Fi Direct (WFD) device supports and advertises in the P2P Capability attribute.
ms.assetid: DAB74B39-A904-4F53-9123-0BBA86EBEEF0
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords:
 - OID_DOT11_WFD_DEVICE_CAPABILITY Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_WFD\_DEVICE\_CAPABILITY


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_WFD\_DEVICE\_CAPABILITY object identifier (OID) modifies the Peer-to-Peer (P2P) device functionality that a Wi-Fi Direct (WFD) device supports and advertises in the P2P Capability attribute.

The data type for this OID is the [**DOT11\_WFD\_DEVICE\_CAPABILITY\_CONFIG**](-dot11-wfd-device-capability-config.md) structure.

A miniport retains the updated information from the [**DOT11\_WFD\_DEVICE\_CAPABILITY\_CONFIG**](-dot11-wfd-device-capability-config.md) for later use in a response.

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


[**DOT11\_WFD\_DEVICE\_CAPABILITY\_CONFIG**](-dot11-wfd-device-capability-config.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_DOT11_WFD_DEVICE_CAPABILITY%20%20RELEASE:%20%288/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


