---
Description: This section introduces you to USB driver development.
title: Getting started with USB client driver development
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Getting started with USB client driver development


This section introduces you to USB driver development. The section applies to you if you are new to driver development; want to implement a driver for a USB device, for which Microsoft does not provide an in-box driver. Such a driver is termed as a *USB client driver* in this documentation set. The topics in this section describe high-level USB concepts and provide step-by-step instructions about performing common tasks of a USB client driver. For detailed information about those concepts, see USB specifications at [USB Documents](http://go.microsoft.com/fwlink/p/?linkid=617552).

As a driver developer, you must have coding experience in the C programming language, and understand the concepts of function pointers, callback functions, and event handlers. If you are going to write a driver based on the User-Mode Driver Framework, make sure that you familiarize yourself with C++ and COM.

## Learning path for USB client driver developers


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Learning step</th>
<th>After completing the step, you should be able to ...</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>Step 1</strong>—Read the <a href="http://go.microsoft.com/fwlink/p/?linkid=617552" data-raw-source="[Official USB specification version 2.0 and 3.0](http://go.microsoft.com/fwlink/p/?linkid=617552)">Official USB specification version 2.0 and 3.0</a>.</p></td>
<td>Learn about the industry specification and different components (device, host controller, and hub) of the architecture. It&#39;s important to understand the data flow model, how the host and device communicate with each other, and the format of the requests that the device expects.</td>
</tr>
<tr class="even">
<td><p><strong>Step 2</strong>—Obtain a test USB device.</p></td>
<td><ul>
<li>Have a USB device and its hardware specification. The specification describes device capabilities and the supported vendor commands. Use the specification to determine the functionality of the device driver and the related design decisions.</li>
<li>Have the OSR USB FX2 learning kit if you are new to USB driver development. The kit is the most suitable to study USB samples included in this documentation set. You can get the learning kit from <a href="http://go.microsoft.com/fwlink/p/?linkid=617553" data-raw-source="[OSR Online](http://go.microsoft.com/fwlink/p/?linkid=617553)">OSR Online</a>.</li>
<li>Have a Microsoft USB Test Tool (MUTT) devices. MUTT hardware can be purchased from <a href="http://go.microsoft.com/fwlink/p/?linkid=617554" data-raw-source="[JJG Technologies](http://go.microsoft.com/fwlink/p/?linkid=617554)">JJG Technologies</a>. The device does not have installed firmware installed. To install firmware, <a href="http://go.microsoft.com/fwlink/p/?linkid=617555" data-raw-source="[download the MUTT software package](http://go.microsoft.com/fwlink/p/?linkid=617555)">download the MUTT software package</a>, and run MUTTUtil.exe. For more information, see the documentation included with the package.</li>
</ul></td>
</tr>
<tr class="odd">
<td><p><strong>Step 3</strong>—Study your <a href="usb-device-layout.md" data-raw-source="[USB device layout](usb-device-layout.md)">USB device layout</a> and the related <a href="usb-descriptors.md" data-raw-source="[USB descriptors](usb-descriptors.md)">USB descriptors</a>.</p></td>
<td>Describe your device capabilities by reading the configuration descriptor, interface descriptors for each supported alternate settings, and their endpoint descriptors. By using <a href="http://go.microsoft.com/fwlink/p/?linkid=617556" data-raw-source="[USBView](http://go.microsoft.com/fwlink/p/?linkid=617556)">USBView</a>, you can browse all USB controllers and the USB devices connected to them, and also inspect the device configuration.</td>
</tr>
<tr class="even">
<td><p><strong>Step 4</strong>—<a href="winusb-considerations.md" data-raw-source="[Choose a driver model for developing a USB client driver](winusb-considerations.md)">Choose a driver model for developing a USB client driver</a>.</p></td>
<td>Determine whether you should write a custom driver or use one of the Microsoft-provided drivers based on the design of your device. For writing a driver, choose the best driver model and describe the features supported by each model.</td>
</tr>
<tr class="odd">
<td><p><strong>Step 5</strong>—Familiarize yourself with the Microsoft-provided USB driver stack and driver development concepts.</p>
<ul>
<li><a href="usb-3-0-driver-stack-architecture.md" data-raw-source="[USB host-side drivers in Windows](usb-3-0-driver-stack-architecture.md)">USB host-side drivers in Windows</a></li>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/ff554731" data-raw-source="[Concepts for All Driver Developers](https://msdn.microsoft.com/library/windows/hardware/ff554731)">Concepts for All Driver Developers</a></li>
<li><a href="usb-concepts-for-all-developers.md" data-raw-source="[Concepts for all USB developers](usb-concepts-for-all-developers.md)">Concepts for all USB developers</a></li>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/ff554721" data-raw-source="[Device nodes and device stacks](https://msdn.microsoft.com/library/windows/hardware/ff554721)">Device nodes and device stacks</a></li>
<li><em>Developing Drivers with Windows Driver Foundation</em>, written by Penny Orwick and Guy Smith. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/dn605830" data-raw-source="[Developing Drivers with WDF](https://msdn.microsoft.com/library/windows/hardware/dn605830)">Developing Drivers with WDF</a>.</li>
<li><a href="usb-driver-samples-in-wdk.md" data-raw-source="[USB driver samples](usb-driver-samples-in-wdk.md)">USB driver samples</a></li>
</ul></td>
<td><ul>
<li>Understand the fundamentals of how drivers work in Windows operating systems. Knowing the fundamentals will help you make appropriate design decisions and allow you to streamline your development process.</li>
<li>Differentiate between user mode and kernel mode driver architecture models.</li>
<li>Understand driver loading and how Windows organizes Plug and Play (PnP) devices in a device tree and device nodes. You should also understand how PnP manager builds device stacks and where your driver and its device objects are placed in the device stack.</li>
</ul></td>
</tr>
<tr class="even">
<td><p><strong>Step 6</strong>—Prepare your development and debugging environment.</p>
<ul>
<li><a href="http://go.microsoft.com/fwlink/p/?linkid=617580" data-raw-source="[Install the latest Windows Driver Kit (WDK)](http://go.microsoft.com/fwlink/p/?linkid=617580)">Install the latest Windows Driver Kit (WDK)</a>.</li>
<li><a href="http://go.microsoft.com/fwlink/p/?linkid=617580" data-raw-source="[Install Microsoft Visual Studio 2012](http://go.microsoft.com/fwlink/p/?linkid=617580)">Install Microsoft Visual Studio 2012</a>.</li>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh450944" data-raw-source="[Get Set Up for Debugging](https://msdn.microsoft.com/library/windows/hardware/hh450944)">Get Set Up for Debugging</a>.</li>
<li>Make sure that you have the <a href="headers-and-libraries-for-a-usb-client-driver.md" data-raw-source="[Headers and libraries required by a USB client driver](headers-and-libraries-for-a-usb-client-driver.md)">Headers and libraries required by a USB client driver</a>.</li>
</ul></td>
<td><ul>
<li>If you are writing a kernel-mode driver, you should have configured debugging on host and target computers over an Ethernet network, 1394 cable, USB 2.0 or 3.0 debug cable, or a null-modem cable.</li>
<li>If you are writing a user-mode driver, you can use the user-mode debuggers available in the Microsoft Visual Studio environment. You should know <a href="https://msdn.microsoft.com/library/windows/hardware/hh406273" data-raw-source="[how to attach to a process or launch a process under the debugger](https://msdn.microsoft.com/library/windows/hardware/hh406273)">how to attach to a process or launch a process under the debugger</a>.</li>
</ul></td>
</tr>
<tr class="odd">
<td><p><strong>Step 7</strong>—Write your first driver.</p>
<ul>
<li><a href="tutorial--write-your-first-usb-client-driver--kmdf-.md" data-raw-source="[How to write your first USB client driver (KMDF)](tutorial--write-your-first-usb-client-driver--kmdf-.md)">How to write your first USB client driver (KMDF)</a></li>
<li><a href="implement-driver-entry-for-a-usb-driver--umdf-.md" data-raw-source="[How to write your first USB client driver (UMDF)](implement-driver-entry-for-a-usb-driver--umdf-.md)">How to write your first USB client driver (UMDF)</a></li>
</ul></td>
<td>Write, build, and install your first USB client driver by using the USB templates included with Visual Studio 2012. You should be able to describe framework driver, device, and queue objects and understand how the framework communicates with your driver.</td>
</tr>
<tr class="even">
<td><strong>Step 8</strong>—Extend your driver by sending a USB control transfer request.</td>
<td>Send standard control requests and vendor commands to your device. For more information, see <a href="usb-control-transfer.md" data-raw-source="[How to send a USB control transfer](usb-control-transfer.md)">How to send a USB control transfer</a>.</td>
</tr>
<tr class="odd">
<td><p><strong>Step 9</strong>—Extend your driver to use WDF USB I/O target objects to perform USB data transfers. <a href="usb-device-i-o.md" data-raw-source="[USB data transfers](usb-device-i-o.md)">USB data transfers</a>.</p></td>
<td><p>Extend your driver to perform common tasks. This topic lists the &quot;How to&quot; topics in this documentation set that provide step-by-step guidance about those tasks.</p>
<ul>
<li><a href="wdk-resources-for-usb-driver-development.md" data-raw-source="[Common tasks for USB client drivers](wdk-resources-for-usb-driver-development.md)">Common tasks for USB client drivers</a></li>
</ul></td>
</tr>
</tbody>
</table>

 

## Community Resources for USB


<a href="" id="microsoft-windows-usb-core-team-blog"></a>[Microsoft Windows USB Core Team Blog](http://go.microsoft.com/fwlink/p/?linkid=617581)  
Check out posts written by the Microsoft USB Team. The blog focuses on the Windows USB driver stack that works with various USB Host controllers and USB hubs found in Windows PC. A useful resource for USB client driver developers and USB hardware designers understand the driver stack implementation, resolve common issues, and explain how to use tools for gathering traces and log files.

<a href="" id="osr-online-lists---ntdev"></a>[OSR Online Lists - ntdev](http://go.microsoft.com/fwlink/p/?linkid=617582)  
Discussion list managed by [OSR Online](http://go.microsoft.com/fwlink/p/?linkid=617590) for kernel-mode driver developers.

<a href="" id="usb-technologies"></a>[USB Technologies](http://go.microsoft.com/fwlink/p/?linkid=617583)  
Miscellaneous resources based on frequently asked questions from developers who are new to developing USB devices and drivers that work with Windows operating systems.

<a href="" id="windows-dev-center-for-hardware-development"></a>[Windows Dev-Center for Hardware Development](http://go.microsoft.com/fwlink/p/?linkid=617584)  
[Download the latest tools for driver development](http://go.microsoft.com/fwlink/p/?linkid=617585), ensure that your product is reliable and compatible with Windows through the [Windows Certification Program](http://go.microsoft.com/fwlink/p/?linkid=617591), learn [Windows driver samples](http://go.microsoft.com/fwlink/p/?LinkId=616507).

## Related topics
[Universal Serial Bus (USB) Drivers](https://msdn.microsoft.com/library/windows/hardware/ff538930)  
[How to enable USB selective suspend and system wake in the UMDF driver for a USB device](http://go.microsoft.com/fwlink/p/?linkid=617587)  
[USB Driver Development Guide](usb-driver-development-guide.md)  



