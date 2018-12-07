---
title: Handling a Change in the System's Power Source
description: Handling a Change in the System's Power Source
ms.assetid: 80e36a23-8a41-46f0-a7cb-0039c306a695
keywords:
- power source changes WDK networking
- NICs WDK networking , power source changes
- network interface cards WDK networking , power source changes
- Plug and Play WDK NDIS miniport , power source changes
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling a Change in the System's Power Source





The system can change from battery power to AC power or vice versa.

After initializing a miniport driver, NDIS calls a miniport driver's [*MiniportDevicePnPEventNotify*](https://msdn.microsoft.com/library/windows/hardware/ff559369) function to notify the miniport driver of the system's power source. The miniport driver can use this information to adjust the power consumption of a NIC. For example, the miniport driver for a wireless LAN (WLAN) device could reduce power consumption if the system is running on battery power or increase power consumption if the system is running on AC power.

 

 





