---
title: CM_PROB_WAITING_ON_DEPENDENCY
description: CM_PROB_WAITING_ON_DEPENDENCY
ms.assetid: 2f45c507-1926-47f4-aca8-f8b834c58601
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# CM_PROB_WAITING_ON_DEPENDENCY


The device did not start because it has a dependency on another device that has not started.

### Error Code

51

### Display Message (Windows Server 2008 and later versions of Windows)

"This device is currently waiting on another device or set of devices to start. (Code 51)."

### Recommended Resolution (Windows Server 2008 and later versions of Windows)

There is currently no resolution to this problem.

To help diagnose the problem, examine other failed devices in the [device tree](https://msdn.microsoft.com/library/windows/hardware/ff543194) that this device might depend on. If you can determine why another related device did not start, you might be able to resolve this issue.

 

 





