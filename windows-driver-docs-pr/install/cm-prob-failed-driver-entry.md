---
title: CM\_PROB\_FAILED\_DRIVER\_ENTRY
description: CM\_PROB\_FAILED\_DRIVER\_ENTRY
ms.assetid: e1345892-69db-4135-be5b-1d182a2a1d66
keywords: ["CM_PROB_FAILED_DRIVER_ENTRY"]
---

# CM\_PROB\_FAILED\_DRIVER\_ENTRY


## <a href="" id="ddk-cm-prob-failed-driver-entry-dg"></a>


The driver returned failure from its **DriverEntry** routine.

### Error Code

37

### Display Message (Windows XP and later versions of Windows)

"Windows cannot initialize the device driver for this hardware. (Code 37)"

### Recommended Resolution (Windows XP and later versions of Windows)

Reinstall or obtain a new driver.

**Note**  If the **DriverEntry** routine returns STATUS\_INSUFFICIENT\_RESOURCES, Device Manager reports the [CM\_PROB\_OUT\_OF\_MEMORY](cm-prob-out-of-memory.md) error code.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20CM_PROB_FAILED_DRIVER_ENTRY%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




