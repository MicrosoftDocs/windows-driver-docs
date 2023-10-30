---
title: Still image USB I/O control codes
description: Still image USB I/O control codes
ms.date: 05/04/2023
---

# Still image USB I/O control codes

The following table lists and describes all of the I/O Control Codes recognized by the kernel-mode still image driver for USB buses.

| I/O control code | Description |
|--|--|
| [**IOCTL_CANCEL_IO**](/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_cancel_io) | Cancels activity on the specified USB transfer pipe. |
| [**IOCTL_GET_CHANNEL_ALIGN_RQST**](/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_get_channel_align_rqst) | Returns a USB device's maximum packet size for the read, write, and interrupt transfer pipes. |
| [**IOCTL_GET_DEVICE_DESCRIPTOR**](/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_get_device_descriptor) | Returns vendor and device identifiers. |
| [**IOCTL_GET_PIPE_CONFIGURATION**](/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_get_pipe_configuration) | Returns a description of every transfer pipe supported for a device. |
| [**IOCTL_GET_USB_DESCRIPTOR**](/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_get_usb_descriptor) | Returns a specified USB Descriptor. |
| [**IOCTL_GET_VERSION**](/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_get_version) | Returns the version number of the driver. |
| [**IOCTL_READ_REGISTERS**](/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_read_registers) | Reads from USB device registers, using the control pipe. |
| [**IOCTL_RESET_PIPE**](/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_reset_pipe) | Resets the specified USB transfer pipe. |
| [**IOCTL_SEND_USB_REQUEST**](/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_send_usb_request) | Sends a vendor-defined request to a USB device, using the control pipe, and optionally sends or receives additional data. |
| [**IOCTL_SET_TIMEOUT**](/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_set_timeout) | Sets the time-out value for USB bulk IN, bulk OUT, or interrupt pipe access. |
| [**IOCTL_WAIT_ON_DEVICE_EVENT**](/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_wait_on_device_event) | Returns information about an event occurring on a USB interrupt pipe. |
| [**IOCTL_WRITE_REGISTERS**](/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_write_registers) | Writes to USB device registers, using the control pipe. |

These codes are defined in *usbscan.h*. For more information about these I/O control codes see:

[USB still image I/O control codes](/windows-hardware/drivers/ddi/_image/index)
