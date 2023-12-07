---
title: Monitor Drivers
description: Monitor Drivers
keywords:
- display devices WDK
- monitor drivers WDK
- display drivers WDK , monitor drivers
ms.date: 12/06/2023
---

# Monitor drivers on Windows

Each monitor has a device stack that includes the following monitor drivers:

* A Microsoft-supplied monitor class function driver, which is required for all monitors.
* Optionally, a vendor-supplied monitor filter driver. Monitor vendors can implement a filter driver to add functionality to their monitor device. For example, a filter driver might provide a custom monitor configuration UI.

The following articles describe the function and filter drivers associated with monitors:

[Monitor Class Function Driver](monitor-class-function-driver.md)

[Monitor Filter Drivers](monitor-filter-drivers.md)
