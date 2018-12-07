---
title: Receiving a Wait/Wake IRP
description: Receiving a Wait/Wake IRP
ms.assetid: 88fa7189-4897-484a-9cf4-b35e56e99d61
keywords: ["power management WDK kernel , wake-up capabilities", "external wake signals WDK", "awakening devices", "wake-up capabilities WDK power management", "device wake ups WDK power management", "IRP_MN_WAIT_WAKE", "receiving wait/wake IRPs", "wait/wake IRPs WDK power management , receiving"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Receiving a Wait/Wake IRP





All PnP drivers must be prepared to receive power IRPs with minor IRP code [**IRP\_MN\_WAIT\_WAKE**](https://msdn.microsoft.com/library/windows/hardware/ff551766). How a driver handles a wait/wake IRP depends on its position in the device stack, the type of device(s) it controls, and the specific states from which its device supports wake-up.

The topics in this section provide guidelines for handling this IRP based on the type of driver and its level of wait/wake support.

 

 




