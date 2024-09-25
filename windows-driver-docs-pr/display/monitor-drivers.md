---
title: Monitor Driver Stack
description: Introduces the Monitor Drivers
keywords:
- display devices WDK
- monitor drivers WDK
- display drivers WDK , monitor drivers
ms.date: 09/23/2024
---

# Monitor driver stack

Each monitor has a [device stack](../gettingstarted/driver-stacks.md) that includes the following monitor drivers:

* A [monitor class function driver](monitor-class-function-driver.md), which is required for all monitors. This driver is provided by Microsoft in the form of *Monitor.sys*.
* An optional [monitor filter driver](monitor-filter-drivers.md), which isn't system-supplied. Vendors can choose to implement a filter driver to add functionality to their monitor device. For example, a filter driver might provide a custom monitor configuration UI.
