---
title: Stopping a Device
description: Stopping a Device
ms.assetid: 65a47e7b-aabd-4b55-8fa6-c3482da1cc84
keywords: ["PnP WDK kernel , stopping devices", "Plug and Play WDK kernel , stopping devices", "stopping PnP devices", "stop IRPs WDK PnP"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Stopping a Device





The PnP manager directs drivers to stop a device in the following situations:

-   To rebalance the hardware resources being used by the device. Rebalancing is typically necessary when a new device is enumerated that requires a resource already in use.

-   To disable the device in response to a Device Manager request (Windows 98/Me only). Windows 2000 and later versions of Windows send remove IRPs in this situation; see [Understanding When Remove IRPs Are Issued](understanding-when-remove-irps-are-issued.md).

-   After a failed [**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749) request (Windows 98/Me only)

This section covers the following topics:

[Stopping a Device to Rebalance Resources](stopping-a-device-to-rebalance-resources.md)

[Stopping a Device to Disable It (Windows 98/Me)](stopping-a-device-to-disable-it--windows-98-me-.md)

[Stopping a Device after a Failed Start (Windows 98/Me)](stopping-a-device-after-a-failed-start--windows-98-me-.md)

[Handling Stop IRPs (Windows 2000 and Later)](handling-stop-irps--windows-2000-and-later-.md)

[Handling Stop IRPs (Windows 98/Me)](handling-stop-irps--windows-98-me-.md)

 

 




