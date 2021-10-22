---
title: C28143 warning
description: Warning C28143 A dispatch routine that calls IoMarkIrpPending must also return STATUS_PENDING.
keywords:
- warnings listed WDK PREfast for Drivers
- errors listed WDK PREfast for Drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
f1_keywords: 
  - "C28143"
---

# C28143


warning C28143: A dispatch routine that calls IoMarkIrpPending must also return STATUS\_PENDING

A dispatch routine that calls [**IoMarkIrpPending**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iomarkirppending) includes at least one path in which the driver returns a value other than STATUS\_PENDING.

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

 

