---
title: AddDevice Routines in Bus Drivers
description: AddDevice Routines in Bus Drivers
ms.assetid: 70af7116-2f29-4d77-a6d5-c1e0417e6f81
keywords: ["bus drivers WDK kernel", "AddDevice routines WDK kernel , bus drivers"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# AddDevice Routines in Bus Drivers





A PnP bus driver has an *AddDevice* routine, but it is called when the bus driver is acting as the function driver for its controller or adapter. For example, the PnP manager calls the USB Hub bus driver's *AddDevice* routine to add the hub device. The hub driver's *AddDevice* routine is not called for a child of the hub (a device that plugs into the hub).

 

 




