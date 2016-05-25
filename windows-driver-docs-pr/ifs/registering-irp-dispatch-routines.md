---
title: Registering IRP Dispatch Routines
author: windows-driver-content
description: Registering IRP Dispatch Routines
ms.assetid: 096f4bb7-2326-4e6c-b3db-a2d95ca4982b
keywords: ["registering IRP dispatch routines", "dispatch routines WDK file system", "IRP dispatch routines WDK file system , registering", "IRPs WDK file system"]
---

# Registering IRP Dispatch Routines


## <span id="ddk_registering_irp_dispatch_routines_if"></span><span id="DDK_REGISTERING_IRP_DISPATCH_ROUTINES_IF"></span>


The *DriverObject* parameter of the filter driver's [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine supplies a pointer to the filter driver's [**driver object**](https://msdn.microsoft.com/library/windows/hardware/ff544174). To register I/O request packet (IRP) dispatch routines, you must store the entry points of these routines into the **MajorFunction** member of the driver object. For example, a hypothetical "MyLegacyFilter" driver can set the entry points for its dispatch routine as follows:

```
for (i = 0; i <= IRP_MJ_MAXIMUM_FUNCTION; i++) {
    DriverObject->MajorFunction[i] = MyLegacyFilterDispatch;
}
DriverObject->MajorFunction[IRP_MJ_CREATE] = MyLegacyFilterCreate;
DriverObject->MajorFunction[IRP_MJ_CLOSE] = MyLegacyFilterClose;
DriverObject->MajorFunction[IRP_MJ_FILE_SYSTEM_CONTROL] = MyLegacyFilterFsControl;
```

Note that the above **FOR** loop assigns a default dispatch routine for all IRP major function codes. This assignment is good practice, because otherwise the I/O Manager completes any unrecognized IRP with STATUS\_INVALID\_DEVICE\_REQUEST by default. File system filter drivers should not reject unfamiliar IRPs in this way, because such requests are usually intended for another driver that is lower in the driver stack. For this reason, the default dispatch routine normally just passes the IRP down to the next-lower-level driver.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Registering%20IRP%20Dispatch%20Routines%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


