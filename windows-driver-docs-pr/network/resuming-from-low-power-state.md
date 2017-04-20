---
title: Resuming from Low Power State
description: Resuming from Low Power State
ms.assetid: 97f05dc9-df6f-4721-858e-9cf027af2cff
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Resuming from Low Power State


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

This section applies only to NDIS 6.20 and later.

When an 802.11 miniport driver resumes operation from a low-power state (D1 through D3), how it behaves and reports its status to the operating system depend on the availability of a nearby access point (AP). The following possible scenarios apply.

### In Proximity to Original AP

If an 802.11 miniport driver resumes from a low-power state while the NIC is in the proximity of an AP with which it was associated before entering the low-power state, the driver must associate with that AP. The driver must also report successful association to the operating system within one second. In this case, the driver does not need to send any status indications to the operating system.

For example, suppose the driver is initially associated with an AP with BSSID = B1 and SSID = S1. When the driver resumes operation in a high-power state at the same location, within one second it must report to the operating system a successful association with BSSID = B1 and SSID = S1.

A possible way to meet this requirement is as follows. When the NIC wakes up, it detects the presence of the AP by broadcasting an 802.11 Probe Request frame. The NIC broadcasts on the channel of the AP with which it originally associated. If the driver is configured for a hidden network profile, it should include the SSID of the original AP in the Probe Request. For more information on hidden APs, see [OID\_DOT11\_HIDDEN\_NETWORK\_ENABLED](https://msdn.microsoft.com/library/windows/hardware/ff569371).

### In Proximity to Another ESS AP

If a miniport driver resumes from a low-power state while the NIC is in the proximity of an AP that it was not associated with before entering the low-power state, but that matches the wireless profile set on the miniport, the driver must associate with that AP. The driver must also report successful association to the operating system within 4 seconds.

For example, suppose the driver is initially associated with an AP with BSSID = B1 and SSID = S1. When the driver resumes operation in a high-power state at a new location that is covered by the same ESS, BSSID B1 is not available, but BSSID = B2 with the same SSID = S1 is detected. In this case, the driver must report to the operating system a successful association to the new AP within 4 seconds. The AP with BSSID = B2 can be on a different PHY or on a different channel from the original BSSID = B1.

A possible way to meet this requirement is as follows. When the NIC wakes up, it performs a scan across all channels and all PHYs to find another AP that belongs to the same SSID. The NIC uses an active scan when not restricted by regulatory requirements. If the driver has configured the 802.11 station to access hidden network profiles, in the scan it should include this SSID in the Probe Request. When the candidate list is generated, the driver should attempt to associate with the best available AP.

### Not in Proximity to Another ESS AP

If a miniport driver resumes from a low-power state and does not find any AP that matches the wireless profile set on the miniport before it entered the low-power state, it should not report a successful association completion to the operating system. However, the driver must perform a scan across all channels and all PHYs to locate a new AP. In response to the next [OID\_DOT11\_DESIRED\_BSSID\_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569141) BSS list query from the operating system, the driver should return a list of all surrounding BSSs.

 

 





