---
title: USB Driver
description: USB Driver
ms.assetid: c20bd393-98d0-498e-a3e8-bbd1958ed774
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# USB Driver





The kernel-mode still image driver for USB buses supports a single control endpoint, along with multiple interrupt, bulk IN, and bulk OUT endpoints. The control and interrupt endpoints are accessible using I/O control codes and [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216). The bulk endpoints are accessible using **ReadFile** and **WriteFile**.

Before calling [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216), **ReadFile**, or **WriteFile**, you must call [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858) (all described in the Microsoft Windows SDK documentation) to obtain a device handle. For devices that support no more than one of each endpoint type (control, interrupt, bulk IN, bulk OUT), a single call to **CreateFile** opens transfer pipes to each endpoint.

For devices that support multiple interrupt or bulk endpoints, a single call to [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858) opens transfer pipes to the highest-numbered endpoint of each type. If you want to use a different endpoint, you must do the following:

1.  Call [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216), specifying an I/O control code of [**IOCTL\_GET\_PIPE\_CONFIGURATION**](https://msdn.microsoft.com/library/windows/hardware/ff542859), to determine a port's endpoint index numbers (that is, indexes into the returned [**USBSCAN\_PIPE\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff548547) structure array). Note that these index numbers are *not* the endpoint numbers described in the *Universal Serial Bus Specification*.

2.  Append a backslash and the endpoint's index number to the port name returned by [**IStiDeviceControl::GetMyDevicePortName**](https://msdn.microsoft.com/library/windows/hardware/ff542944) when calling CreateFile.

For example, suppose a device (with a port name of "usbscan0") has two endpoints of each type (interrupt, bulk IN, bulk OUT), with index numbers as follows:

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Index</th>
<th>Type</th>
<th>Endpoint#</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>0</p></td>
<td><p>Interrupt</p></td>
<td><p>0x01</p></td>
</tr>
<tr class="even">
<td><p>1</p></td>
<td><p>Bulk IN</p></td>
<td><p>0x82</p></td>
</tr>
<tr class="odd">
<td><p>2</p></td>
<td><p>Bulk IN</p></td>
<td><p>0x83</p></td>
</tr>
<tr class="even">
<td><p>3</p></td>
<td><p>Bulk OUT</p></td>
<td><p>0x04</p></td>
</tr>
<tr class="odd">
<td><p>4</p></td>
<td><p>Bulk OUT</p></td>
<td><p>0x05</p></td>
</tr>
<tr class="even">
<td><p>5</p></td>
<td><p>Interrupt</p></td>
<td><p>0x06</p></td>
</tr>
</tbody>
</table>

 

If you call [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858) with a port name of "usbscan0", the function opens transfer pipes to endpoints with index values of 2, 4, and 5, as well as the control endpoint.

If you call [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858) with a port name of "usbscan0\\1", the function opens transfer pipes to endpoints with index values of 1, 4, and 5, as well as the control endpoint.

For this device, if you want to use interrupt endpoint 0, bulk IN endpoint 1, and bulk OUT endpoint 3, call [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858) three times, specifying port names of "usbscan0\\0", "usbscan0\\1", and "usbscan0\\3". This creates three device handles. Whenever a subsequent call to [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216), **ReadFile**, or **WriteFile** is made, the device handle associated with the desired pipe should be specified.

Because only one control endpoint is supported, specifying any I/O control code that uses the control pipe causes the driver to use the proper endpoint, regardless of which endpoint (if any) was specified to [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858).

For descriptions of all I/O control codes, see [USB Still Image I/O Control Codes](https://msdn.microsoft.com/library/windows/hardware/ff548569).

The kernel-mode USB driver does not implement a package or message protocol. Read operations do not require any particular packet alignment, but better performance can be achieved if read requests are aligned to maximum packet size boundaries. The maximum packet size can be obtained using the [**IOCTL\_GET\_CHANNEL\_ALIGN\_RQST**](https://msdn.microsoft.com/library/windows/hardware/ff542849) I/O control code.

 

 




