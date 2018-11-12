---
title: Battery Devices Design Guide
description: Battery Devices Design Guide
ms.assetid: d8eecfcb-6c06-40d1-8c78-b8c88eb890f2
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Battery Devices Design Guide


## <span id="ddk_design_guide_battery_devices_dg"></span><span id="DDK_DESIGN_GUIDE_BATTERY_DEVICES_DG"></span>


A battery typically has a pair of drivers: the generic battery class driver that Microsoft provides, and a miniclass driver written specifically for that individual type of battery.

The class driver defines the overall functionality of the batteries in the system and interacts with the power manager.

This design guide focuses on [Writing Battery Miniclass Drivers](writing-battery-miniclass-drivers.md).

In addition this section includes information on [Writing UPS Minidrivers](writing-ups-minidrivers.md) that were used with older versions of Windows.

 

 




