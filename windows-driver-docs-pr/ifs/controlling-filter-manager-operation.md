---
title: Controlling Filter Manager Operation
description: Controlling Filter Manager Operation
ms.assetid: 884e6a15-5bfa-41bf-b759-af6e43078fad
keywords:
- filter manager WDK file system minifilter , controlling operation
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Controlling Filter Manager Operation


The operation of filter manager on versions of Windows earlier than Windows Vista is controlled by the REG\_DWORD *AttachWhenLoaded* registry value stored under the following key:

```cpp
HKLM\System\CurrentControlSet\Services\FltMgr
```

When *AttachWhenLoaded* is set to zero, the filter manager does not attach to any volumes until a minifilter driver registers with the filter manager. When *AttachWhenLoaded* is set to 1, the filter manager attaches at boot time to all volumes.

The default value for *AttachWhenLoaded* is zero with Windows XP with Service Pack 2 (SP2) and later.

The default value for *AttachWhenLoaded* is 1 on Windows Server 2003 with Service Pack 1 (SP1) and later versions.

The *AttachWhenLoaded* registry value does not exist on Windows Vista and only applies to previous versions of Windows.

When a minifilter driver is installed on Windows prior to Windows Vista, the software installer should set *AttachWhenLoaded* to 1 if this registry value is not currently set to 1. If the previous value of *AttachWhenLoaded* was zero, the installer should reboot the system after the installation of the minifilter driver.

 

 




