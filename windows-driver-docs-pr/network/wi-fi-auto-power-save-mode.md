---
title: Wi-Fi Auto Power Save Mode
description: Wi-Fi miniport drivers are required to perform detection and negotiation of proper Wi-Fi Power Save Mode (PSM) between the device and the Wi-Fi Access Point and report it in driver capability during initialization in DOT11\_EXTSTA\_ATTRIBUTES.Windows 8 miniport drivers need to continue to support the OID\_DOT11\_POWER\_MGMT\_REQUEST which should be treated as a hint to the users preferred power consumption level.
ms.assetid: F8292C7E-4AEE-44E8-88BA-BF0D52654192
---

# Wi-Fi Auto Power Save Mode


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

Wi-Fi miniport drivers are required to perform detection and negotiation of proper Wi-Fi Power Save Mode (PSM) between the device and the Wi-Fi Access Point and report it in driver capability during initialization in [**DOT11\_EXTSTA\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff547688).

If the miniport driver reports that it supports PSM detection, then the WLAN Service will delegate the PSM decision to the miniport driver by default. If the miniport driver supports the Auto-PSM capability then the Wi-Fi service will no longer set the broadcast management filter to receive beacons from the miniport driver and will instead set an OID to turn on Auto-PSM in the miniport driver. When in Auto-PSM, the miniport driver should always negotiate PSM mode when it detects that the Wi-Fi Access Point supports it and manage the use of PSM between the device and the Wi-Fi Access Point to ensure optimal connectivity while using the least amount of power.

In addition, Windows 8 miniport drivers need to continue to support the [OID\_DOT11\_POWER\_MGMT\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569402) which should be treated as a hint to the users preferred power consumption level.

For legacy drivers that do not support Auto-PSM detection, the WLAN Service will continue to set the PSM mode via OID\_DOT11\_POWER\_MGMT\_REQUEST for the miniport driver after evaluating beacon information.

## Related topics


[Wi-Fi Auto Power Save Mode Reference](https://msdn.microsoft.com/library/windows/hardware/hh440283)

 

 






