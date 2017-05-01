---
Description: Universal Serial Bus (USB) provides an expandable, hot-pluggable Plug and Play serial interface that ensures a standard, low-cost connection for peripheral devices such as keyboards, mice, joysticks, printers, scanners, storage devices, modems, and video conferencing cameras. Migration to USB is recommended for all peripheral devices that use legacy ports such as PS/2, serial, and parallel ports. The USB-IF is a Special Interest Groups (SIGs) that maintains the Official USB Specification, test specifications and tools. Windows operating systems include native support for USB host controllers, hubs, and devices and systems that comply with the official USB specification. Windows also provides programming interfaces that you can use to develop device drivers and applications that communicate with a USB device.
title: Universal Serial Bus (USB)
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Universal Serial Bus (USB)


Universal Serial Bus (USB) provides an expandable, hot-pluggable Plug and Play serial interface that ensures a standard, low-cost connection for peripheral devices such as keyboards, mice, joysticks, printers, scanners, storage devices, modems, and video conferencing cameras. Migration to USB is recommended for all peripheral devices that use legacy ports such as PS/2, serial, and parallel ports.

The USB-IF is a Special Interest Groups (SIGs) that maintains the [Official USB Specification](http://www.usb.org/developers/docs/), test specifications and tools.

Windows operating systems include native support for USB host controllers, hubs, and devices and systems that comply with the official USB specification. Windows also provides programming interfaces that you can use to develop [device drivers](usb-driver-development-guide.md) and [applications](developing-windows-applications-that-communicate-with-a-usb-device.md) that communicate with a USB device.

[![usb for device builders](images/icon-dev.png)](building-usb-devices-for-windows.md)[![usb for driver developers](images/icon-driver.png)](usb-driver-development-guide.md)[![usb for app developers](images/icon-app.png)](developing-windows-applications-that-communicate-with-a-usb-device.md)[![usb hck certification](images/icon-cert.png)](windows-hardware-certification-kit-tests-for-usb.md)

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>USB in Windows</strong>
<p></p>
[Windows 10: What's new for USB](windows-10--what-s-new-for-usb.md)
<p>Overview of new features and improvements in USB in Windows 10.</p>
[USB FAQ](usb-faq--introductory-level.md)
<p>Frequently asked questions from driver developers about the USB stack and features that are supported in USB.</p>
[Microsoft OS Descriptors for USB Devices](microsoft-defined-usb-descriptors.md)
<p>Windows defines MS OS descriptors that allows better enumeration when connected to system running Windows operating system</p>
<strong>Microsoft-provided USB drivers</strong>
<p></p>
[USB device-side drivers in Windows](usb-device-side-drivers-in-windows.md)
<p>A set of drivers for handling common function logic for USB devices.</p>
[USB host-side drivers in Windows](usb-3-0-driver-stack-architecture.md)
<p>Microsoft provides a core stack of drivers that interoperate with devices that are connected to EHCI and xHCI controllers.</p>
[USB-IF device class drivers](supported-usb-classes.md)
<p>Windows provides in-box device class drivers for many USB-IF approved device classes, audio, mass storage, and so on.</p>
[USB generic function driver–WinUSB](winusb.md)
<p>Windows provides Winusb.sys that can be loaded as a function driver for a custom device and a function of a composite device.</p>
[USB generic parent driver for composite devices–Usbccgp](usb-common-class-generic-parent-driver.md)
<p>Parent driver for USB devices with multiple functions. Usbccgp creates physical device objects (PDOs) for each of those functions. Those individual PDOs are managed by their respective USB function drivers, which could be the Winusb.sys driver or a USB device class driver.</p>
<strong>WDF extension for developing USB drivers</strong>
<ul>
<li>[USB connector manager class extension (UcmCx)](https://msdn.microsoft.com/library/windows/hardware/mt188011)</li>
<li>[USB host controller extension (UCX) reference](https://msdn.microsoft.com/library/windows/hardware/mt188009)</li>
<li>[USB function class extension (UFX) reference](https://msdn.microsoft.com/library/windows/hardware/mt188013)</li>
</ul>
<strong>Testing USB devices with Windows</strong>
<p></p>
[Testing USB hardware, drivers, and apps in Windows](usb-driver-testing-guide.md)
<p>Get information about the tools that you can use to test your USB hardware or software, capture traces of operations and other system events, and observe how the USB driver stack responds to a request sent by a client driver or an application.</p>
<p>Read an overview of tests in the Hardware Certification Kit that enable hardware vendors and device manufacturers to prepare their USB devices and host controllers for Windows Hardware Certification submission.</p>
<p><strong>Other Resources for USB</strong></p>
[Official USB Specification](http://www.usb.org/developers/docs/)
<p>Provides complete technical details for the USB protocol.</p>
[Microsoft Windows USB Core Team Blog](http://blogs.msdn.com/b/usbcoreblog/)
<p>Check out posts written by the Microsoft USB Team. The blog focuses on the Windows USB driver stack that works with various USB Host controllers and USB hubs found in Windows PC. A useful resource for USB client driver developers and USB hardware designers understand the driver stack implementation, resolve common issues, and explain how to use tools for gathering traces and log files.</p>
[OSR Online Lists - ntdev](http://www.osronline.com/cf.cfm?PageURL=showlists.cfm?list=NTDEV)
<p>Discussion list managed by [OSR Online](http://www.osronline.com/index.cfm) for kernel-mode driver developers.</p>
[Windows Dev-Center for Hardware Development](https://msdn.microsoft.com/windows/hardware/)
<p>Miscellaneous resources based on frequently asked questions from developers who are new to developing USB devices and drivers that work with Windows operating systems.</p>
<p></p>
<p><strong>USB-related videos</strong></p>
[Windows Store apps for USB devices](http://channel9.msdn.com/Events/Build/2013/3-924a)
[Understanding USB 3.0 in Windows 8](http://channel9.msdn.com/events/BUILD/BUILD2011/HW-256T)
[Building great USB 3.0 devices](http://channel9.msdn.com/events/BUILD/BUILD2011/HW-773T)
[USB Debugging Innovations in Windows 8 (Part I, II, &amp; III)](http://channel9.msdn.com/events/BUILD/BUILD2011/HW-258P)
<p><strong>USB hardware for learning</strong></p>
[MUTT devices](microsoft-usb-test-tool--mutt--devices.md)
<p>MUTT and SuperMUTT devices and the accompanying software package are integrated into the HCK suite of USB tests. They provide automated testing that can be used during the development cycle of USB controllers, devices and systems, especially stress testing.</p>
[OSR USB FX2 Learning Kit](http://www.osronline.com/index.cfm)
<p>If you are new to USB driver development. The kit is the most suitable to study USB samples included in this documentation set. You can get the learning kit from OSR Online Store.</p></td>
<td><strong>Write a USB client driver (KMDF, UMDF)</strong>
<p>Introduces you to USB driver development. Provides information about choosing the most appropriate model for providing a USB driver for your device. This section also includes tutorials about writing your first user-mode and kernel-mode USB drivers by using the USB templates included with Microsoft Visual Studio.</p>
<p>[Getting started with USB client driver development](getting-started-with-usb-client-driver-development.md)</p>
<p>[USB device driver programming reference](https://msdn.microsoft.com/library/windows/hardware/ff540134)</p>
<strong>Write a USB host controller driver</strong>
<p>If you are developing an xHCI host controller that is not compliant with the specification or developing a custom non-xHCI hardware (such as a virtual host controller), you can write a host controller driver that communicates with UCX. For example, consider a wireless dock that supports USB devices. The PC communicates with USB devices through the wireless dock by using USB over TCP as a transport.</p>
<p>[Developing Windows drivers for USB host controllers](developing-windows-drivers-for-usb-host-controllers.md)</p>
<p>[USB host controller driver programming reference](https://msdn.microsoft.com/library/windows/hardware/mt188009)</p>
<strong>Write a function controller driver for a USB device</strong>
<p>You can develop a controller driver that handles all USB data transfers and commands sent by the host to the device. This driver communicates with the Microsoft-provided USB function controller extension (UFX).</p>
<p>[Developing Windows drivers for USB function controllers](developing-windows-drivers-for-usb-function-controllers.md)</p>
<p>[USB function controller programming reference](https://msdn.microsoft.com/library/windows/hardware/mt188013)</p>
<strong>Write a USB Type-C connector driver</strong>
<p>Windows 10 introduces support for the new USB connector: USB Type-C. You can write a driver for the connector that communicates with the Microsoft-provided class extension module: UcmCx to handle scenarios related to Type-C connectors such as, which ports support Type-C, which ports support power delivery.</p>
<p>[Developing Windows drivers for USB Type-C connectors](developing-windows-drivers-for-usb-type-c-connectors.md)</p>
<p>[USB connector manager class extension (UcmCx) reference](https://msdn.microsoft.com/library/windows/hardware/mt188011)</p>
<strong>Write a USB dual-role controller driver</strong>
<p>USB Dual Role controllers are now supported in Windows 10. Windows includes in-box client drivers for ChipIdea and Synopsys controllers. For other controllers, Microsoft provides a set of programming interfaces that allow the dual-role class extension (UrsCx) and its client driver to communicate with each other to handle the role-switching capability of a dual-role controller.</p>
<p>For more information about this feature, see:</p>
<p>[USB Dual Role Driver Stack Architecture](usb-dual-role-driver-stack-architecture.md)</p>
<p>[USB dual-role controller driver programming reference](https://msdn.microsoft.com/library/windows/hardware/mt628026)</p>
<strong>Write a USB driver for emulated devices</strong>
<p>Windows 10 introduces support for emulated devices. Now you can develop an emulated Universal Serial Bus (USB) host controller driver and a connected virtual USB device. Both components are combined into a single KMDF driver that communicates with the Microsoft-provided USB device emulation class extension (UdeCx).</p>
<p>[Developing Windows drivers for emulated USB devices (UDE)](developing-windows-drivers-for-emulated-usb-host-controllers-and-devices.md)</p>
<p>[Emulated USB host controller driver programming reference](https://msdn.microsoft.com/library/windows/hardware/mt628025)</p>
<strong>Write a Windows Store app</strong>
<p>Provides step-by-step instructions about implementing USB features in a Windows Store app. To write such an app for a USB device you need Visual Studio and Microsoft Windows Software Development Kit (SDK) .</p>
<p>[Talk to USB devices, start to finish](talking-to-usb-devices-start-to-finish.md)</p>
<p>[<strong>Windows.Devices.Usb</strong>](https://docs.microsoft.com/uwp/api/Windows.Devices.Usb)</p>
<strong>Write a Windows desktop app</strong>
<p>Describes how an application can call WinUSB Functions to communicate with a USB device.</p>
<p>[Write a WinUSB application](how-to-write-a-windows-desktop-app-that-communicates-with-a-usb-device.md)</p>
<p>[<strong>WinUSB Functions</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540046#winusb)</p>
[Common programming scenarios](wdk-resources-for-usb-driver-development.md)
<p>List of common tasks that a driver or an app performs in order to communicate with a USB device. Get quick info about the programming interfaces you need for each task.</p>
<p></p>
<p><strong>USB samples</strong></p>
<p>[Windows Store app samples for USB](http://go.microsoft.com/fwlink/p/?LinkID=309716)</p>
<p>[Windows driver samples for USB](http://go.microsoft.com/fwlink/p/?linkid=618021)</p>
<p><strong>Development tools</strong></p>
[Download kits and tools for Windows]( http://go.microsoft.com/fwlink/p/?linkid=619491)</td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdknodes\wdknodes%5D:%20Universal%20Serial%20Bus%20%28USB%29%20%20RELEASE:%20%282/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


