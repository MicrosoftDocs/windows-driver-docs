---
title: C28165 Warning
description: Warning C28165 The function pointer of class does not match the function class.
keywords:
- warnings listed WDK PREfast for Drivers
- errors listed WDK PREfast for Drivers
ms.date: 04/20/2017
f1_keywords: 
  - "C28165"
---

# C28165


warning C28165: The function pointer of class does not match the function class

A function pointer has a **\_\_drv\_functionClass** annotation that specifies that only functions of a particular functional class should be assigned to it. In an assignment or implied assignment in a function call, the source and target must be of the same function class, but the function classes do not match.

### <span id="example"></span><span id="EXAMPLE"></span>Example

The following code example elicits this warning.

```
IoSetCancelRoutine(MyStartIo);
```

The following code example avoids this warning.

```
IoSetCancelRoutine(MyCancelRoutine);
```

