---
title: Virtual WiFi Implementation Guidelines
description: Virtual WiFi Implementation Guidelines
ms.assetid: e8a6903c-a673-4393-8a43-98ce4b219116
keywords: ["Virtual WiFi in kernel mode WDK networking , implementation"]
---

# Virtual WiFi Implementation Guidelines


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

During initialization, the 802.11 miniport driver must initialize the default 802.11 MAC entity. However, the driver is not required to register with NDIS the NDIS port corresponding to the default MAC entity.

The miniport driver must delete all MAC entities when the driver is halted. In this situation the driver should also free the ports that are registered with NDIS. For an NDIS 6.0 or later miniport, the [*MiniportHaltEx*](https://msdn.microsoft.com/library/windows/hardware/ff559388) handler will be called to halt the NIC.

The miniport driver completes a [**DOT11\_VWIFI\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff548808) structure to report the attributes of the driver and 802.11 station in Virtual WiFi mode. These attributes are reported through the **VWiFiAttributes** member of the [**NDIS\_MINIPORT\_ADAPTER\_NATIVE\_802\_11\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565926) structure.

The following are recommendations for how the miniport driver should implement support for virtualization.

1.  The miniport driver should implement an algorithm to schedule hardware access to the various MAC entities. The miniport must minimize scheduling hardware access for a MAC entity that is not in the OP (operational) state

2.  The driver must ensure that none of the MAC entities is starved for hardware access.

3.  The driver should centralize operations that are common across the different MAC entities (for example, [Native 802.11 Scan Operations](native-802-11-scan-operations.md)) and not repeat such operations for individual MAC entities.

4.  The driver must ensure that the security contexts for the different MAC entities are absolutely separate. Specifically the security settings for a MAC entity must be programmed on the hardware before any data is transmitted for that MAC.

5.  If the NIC hardware does not support per-MAC default keys, the driver can perform encryption and decryption using default keys in software.

 

 





