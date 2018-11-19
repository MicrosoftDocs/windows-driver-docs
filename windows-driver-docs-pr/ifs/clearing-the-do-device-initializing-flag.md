---
title: Clearing the DO_DEVICE_INITIALIZING Flag
description: Clearing the DO_DEVICE_INITIALIZING Flag
ms.assetid: 1c1cca60-bb95-4a8d-9e17-4db54983bbb0
keywords:
- filter drivers WDK file system , attaching filters
- file system filter drivers WDK , attaching filters
- attaching filters to file system or volume
- volumes WDK file system , attaching filters
- DO_DEVICE_INITIALIZING
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Clearing the DO\_DEVICE\_INITIALIZING Flag


## <span id="ddk_clearing_the_do_device_initializing_flag_if"></span><span id="DDK_CLEARING_THE_DO_DEVICE_INITIALIZING_FLAG_IF"></span>


After attaching a filter device object to a file system or volume, always be sure to clear the DO\_DEVICE\_INITIALIZING flag on the filter device object. (For more information about this flag, see [**DEVICE\_OBJECT**](https://msdn.microsoft.com/library/windows/hardware/ff543147) in the Kernel Reference.) This can be done as follows using the **ClearFlag** macro defined in *ntifs.h*:

```cpp
ClearFlag(NewDeviceObject->Flags, DO_DEVICE_INITIALIZING);
```

When the filter device object is created, [**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397) sets the DO\_DEVICE\_INITIALIZING flag on the device object. After the filter is successfully attached, this flag must be cleared. Note that if this flag is not cleared, no more filter drivers can attach to the filter chain because the call to [**IoAttachDeviceToDeviceStackSafe**](https://msdn.microsoft.com/library/windows/hardware/ff548236) will fail.

**Note**   It is not necessary to clear the DO\_DEVICE\_INITIALIZING flag on device objects that are created in DriverEntry, because this is done automatically by the I/O Manager. However, your driver should clear this flag on all other device objects that it creates.

 

 

 




