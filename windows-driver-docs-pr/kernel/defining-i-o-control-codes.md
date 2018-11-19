---
title: Defining I/O Control Codes
description: Defining I/O Control Codes
ms.assetid: 967b0199-e9a0-4c8d-9130-c81436c59ca3
keywords: ["I/O control codes WDK kernel , defining", "control codes WDK IOCTLs , defining", "IOCTLs WDK kernel , defining", "CTL_CODE macro", "IOCTLs WDK user-mode", "user-mode components WDK IOCTLs", "I/O control codes WDK user-mode", "control codes WDK user-mode", "layouts WDK IOCTLs"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Defining I/O Control Codes





When defining new IOCTLs, it is important to remember the following rules:

-   If a new IOCTL will be available to user-mode software components, the IOCTL must be used with [**IRP\_MJ\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550744) requests. User-mode components send **IRP\_MJ\_DEVICE\_CONTROL** requests by calling the [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216), which is a Win32 function.
-   If a new IOCTL will be available only to kernel-mode driver components, the IOCTL must be used with [**IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550766) requests. Kernel-mode components create **IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL** requests by calling **IoBuildDeviceIoControlRequest**. For more information, see [Creating IOCTL Requests in Drivers](creating-ioctl-requests-in-drivers.md).

An I/O control code is a 32-bit value that consists of several fields. The following figure illustrates the layout of I/O control codes.

![diagram illustrating the i/o control code layout](images/ioctl-1.png)

Use the system-supplied **CTL\_CODE** macro, which is defined in Wdm.h and Ntddk.h, to define new I/O control codes. The definition of a new IOCTL code, whether intended for use with **IRP\_MJ\_DEVICE\_CONTROL** or **IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL** requests, uses the following format:

```cpp
#define IOCTL_Device_Function CTL_CODE(DeviceType, Function, Method, Access)
```

Choose a descriptive constant name for the IOCTL, of the form IOCTL\_*Device*\_*Function*, where *Device* indicates the type of device and *Function* indicates the operation. An example constant name is IOCTL\_VIDEO\_ENABLE\_CURSOR.

Supply the following parameters to the **CTL\_CODE** macro:

<a href="" id="devicetype"></a>*DeviceType*  
Identifies the device type. This value must match the value that is set in the **DeviceType** member of the driver's [**DEVICE\_OBJECT**](https://msdn.microsoft.com/library/windows/hardware/ff543147) structure. (See [Specifying Device Types](specifying-device-types.md)). Values of less than 0x8000 are reserved for Microsoft. Values of 0x8000 and higher can be used by vendors. Note that the vendor-assigned values set the **Common** bit.

<a href="" id="functioncode"></a>*FunctionCode*  
Identifies the function to be performed by the driver. Values of less than 0x800 are reserved for Microsoft. Values of 0x800 and higher can be used by vendors. Note that the vendor-assigned values set the **Custom** bit.

<a href="" id="transfertype"></a>*TransferType*  
Indicates how the system will pass data between the caller of [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) (or [**IoBuildDeviceIoControlRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548318)) and the driver that handles the IRP.

Use one of the following system-defined constants:

<a href="" id="method-buffered"></a>METHOD\_BUFFERED  
Specifies the [buffered I/O](methods-for-accessing-data-buffers.md) method, which is typically used for transferring small amounts of data per request. Most I/O control codes for device and intermediate drivers use this *TransferType* value.

For information about how the system specifies data buffers for METHOD\_BUFFERED I/O control codes, see [Buffer Descriptions for I/O Control Codes](buffer-descriptions-for-i-o-control-codes.md).

For more information about buffered I/O, see [Using Buffered I/O](using-buffered-i-o.md).

<a href="" id="method-in-direct-or-method-out-direct"></a>METHOD\_IN\_DIRECT or METHOD\_OUT\_DIRECT  
Specifies the [direct I/O](methods-for-accessing-data-buffers.md) method, which is typically used for reading or writing large amounts of data, using DMA or PIO, that must be transferred quickly.

Specify METHOD\_IN\_DIRECT if the caller of [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) or **IoBuildDeviceIoControlRequest** will pass data to the driver.

Specify METHOD\_OUT\_DIRECT if the caller of [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) or **IoBuildDeviceIoControlRequest** will receive data from the driver.

For information about how the system specifies data buffers for METHOD\_IN\_DIRECT and METHOD\_OUT\_DIRECT I/O control codes, see [Buffer Descriptions for I/O Control Codes](buffer-descriptions-for-i-o-control-codes.md).

For more information about direct I/O, see [Using Direct I/O](using-direct-i-o.md).

<a href="" id="method-neither"></a>METHOD\_NEITHER  
Specifies [neither buffered nor direct I/O](using-neither-buffered-nor-direct-i-o.md). The I/O manager does not provide any system buffers or MDLs. The IRP supplies the user-mode virtual addresses of the input and output buffers that were specified to [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) or **IoBuildDeviceIoControlRequest**, without validating or mapping them.

For information about how the system specifies data buffers for METHOD\_NEITHER I/O control codes, see [Buffer Descriptions for I/O Control Codes](buffer-descriptions-for-i-o-control-codes.md).

This method can be used only if the driver can be guaranteed to be running in the context of the thread that originated the I/O control request. Only a highest-level kernel-mode driver is guaranteed to meet this condition, so METHOD\_NEITHER is seldom used for the I/O control codes that are passed to low-level device drivers.

With this method, the highest-level driver must determine whether to set up buffered or direct access to user data on receipt of the request, possibly must lock down the user buffer, and must wrap its access to the user buffer in a structured exception handler (see [Handling Exceptions](handling-exceptions.md)). Otherwise, the originating user-mode caller might change the buffered data before the driver can use it, or the caller could be swapped out just as the driver is accessing the user buffer.

For more information, see [Using Neither Buffered Nor Direct I/O](using-neither-buffered-nor-direct-i-o.md).

<a href="" id="requiredaccess"></a>*RequiredAccess*  
Indicates the type of access that a caller must request when opening the file object that represents the device (see [**IRP\_MJ\_CREATE**](https://msdn.microsoft.com/library/windows/hardware/ff550729)). The I/O manager will create IRPs and call the driver with a particular I/O control code only if the caller has requested the specified access rights. *RequiredAccess* is specified by using the following system-defined constants:

<a href="" id="file-any-access"></a>FILE\_ANY\_ACCESS  
The I/O manager sends the IRP for any caller that has a handle to the file object that represents the target device object.

<a href="" id="file-read-data"></a>FILE\_READ\_DATA  
The I/O manager sends the IRP only for a caller with read access rights, allowing the underlying device driver to transfer data from the device to system memory.

<a href="" id="file-write-data"></a>FILE\_WRITE\_DATA  
The I/O manager sends the IRP only for a caller with write access rights, allowing the underlying device driver to transfer data from system memory to its device.

FILE\_READ\_DATA and FILE\_WRITE\_DATA can be ORed together if the caller must have both read and write access rights.

Some system-defined I/O control codes have a *RequiredAccess* value of FILE\_ANY\_ACCESS, which allows the caller to send the particular IOCTL regardless of the access granted to the device. Examples include I/O control codes that are sent to drivers of [*exclusive devices*](https://msdn.microsoft.com/library/windows/hardware/ff556279#wdkgloss-exclusive-device).

Other system-defined I/O control codes require the caller to have read access rights, write access rights, or both. For example, the following definition of the public I/O control code IOCTL\_DISK\_SET\_PARTITION\_INFO shows that this I/O request can be sent to a driver only if the caller has both read and write access rights:

```cpp
#define IOCTL_DISK_SET_PARTITION_INFO\
        CTL_CODE(IOCTL_DISK_BASE, 0x008, METHOD_BUFFERED,\
        FILE_READ_DATA | FILE_WRITE_DATA)
```

**Note**   Before specifying FILE\_ANY\_ACCESS for a new IOCTL code, you must be absolutely certain that allowing unrestricted access to your device does not create a possible path for malicious users to compromise the system.

 

Drivers can use [**IoValidateDeviceIoControlAccess**](https://msdn.microsoft.com/library/windows/hardware/ff550418) to perform stricter access checking than that provided by an IOCTL's *RequiredAccess* bits.

## Other useful macros


The following macros are useful for extracting the 16-bit *DeviceType* and 2-bit *TransferType* fields from an IOCTL code:

```cpp
#define DEVICE_TYPE_FROM_CTL_CODE(ctrlCode)   (((ULONG)(ctrlCode & 0xffff0000)) >> 16)
#define METHOD_FROM_CTL_CODE(ctrlCode)        ((ULONG)(ctrlCode & 3))
```

These macros are defined in Wdm.h and Ntddk.h.

 

 




