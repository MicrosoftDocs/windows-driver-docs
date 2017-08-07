---
title: OID\_DOT11\_OFFLOAD\_NETWORK\_LIST
author: windows-driver-content
description: This OID supports Set operation.
ms.assetid: F404E428-4B82-45F3-9AFA-AABA213B6C2A
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords:
 - OID_DOT11_OFFLOAD_NETWORK_LIST Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_OFFLOAD\_NETWORK\_LIST


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

This OID supports Set operation. OID\_DOT11\_OFFLOAD\_NETWORK\_LIST Set OID requests the Wi-Fi device to set up hardware to scan for networks in the offload list. Hardware should scan for all SSIDs on hinted channels and only interrupt Windows when it finds one or more networks with BSS's in the offload list. This list contains SSID's that are setup to auto-connect. Devices must configure the offload of all networks on the list or none when it returns failure. The offload-list may contain networks less or equal to the number of **uMaxNetworkOffloadListSize** in the [**DOT11\_EXTSTA\_ATTRIBUTES**](dot11-extsta-attributes.md) structure. The NIC should indicate when the network appears but not when the network disappears. If the device is in a low power state (D3), the NIC should wake Windows, to indicate a match within the NLO list.

The NIC scans for offload network list in two phases, first fast-scan phase followed by the slow-scan phase. This is to allow a backoff from aggressive scanning to better improve battery efficiency.

If the request is successful, the full list is offloaded and functional. If not successful, no entries in the list should be offloaded. If a device succeeds this request, it continues to function in this mode until Windows explicitly resets the OID.

When a miniport driver receives an OID\_DOT11\_OFFLOAD\_NETWORK\_LIST with non-empty list, it starts to scan for networks. Once that initial scan is complete it follows the fast scan and slow scan schedule. It indicates [NDIS\_STATUS\_DOT11\_OFFLOAD\_NETWORK\_STATUS\_CHANGED](https://msdn.microsoft.com/library/windows/hardware/hh451702) when a newly discovered network is on the list, but not when one disappears from the list. A "newly" discovered network is a network that comes into range. A given network should only trigger an indication once during the lifetime of the NLO Set operation.

The NIC should not scan if the radio is off even though NLO is configured. The NIC in low power state should wake Windows for offload network list change indications. Miniport drivers should prepare devices to wake up Windows prior to device entering a low power state.

For example:

FastScanPeriod=60 seconds

FastScanIteration=15

SlowScanPeriod=1800 seconds

Unless Windows issues a new offload list, the NIC will scan for offload network list every 60 seconds for 15 times. After 15 times, the NIC switches to SlowScanPeriod when the NIC will scan every 1800 seconds.

In response to a [NDIS\_STATUS\_DOT11\_OFFLOAD\_NETWORK\_STATUS\_CHANGED](https://msdn.microsoft.com/library/windows/hardware/hh451702) indication, Windows may follow-up with a full scan and query for [OID\_DOT11\_ENUM\_BSS\_LIST](oid-dot11-enum-bss-list.md) to decide the best network from the visible networks in order to make a connection. For each indication, Windows may make a connection and subsequently clear the list. When Windows decides to make a connection, NWifi first issues a DOT11 reset which makes the miniport driver/NIC clear all offloads. Windows then evaluates and plumbs down a new network offload list once the connection is complete. Other protocol offloads may be plumbed down at this time.

![network list offload example sequence showing calls down to the miniport driver and the hardware](images/nlo.png)

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
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_DOT11_OFFLOAD_NETWORK_LIST%20%20RELEASE:%20%288/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


