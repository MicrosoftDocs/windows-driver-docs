---
title: Setting the MofImagePath Registry Value
description: Setting the MofImagePath Registry Value
ms.assetid: b8c43cd3-d4f4-4f1e-b692-8005d845d64a
keywords: ["WMI WDK kernel , publishing schema", "publishing WMI schema WDK", "schema publishing WDK WMI", "MOF files WDK WMI", "MofImagePath"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Setting the MofImagePath Registry Value





A driver's schema can be published by including a compiled MOF resource in a separate file, such as a DLL, and setting **MofImagePath** in the registry to the path of that file. A schema published in this way can be updated without recompiling the driver.

To publish a driver's schema in a separate file:

1.  Compile the MOF file as described in [Compiling a Driver's MOF File](compiling-a-driver-s-mof-file.md).

2.  Include the compiled MOF file as a resource in a file such as a DLL.

3.  Add the **MofImagePath** registry value under the driver's Services key. For example, the following shows the registry value for a driver named *DriverName*:

    ```cpp
    HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services
        \DriverName
            MofImagePath    "\SystemRoot\System32\Drivers\DriverNameMof.dll"
    ```

You can set this key in the driver's INF file, as follows:

```cpp
; This is the Services section for the driver
[Driver_service_install_section]
AddReg=Driver_AddReg

; This is the Services AddReg section declared above.
[Driver_AddReg]
HKR,,MofImagePath,,DriverMof.dll 
```

See [**INF DDInstall.Services Section**](https://msdn.microsoft.com/library/windows/hardware/ff547349) and [**INF AddReg Directive**](https://msdn.microsoft.com/library/windows/hardware/ff546320) for details.

 

 




