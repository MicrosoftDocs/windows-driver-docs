---
title: Native 802.11 Miniport Driver Reset
description: Native 802.11 Miniport Driver Reset
ms.assetid: 9d1b02de-bc8c-4aaf-8e6b-4ed5000a0021
keywords: ["Native 802.11 miniport drivers WDK networking , reset operations", "miniport drivers WDK Native 802.11 , reset operations"]
---

# Native 802.11 Miniport Driver Reset


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

For the most part, Native 802.11 miniport drivers follow the same guidelines for [*MiniportResetEx*](https://msdn.microsoft.com/library/windows/hardware/ff559432) as other NDIS miniport drivers. For more information about these guidelines, see [Adapter Check-for-Hang and Reset](miniport-adapter-check-for-hang-and-reset-operations.md).

In addition, a Native 802.11 miniport driver must do the following when the [*MiniportResetEx*](https://msdn.microsoft.com/library/windows/hardware/ff559432) function is called:

-   Reset the NIC, which would include a reset of both the media access control (MAC) and PHY layers on the 802.11 station.

-   Cancel any explicit scan operations in progress that were initiated through a set of [OID\_DOT11\_SCAN\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569413). The miniport driver must also cancel any implicit scan operations initiated by the 802.11 station.

    The miniport driver must not clear the cached list of BSS networks that it detected during the previous scan operations.

    For more information about the scan operation, see [Native 802.11 Scan Operations](native-802-11-scan-operations.md).

-   Cancel any explicit scan operations in progress.

-   Restore the MAC address used by the 802.11 station to the address previously used before the NIC reset. If the miniport driver was configured with a locally administered MAC address, the driver must configure the 802.11 station to use that address. Otherwise, the driver must configure the 802.11 station to use its permanent MAC address.

-   Retain the configuration settings and configure the 802.11 station with these settings following the NIC reset, including any cipher keys previously downloaded to the 802.11 station through set requests of Native 802.11 object identifiers (OIDs). The miniport driver must remain in the Native 802.11 operating state that it was in before the NIC reset.

If the miniport driver is operating in the Extensible Station (ExtSTA) mode, it must restore the connection if the 802.11 station becomes disconnected because of the reset. In this situation, the miniport driver must follow these guidelines:

-   If the 802.11 station is able to reconnect to the BSS, the miniport driver must issue indications defined for the roaming operation. For more information about the roaming operation, see [Roaming Operations](roaming-operations.md).

-   If the 802.11 station is unable to reconnect, the miniport driver must issue indications defined for the disconnection operation. For more information about the disconnection operation, see [Disconnection Operations](disconnection-operations.md).

## Related topics


[Adapter States of a Miniport Driver](adapter-states-of-a-miniport-driver.md)

[Miniport Adapter States and Operations](miniport-adapter-states-and-operations.md)

[Native 802.11 Reset, Halt, and Shutdown Operations](native-802-11-reset--halt-and-shutdown-operations.md)

 

 






