---
title: C28175
description: Warning C28175 The member of struct should not be accessed by a driver.
ms.assetid: 259a90d7-29ef-4a27-a921-8fff93b325bd
keywords:
- warnings listed WDK PREfast for Drivers
- errors listed WDK PREfast for Drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# C28175


warning C28175: The member of struct should not be accessed by a driver

This warning indicates that a driver accessed an undocumented structure member that drivers should never access.

Drivers should never access the specified undocumented structure member. For most undocumented members of opaque or partially opaque structures, this prohibition is absolute. However, drivers may access certain undocumented structure members from within particular routines. For example, the driver may access the undocumented members of the partially opaque [**DRIVER\_OBJECT**](https://msdn.microsoft.com/library/windows/hardware/ff544174) structure only within a DRIVER\_INITIALIZE or DRIVER\_UNLOAD routine.

Sometimes the reason that this rule applies to a particular member is not immediately obvious. For example, one instance where this occurs is with the **NextDevice** member of **\_DEVICE\_OBJECT**. In this instance, a lock should be used to safely access this linked list, but that lock is not available to the driver. In this case, violating this rule causes infrequent but hard-to-diagnose failures. The proper way to access the related devices is to use the [**IoEnumerateDeviceObjectList**](https://msdn.microsoft.com/library/windows/hardware/ff548342) function.

 

 





