---
title: Defining I/O Control Codes
description: Provides information about defining I/O control codes.
keywords: ["I/O control codes WDK kernel , defining", "control codes WDK IOCTLs , defining", "IOCTLs WDK kernel , defining", "CTL_CODE macro", "IOCTLs WDK user-mode", "user-mode components WDK IOCTLs", "I/O control codes WDK user-mode", "control codes WDK user-mode", "layouts WDK IOCTLs"]
ms.date: 06/16/2025
ms.topic: concept-article
---

# Defining I/O control codes

This article describes how to create a unique [I/O control code (IOCTL)](introduction-to-i-o-control-codes.md). IOCTLs can be:

* Public IOCTLs, which are typically system-defined and documented by Microsoft.
* Private IOCTLs, which are typically meant to be used exclusively by a vendor's software components to communicate with each other. They're usually defined in a vendor's header file and aren't documented by Microsoft.

## IOCTL layout

An IOCTL is a 32-bit value that consists of several fields. The following figure illustrates the bit-wise layout of an IOCTL:

![diagram illustrating the bitwise layout of a 32-bit i/o control code.](images/ioctl-bit-layout.png)

Each field in the IOCTL has a specific purpose, as described in the following table:

| Field | Bits in IOCTL | Description |
| ----- | ------------- | ----------- |
| **Common** | 31 | Vendors must set this bit when they use a vendor-assigned value for **DeviceType**. |
| **DeviceType** | 16-30 |  Identifies the type of device. This value must match the value set in the **DeviceType** member of the driver's [**DEVICE_OBJECT**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_device_object) structure. Vendors should use a value from 32768 through 65535 (0x8000 through 0xffff), and should set the **Common** bit. Values 0 through 32767 (0x0000 through 0x7fff) are reserved for Microsoft. For more information, see [Specifying Device Types](specifying-device-types.md). |
| **Access** | 14-15 | Indicates the type of access that a caller must request when opening the file object that represents the device (see [**IRP_MJ_CREATE**](irp-mj-create.md)). The I/O manager will create IRPs and call the driver with a particular IOCTL only if the caller requested the specified access rights. This field is specified using the following system-defined constants: FILE_ANY_ACCESS, FILE_READ_DATA, and FILE_WRITE_DATA. |
| **Custom** | 13 | When set, indicates that the IOCTL is a vendor-defined IOCTL. |
| **Function** | 2-12 | Unique code for the driver that identifies the function that it's to perform. For a vendor-created IOCTL, use a value 2048 through 4095 (0x800 through 0xfff) and set the **Custom** bit. Values less than 2048 (0x000 through 0x7ff) are reserved for Microsoft. |
| **Method** | 0-1 | Indicates how the system is to pass data between the caller of [**DeviceIoControl**](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol) (or [**IoBuildDeviceIoControlRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iobuilddeviceiocontrolrequest)) and the driver that handles the IRP. For more information, see [Guidance for setting the Method bits](#guidance-for-setting-the-method-bits). |

## Macro for defining I/O control codes

Use the system-supplied **CTL_CODE** macro to define new I/O control codes. This macro is defined in *devioctl.h* as follows:

``` cpp
#define CTL_CODE( DeviceType, Function, Method, Access ) (                 \
    ((DeviceType) << 16) | ((Access) << 14) | ((Function) << 2) | (Method) \
)
```

See the preceding section for a description of **DeviceType**, **Function**, **Method**, and **Access**.

Keep the following rules in mind when defining new I/O control codes:

* If a new IOCTL will be available to user-mode software components, it must be used with [**IRP_MJ_DEVICE_CONTROL**](./irp-mj-device-control.md) requests. User-mode components call [**DeviceIoControl**](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol) to send **IRP_MJ_DEVICE_CONTROL** requests.

* If a new IOCTL will be available only to kernel-mode driver components, it must be used with [**IRP_MJ_INTERNAL_DEVICE_CONTROL**](irp-mj-internal-device-control.md) requests. Kernel-mode components can create **IRP_MJ_INTERNAL_DEVICE_CONTROL** requests by calling [**IoBuildDeviceIoControlRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iobuilddeviceiocontrolrequest). For more information, see [Creating IOCTL Requests in Drivers](creating-ioctl-requests-in-drivers.md).

The definition of a new IOCTL code, whether intended for use with **IRP_MJ_DEVICE_CONTROL** or **IRP_MJ_INTERNAL_DEVICE_CONTROL** requests, uses the following format:

```cpp
#define IOCTL_Device_Function CTL_CODE(DeviceType, Function, Method, Access)
```

Choose a descriptive constant name for the IOCTL, of the form IOCTL_*Device*_*Function*, where *Device* indicates the [type of device](specifying-device-types.md) and *Function* indicates the operation. For example, the system-supplied IOCTL_VIDEO_ENABLE_CURSOR constant uses "VIDEO" for *Device* and "ENABLE_CURSOR" for *Function*.

### Guidance for setting the Access bits

When defining a new IOCTL, you must choose a value for the **Access** bit field that indicates the type of access that a caller must request when [opening the file object that represents the device](irp-mj-create.md). The I/O manager will create IRPs and call the driver with a particular IOCTL only if the caller requested the specified access rights.

**Access** is specified by using the following system-defined constants:

* FILE_ANY_ACCESS  

  The I/O manager sends the IRP for any caller that has a handle to the file object that represents the target device object. Before specifying FILE_ANY_ACCESS for a new IOCTL code, you must be absolutely certain that allowing unrestricted access to your device doesn't create a possible path for malicious users to compromise the system.

* FILE_READ_DATA  

  The I/O manager sends the IRP only for a caller with read access rights, allowing the underlying device driver to transfer data from the device to system memory.

* FILE_WRITE_DATA  

  The I/O manager sends the IRP only for a caller with write access rights, allowing the underlying device driver to transfer data from system memory to its device.

FILE_READ_DATA and FILE_WRITE_DATA can be ORed together if the caller must have both read and write access rights.

Some system-defined I/O control codes have an **Access** value of FILE_ANY_ACCESS, which allows the caller to send the particular IOCTL regardless of the access granted to the device. Examples include I/O control codes that are sent to drivers of *exclusive devices*.

Other system-defined I/O control codes require the caller to have read access rights, write access rights, or both. For example, the following definition of the public IOCTL_DISK_SET_PARTITION_INFO IOCTL shows that this I/O request can be sent to a driver only if the caller has both read and write access rights:

```cpp
#define IOCTL_DISK_SET_PARTITION_INFO\
        CTL_CODE(IOCTL_DISK_BASE, 0x008, METHOD_BUFFERED,\
        FILE_READ_DATA | FILE_WRITE_DATA)
```

Drivers can use [**IoValidateDeviceIoControlAccess**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iovalidatedeviceiocontrolaccess) to perform stricter access checking than that provided by an IOCTL's **Access** bits.

### Guidance for setting the Method bits

When defining a new IOCTL, you must choose a value for the **Method** bit field that indicates how the system is to pass data between the caller of [**DeviceIoControl**](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol) (or [**IoBuildDeviceIoControlRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iobuilddeviceiocontrolrequest)) and the driver that handles the IRP.

Use one of the following system-defined constants to set the **Method** field.

* METHOD_BUFFERED

  Specifies the [buffered I/O](methods-for-accessing-data-buffers.md) method, which is typically used for transferring small amounts of data per request. Most I/O control codes for device and intermediate drivers use this value.

  For information about how the system specifies data buffers for METHOD_BUFFERED I/O control codes, see [Buffer Descriptions for I/O Control Codes](buffer-descriptions-for-i-o-control-codes.md).

  For more information about buffered I/O, see [Using Buffered I/O](using-buffered-i-o.md).

* METHOD_IN_DIRECT or METHOD_OUT_DIRECT  

  Specifies the [direct I/O](methods-for-accessing-data-buffers.md) method, which is typically used for reading or writing large amounts of data using DMA or PIO that must be transferred quickly.

  * Specify METHOD_IN_DIRECT if the caller of [**DeviceIoControl**](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol) or [**IoBuildDeviceIoControlRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iobuilddeviceiocontrolrequest) will pass data to the driver.

  * Specify METHOD_OUT_DIRECT if the caller of **DeviceIoControl** or **IoBuildDeviceIoControlRequest** will receive data from the driver.

  For information about how the system specifies data buffers for METHOD_IN_DIRECT and METHOD_OUT_DIRECT I/O control codes, see [Buffer Descriptions for I/O Control Codes](buffer-descriptions-for-i-o-control-codes.md).

  For more information about direct I/O, see [Using Direct I/O](using-direct-i-o.md).

* METHOD_NEITHER  

  Specifies [the I/O method isn't buffered or direct](methods-for-accessing-data-buffers.md). The I/O manager doesn't provide any system buffers or MDLs. The IRP supplies the user-mode virtual addresses of the input and output buffers that were specified to [**DeviceIoControl**](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol) or **IoBuildDeviceIoControlRequest**, without validating or mapping them.

  For information about how the system specifies data buffers for METHOD_NEITHER I/O control codes, see [Buffer Descriptions for I/O Control Codes](buffer-descriptions-for-i-o-control-codes.md).

  This method can be used only if the driver is guaranteed to be running in the context of the thread that originated the I/O control request. Only a highest-level kernel-mode driver is guaranteed to meet this condition, so METHOD_NEITHER is seldom used for IOCTLs that are passed to low-level device drivers.

  With this method, the highest-level driver:

  * Must determine whether to set up buffered or direct access to user data on receipt of the request.
  * Possibly must lock down the user buffer.
  * Must wrap its access to the user buffer in a structured exception handler (see [Handling Exceptions](handling-exceptions.md)).

  Otherwise, the originating user-mode caller might change the buffered data before the driver can use it, or the caller could be swapped out just as the driver is accessing the user buffer.

  For more information, see [Using Neither Buffered Nor Direct I/O](using-neither-buffered-nor-direct-i-o.md).

## Other useful macros

The following macros are useful for extracting the 16-bit **DeviceType** and 2-bit **Method** fields from an IOCTL.

```cpp
#define DEVICE_TYPE_FROM_CTL_CODE(ctrlCode)   (((ULONG)(ctrlCode & 0xffff0000)) >> 16)
#define METHOD_FROM_CTL_CODE(ctrlCode)        ((ULONG)(ctrlCode & 3))
```

These macros are defined in *Wdm.h* and *Ntddk.h*.
