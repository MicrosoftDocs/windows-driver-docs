---
title: Avoiding Reboot when Updating a UMDF Driver
author: windows-driver-content
description: Avoiding Reboot when Updating a UMDF Driver
ms.assetid: B5321732-50FD-4719-BBD0-F0A3BE1EE532
---

# Avoiding Reboot when Updating a UMDF Driver


To avoid a required reboot when you update a UMDF driver, specify the **COPYFLG\_IN\_USE\_RENAME** flag in the [**CopyFiles Directive**](https://msdn.microsoft.com/library/windows/hardware/ff546346) in your driver's INF file, as shown in this example:

```
[VirtualSerial_Install.NT]
CopyFiles=UMDriverCopy
 
[UMDriverCopy]
Virtualserial.dll,,,0x00004000  ; COPYFLG_IN_USE_RENAME
```

 

 





