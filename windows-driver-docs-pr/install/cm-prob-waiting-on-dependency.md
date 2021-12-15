---
title: CM_PROB_WAITING_ON_DEPENDENCY
description: CM_PROB_WAITING_ON_DEPENDENCY
ms.date: 04/20/2017
---

# Code 51 - CM_PROB_WAITING_ON_DEPENDENCY

This Device Manager error message indicates that the device did not start because it has a dependency on another device that has not started.

## Error Code

51

### Display Message

"This device is currently waiting on another device or set of devices to start. (Code 51)."

### Recommended Resolution

There is currently no resolution to this problem.

To help diagnose the problem, examine other failed devices in the [device tree](../kernel/device-tree.md) that this device might depend on. If you can determine why another related device did not start, you might be able to resolve this issue.
