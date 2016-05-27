---
title: Clearing the DO\_DEVICE\_INITIALIZING Flag
author: windows-driver-content
description: Clearing the DO\_DEVICE\_INITIALIZING Flag
ms.assetid: 1c1cca60-bb95-4a8d-9e17-4db54983bbb0
keywords: ["filter drivers WDK file system , attaching filters", "file system filter drivers WDK , attaching filters", "attaching filters to file system or volume", "volumes WDK file system , attaching filters", "DO_DEVICE_INITIALIZING"]
---

# Clearing the DO\_DEVICE\_INITIALIZING Flag


## <span id="ddk_clearing_the_do_device_initializing_flag_if"></span><span id="DDK_CLEARING_THE_DO_DEVICE_INITIALIZING_FLAG_IF"></span>


After attaching a filter device object to a file system or volume, always be sure to clear the DO\_DEVICE\_INITIALIZING flag on the filter device object. (For more information about this flag, see [**DEVICE\_OBJECT**](https://msdn.microsoft.com/library/windows/hardware/ff543147) in the Kernel Reference.) This can be done as follows using the **ClearFlag** macro defined in *ntifs.h*:

```
ClearFlag(NewDeviceObject->Flags, DO_DEVICE_INITIALIZING);
```

When the filter device object is created, [**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397) sets the DO\_DEVICE\_INITIALIZING flag on the device object. After the filter is successfully attached, this flag must be cleared. Note that if this flag is not cleared, no more filter drivers can attach to the filter chain because the call to [**IoAttachDeviceToDeviceStackSafe**](https://msdn.microsoft.com/library/windows/hardware/ff548236) will fail.

**Note**   It is not necessary to clear the DO\_DEVICE\_INITIALIZING flag on device objects that are created in DriverEntry, because this is done automatically by the I/O Manager. However, your driver should clear this flag on all other device objects that it creates.

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Clearing%20the%20DO_DEVICE_INITIALIZING%20Flag%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


