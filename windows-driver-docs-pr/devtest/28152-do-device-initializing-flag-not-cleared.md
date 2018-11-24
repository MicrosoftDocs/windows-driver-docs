---
title: C28152
description: Warning C28152 The return from an AddDevice-like function unexpectedly DO_DEVICE_INITIALIZING.
ms.assetid: df2b68dc-b22b-4aaa-b1ba-b34bfdd9b886
keywords:
- warnings listed WDK PREfast for Drivers
- errors listed WDK PREfast for Drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# C28152


warning C28152: The return from an AddDevice-like function unexpectedly DO\_DEVICE\_INITIALIZING

The driver has returned from its **AddDevice** routine, or a similar utility routine, but the **DO\_DEVICE\_INITIALIZING** bit of the **Flags** word (**DeviceObject-&gt;Flags**) in the **DeviceObject** routine is not cleared.

The **AddDevice** routine must contain code similar to the following to clear the **DO\_DEVICE\_INITIALIZING** flag.

```
FunctionalDeviceObject->Flags &= ~DO_DEVICE_INITIALIZING;
```

For more information about **AddDevice** routines, see [AddDevice Routines in Function or Filter Drivers](https://msdn.microsoft.com/library/windows/hardware/ff540529)

 

 





