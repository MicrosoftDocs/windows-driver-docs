---
title: IRP-Based IOCTL and FSCTL Operations
description: IRP-Based IOCTL and FSCTL Operations
ms.assetid: 08d6cf89-aaba-4aa1-baff-eb6aece2875f
keywords: ["IOCTLs WDK file systems", "FSCTL WDK file system", "no buffers WDK file system"]
---

# IRP-Based IOCTL and FSCTL Operations


## <span id="ddk_irp_based_ioctl_and_fsctl_operations_if"></span><span id="DDK_IRP_BASED_IOCTL_AND_FSCTL_OPERATIONS_IF"></span>


The following IRP-based I/O operations use the buffering method that matches the transfer type that is specified in the definition of the I/O control code (IOCTL) or file system control code (FSCTL):

-   IRP\_MJ\_DEVICE\_CONTROL

-   IRP\_MJ\_FILE\_SYSTEM\_CONTROL

-   IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL

The transfer type is specified in the *TransferType* parameter of the CTL\_CODE macro. To obtain the transfer type for a given IOCTL or FSCTL, use the following macro:

```
#define METHOD_FROM_CTL_CODE(ctrlCode)         ((ULONG)(ctrlCode &amp; 3))
```

This macro returns one of the following values:

```
#define METHOD_BUFFERED                 0
#define METHOD_IN_DIRECT                1
#define METHOD_OUT_DIRECT               2
#define METHOD_NEITHER                  3
```

For more information about the CTL\_CODE macro, see [Defining I/O Control Codes](https://msdn.microsoft.com/library/windows/hardware/ff543023).

Note that IRP\_MJ\_DEVICE\_CONTROL can also be a fast I/O operation. When it is a fast I/O operation, it always uses neither buffered nor direct I/O, regardless of the IOCTL's transfer type. For more information about when IRP\_MJ\_DEVICE\_CONTROL can be a fast I/O operation, see [Operations That Can Be IRP-Based or Fast I/O](operations-that-can-be-irp-based-or-fast-i-o.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20IRP-Based%20IOCTL%20and%20FSCTL%20Operations%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




