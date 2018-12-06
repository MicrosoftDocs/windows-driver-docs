---
title: Propagating the DO_BUFFERED_IO and DO_DIRECT_IO Flags
description: Propagating the DO_BUFFERED_IO and DO_DIRECT_IO Flags
ms.assetid: a0cb4f1a-3c27-4608-a208-ffcf4113b722
keywords:
- filter drivers WDK file system , attaching filters
- file system filter drivers WDK , attaching filters
- attaching filters to file system or volume
- volumes WDK file system , attaching filters
- DO_BUFFERED_IO
- propagating DO_BUFFERED_IO flag
- DO_DIRECT_IO
- propagating DO_DIRECT_IO flag
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Propagating the DO\_BUFFERED\_IO and DO\_DIRECT\_IO Flags


## <span id="ddk_propagating_the_do_buffered_io_and_do_direct_io_flags_if"></span><span id="DDK_PROPAGATING_THE_DO_BUFFERED_IO_AND_DO_DIRECT_IO_FLAGS_IF"></span>


After attaching a filter device object to a file system or volume, always be sure to set or clear the DO\_BUFFERED\_IO and DO\_DIRECT\_IO flags as needed so that they match the values of the next-lower device object on the driver stack. (For more information about these flags, see [Methods for Accessing Data Buffers](https://msdn.microsoft.com/library/windows/hardware/ff554436).) An example of this follows:

```cpp
if (FlagOn( DeviceObject->Flags, DO_BUFFERED_IO )) {
    SetFlag( myLegacyFilterDeviceObject->Flags, DO_BUFFERED_IO );
}
if (FlagOn( DeviceObject->Flags, DO_DIRECT_IO )) {
    SetFlag(myLegacyFilterDeviceObject->Flags, DO_DIRECT_IO );
}
```

In the above code snippet, *DeviceObject* is a pointer to the device object to which the filter device object has just been attached; myLegacyFilter *DeviceObject* is a pointer to the filter device object itself.

 

 




