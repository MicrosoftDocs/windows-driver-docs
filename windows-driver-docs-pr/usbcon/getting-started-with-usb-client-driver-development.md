---
Description: 'This section introduces you to USB driver development.'
MS-HAID: 'buses.getting\_started\_with\_usb\_client\_driver\_development'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
title: Getting started with USB client driver development
author: windows-driver-content
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
<td><p><strong>Step 1</strong>—Read the [Official USB specification version 2.0 and 3.0](http://go.microsoft.com/fwlink/p/?linkid=617552).</p></td>
<td>Learn about the industry specification and different components (device, host controller, and hub) of the architecture. It's important to understand the data flow model, how the host and device communicate with each other, and the format of the requests that the device expects.</td>
</tr>
<tr class="even">
<td><p><strong>Step 2</strong>—Obtain a test USB device.</p></td>
<td><ul>
<li>Have a USB device and its hardware specification. The specification describes device capabilities and the supported vendor commands. Use the specification to determine the functionality of the device driver and the related design decisions.</li>
<li>Have the OSR USB FX2 learning kit if you are new to USB driver development. The kit is the most suitable to study USB samples included in this documentation set. You can get the learning kit from [OSR Online](http://go.microsoft.com/fwlink/p/?linkid=617553).</li>
<li>Have a Microsoft USB Test Tool (MUTT) devices. MUTT hardware can be purchased from [JJG Technologies](http://go.microsoft.com/fwlink/p/?linkid=617554). The device does not have installed firmware installed. To install firmware, [download the MUTT software package](http://go.microsoft.com/fwlink/p/?linkid=617555), and run MUTTUtil.exe. For more information, see the documentation included with the package.</li>
</ul></td>
</tr>
<tr class="odd">
<td><p><strong>Step 3</strong>—Study your [USB device layout](usb-device-layout.md) and the related [USB descriptors](usb-descriptors.md).</p></td>
<td>Describe your device capabilities by reading the configuration descriptor, interface descriptors for each supported alternate settings, and their endpoint descriptors. By using [USBView](http://go.microsoft.com/fwlink/p/?linkid=617556), you can browse all USB controllers and the USB devices connected to them, and also inspect the device configuration.</td>
</tr>
<tr class="even">
<td><p><strong>Step 4</strong>—[Choose a driver model for developing a USB client driver](winusb-considerations.md).</p></td>
<td>Determine whether you should write a custom driver or use one of the Microsoft-provided drivers based on the design of your device. For writing a driver, choose the best driver model and describe the features supported by each model.</td>
</tr>
<tr class="odd">
<td><p><strong>Step 5</strong>—Familiarize yourself with the Microsoft-provided USB driver stack and driver development concepts.</p>
<ul>
<li>[USB host-side drivers in Windows](usb-3-0-driver-stack-architecture.md)</li>
<li>[Concepts for All Driver Developers](https://msdn.microsoft.com/library/windows/hardware/ff554731)</li>
<li>[Concepts for all USB developers](usb-concepts-for-all-developers.md)</li>
<li>[Device nodes and device stacks](https://msdn.microsoft.com/library/windows/hardware/ff554721)</li>
<li><em>Developing Drivers with Windows Driver Foundation</em>, written by Penny Orwick and Guy Smith. For more information, see [Developing Drivers with WDF](https://msdn.microsoft.com/library/windows/hardware/dn605830).</li>
<li>[USB driver samples](usb-driver-samples-in-wdk.md)</li>
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
<li>[Install the latest Windows Driver Kit (WDK)](http://go.microsoft.com/fwlink/p/?linkid=617580).</li>
<li>[Install Microsoft Visual Studio 2012](http://go.microsoft.com/fwlink/p/?linkid=617580).</li>
<li>[Get Set Up for Debugging](https://msdn.microsoft.com/library/windows/hardware/hh450944).</li>
<li>Make sure that you have the [Headers and libraries required by a USB client driver](headers-and-libraries-for-a-usb-client-driver.md).</li>
</ul></td>
<td><ul>
<li>If you are writing a kernel-mode driver, you should have configured debugging on host and target computers over an Ethernet network, 1394 cable, USB 2.0 or 3.0 debug cable, or a null-modem cable.</li>
<li>If you are writing a user-mode driver, you can use the user-mode debuggers available in the Microsoft Visual Studio environment. You should know [how to attach to a process or launch a process under the debugger](https://msdn.microsoft.com/library/windows/hardware/hh406273).</li>
</ul></td>
</tr>
<tr class="odd">
<td><p><strong>Step 7</strong>—Write your first driver.</p>
<ul>
<li>[How to write your first USB client driver (KMDF)](tutorial--write-your-first-usb-client-driver--kmdf-.md)</li>
<li>[How to write your first USB client driver (UMDF)](implement-driver-entry-for-a-usb-driver--umdf-.md)</li>
</ul></td>
<td>Write, build, and install your first USB client driver by using the USB templates included with Visual Studio 2012. You should be able to describe framework driver, device, and queue objects and understand how the framework communicates with your driver.</td>
</tr>
<tr class="even">
<td><strong>Step 8</strong>—Extend your driver by sending a USB control transfer request.</td>
<td>Send standard control requests and vendor commands to your device. For more information, see [How to send a USB control transfer](usb-control-transfer.md).</td>
</tr>
<tr class="odd">
<td><p><strong>Step 9</strong>—Extend your driver to use WDF USB I/O target objects to perform USB data transfers. [USB data transfers](usb-device-i-o.md).</p></td>
<td><p>Extend your driver to perform common tasks. This topic lists the &quot;How to&quot; topics in this documentation set that provide step-by-step guidance about those tasks.</p>
<ul>
<li>[Common tasks for USB client drivers](wdk-resources-for-usb-driver-development.md)</li>
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

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20Getting%20started%20with%20USB%20client%20driver%20development%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


