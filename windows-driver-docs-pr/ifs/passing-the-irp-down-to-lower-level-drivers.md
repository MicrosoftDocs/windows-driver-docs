---
title: Passing the IRP Down to Lower-Level Drivers
description: Passing the IRP Down to Lower-Level Drivers
ms.assetid: 9a8e72fb-b0a8-4026-8606-57fa03344146
keywords:
- IRP dispatch routines WDK file system , passing IRP down
- passing IRPs down device stack WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Passing the IRP Down to Lower-Level Drivers


## <span id="ddk_passing_the_irp_down_to_lower_level_drivers_if"></span><span id="DDK_PASSING_THE_IRP_DOWN_TO_LOWER_LEVEL_DRIVERS_IF"></span>


By default every dispatch routine, after checking the IRP's target device object, must pass the IRP down to the next-lower-level device driver by calling [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336). It is especially important that your filter driver pass down any IRPs that it does not recognize instead of simply failing them. Failing unfamiliar IRPs can cause the operating system itself to fail in unexpected ways. For example, failing IRP\_MJ\_PNP requests in a file system filter driver can interfere with power management by preventing system hibernation. This is true despite the fact that file system filter drivers are not involved in power management and do not receive [**IRP\_MJ\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff550784) requests.

 

 




