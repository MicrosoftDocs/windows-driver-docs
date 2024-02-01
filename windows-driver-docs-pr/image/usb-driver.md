---
title: USB Driver
description: USB driver
ms.date: 05/02/2023
---

# USB driver

The kernel-mode still image driver for USB buses supports a single control endpoint, along with multiple interrupt, bulk IN, and bulk OUT endpoints. The control and interrupt endpoints are accessible using I/O control codes and [**DeviceIoControl**](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol). The bulk endpoints are accessible using **ReadFile** and **WriteFile**.

Before calling [**DeviceIoControl**](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol), **ReadFile**, or **WriteFile**, you must call [**CreateFile**](/windows/win32/api/fileapi/nf-fileapi-createfilea) (all described in the Microsoft Windows SDK documentation) to obtain a device handle. For devices that support no more than one of each endpoint type (control, interrupt, bulk IN, bulk OUT), a single call to **CreateFile** opens transfer pipes to each endpoint.

For devices that support multiple interrupt or bulk endpoints, a single call to [**CreateFile**](/windows/win32/api/fileapi/nf-fileapi-createfilea) opens transfer pipes to the highest-numbered endpoint of each type. If you want to use a different endpoint, you must do the following:

1. Call [**DeviceIoControl**](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol), specifying an I/O control code of [**IOCTL_GET_PIPE_CONFIGURATION**](/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_get_pipe_configuration), to determine a port's endpoint index numbers (that is, indexes into the returned [**USBSCAN_PIPE_INFORMATION**](/windows-hardware/drivers/ddi/usbscan/ns-usbscan-_usbscan_pipe_information) structure array). Note that these index numbers are *not* the endpoint numbers described in the *Universal Serial Bus Specification*.

2. Append a backslash and the endpoint's index number to the port name returned by [**IStiDeviceControl::GetMyDevicePortName**](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istidevicecontrol-getmydeviceportname) when calling CreateFile.

For example, suppose a device (with a port name of "usbscan0") has two endpoints of each type (interrupt, bulk IN, bulk OUT), with index numbers as follows:

| Index | Type | Endpoint# |
|--|--|--|
| 0 | Interrupt | 0x01 |
| 1 | Bulk IN | 0x82 |
| 2 | Bulk IN | 0x83 |
| 3 | Bulk OUT | 0x04 |
| 4 | Bulk OUT | 0x05 |
| 5 | Interrupt | 0x06 |

If you call [**CreateFile**](/windows/win32/api/fileapi/nf-fileapi-createfilea) with a port name of "usbscan0", the function opens transfer pipes to endpoints with index values of 2, 4, and 5, as well as the control endpoint.

If you call [**CreateFile**](/windows/win32/api/fileapi/nf-fileapi-createfilea) with a port name of "usbscan0\\1", the function opens transfer pipes to endpoints with index values of 1, 4, and 5, as well as the control endpoint.

For this device, if you want to use interrupt endpoint 0, bulk IN endpoint 1, and bulk OUT endpoint 3, call [**CreateFile**](/windows/win32/api/fileapi/nf-fileapi-createfilea) three times, specifying port names of "usbscan0\\0", "usbscan0\\1", and "usbscan0\\3". This creates three device handles. Whenever a subsequent call to [**DeviceIoControl**](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol), **ReadFile**, or **WriteFile** is made, the device handle associated with the desired pipe should be specified.

Because only one control endpoint is supported, specifying any I/O control code that uses the control pipe causes the driver to use the proper endpoint, regardless of which endpoint (if any) was specified to [**CreateFile**](/windows/win32/api/fileapi/nf-fileapi-createfilea).

For descriptions of all I/O control codes, see [USB Still Image I/O Control Codes](/windows-hardware/drivers/ddi/_image/index).

The kernel-mode USB driver does not implement a package or message protocol. Read operations do not require any particular packet alignment, but better performance can be achieved if read requests are aligned to maximum packet size boundaries. The maximum packet size can be obtained using the [**IOCTL_GET_CHANNEL_ALIGN_RQST**](/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_get_channel_align_rqst) I/O control code.
