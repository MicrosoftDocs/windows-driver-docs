---
title: C28135 warning
description: Warning C28135 If the first argument to KeWaitForSingleObject is a local variable, the Mode parameter must be KernelMode.
keywords:
- warnings listed WDK PREfast for Drivers
- errors listed WDK PREfast for Drivers
ms.date: 04/20/2017
f1_keywords: 
  - "C28135"
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

