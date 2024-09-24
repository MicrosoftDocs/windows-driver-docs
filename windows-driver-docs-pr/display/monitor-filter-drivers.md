---
title: Monitor Filter Drivers
description: Monitor Filter Drivers
keywords:
- filter drivers WDK monitors
ms.date: 09/23/2024
---

# Monitor Filter Drivers

Microsoft provides a general-purpose [monitor class function driver](monitor-class-function-driver.md) that handles most monitor-related tasks. There's no need for a vendor-supplied monitor driver unless the vendor wants to provide services beyond what the monitor class function driver provides.

If a monitor vendor chooses to provide a filter driver, that driver is represented by a filter device object (filter DO) that sits above the functional device object (FDO) in the monitor's device stack. The filter driver handles requests from user-mode applications, also provided by the monitor vendor. The interface between the filter driver and the user-mode applications is private and known only to the monitor vendor.

The monitor device stack doesn't handle programmatic control of a monitor through the Display Data Channel Command Interface (DDC/CI), so monitor vendors shouldn't write filter drivers for that purpose.

For a representation of a monitor device stack, see [Monitor Class Function Driver](monitor-class-function-driver.md).
