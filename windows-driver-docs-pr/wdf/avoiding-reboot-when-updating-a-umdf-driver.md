---
title: Avoiding Reboot when Updating a UMDF Driver
description: Avoiding Reboot when Updating a UMDF Driver
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Avoiding Reboot when Updating a UMDF Driver


To avoid a required reboot when you update a UMDF driver, specify the **COPYFLG\_IN\_USE\_RENAME** flag in the [**CopyFiles Directive**](../install/inf-copyfiles-directive.md) in your driver's INF file, as shown in this example:

```cpp
[VirtualSerial_Install.NT]
CopyFiles=UMDriverCopy
 
[UMDriverCopy]
Virtualserial.dll,,,0x00004000  ; COPYFLG_IN_USE_RENAME
```

 

