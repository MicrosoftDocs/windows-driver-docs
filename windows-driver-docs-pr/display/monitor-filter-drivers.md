---
title: Monitor Filter Drivers
description: Monitor Filter Drivers
ms.assetid: cf2bd4c5-d586-4202-ad79-4e7ff9ad6061
keywords:
- filter drivers WDK monitors
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Monitor Filter Drivers


## <span id="ddk_monitor_filter_drivers_gg"></span><span id="DDK_MONITOR_FILTER_DRIVERS_GG"></span>


Microsoft provides a general-purpose monitor class function driver, Monitor.sys, that handles most monitor-related tasks. There is no need for a vendor-supplied monitor driver unless the vendor wants to provide services beyond those provided by the monitor class function driver.

If a monitor vendor chooses to provide a filter driver, that driver is represented by a filter device object that sits above the functional device object in the monitor's device stack. The filter driver handles requests from user-mode applications, also provided by the monitor vendor. The interface between the filter driver and the user-mode applications is private and known only to the monitor vendor.

Note that programmatic control of a monitor through the Display Data Channel Command Interface (DDC/CI) is not handled by the monitor device stack, so monitor vendors should not write filter drivers for that purpose.

For a representation of a monitor device stack, see [Monitor Class Function Driver](monitor-class-function-driver.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Monitor%20Filter%20Drivers%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




