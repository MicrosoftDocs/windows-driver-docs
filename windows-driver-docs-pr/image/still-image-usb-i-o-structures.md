---
title: Still Image USB I/O Structures
description: Still image USB I/O structures
ms.date: 05/04/2023
---

# Still image USB I/O structures

The following table lists and describes all of the structures associated with the I/O Control Codes recognized by the kernel-mode still image driver for SCSI buses.

| Structure | Description |
|--|--|
| [**CHANNEL_INFO**](/windows-hardware/drivers/ddi/usbscan/ns-usbscan-_channel_info) | Used as a parameter to [**DeviceIoControl**](/windows/win32/api/ioapiset/), when the specified I/O control code is [**IOCTL_GET_CHANNEL_ALIGN_RQST**](/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_get_channel_align_rqst). |
| [**DEVICE_DESCRIPTOR**](/windows-hardware/drivers/ddi/usbscan/ns-usbscan-_device_descriptor) | Used as a parameter to  [**DeviceIoControl**](/windows/win32/api/ioapiset/), when the specified I/O control code is  [**IOCTL_GET_DEVICE_DESCRIPTOR**](/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_get_device_descriptor) . |
| [**DRV_VERSION**](/windows-hardware/drivers/ddi/usbscan/ns-usbscan-_drv_version) | Used as a parameter to  [**DeviceIoControl**](/windows/win32/api/ioapiset/), when the specified I/O control code is  [**IOCTL_GET_VERSION**](/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_get_version). |
| [**IO_BLOCK**](/windows-hardware/drivers/ddi/usbscan/ns-usbscan-_io_block) | Used as a parameter to  [**DeviceIoControl**](/windows/win32/api/ioapiset/), when the specified I/O control code is  [**IOCTL_READ_REGISTERS**](/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_read_registers) or [**IOCTL_WRITE_REGISTERS**](/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_write_registers). |
| [**IO_BLOCK_EX**](/windows-hardware/drivers/ddi/usbscan/ns-usbscan-_io_block_ex)  | Used as a parameter to  [**DeviceIoControl**](/windows/win32/api/ioapiset/), when the specified I/O control code is  [**IOCTL_SEND_USB_REQUEST**](/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_send_usb_request). |
| [**USBSCAN_GET_DESCRIPTOR**](/windows-hardware/drivers/ddi/usbscan/ns-usbscan-_usbscan_get_descriptor)  | Used as a parameter to  [**DeviceIoControl**](/windows/win32/api/ioapiset/), when the specified I/O control code is  [**IOCTL_GET_USB_DESCRIPTOR**](/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_get_usb_descriptor). |
| [**USBSCAN_PIPE_CONFIGURATION**](/windows-hardware/drivers/ddi/usbscan/ns-usbscan-_usbscan_pipe_configuration)  | Used as a parameter to  [**DeviceIoControl**](/windows/win32/api/ioapiset/), when the specified I/O control code is  [**IOCTL_GET_PIPE_CONFIGURATION**](/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_get_pipe_configuration). |
| [**USBSCAN_PIPE_INFORMATION**](/windows-hardware/drivers/ddi/usbscan/ns-usbscan-_usbscan_pipe_information) | Used to describe a USB transfer pipe for a still image device. |
| [**USBSCAN_TIMEOUT**](/windows-hardware/drivers/ddi/usbscan/ns-usbscan-_usbscan_timeout) | Stores time-out values for USB bulk IN and bulk OUT operations, and interrupts. |

These structures are defined in *usbscan.h*. For more information about these structures see:

[USB still image structures](/windows-hardware/drivers/ddi/_image/index)
