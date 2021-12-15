---
title: Still Image USB I/O Control Codes
description: Still Image USB I/O Control Codes
ms.date: 04/20/2017
---

# Still Image USB I/O Control Codes





The following table lists and describes all of the I/O Control Codes recognized by the kernel-mode still image driver for USB buses.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>I/O Control Code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_cancel_io" data-raw-source="[&lt;strong&gt;IOCTL_CANCEL_IO&lt;/strong&gt;](/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_cancel_io)"><strong>IOCTL_CANCEL_IO</strong></a></p></td>
<td><p>Cancels activity on the specified USB transfer pipe.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_get_channel_align_rqst" data-raw-source="[&lt;strong&gt;IOCTL_GET_CHANNEL_ALIGN_RQST&lt;/strong&gt;](/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_get_channel_align_rqst)"><strong>IOCTL_GET_CHANNEL_ALIGN_RQST</strong></a></p></td>
<td><p>Returns a USB device's maximum packet size for the read, write, and interrupt transfer pipes.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_get_device_descriptor" data-raw-source="[&lt;strong&gt;IOCTL_GET_DEVICE_DESCRIPTOR&lt;/strong&gt;](/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_get_device_descriptor)"><strong>IOCTL_GET_DEVICE_DESCRIPTOR</strong></a></p></td>
<td><p>Returns vendor and device identifiers.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_get_pipe_configuration" data-raw-source="[&lt;strong&gt;IOCTL_GET_PIPE_CONFIGURATION&lt;/strong&gt;](/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_get_pipe_configuration)"><strong>IOCTL_GET_PIPE_CONFIGURATION</strong></a></p></td>
<td><p>Returns a description of every transfer pipe supported for a device.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_get_usb_descriptor" data-raw-source="[&lt;strong&gt;IOCTL_GET_USB_DESCRIPTOR&lt;/strong&gt;](/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_get_usb_descriptor)"><strong>IOCTL_GET_USB_DESCRIPTOR</strong></a></p></td>
<td><p>Returns a specified USB Descriptor.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_get_version" data-raw-source="[&lt;strong&gt;IOCTL_GET_VERSION&lt;/strong&gt;](/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_get_version)"><strong>IOCTL_GET_VERSION</strong></a></p></td>
<td><p>Returns the version number of the driver.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_read_registers" data-raw-source="[&lt;strong&gt;IOCTL_READ_REGISTERS&lt;/strong&gt;](/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_read_registers)"><strong>IOCTL_READ_REGISTERS</strong></a></p></td>
<td><p>Reads from USB device registers, using the control pipe.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_reset_pipe" data-raw-source="[&lt;strong&gt;IOCTL_RESET_PIPE&lt;/strong&gt;](/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_reset_pipe)"><strong>IOCTL_RESET_PIPE</strong></a></p></td>
<td><p>Resets the specified USB transfer pipe.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_send_usb_request" data-raw-source="[&lt;strong&gt;IOCTL_SEND_USB_REQUEST&lt;/strong&gt;](/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_send_usb_request)"><strong>IOCTL_SEND_USB_REQUEST</strong></a></p></td>
<td><p>Sends a vendor-defined request to a USB device, using the control pipe, and optionally sends or receives additional data.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_set_timeout" data-raw-source="[&lt;strong&gt;IOCTL_SET_TIMEOUT&lt;/strong&gt;](/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_set_timeout)"><strong>IOCTL_SET_TIMEOUT</strong></a></p></td>
<td><p>Sets the time-out value for USB bulk IN, bulk OUT, or interrupt pipe access.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_wait_on_device_event" data-raw-source="[&lt;strong&gt;IOCTL_WAIT_ON_DEVICE_EVENT&lt;/strong&gt;](/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_wait_on_device_event)"><strong>IOCTL_WAIT_ON_DEVICE_EVENT</strong></a></p></td>
<td><p>Returns information about an event occurring on a USB interrupt pipe.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_write_registers" data-raw-source="[&lt;strong&gt;IOCTL_WRITE_REGISTERS&lt;/strong&gt;](/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_write_registers)"><strong>IOCTL_WRITE_REGISTERS</strong></a></p></td>
<td><p>Writes to USB device registers, using the control pipe.</p></td>
</tr>
</tbody>
</table>

 

These codes are defined in *usbscan.h*. For more information about these I/O control codes see:

[USB Still Image I/O Control Codes](/windows-hardware/drivers/ddi/_image/index)

