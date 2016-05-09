---
title: Propagating the FILE\_DEVICE\_SECURE\_OPEN Flag
description: Propagating the FILE\_DEVICE\_SECURE\_OPEN Flag
ms.assetid: cbc254ab-3ac6-44aa-bb16-16d701d5ada7
keywords: ["filter drivers WDK file system , attaching filters", "file system filter drivers WDK , attaching filters", "attaching filters to file system or volume", "volumes WDK file system , attaching filters", "FILE_DEVICE_SECURE_OPEN", "propagating FILE_DEVICE_SECURE_OPEN flag"]
---

# Propagating the FILE\_DEVICE\_SECURE\_OPEN Flag


## <span id="ddk_clearing_the_do_device_initializing_flag_if"></span><span id="DDK_CLEARING_THE_DO_DEVICE_INITIALIZING_FLAG_IF"></span>


After attaching a filter device object to a file system (but not to a volume), always be sure to set the FILE\_DEVICE\_SECURE\_OPEN flag on the filter device object as needed to so that it matches the value of the next-lower device object on the driver stack. (For more information about this flag, see [Specifying Device Characteristics](https://msdn.microsoft.com/library/windows/hardware/ff563818) in the Kernel Architecture Design Guide and [**DEVICE\_OBJECT**](https://msdn.microsoft.com/library/windows/hardware/ff543147) in the Kernel Reference.) An example of this follows:

```
if (FlagOn( DeviceObject->Characteristics, FILE_DEVICE_SECURE_OPEN )) {
    SetFlag(myLegacyFilterDeviceObject->Characteristics, FILE_DEVICE_SECURE_OPEN );
}
```

In the above code snippet, *DeviceObject* is a pointer to the device object to which the filter device object has just been attached; myLegacyFilter *DeviceObject* is a pointer to the filter device object itself.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Propagating%20the%20FILE_DEVICE_SECURE_OPEN%20Flag%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




