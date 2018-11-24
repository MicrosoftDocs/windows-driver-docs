---
title: Monitor Filter Drivers
description: Monitor Filter Drivers
ms.assetid: cf2bd4c5-d586-4202-ad79-4e7ff9ad6061
keywords:
- filter drivers WDK monitors
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Monitor Filter Drivers


## <span id="ddk_monitor_filter_drivers_gg"></span><span id="DDK_MONITOR_FILTER_DRIVERS_GG"></span>


Microsoft provides a general-purpose monitor class function driver, Monitor.sys, that handles most monitor-related tasks. There is no need for a vendor-supplied monitor driver unless the vendor wants to provide services beyond those provided by the monitor class function driver.

If a monitor vendor chooses to provide a filter driver, that driver is represented by a filter device object that sits above the functional device object in the monitor's device stack. The filter driver handles requests from user-mode applications, also provided by the monitor vendor. The interface between the filter driver and the user-mode applications is private and known only to the monitor vendor.

Note that programmatic control of a monitor through the Display Data Channel Command Interface (DDC/CI) is not handled by the monitor device stack, so monitor vendors should not write filter drivers for that purpose.

For a representation of a monitor device stack, see [Monitor Class Function Driver](monitor-class-function-driver.md).

 

 





