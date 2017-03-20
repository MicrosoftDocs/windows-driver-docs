---
Description: 'PurposeThis section describes Universal Serial Bus (USB) support in the Windows operating system, so that you can develop USB device drivers that are interoperable with Windows.'
MS-HAID: 'buses.usb\_driver\_development\_guide'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
title: Developing Windows client drivers for USB devices
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
<p>USB devices are peripherals, such as mouse devices and keyboards, that are connected to a computer through a single port. A USB client driver is the software installed on the computer that communicates with the hardware to make the device function. If the device belongs to a device class supported by Microsoft, Windows loads one of the [Microsoft-provided USB drivers](system-supplied-usb-drivers.md) (in-box class drivers) for the device. Otherwise, a custom client driver must be provided by the hardware manufacturer or a third party vendor. The user installs the client driver for the device when the device is first detected by Windows. After successful installation, Windows loads the client driver every time the device is attached and unloads the driver when the device is detached from the host computer.</p>
<p>You can develop a custom client driver for a USB device by using the [Windows Driver Frameworks](https://msdn.microsoft.com/library/windows/hardware/ff557565) (WDF) or the [Windows Driver Model](https://msdn.microsoft.com/library/windows/hardware/ff565698) (WDM). Instead of communicating with the hardware directly, most client drivers send their requests to the Microsoft-provided USB driver stack that makes hardware abstraction layer (HAL) function calls to send the client driver's request to the hardware. The topics in this section describe the typical requests that a client driver can send and the device driver interfaces (DDIs) that the client driver must call to create those requests.</p>
<p><strong>Developer audience</strong></p>
<p>A client driver for a USB device is a WDF or WDM driver that communicates with the device through DDIs exposed by the USB driver stack. This section is intended for use by C/C++ programmers who are familiar with WDM. Before you use this section, you should understand basic driver development. For more information, see [Getting Started with Windows Drivers](https://msdn.microsoft.com/library/windows/hardware/ff554690). For WDF drivers, the client driver can use [Kernel-Mode Driver Framework](https://msdn.microsoft.com/library/windows/hardware/ff551869) (KMDF) or [User-Mode Driver Framework](https://msdn.microsoft.com/library/windows/hardware/ff557565) (UMDF) interfaces designed specifically to work with USB targets. For more information about the USB-specific interfaces, see [WDF USB Reference](https://msdn.microsoft.com/library/windows/hardware/dn265671) and [UMDF USB I/O Target Interfaces](https://msdn.microsoft.com/library/windows/hardware/ff561332).</p>
<p><strong>Development tools</strong></p>
<p>The Windows Driver Kit (WDK) contains resources that are required for driver development, such as headers, libraries, tools, and samples.</p>
<p>[Download kits and tools for Windows](http://go.microsoft.com/fwlink/p/?linkid=617155)</p>
<p><strong>USB programming reference</strong></p>
<p>Gives specifications for I/O requests, support routines, structures, and interfaces used by USB client drivers. Those routines and related data structures are defined in the WDK headers.</p>
<p><strong>USB driver samples</strong></p>
<p>Use these samples to get started with USB client driver programming.</p>
<ul>
<li>[Usbsamp Generic USB Driver]( http://go.microsoft.com/fwlink/p/?linkid=617157)</li>
<li>[Sample KMDF Function Driver for OSR USB-FX2](http://go.microsoft.com/fwlink/p/?linkid=617158)</li>
<li>[Sample UMDF Function Driver for OSR USB-FX2](http://go.microsoft.com/fwlink/p/?LinkId=618002)</li>
</ul>
<p><strong>Related standards and specifications</strong></p>
<p>You can download official USB specifications from the [Universal Serial Bus Documents]( http://go.microsoft.com/fwlink/p/?linkid=224892) website. This website contains links to the Universal Serial Bus Revision 3.0 Specification and the Universal Serial Bus Revision 2.0 specification.</p></td>
<td><p><strong>Documentation sections</strong></p>
<p>[Getting started with USB client driver development](getting-started-with-usb-client-driver-development.md)</p>
Introduces you to USB driver development. Provides information about choosing the most appropriate model for providing a USB driver for your device.
Write, build, and install your first skeleton user-mode and kernel-mode USB drivers by using the USB templates included with Microsoft Visual Studio.
<p>[USB host-side drivers in Windows](usb-3-0-driver-stack-architecture.md)</p>
Provides an overview of the USB driver stack architecture.
<p>[About USB Block Requests (URBs)](communicating-with-a-usb-device.md)</p>
Learn how a client driver builds a variable-length data structure called a USB Request Block (URB) to submit requests to the USB driver stack.
<p>[USB descriptors](usb-descriptors.md)</p>
Learn how a client driver builds a variable-length data structure called a USB Request Block (URB) to submit requests to the USB driver stack.
<p>[Selecting a USB configuration in USB drivers](configuring-usb-devices.md)</p>
Device configuration refers to the tasks that the client driver performs to select a USB configuration and an alternate interface in each interface. The section shows the methods calls required to select a USB configuration.
<p>[Sending USB data transfers in USB client drivers](usb-device-i-o.md)</p>
Device configuration refers to the tasks that the client driver performs to select a USB configuration and an alternate interface in each interface. The section shows the methods calls required to select a USB configuration.
<p>[Implementing power management in USB client drivers](usb-power-management.md)</p>
Use the power management abilities of USB devices that comply with the Universal Serial Bus (USB) specification have a rich and complex set of power management features.</td>
</tr>
</tbody>
</table>

 

## Related topics


****
[Universal Serial Bus (USB)](https://msdn.microsoft.com/library/windows/hardware/ff538930)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20Developing%20Windows%20client%20drivers%20for%20USB%20devices%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




