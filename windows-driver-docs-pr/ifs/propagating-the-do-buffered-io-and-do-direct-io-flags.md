---
title: Propagating the DO\_BUFFERED\_IO and DO\_DIRECT\_IO Flags
author: windows-driver-content
description: Propagating the DO\_BUFFERED\_IO and DO\_DIRECT\_IO Flags
ms.assetid: a0cb4f1a-3c27-4608-a208-ffcf4113b722
keywords: ["filter drivers WDK file system , attaching filters", "file system filter drivers WDK , attaching filters", "attaching filters to file system or volume", "volumes WDK file system , attaching filters", "DO_BUFFERED_IO", "propagating DO_BUFFERED_IO flag", "DO_DIRECT_IO", "propagating DO_DIRECT_IO flag"]
---

# Propagating the DO\_BUFFERED\_IO and DO\_DIRECT\_IO Flags


## <span id="ddk_propagating_the_do_buffered_io_and_do_direct_io_flags_if"></span><span id="DDK_PROPAGATING_THE_DO_BUFFERED_IO_AND_DO_DIRECT_IO_FLAGS_IF"></span>


After attaching a filter device object to a file system or volume, always be sure to set or clear the DO\_BUFFERED\_IO and DO\_DIRECT\_IO flags as needed so that they match the values of the next-lower device object on the driver stack. (For more information about these flags, see [Methods for Accessing Data Buffers](https://msdn.microsoft.com/library/windows/hardware/ff554436).) An example of this follows:

```
if (FlagOn( DeviceObject->Flags, DO_BUFFERED_IO )) {
    SetFlag( myLegacyFilterDeviceObject->Flags, DO_BUFFERED_IO );
}
if (FlagOn( DeviceObject->Flags, DO_DIRECT_IO )) {
    SetFlag(myLegacyFilterDeviceObject->Flags, DO_DIRECT_IO );
}
```

In the above code snippet, *DeviceObject* is a pointer to the device object to which the filter device object has just been attached; myLegacyFilter *DeviceObject* is a pointer to the filter device object itself.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Propagating%20the%20DO_BUFFERED_IO%20and%20DO_DIRECT_IO%20Flags%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


