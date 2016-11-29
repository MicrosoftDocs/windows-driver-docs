---
title: DO\_DEVICE\_INITIALIZING Annotation for drivers
description: .
ms.assetid: EFC5F0A3-7B20-49A5-9D50-1737DF76DC9E
---

# DO\_DEVICE\_INITIALIZING Annotation for drivers


Use the \_Kernel\_clear\_do\_init\_ annotation to specify whether the annotated function is expected to clear the DO\_DEVICE\_INITIALIZING bit in the Flags field of the device object.

This annotation has the following syntax:

``` syntax
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20DO_DEVICE_INITIALIZING%20Annotation%20for%20drivers%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





