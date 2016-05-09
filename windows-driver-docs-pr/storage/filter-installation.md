---
title: Filter Installation
author: windows-driver-content
description: Filter Installation
ms.assetid: 118d9fd9-c499-4371-9084-a4368a78f5e0
---

# Filter Installation


Crash dump filter drivers can be installed in the crash dump stack by adding the service name in the registry key shown in the following code example. When crash dump or hibernation is initialized, the dump drivers are loaded. The filter drivers mentioned in the registry key are loaded at this time.

```
HKLM\SYSTEM\CurrentControlSet\Control\CrashControl

DumpFilters REG_MULTI_SZ DriverName

e.g. dumpfltr.sys
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Filter%20Installation%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


