---
title: Evaluating ACPI Control Methods Synchronously
author: windows-driver-content
description: Evaluating ACPI Control Methods Synchronously
MS-HAID:
- 'acpi-meth-eval-dg\_9b7607f3-1ab5-489a-9fc0-a3f0b68e2bee.xml'
- 'acpi.evaluating\_acpi\_control\_methods\_synchronously'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 3fd8f7bd-bfae-4846-8051-3a0023d565e4
keywords: ["ACPI control methods WDK , evaluating synchronously", "ACPI control methods WDK , input buffer structures", "ACPI control methods WDK , SendDownStreamIrp code sample"]
---

# Evaluating ACPI Control Methods Synchronously


A device driver can use the following device control requests to synchronously evaluate control methods that are defined in the ACPI namespace of a device:

-   [**IOCTL\_ACPI\_EVAL\_METHOD**](https://msdn.microsoft.com/library/windows/hardware/ff536148)

    Starting with Windows 2000, this request evaluates a control method that is an immediate child object in the ACPI namespace of the device to which the request is sent.

-   [**IOCTL\_ACPI\_EVAL\_METHOD\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff536149)

    Starting with Windows Server 2008 and Windows Vista, this request synchronously evaluates a control method that is supported by the device or a descendant child object of the device to which the request is sent.

The [Windows ACPI driver](https://msdn.microsoft.com/library/windows/hardware/ff540493), Acpi.sys, handles these requests on behalf of devices that are specified in the system description tables in the [ACPI BIOS](https://msdn.microsoft.com/library/windows/hardware/ff540487). These requests can be used by kernel-mode device drivers that comply with the requirements of [Kernel-Mode Driver Framework (KMDF)](https://msdn.microsoft.com/library/windows/hardware/dn265580) or [Windows Driver Model (WDM)](https://msdn.microsoft.com/library/windows/hardware/ff565698). Starting with Windows 8, user-mode device drivers that comply with the requirements of [User-Mode Driver Framework (UMDF)](https://msdn.microsoft.com/library/windows/hardware/ff560442) can use these requests.

For example, a WDM driver performs the following sequence of operations to use one of these IOCTLs:

1.  Calls [**IoBuildDeviceIoControlRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548318) to build the request.

2.  Calls [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) to send the request down the device stack.

3.  Waits for the I/O manager to signal the driver that the lower-level drivers have completed the request.

4.  Checks the status of the request.

5.  Checks the validity of the output arguments.

6.  Processes the output arguments that are returned to the driver.

7.  Completes the request.

To build a request, a driver calls **IoBuildDeviceIoControlRequest** and supplies the following parameters:

-   *IoControlCode* is set to **IOCTL\_ACPI\_EVAL\_METHOD** or **IOCTL\_ACPI\_EVAL\_METHOD\_EX**.

-   *DeviceObject* is set to a pointer to the physical device object (PDO) of the device.

-   *InputBuffer* is set to a pointer to an input buffer structure that depends on the type of input arguments to be passed to the control method. The ACPI driver supports methods that take no input arguments, that take a single integer, that take an ASCII string, or that take a custom array of input arguments. For more information about the supported input buffer structures, see [Control Method Input Buffer Structures](control-method-input-buffer-structures.md).

-   *InputBufferLength* is set to the size, in bytes, of the input buffer that is supplied by *InputBuffer*.

-   *OutputBufferLength* supplies the size, in bytes, of the output buffer that is supplied by *OutputBuffer*.

-   *InternalDeviceIoControl* is set to **FALSE**.

-   *Event* is set to a pointer to a caller-allocated and initialized event object. The driver waits until the I/O manager signals this event, which indicates that the lower-level drivers have completed the request.

-   *OutputBuffer* supplies a pointer to an [**ACPI\_EVAL\_OUTPUT\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff536123) structure that contains the output arguments from the control method. Output arguments are specific to a given control method. For a driver to return any output, it must allocate a buffer that is large enough to hold all the output arguments.

-   *IoStatusBlock* is set to an [**IO\_STATUS\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff550671) structure. This returns the status of the request that was set by the lower-level drivers.

For a code example of how to evaluate a control method that does not take input arguments, see [Evaluating a Control Method Without Input Arguments](evaluating-a-control-method-without-input-arguments.md).

For a code example of how to evaluate a control method that takes input arguments, see [Evaluating a Control Method that Takes Input Arguments](evaluating-a-control-method-that-takes-input-arguments.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bacpi\acpi%5D:%20Evaluating%20ACPI%20Control%20Methods%20Synchronously%20%20RELEASE:%20%284/27/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


