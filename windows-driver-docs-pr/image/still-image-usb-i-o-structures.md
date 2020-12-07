---
title: Still Image USB I/O Structures
description: Still Image USB I/O Structures
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Still Image USB I/O Structures





The following table lists and describes all of the structures associated with the I/O Control Codes recognized by the kernel-mode still image driver for SCSI buses.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Structure</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/usbscan/ns-usbscan-_channel_info" data-raw-source="[&lt;strong&gt;CHANNEL_INFO&lt;/strong&gt;](/windows-hardware/drivers/ddi/usbscan/ns-usbscan-_channel_info)"><strong>CHANNEL_INFO</strong></a></p></td>
<td><p>Used as a parameter to <a href="/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol" data-raw-source="[&lt;strong&gt;DeviceIoControl&lt;/strong&gt;](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol)"><strong>DeviceIoControl</strong></a>, when the specified I/O control code is <a href="/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_get_channel_align_rqst" data-raw-source="[&lt;strong&gt;IOCTL_GET_CHANNEL_ALIGN_RQST&lt;/strong&gt;](/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_get_channel_align_rqst)"><strong>IOCTL_GET_CHANNEL_ALIGN_RQST</strong></a>.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/usbscan/ns-usbscan-_device_descriptor" data-raw-source="[&lt;strong&gt;DEVICE_DESCRIPTOR&lt;/strong&gt;](/windows-hardware/drivers/ddi/usbscan/ns-usbscan-_device_descriptor)"><strong>DEVICE_DESCRIPTOR</strong></a></p></td>
<td><p>Used as a parameter to <a href="/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol" data-raw-source="[&lt;strong&gt;DeviceIoControl&lt;/strong&gt;](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol)"><strong>DeviceIoControl</strong></a>, when the specified I/O control code is <a href="/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_get_device_descriptor" data-raw-source="[&lt;strong&gt;IOCTL_GET_DEVICE_DESCRIPTOR&lt;/strong&gt;](/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_get_device_descriptor)"><strong>IOCTL_GET_DEVICE_DESCRIPTOR</strong></a>.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/usbscan/ns-usbscan-_drv_version" data-raw-source="[&lt;strong&gt;DRV_VERSION&lt;/strong&gt;](/windows-hardware/drivers/ddi/usbscan/ns-usbscan-_drv_version)"><strong>DRV_VERSION</strong></a></p></td>
<td><p>Used as a parameter to <a href="/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol" data-raw-source="[&lt;strong&gt;DeviceIoControl&lt;/strong&gt;](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol)"><strong>DeviceIoControl</strong></a>, when the specified I/O control code is <a href="/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_get_version" data-raw-source="[&lt;strong&gt;IOCTL_GET_VERSION&lt;/strong&gt;](/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_get_version)"><strong>IOCTL_GET_VERSION</strong></a>.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/usbscan/ns-usbscan-_io_block" data-raw-source="[&lt;strong&gt;IO_BLOCK&lt;/strong&gt;](/windows-hardware/drivers/ddi/usbscan/ns-usbscan-_io_block)"><strong>IO_BLOCK</strong></a></p></td>
<td><p>Used as a parameter to <a href="/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol" data-raw-source="[&lt;strong&gt;DeviceIoControl&lt;/strong&gt;](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol)"><strong>DeviceIoControl</strong></a>, when the specified I/O control code is <a href="/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_read_registers" data-raw-source="[&lt;strong&gt;IOCTL_READ_REGISTERS&lt;/strong&gt;](/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_read_registers)"><strong>IOCTL_READ_REGISTERS</strong></a> or <a href="/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_write_registers" data-raw-source="[&lt;strong&gt;IOCTL_WRITE_REGISTERS&lt;/strong&gt;](/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_write_registers)"><strong>IOCTL_WRITE_REGISTERS</strong></a>.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/usbscan/ns-usbscan-_io_block_ex" data-raw-source="[&lt;strong&gt;IO_BLOCK_EX&lt;/strong&gt;](/windows-hardware/drivers/ddi/usbscan/ns-usbscan-_io_block_ex)"><strong>IO_BLOCK_EX</strong></a></p></td>
<td><p>Used as a parameter to <a href="/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol" data-raw-source="[&lt;strong&gt;DeviceIoControl&lt;/strong&gt;](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol)"><strong>DeviceIoControl</strong></a>, when the specified I/O control code is <a href="/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_send_usb_request" data-raw-source="[&lt;strong&gt;IOCTL_SEND_USB_REQUEST&lt;/strong&gt;](/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_send_usb_request)"><strong>IOCTL_SEND_USB_REQUEST</strong></a>.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/usbscan/ns-usbscan-_usbscan_get_descriptor" data-raw-source="[&lt;strong&gt;USBSCAN_GET_DESCRIPTOR&lt;/strong&gt;](/windows-hardware/drivers/ddi/usbscan/ns-usbscan-_usbscan_get_descriptor)"><strong>USBSCAN_GET_DESCRIPTOR</strong></a></p></td>
<td><p>Used as a parameter to <a href="/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol" data-raw-source="[&lt;strong&gt;DeviceIoControl&lt;/strong&gt;](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol)"><strong>DeviceIoControl</strong></a>, when the specified I/O control code is <a href="/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_get_usb_descriptor" data-raw-source="[&lt;strong&gt;IOCTL_GET_USB_DESCRIPTOR&lt;/strong&gt;](/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_get_usb_descriptor)"><strong>IOCTL_GET_USB_DESCRIPTOR</strong></a>.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/usbscan/ns-usbscan-_usbscan_pipe_configuration" data-raw-source="[&lt;strong&gt;USBSCAN_PIPE_CONFIGURATION&lt;/strong&gt;](/windows-hardware/drivers/ddi/usbscan/ns-usbscan-_usbscan_pipe_configuration)"><strong>USBSCAN_PIPE_CONFIGURATION</strong></a></p></td>
<td><p>Used as a parameter to <a href="/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol" data-raw-source="[&lt;strong&gt;DeviceIoControl&lt;/strong&gt;](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol)"><strong>DeviceIoControl</strong></a>, when the specified I/O control code is <a href="/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_get_pipe_configuration" data-raw-source="[&lt;strong&gt;IOCTL_GET_PIPE_CONFIGURATION&lt;/strong&gt;](/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_get_pipe_configuration)"><strong>IOCTL_GET_PIPE_CONFIGURATION</strong></a>.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/usbscan/ns-usbscan-_usbscan_pipe_information" data-raw-source="[&lt;strong&gt;USBSCAN_PIPE_INFORMATION&lt;/strong&gt;](/windows-hardware/drivers/ddi/usbscan/ns-usbscan-_usbscan_pipe_information)"><strong>USBSCAN_PIPE_INFORMATION</strong></a></p></td>
<td><p>Used to describe a USB transfer pipe for a still image device.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/usbscan/ns-usbscan-_usbscan_timeout" data-raw-source="[&lt;strong&gt;USBSCAN_TIMEOUT&lt;/strong&gt;](/windows-hardware/drivers/ddi/usbscan/ns-usbscan-_usbscan_timeout)"><strong>USBSCAN_TIMEOUT</strong></a></p></td>
<td><p>Stores time-out values for USB bulk IN and bulk OUT operations, and interrupts.</p></td>
</tr>
</tbody>
</table>

 

These structures are defined in *usbscan.h*. For more information about these structures see:

[USB Still Image Structures](/windows-hardware/drivers/ddi/_image/index)

