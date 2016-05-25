---
title: Controlling Filter Manager Operation
author: windows-driver-content
description: Controlling Filter Manager Operation
ms.assetid: 884e6a15-5bfa-41bf-b759-af6e43078fad
keywords: ["filter manager WDK file system minifilter , controlling operation"]
---

# Controlling Filter Manager Operation


The operation of filter manager on versions of Windows earlier than Windows Vista is controlled by the REG\_DWORD *AttachWhenLoaded* registry value stored under the following key:

```
HKLM\System\CurrentControlSet\Services\FltMgr
```

When *AttachWhenLoaded* is set to zero, the filter manager does not attach to any volumes until a minifilter driver registers with the filter manager. When *AttachWhenLoaded* is set to 1, the filter manager attaches at boot time to all volumes.

The default value for *AttachWhenLoaded* is zero with Windows XP with Service Pack 2 (SP2) and later.

The default value for *AttachWhenLoaded* is 1 on Windows Server 2003 with Service Pack 1 (SP1) and later versions.

The *AttachWhenLoaded* registry value does not exist on Windows Vista and only applies to previous versions of Windows.

When a minifilter driver is installed on Windows prior to Windows Vista, the software installer should set *AttachWhenLoaded* to 1 if this registry value is not currently set to 1. If the previous value of *AttachWhenLoaded* was zero, the installer should reboot the system after the installation of the minifilter driver.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Controlling%20Filter%20Manager%20Operation%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


