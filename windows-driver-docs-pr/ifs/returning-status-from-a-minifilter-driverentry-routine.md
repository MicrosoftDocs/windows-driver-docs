---
title: Returning Status from a Minifilter DriverEntry Routine
author: windows-driver-content
description: Returning Status from a Minifilter DriverEntry Routine
ms.assetid: a9448908-f712-43f7-99c0-e02abc1678ed
keywords: ["status values WDK file system", "returning status WDK file system"]
---

# Returning Status from a Minifilter DriverEntry Routine


## <span id="ddk_returning_status_from_a_minifilter_driverentry_routine_if"></span><span id="DDK_RETURNING_STATUS_FROM_A_MINIFILTER_DRIVERENTRY_ROUTINE_IF"></span>


A minifilter driver's **DriverEntry** routine normally returns STATUS\_SUCCESS. But if minifilter initialization fails, the **DriverEntry** routine should return an appropriate error NTSTATUS value.

If the **DriverEntry** routine returns a status value that is not a success NTSTATUS value, the system responds by unloading the minifilter driver. The minifilter driver's [**FilterUnloadCallback**](https://msdn.microsoft.com/library/windows/hardware/ff551085) routine is not called. For this reason, the **DriverEntry** routine must free any memory that was allocated for system resources before returning a status value that is not a success NTSTATUS value.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Returning%20Status%20from%20a%20Minifilter%20DriverEntry%20Routine%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


