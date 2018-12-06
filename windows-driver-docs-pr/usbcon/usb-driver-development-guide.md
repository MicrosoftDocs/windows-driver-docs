---
Description: PurposeThis section describes Universal Serial Bus (USB) support in the Windows operating system, so that you can develop USB device drivers that are interoperable with Windows.
title: Developing Windows client drivers for USB devices
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Developing Windows client drivers for USB devices


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Purpose</strong></p>
<p>This section describes Universal Serial Bus (USB) support in the Windows operating system, so that you can develop USB device drivers that are interoperable with Windows.</p>
<p><strong>Where applicable</strong></p>
<p>USB devices are peripherals, such as mouse devices and keyboards, that are connected to a computer through a single port. A USB client driver is the software installed on the computer that communicates with the hardware to make the device function. If the device belongs to a device class supported by Microsoft, Windows loads one of the <a href="system-supplied-usb-drivers.md" data-raw-source="[Microsoft-provided USB drivers](system-supplied-usb-drivers.md)">Microsoft-provided USB drivers</a> (in-box class drivers) for the device. Otherwise, a custom client driver must be provided by the hardware manufacturer or a third party vendor. The user installs the client driver for the device when the device is first detected by Windows. After successful installation, Windows loads the client driver every time the device is attached and unloads the driver when the device is detached from the host computer.</p>
<p>You can develop a custom client driver for a USB device by using the <a href="https://docs.microsoft.com/windows-hardware/drivers/wdf/" data-raw-source="[Windows Driver Frameworks](https://docs.microsoft.com/windows-hardware/drivers/wdf/)">Windows Driver Frameworks</a> (WDF) or the <a href="https://msdn.microsoft.com/library/windows/hardware/ff565698" data-raw-source="[Windows Driver Model](https://msdn.microsoft.com/library/windows/hardware/ff565698)">Windows Driver Model</a> (WDM). Instead of communicating with the hardware directly, most client drivers send their requests to the Microsoft-provided USB driver stack that makes hardware abstraction layer (HAL) function calls to send the client driver&#39;s request to the hardware. The topics in this section describe the typical requests that a client driver can send and the device driver interfaces (DDIs) that the client driver must call to create those requests.</p>
<p><strong>Developer audience</strong></p>
<p>A client driver for a USB device is a WDF or WDM driver that communicates with the device through DDIs exposed by the USB driver stack. This section is intended for use by C/C++ programmers who are familiar with WDM. Before you use this section, you should understand basic driver development. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff554690" data-raw-source="[Getting Started with Windows Drivers](https://msdn.microsoft.com/library/windows/hardware/ff554690)">Getting Started with Windows Drivers</a>. For WDF drivers, the client driver can use <a href="https://msdn.microsoft.com/library/windows/hardware/ff551869" data-raw-source="[Kernel-Mode Driver Framework](https://msdn.microsoft.com/library/windows/hardware/ff551869)">Kernel-Mode Driver Framework</a> (KMDF) or <a href="https://docs.microsoft.com/windows-hardware/drivers/wdf/" data-raw-source="[User-Mode Driver Framework](https://docs.microsoft.com/windows-hardware/drivers/wdf/)">User-Mode Driver Framework</a> (UMDF) interfaces designed specifically to work with USB targets. For more information about the USB-specific interfaces, see <a href="https://msdn.microsoft.com/library/windows/hardware/dn265671" data-raw-source="[WDF USB Reference](https://msdn.microsoft.com/library/windows/hardware/dn265671)">WDF USB Reference</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff561332" data-raw-source="[UMDF USB I/O Target Interfaces](https://msdn.microsoft.com/library/windows/hardware/ff561332)">UMDF USB I/O Target Interfaces</a>.</p>
<p><strong>Development tools</strong></p>
<p>The Windows Driver Kit (WDK) contains resources that are required for driver development, such as headers, libraries, tools, and samples.</p>
<p><a href="http://go.microsoft.com/fwlink/p/?linkid=617155" data-raw-source="[Download kits and tools for Windows](http://go.microsoft.com/fwlink/p/?linkid=617155)">Download kits and tools for Windows</a></p>
<p><strong>USB programming reference</strong></p>
<p>Gives specifications for I/O requests, support routines, structures, and interfaces used by USB client drivers. Those routines and related data structures are defined in the WDK headers.</p>
<p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/_usbref/#common-usb-client-driver-reference" data-raw-source="[Universal Serial Bus (USB) programming reference](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/_usbref/#common-usb-client-driver-reference)">Universal Serial Bus (USB) programming reference</a>.</p>
<p><strong>USB driver samples</strong></p>
<p>Use these samples to get started with USB client driver programming.</p>
<ul>
<li><a href="http://go.microsoft.com/fwlink/p/?linkid=617157" data-raw-source="[Usbsamp Generic USB Driver]( http://go.microsoft.com/fwlink/p/?linkid=617157)">Usbsamp Generic USB Driver</a></li>
<li><a href="http://go.microsoft.com/fwlink/p/?linkid=617158" data-raw-source="[Sample KMDF Function Driver for OSR USB-FX2](http://go.microsoft.com/fwlink/p/?linkid=617158)">Sample KMDF Function Driver for OSR USB-FX2</a></li>
<li><a href="http://go.microsoft.com/fwlink/p/?LinkId=618002" data-raw-source="[Sample UMDF Function Driver for OSR USB-FX2](http://go.microsoft.com/fwlink/p/?LinkId=618002)">Sample UMDF Function Driver for OSR USB-FX2</a></li>
</ul>
<p><strong>Related standards and specifications</strong></p>
<p>You can download official USB specifications from the <a href="http://go.microsoft.com/fwlink/p/?linkid=224892" data-raw-source="[Universal Serial Bus Documents]( http://go.microsoft.com/fwlink/p/?linkid=224892)">Universal Serial Bus Documents</a> website. This website contains links to the Universal Serial Bus Revision 3.0 Specification and the Universal Serial Bus Revision 2.0 specification.</p></td>
<td><p><strong>Documentation sections</strong></p>
<p><a href="getting-started-with-usb-client-driver-development.md" data-raw-source="[Getting started with USB client driver development](getting-started-with-usb-client-driver-development.md)">Getting started with USB client driver development</a></p>
Introduces you to USB driver development. Provides information about choosing the most appropriate model for providing a USB driver for your device.
Write, build, and install your first skeleton user-mode and kernel-mode USB drivers by using the USB templates included with Microsoft Visual Studio.
<p><a href="usb-3-0-driver-stack-architecture.md" data-raw-source="[USB host-side drivers in Windows](usb-3-0-driver-stack-architecture.md)">USB host-side drivers in Windows</a></p>
Provides an overview of the USB driver stack architecture.
<p><a href="communicating-with-a-usb-device.md" data-raw-source="[About USB Block Requests (URBs)](communicating-with-a-usb-device.md)">About USB Block Requests (URBs)</a></p>
Learn how a client driver builds a variable-length data structure called a USB Request Block (URB) to submit requests to the USB driver stack.
<p><a href="usb-descriptors.md" data-raw-source="[USB descriptors](usb-descriptors.md)">USB descriptors</a></p>
Learn how a client driver builds a variable-length data structure called a USB Request Block (URB) to submit requests to the USB driver stack.
<p><a href="configuring-usb-devices.md" data-raw-source="[Selecting a USB configuration in USB drivers](configuring-usb-devices.md)">Selecting a USB configuration in USB drivers</a></p>
Device configuration refers to the tasks that the client driver performs to select a USB configuration and an alternate interface in each interface. The section shows the methods calls required to select a USB configuration.
<p><a href="usb-device-i-o.md" data-raw-source="[Sending USB data transfers in USB client drivers](usb-device-i-o.md)">Sending USB data transfers in USB client drivers</a></p>
Device configuration refers to the tasks that the client driver performs to select a USB configuration and an alternate interface in each interface. The section shows the methods calls required to select a USB configuration.
<p><a href="usb-power-management.md" data-raw-source="[Implementing power management in USB client drivers](usb-power-management.md)">Implementing power management in USB client drivers</a></p>
Use the power management abilities of USB devices that comply with the Universal Serial Bus (USB) specification have a rich and complex set of power management features.</td>
</tr>
</tbody>
</table>

 

## Related topics
[Universal Serial Bus (USB)](https://msdn.microsoft.com/library/windows/hardware/ff538930)  



