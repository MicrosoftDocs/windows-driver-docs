---
title: Returning Status
description: Returning Status
ms.assetid: fd490517-f4c5-4e20-9eac-6a9ac7d04992
keywords: ["status values WDK file system", "success status values WDK file system", "returning status WDK file system"]
---

# Returning Status


## <span id="ddk_returning_status_if"></span><span id="DDK_RETURNING_STATUS_IF"></span>


A file system filter driver's **DriverEntry** routine normally returns STATUS\_SUCCESS. However, if driver initialization fails, the **DriverEntry** routine should return an appropriate error status value.

If the **DriverEntry** routine returns a status value that is not a success status value, the system responds by unloading the driver. For this reason, the **DriverEntry** routine must always free any memory that was allocated for system resources, such as device objects, before returning a status value that is not a success status value.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Returning%20Status%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




