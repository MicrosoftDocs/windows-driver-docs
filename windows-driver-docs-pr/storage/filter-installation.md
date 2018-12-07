---
title: Filter Installation
description: Filter Installation
ms.assetid: 118d9fd9-c499-4371-9084-a4368a78f5e0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Filter Installation


Crash dump filter drivers can be installed in the crash dump stack by adding the service name in the registry key shown in the following code example. When crash dump or hibernation is initialized, the dump drivers are loaded. The filter drivers mentioned in the registry key are loaded at this time.

```cpp
HKLM\SYSTEM\CurrentControlSet\Control\CrashControl

DumpFilters REG_MULTI_SZ DriverName

e.g. dumpfltr.sys
```

 

 




