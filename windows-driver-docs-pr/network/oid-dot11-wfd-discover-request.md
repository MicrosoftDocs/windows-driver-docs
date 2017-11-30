---
title: OID_DOT11_WFD_DISCOVER_REQUEST
author: windows-driver-content
description: When set, the OID_DOT11_WFD_DISCOVER_REQUEST object identifier (OID) requests that the miniport driver perform a device discovery operation and return the list of discovered devices and networks.
ms.assetid: 87EB02C3-09CA-4F7E-9523-35096727B16B
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_WFD_DISCOVER_REQUEST Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_WFD\_DISCOVER\_REQUEST


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_WFD\_DISCOVER\_REQUEST object identifier (OID) requests that the miniport driver perform a device discovery operation and return the list of discovered devices and networks.

The data type for OID\_DOT11\_WFD\_DISCOVER\_REQUEST is the [**DOT11\_WFD\_DISCOVER\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/hh464149) structure.

The system may provide the miniport driver additional Information Elements (IEs) that it should insert into the probe request packets for Wi-Fi Direct (WFD) device discovery. If provided, the driver should include these in probe requests sent for WFD devices. If IEs are not provided, the miniport driver must use the default request IEs in the [**DOT11\_WFD\_ADDITIONAL\_IE**](https://msdn.microsoft.com/library/windows/hardware/hh464144) structure that was sent with [OID\_DOT11\_WFD\_ADDITIONAL\_IE](oid-dot11-wfd-additional-ie.md).

After the device discovery has started, the miniport must perform the following to complete the OID:

-   If the process started successfully, the OID must be completed with **NDIS\_STATUS\_INDICATION\_REQUIRED**.

-   The completion of device discovery initiated by OID\_DOT11\_WFD\_DISCOVER\_REQUEST must be indicated to the system with a [**NDIS\_STATUS\_DOT11\_WFD\_DISCOVER\_COMPLETE**](https://msdn.microsoft.com/library/windows/hardware/hh451704) status indication.

When the WFD device port performs a device discovery operation, the miniport driver should cache the received beacon and probe response packets. The miniport driver returns the list of the cached beacon and probe response packets in the completion indication and when queried by [OID\_DOT11\_WFD\_ENUM\_DEVICE\_LIST](oid-dot11-wfd-enum-device-list.md). This list can contain devices discovered in other recent scans.

The miniport driver must not report about any devices that have sent only probe requests and have not sent beacons or probe responses. The [**DOT11\_WFD\_DEVICE\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/hh464146) structure for each discovered peer device should include the IEs from both the beacon and probe response packets.

While device discovery is in progress, the miniport may receive [OID\_DOT11\_WFD\_ENUM\_DEVICE\_LIST](oid-dot11-wfd-enum-device-list.md) requests. It should return a device list that includes the devices found during the ongoing discovery, in addition to devices that have been discovered in other recent scans.

The miniport must handle the situation where a WFD device supports multiple concurrent groups and can respond to probe requests as a WFD device as well as one or more WFD direct Group Owners (GOs). The miniport can use the transmitter address or BSSID from the received packets to distinguish various responses from the same Peer-to-Peer (P2P) device address.

The miniport driver should delete stale entries from its cached device list. The rules for identifying stale entries is determined by miniport. Devices that have not been visible for more than five minutes must not be reported to the system. The miniport driver can also perform internal device discovery operations to add or update its cached device list.

While operating system-requested discovery is in progress, the miniport should not enter the listen state except during the Find phase. That is, the miniport should ignore the listen-state discoverability setting if it is set to a value other than DOT11\_WFD\_DEVICE\_NOT\_DISCOVERABLE.

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


[**DOT11\_WFD\_ADDITIONAL\_IE**](https://msdn.microsoft.com/library/windows/hardware/hh464144)

[**DOT11\_WFD\_DEVICE\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/hh464146)

[**DOT11\_WFD\_DISCOVER\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/hh464149)

[**NDIS\_STATUS\_DOT11\_WFD\_DISCOVER\_COMPLETE**](https://msdn.microsoft.com/library/windows/hardware/hh451704)

[OID\_DOT11\_WFD\_ENUM\_DEVICE\_LIST](oid-dot11-wfd-enum-device-list.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_DOT11_WFD_DISCOVER_REQUEST%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


