---
title: OID\_DOT11\_WFD\_LISTEN\_STATE\_DISCOVERABILITY
author: windows-driver-content
description: When set, the OID\_DOT11\_WFD\_LISTEN\_STATE\_DISCOVERABILITY object identifier (OID) is used to set the discoverability state of a Wi-Fi Direct (WFD) device and to configure its availability settings.
ms.assetid: C2BFB189-18B4-4FA9-AC17-2FEE53DC2E53
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_WFD_LISTEN_STATE_DISCOVERABILITY Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_WFD\_LISTEN\_STATE\_DISCOVERABILITY


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_WFD\_LISTEN\_STATE\_DISCOVERABILITY object identifier (OID) is used to set the discoverability state of a Wi-Fi Direct (WFD) device and to configure its availability settings.

The data type for OID\_DOT11\_WFD\_LISTEN\_STATE\_DISCOVERABILITY is a **ULONG** availability value.

The WFD availability is set to one of the following values.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Term</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>DOT11_WFD_DEVICE_NOT_DISCOVERABLE</p></td>
<td><p>The WFD device port must remain undiscoverable. The device must not periodically put itself in the listen state to allow other devices to discover it. This is the default availability setting.</p></td>
</tr>
<tr class="even">
<td><p> DOT11_WFD_DEVICE_AUTO_AVAILABILITY</p></td>
<td><p>The WFD device port must periodically put itself in the listen state to become discoverable. It must use appropriate availability periods to balance power, discoverability, and performance of the WFD ports and other ports on the miniport. It must follow the availability guidelines in the Wi-Fi Direct Peer-To-Peer Technical Specification.</p></td>
</tr>
<tr class="odd">
<td><p>DOT11_WFD_DEVICE_HIGH_AVAILABILITY</p></td>
<td><p>The WFD device port must frequently put itself into the listen state for an extended duration to increase the speed and reliability of remote devices discovering it. For example, a remote device that periodically scans the listen channel at 250ms intervals should discover the device within no more than 250ms. To achieve this, the device may be available on the listen channel for a contiguous 300ms every 400ms. The DOT11_WFD_DEVICE_HIGH_AVAILABILITY setting must not result in loss of connectivity on the ExtSTA (infrastructure) or any Wi-Fi Direct ports. It is, however, expected that this setting may degrade the performance of these connections in terms of latency and throughput.</p></td>
</tr>
</tbody>
</table>

 

Responding to the OID\_DOT11\_WFD\_LISTEN\_STATE\_DISCOVERABILITY request is only applicable when the WFD port is in device mode. When the port is in Group Owner (GO) mode and the group is started, it must be discoverable as required by the Wi-Fi Peer-To-Peer Technical Specification.

When the WFD device is discoverable, the miniport driver selects a listen channel. After the miniport sets the device to discoverable, it should transition in and out of the listen state as required by the Wi-Fi Direct Peer-To-Peer Technical Specification.

On initialization, the WFD port must use the default availability setting, **DOT11\_WFD\_DEVICE\_NOT\_DISCOVERABLE**, to determine its behavior.

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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_DOT11_WFD_LISTEN_STATE_DISCOVERABILITY%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


