---
title: C28176
description: Warning C28176 The member of struct should not be modified by a driver.
ms.assetid: 837b2dcd-0682-460f-a3ae-ebd82bcc451b
keywords:
- warnings listed WDK PREfast for Drivers
- errors listed WDK PREfast for Drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# C28176


warning C28176: The member of struct should not be modified by a driver

This warning indicates that a driver changed an undocumented structure member that drivers should never change.

Drivers should not write to the specified undocumented structure member. For most undocumented members of opaque or partially opaque structures, this prohibition is absolute. However, drivers may write certain undocumented structure members from within particular routines. For example, the [**DEVICE\_OBJECT.NextDevice**](https://msdn.microsoft.com/library/windows/hardware/ff543147) member can be written only within a DRIVER\_INITIALIZE or DRIVER\_UNLOAD routine.

 

 





