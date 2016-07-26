---
title: CM\_PROB\_DRIVER\_FAILED\_LOAD
description: CM\_PROB\_DRIVER\_FAILED\_LOAD
ms.assetid: 84d88db9-338b-4318-ba05-696521c96dd6
keywords: ["CM_PROB_DRIVER_FAILED_LOAD"]
---

# CM\_PROB\_DRIVER\_FAILED\_LOAD


## <a href="" id="ddk-cm-prob-driver-failed-load-dg"></a>


The driver could not be loaded.

### Error Code

39

### Display Message (Windows XP and later versions of Windows)

"Windows cannot load the device driver for this hardware. The driver may be corrupted or missing. (Code 39)"

### Recommended Resolution (Windows XP and later versions of Windows)

Reinstall or obtain a new driver.

Reasons for this error include the following:

-   A driver file that is not present, a binary file that is corrupted, a file I/O problem, or a driver that references an entry point in another binary that could not be loaded.

-   Starting with Windows Vista, the driver does not comply with [kernel-mode code signing policy](kernel-mode-code-signing-policy--windows-vista-and-later-.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20CM_PROB_DRIVER_FAILED_LOAD%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




