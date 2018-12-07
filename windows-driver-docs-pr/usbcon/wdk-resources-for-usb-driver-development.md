---
Description: This topic lists the "How to" topics in the USB driver documentation set. Each how-to topic presents a set of tasks as a sequence of steps with code examples.
title: Common tasks for USB client drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Common tasks for USB client drivers


This topic lists the "How to" topics in this documentation set. Each how-to topic presents a set of tasks as a sequence of steps with code examples.

A How to topic provides you with step-by-step instructions about a process related to a USB client driver task. Generally, the topics are written with the assumption that you are extending the drivers created by USB templates included with Microsoft Visual Studio 2012.

This list contains links to the how-to topics for USB client drivers.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Task</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="tutorial--write-your-first-usb-client-driver--kmdf-.md" data-raw-source="[How to write your first USB client driver (KMDF)](tutorial--write-your-first-usb-client-driver--kmdf-.md)">How to write your first USB client driver (KMDF)</a></p></td>
<td><p>In this topic you&#39;ll use the USB Kernel-Mode Driver template provided with Microsoft Visual Studio 11 Professional Beta to write a simple kernel-mode driver framework (KMDF)-based client driver. After building and installing the client driver, you&#39;ll view the client driver in Device Manager and view the driver output in a debugger.</p></td>
</tr>
<tr class="even">
<td><p><a href="implement-driver-entry-for-a-usb-driver--umdf-.md" data-raw-source="[How to write your first USB client driver (UMDF)](implement-driver-entry-for-a-usb-driver--umdf-.md)">How to write your first USB client driver (UMDF)</a></p></td>
<td><p>In this topic you&#39;ll use the USB User-Mode Driver template provided with Microsoft Visual Studio 11 Beta to write a user-mode driver framework (UMDF)-based client driver. After building and installing the client driver, you&#39;ll view the client driver in Device Manager and view the driver output in a debugger.</p></td>
</tr>
<tr class="odd">
<td><p><a href="usb-configuration-descriptors.md" data-raw-source="[How to get the configuration descriptor](usb-configuration-descriptors.md)">How to get the configuration descriptor</a></p></td>
<td><p>This topic describes the important fields of a configuration and includes step-by-step guidance about how to obtain the configuration descriptor from a USB device.</p></td>
</tr>
<tr class="even">
<td><p><a href="send-requests-to-the-usb-driver-stack.md" data-raw-source="[How to Submit an URB (WDM)](send-requests-to-the-usb-driver-stack.md)">How to Submit an URB (WDM)</a></p></td>
<td><p>This topic describes the steps that are required to submit an initialized URB to the USB driver stack to process a particular request.</p></td>
</tr>
<tr class="odd">
<td><p><a href="how-to-select-a-configuration-for-a-usb-device.md" data-raw-source="[How to select a configuration for a USB device](how-to-select-a-configuration-for-a-usb-device.md)">How to select a configuration for a USB device</a></p></td>
<td><p>In this topic, you&#39;ll learn about how to select a configuration in a universal serial bus (USB) device. This topic describes the process of sending a select-configuration request by submitting an URB.</p></td>
</tr>
<tr class="even">
<td><p><a href="select-a-usb-alternate-setting.md" data-raw-source="[How to select an alternate setting in a USB interface](select-a-usb-alternate-setting.md)">How to select an alternate setting in a USB interface</a></p></td>
<td><p>This topic describes the steps for issuing a select-interface request to activate an alternate setting in a USB interface. The client driver must issue this request after selecting a USB configuration. Selecting a configuration, by default, also activates the first alternate setting in each interface in that configuration.</p></td>
</tr>
<tr class="odd">
<td><p><a href="how-to-get-usb-pipe-handles.md" data-raw-source="[How to enumerate USB pipes](how-to-get-usb-pipe-handles.md)">How to enumerate USB pipes</a></p></td>
<td><p>This topic provides an overview of USB pipes and describes the steps required by a USB client driver to obtain pipe handles from the USB driver stack.</p></td>
</tr>
<tr class="even">
<td><p><a href="how-to-use-the-continous-reader-for-getting-data-from-a-usb-endpoint--umdf-.md" data-raw-source="[How to use the continuous reader for reading data from a USB pipe](how-to-use-the-continous-reader-for-getting-data-from-a-usb-endpoint--umdf-.md)">How to use the continuous reader for reading data from a USB pipe</a></p></td>
<td><p>This topic describes the WDF-provided continuous reader object. The procedures in this topic provided step-by-step instructions about how to configure the object and use it to read data from a USB pipe.</p></td>
</tr>
<tr class="odd">
<td><p><a href="usb-control-transfer.md" data-raw-source="[How to send a USB control transfer](usb-control-transfer.md)">How to send a USB control transfer</a></p></td>
<td><p>This topic explains the structure of a control transfer and how a client driver should send a control request to the device.</p></td>
</tr>
<tr class="even">
<td><p><a href="usb-bulk-and-interrupt-transfer.md" data-raw-source="[How to transfer data to USB bulk endpoints](usb-bulk-and-interrupt-transfer.md)">How to transfer data to USB bulk endpoints</a></p></td>
<td><p>This topic provides a brief overview about USB bulk transfers. It also provides step-by-step instructions about how a client driver can send and receive bulk data from the device.</p></td>
</tr>
<tr class="odd">
<td><p><a href="how-to-open-streams-in-a-usb-endpoint.md" data-raw-source="[How to open and close static streams in a USB bulk endpoint](how-to-open-streams-in-a-usb-endpoint.md)">How to open and close static streams in a USB bulk endpoint</a></p></td>
<td><p>This topic discusses static streams capability and explains how a USB client driver can open and close streams in a bulk endpoint of a USB 3.0 device.</p></td>
</tr>
<tr class="even">
<td><p><a href="transfer-data-to-isochronous-endpoints.md" data-raw-source="[How to transfer data to USB isochronous endpoints](transfer-data-to-isochronous-endpoints.md)">How to transfer data to USB isochronous endpoints</a></p></td>
<td><p>This topic describes how a client driver can build a USB Request Block (URB) to transfer data to and from supported isochronous endpoints in a USB device.</p></td>
</tr>
<tr class="odd">
<td><p><a href="how-to-recover-from-usb-pipe-errors.md" data-raw-source="[How to recover from USB pipe errors](how-to-recover-from-usb-pipe-errors.md)">How to recover from USB pipe errors</a></p></td>
<td><p>This topic provides information about steps you can try when a data transfer to a USB pipe fails. The mechanisms described in this topic cover abort, reset, and cycle port operations on bulk, interrupt, and isochronous pipes.</p></td>
</tr>
<tr class="even">
<td><p><a href="how-to-send-chained-mdls.md" data-raw-source="[How to send chained MDLs](how-to-send-chained-mdls.md)">How to send chained MDLs</a></p></td>
<td><p>In this topic, you will learn about the chained MDLs capability in the USB driver stack, and how a client driver can send a transfer buffer as a chain of MDL structure.</p></td>
</tr>
<tr class="odd">
<td><p><a href="register-a-composite-driver.md" data-raw-source="[How to Register a Composite Device](register-a-composite-driver.md)">How to Register a Composite Device</a></p></td>
<td><p>This topic describes how a driver of a USB multi-function device, called a composite driver, can register and unregister the composite device with the underlying USB driver stack. The Microsoft-provided driver, Usbccgp.sys, is the default composite driver that is loaded by Windows. The procedure in this topic applies to a custom Windows Driver Model (WDM)-based composite driver that replaces Usbccgp.sys.</p></td>
</tr>
<tr class="even">
<td><p><a href="how-to--implement-remote-and-function-wake-support.md" data-raw-source="[How to Implement Function Suspend in a Composite Driver](how-to--implement-remote-and-function-wake-support.md)">How to Implement Function Suspend in a Composite Driver</a></p></td>
<td><p>This topic provides an overview of function suspend and function remote wake-up features for Universal Serial Bus (USB) 3.0 multi-function devices (composite devices). In this topic you will learn about implementing those features in a driver that controls a composite device. The topic applies to composite drivers that replace Usbccgp.sys.</p></td>
</tr>
</tbody>
</table>

 

## Related topics
[Universal Serial Bus (USB) Drivers](https://msdn.microsoft.com/library/windows/hardware/ff538930)  



