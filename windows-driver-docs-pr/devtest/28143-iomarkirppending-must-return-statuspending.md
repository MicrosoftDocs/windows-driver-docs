---
title: C28143
description: Warning C28143 A dispatch routine that calls IoMarkIrpPending must also return STATUS_PENDING.
ms.assetid: 3b9e6c4f-73d1-4abc-9495-85bb56e2532b
keywords:
- warnings listed WDK PREfast for Drivers
- errors listed WDK PREfast for Drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# C28143


warning C28143: A dispatch routine that calls IoMarkIrpPending must also return STATUS\_PENDING

A dispatch routine that calls [**IoMarkIrpPending**](https://msdn.microsoft.com/library/windows/hardware/ff549422) includes at least one path in which the driver returns a value other than STATUS\_PENDING.

### <span id="example"></span><span id="EXAMPLE"></span>Example

The following code example elicits this warning.

```
IoMarkIrpPending(Irp);
...
return STATUS_SUCCESS;
```

The following code example avoids this warning.

```
IoMarkIrpPending(Irp);
...
return STATUS_PENDING;
```

 

 





