---
title: C28152
description: Warning C28152 The return from an AddDevice-like function unexpectedly DO_DEVICE_INITIALIZING.
keywords:
- warnings listed WDK PREfast for Drivers
- errors listed WDK PREfast for Drivers
ms.date: 04/20/2017
ms.localizationpriority: medium 
f1_keywords: 
  - "C28152"
---

# C28152


warning C28152: The return from an AddDevice-like function unexpectedly DO\_DEVICE\_INITIALIZING

The driver has returned from its **AddDevice** routine, or a similar utility routine, but the **DO\_DEVICE\_INITIALIZING** bit of the **Flags** word (**DeviceObject-&gt;Flags**) in the **DeviceObject** routine is not cleared.

The **AddDevice** routine must contain code similar to the following to clear the **DO\_DEVICE\_INITIALIZING** flag.

```
FunctionalDeviceObject->Flags &= ~DO_DEVICE_INITIALIZING;
```

For more information about **AddDevice** routines, see [AddDevice Routines in Function or Filter Drivers](../kernel/adddevice-routines-in-function-or-filter-drivers.md)

 

