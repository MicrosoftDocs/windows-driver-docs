---
title: C28176 warning
description: Warning C28176 The member of struct should not be modified by a driver.
keywords:
- warnings listed WDK PREfast for Drivers
- errors listed WDK PREfast for Drivers
ms.date: 04/20/2017
f1_keywords: 
  - "C28176"
---

# C28176


warning C28176: The member of struct should not be modified by a driver

This warning indicates that a driver changed an undocumented structure member that drivers should never change.

Drivers should not write to the specified undocumented structure member. For most undocumented members of opaque or partially opaque structures, this prohibition is absolute. However, drivers may write certain undocumented structure members from within particular routines. For example, the [**DEVICE\_OBJECT.NextDevice**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_device_object) member can be written only within a DRIVER\_INITIALIZE or DRIVER\_UNLOAD routine.

 

