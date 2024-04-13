---
title: Security Issues for I/O Control Codes
description: Security Issues for I/O Control Codes
keywords: ["I/O control codes WDK kernel , security", "control codes WDK IOCTLs , security", "IOCTLs WDK kernel , security", "security WDK IOCTLs"]
ms.date: 06/16/2017
---

# Security Issues for I/O Control Codes





Secure processing of IRPs that contain I/O control codes depends on defining IOCTL codes properly and on carefully examining parameters that the driver receives with the IRP.

When defining new IOCTL codes, use the following rules:

-   Always specify a *FunctionCode* value that is equal to or greater than 0x800.

-   Always specify a *RequiredAccess* value. The I/O manager does not send IOCTLs if the caller has insufficient access rights.

-   Do not define IOCTL codes that allow callers to read or write nonspecific areas of kernel memory.

When processing IOCTL codes within a driver, use the following rules:

-   Whenever a driver's dispatch routines test received IOCTL codes, they must always test the entire 32-bit value.

-   Drivers can use [**IoValidateDeviceIoControlAccess**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iovalidatedeviceiocontrolaccess) to dynamically perform stricter access checking than that specified by the *RequiredAccess* value in the definition of the I/O control code.

-   Never read or write more data than the buffer that is pointed to by **Irp-&gt;AssociatedIrp.SystemBuffer** can contain. Therefore, always check **Parameters.DeviceIoControl.InputBufferLength** or **Parameters.DeviceIoControl.OutputBufferLength** in the [**IO\_STACK\_LOCATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location) structure to determine buffer limits.

-   Always zero driver-allocated buffers that will contain data intended for an application that originated an IOCTL request. That way, you will not accidentally copy sensitive data to the application.

-   For METHOD\_IN\_DIRECT and METHOD\_OUT\_DIRECT transfers, follow the rules above. Additionally, check for a **NULL** return value from [**MmGetSystemAddressForMdlSafe**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmgetsystemaddressformdlsafe), which indicates that mapping failed or that a zero-length buffer was supplied.

-   For METHOD\_NEITHER transfers, follow the rules that are provided in [Using Neither Buffered Nor Direct I/O](using-neither-buffered-nor-direct-i-o.md).

 

