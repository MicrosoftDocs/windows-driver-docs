---
title: C28128
description: Warning C28128 An access to a field has been made directly. It should be made by a routine.
ms.assetid: 66b3345b-fab8-4f1a-b7ab-dfc5e70ca312
keywords:
- warnings listed WDK PREfast for Drivers
- errors listed WDK PREfast for Drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# C28128


warning C28128: An access to a field has been made directly. It should be made by a routine.

The driver directly accessed a structure member that should be accessed only by using specialized functions.

For example, you should use the [**IoSetCancelRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff549674) instead of directly modifying the **CancelRoutine** member of the [**IRP**](https://msdn.microsoft.com/library/windows/hardware/ff550694) structure.

### <span id="example"></span><span id="EXAMPLE"></span>Example

The following code example elicits this warning.

```
irp->CancelRoutine = myCancelRoutine;
```

The following code example avoids this warning.

```
oldCancel = IoSetCancelRoutine(irp, myCancelRoutine);
```

 

 





