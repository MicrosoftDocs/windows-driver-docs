---
title: C28165
description: Warning C28165 The function pointer of class does not match the function class.
ms.assetid: 0fc2b542-058c-4e98-b08e-2661c65e2dd0
keywords:
- warnings listed WDK PREfast for Drivers
- errors listed WDK PREfast for Drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





