---
title: IRP-Based IOCTL and FSCTL Operations
description: IRP-Based IOCTL and FSCTL Operations
ms.assetid: 08d6cf89-aaba-4aa1-baff-eb6aece2875f
keywords:
- IOCTLs WDK file systems
- FSCTL WDK file system
- no buffers WDK file system
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# IRP-Based IOCTL and FSCTL Operations


## <span id="ddk_irp_based_ioctl_and_fsctl_operations_if"></span><span id="DDK_IRP_BASED_IOCTL_AND_FSCTL_OPERATIONS_IF"></span>


The following IRP-based I/O operations use the buffering method that matches the transfer type that is specified in the definition of the I/O control code (IOCTL) or file system control code (FSCTL):

-   IRP\_MJ\_DEVICE\_CONTROL

-   IRP\_MJ\_FILE\_SYSTEM\_CONTROL

-   IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL

The transfer type is specified in the *TransferType* parameter of the CTL\_CODE macro. To obtain the transfer type for a given IOCTL or FSCTL, use the following macro:

```cpp
#define METHOD_FROM_CTL_CODE(ctrlCode)         ((ULONG)(ctrlCode & 3))
```

This macro returns one of the following values:

```cpp
#define METHOD_BUFFERED                 0
#define METHOD_IN_DIRECT                1
#define METHOD_OUT_DIRECT               2
#define METHOD_NEITHER                  3
```

For more information about the CTL\_CODE macro, see [Defining I/O Control Codes](https://msdn.microsoft.com/library/windows/hardware/ff543023).

Note that IRP\_MJ\_DEVICE\_CONTROL can also be a fast I/O operation. When it is a fast I/O operation, it always uses neither buffered nor direct I/O, regardless of the IOCTL's transfer type. For more information about when IRP\_MJ\_DEVICE\_CONTROL can be a fast I/O operation, see [Operations That Can Be IRP-Based or Fast I/O](operations-that-can-be-irp-based-or-fast-i-o.md).

 

 




