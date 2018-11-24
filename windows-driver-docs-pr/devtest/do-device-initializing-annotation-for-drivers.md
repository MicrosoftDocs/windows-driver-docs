---
title: DO_DEVICE_INITIALIZING Annotation for drivers
description: Use to specify whether the annotated function is expected to clear the DO_DEVICE_INITIALIZING bit in the Flags field of the device object.
ms.assetid: EFC5F0A3-7B20-49A5-9D50-1737DF76DC9E
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DO\_DEVICE\_INITIALIZING Annotation for drivers


Use the \_Kernel\_clear\_do\_init\_ annotation to specify whether the annotated function is expected to clear the DO\_DEVICE\_INITIALIZING bit in the Flags field of the device object.

This annotation has the following syntax:

```
_Kernel_clear_do_init_(yes|no)
```

Calling a function that is annotated with \_Kernel\_clear\_do\_init\_(yes) exempts the calling function from having to clear the DO\_DEVICE\_INITIALIZING bit.

The annotation should almost always be used in a conditional context when the function returns success, unless the annotation is applied to a function type definition. For example, in the following function type definition for the DRIVER\_ADD\_DEVICE function class, the annotations specify that the function cannot raise the IRQL and that the function is expected to clear the DO\_DEVICE\_INITIALIZING bit.

```
typedef
_IRQL_always_function_max_(PASSIVE_LEVEL)
_IRQL_requires_same_
_Kernel_clear_do_init_(yes)
__drv_functionClass(DRIVER_ADD_DEVICE)
NTSTATUS
DRIVER_ADD_DEVICE (
    _In_ struct _DRIVER_OBJECT *DriverObject,
    _In_ struct _DEVICE_OBJECT *PhysicalDeviceObject
    );
typedef DRIVER_ADD_DEVICE *PDRIVER_ADD_DEVICE;
```

## <span id="related_topics"></span>Related topics


[SAL 2.0 Annotations for Windows Drivers](sal-2-annotations-for-windows-drivers.md)










