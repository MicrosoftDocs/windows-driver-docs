---
title: C28128
description: Warning C28128 An access to a field has been made directly. It should be made by a routine.
keywords:
- warnings listed WDK PREfast for Drivers
- errors listed WDK PREfast for Drivers
ms.date: 04/20/2017
ms.localizationpriority: medium 
f1_keywords: 
  - "C28128"
---

# C28128


warning C28128: An access to a field has been made directly. It should be made by a routine.

The driver directly accessed a structure member that should be accessed only by using specialized functions.

For example, you should use the [**IoSetCancelRoutine**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iosetcancelroutine) instead of directly modifying the **CancelRoutine** member of the [**IRP**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_irp) structure.

### <span id="example"></span><span id="EXAMPLE"></span>Example

The following code example elicits this warning.

```
irp->CancelRoutine = myCancelRoutine;
```

The following code example avoids this warning.

```
oldCancel = IoSetCancelRoutine(irp, myCancelRoutine);
```

 

