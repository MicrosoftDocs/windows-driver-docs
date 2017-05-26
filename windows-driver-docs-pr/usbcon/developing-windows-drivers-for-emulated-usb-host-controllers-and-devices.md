---
Description: Developing Windows drivers for emulated USB devices (UDE)
title: Developing Windows drivers for emulated USB devices (UDE)
author: windows-driver-content
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Developing Windows drivers for emulated USB devices (UDE)


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Purpose</strong></p>
<p>This section describes USB emulated device (UDE) support in the Windows operating system, for developing an emulated Universal Serial Bus (USB) host controller driver and a connected virtual USB device. Both components are combined into a single KMDF driver that communicates with the Microsoft-provided USB device emulation class extension (UdeCx).</p>
<p><strong>Development tools and Microsoft-provided binaries</strong></p>
<p>The Windows Driver Kit (WDK) contains resources that are required for driver development, such as headers, libraries, tools, and samples.</p>
<p>[Download kits and tools for Windows](http://go.microsoft.com/fwlink/p/?linkid=617155)</p>
<p>To write a function controller driver, you need:</p>
<ul>
<li>UdeCx: (udecx.sys) a WDF extension used by the function driver. This extension is included in Windows.</li>
<li>Link to the stub library (Udecxstub.lib). The stub library is in the WDK.</li>
<li>Include Udecx.h provided in the WDK.</li>
</ul>
<p><strong>Version history</strong></p>
<p></p>
<dl>
<dt><a href=""></a>Windows 10</dt>
<dd><p>UDE version 1.0.</p>
<p>KMDF version 1.15.</p>
<p>UMDF is not supported.</p>
</dd>
</dl></td>
<td><p><strong>Architecture of UDE</strong></p>
[Architecture: USB Device Emulation (UDE)](usb-emulated-device--ude--architecture.md)
[USB host-side drivers](usb-3-0-driver-stack-architecture.md) in Windows
<p><strong>Writing drivers for emulated host controller and devices</strong></p>
<p>Familiarize yourself with UDE objects and handles. For details on WDF objects, see [Introduction to Framework Objects](https://msdn.microsoft.com/library/windows/hardware/ff544249).</p>
<p>Understand the behavior of UDE, how it interacts with the client driver, and the features that the client driver is expected to implement.</p>
<p>[Write a UDE client driver](writing-a-ude-client-driver.md)</p>
<p><strong>Programming reference sections</strong></p>
<p>[Emulated USB host controller driver programming reference](https://msdn.microsoft.com/library/windows/hardware/mt628025)</p>
<p>[WDF Reference](https://msdn.microsoft.com/library/windows/hardware/dn265590)</p></td>
</tr>
</tbody>
</table>

 

## Related topics
[Universal Serial Bus (USB)](https://msdn.microsoft.com/library/windows/hardware/ff538930)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20Developing%20Windows%20drivers%20for%20emulated%20USB%20devices%20%28UDE%29%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


