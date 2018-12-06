---
title: C28135
description: Warning C28135 If the first argument to KeWaitForSingleObject is a local variable, the Mode parameter must be KernelMode.
ms.assetid: f42e41d7-240f-4de1-97b7-e50415aee14f
keywords:
- warnings listed WDK PREfast for Drivers
- errors listed WDK PREfast for Drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# C28135


warning C28135: If the first argument to KeWaitForSingleObject is a local variable, the Mode parameter must be KernelMode

The driver is waiting in user mode. As such, the kernel stack can be swapped out during the wait. If the driver attempts to pass parameters on the stack, a system crash can result.

### <span id="example"></span><span id="EXAMPLE"></span>Example

The following code example elicits this warning.

```
KeWaitForSingleObject(&MyMutex, UserRequest, UserMode, false, NULL);
```

The following code example avoids this warning.

```
KeWaitForSingleObject(&MyMutex, UserRequest, KernelMode, false, NULL);
```

 

 





