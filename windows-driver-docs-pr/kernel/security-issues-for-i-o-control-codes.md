---
title: Security Issues for I/O Control Codes
author: windows-driver-content
description: Security Issues for I/O Control Codes
MS-HAID:
- 'IRPs\_6d76f5b4-f0df-4199-82f6-193cc959d81c.xml'
- 'kernel.security\_issues\_for\_i\_o\_control\_codes'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: cab8aed2-7185-4622-9a8f-bc8eab3c8c59
keywords: ["I/O control codes WDK kernel , security", "control codes WDK IOCTLs , security", "IOCTLs WDK kernel , security", "security WDK IOCTLs"]
---

# Security Issues for I/O Control Codes


## <a href="" id="ddk-security-issues-for-i-o-control-codes-kg"></a>


Secure processing of IRPs that contain I/O control codes depends on defining IOCTL codes properly and on carefully examining parameters that the driver receives with the IRP.

When defining new IOCTL codes, use the following rules:

-   Always specify a *FunctionCode* value that is equal to or greater than 0x800.

-   Always specify a *RequiredAccess* value. The I/O manager does not send IOCTLs if the caller has insufficient access rights.

-   Do not define IOCTL codes that allow callers to read or write nonspecific areas of kernel memory.

When processing IOCTL codes within a driver, use the following rules:

-   Whenever a driver's dispatch routines test received IOCTL codes, they must always test the entire 32-bit value.

-   Drivers can use [**IoValidateDeviceIoControlAccess**](https://msdn.microsoft.com/library/windows/hardware/ff550418) to dynamically perform stricter access checking than that specified by the *RequiredAccess* value in the definition of the I/O control code.

-   Never read or write more data than the buffer that is pointed to by **Irp-&gt;AssociatedIrp.SystemBuffer** can contain. Therefore, always check **Parameters.DeviceIoControl.InputBufferLength** or **Parameters.DeviceIoControl.OutputBufferLength** in the [**IO\_STACK\_LOCATION**](https://msdn.microsoft.com/library/windows/hardware/ff550659) structure to determine buffer limits.

-   Always zero driver-allocated buffers that will contain data intended for an application that originated an IOCTL request. That way, you will not accidentally copy sensitive data to the application.

-   For METHOD\_IN\_DIRECT and METHOD\_OUT\_DIRECT transfers, follow the rules above. Additionally, check for a **NULL** return value from [**MmGetSystemAddressForMdlSafe**](https://msdn.microsoft.com/library/windows/hardware/ff554559), which indicates that mapping failed or that a zero-length buffer was supplied.

-   For METHOD\_NEITHER transfers, follow the rules that are provided in [Using Neither Buffered Nor Direct I/O](using-neither-buffered-nor-direct-i-o.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Security%20Issues%20for%20I/O%20Control%20Codes%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


