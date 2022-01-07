---
description: Overview of developing Windows drivers for emulated USB devices (UDE)
title: Overview of developing Windows drivers for emulated USB devices (UDE)
ms.date: 10/23/2019
---

# Overview of developing Windows drivers for emulated USB devices (UDE)


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
<p><a href="https://go.microsoft.com/fwlink/p/?linkid=617155" data-raw-source="[Download kits and tools for Windows](https://go.microsoft.com/fwlink/p/?linkid=617155)">Download kits and tools for Windows</a></p>
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
<a href="usb-emulated-device--ude--architecture.md" data-raw-source="[Architecture: USB Device Emulation (UDE)](usb-emulated-device--ude--architecture.md)">Architecture: USB Device Emulation (UDE)</a>
<a href="usb-3-0-driver-stack-architecture.md" data-raw-source="[USB host-side drivers](usb-3-0-driver-stack-architecture.md)">USB host-side drivers</a> in Windows
<p><strong>Writing drivers for emulated host controller and devices</strong></p>
<p>Familiarize yourself with UDE objects and handles. For details on WDF objects, see <a href="/windows-hardware/drivers/wdf/introduction-to-framework-objects" data-raw-source="[Introduction to Framework Objects](../wdf/introduction-to-framework-objects.md)">Introduction to Framework Objects</a>.</p>
<p>Understand the behavior of UDE, how it interacts with the client driver, and the features that the client driver is expected to implement.</p>
<p><a href="writing-a-ude-client-driver.md" data-raw-source="[Write a UDE client driver](writing-a-ude-client-driver.md)">Write a UDE client driver</a></p>
<p><strong>Programming reference sections</strong></p>
<p><a href="/windows-hardware/drivers/ddi/_usbref/#emulated-host-controller-driver-reference" data-raw-source="[Emulated USB host controller driver programming reference](/windows-hardware/drivers/ddi/_usbref/#emulated-host-controller-driver-reference)">Emulated USB host controller driver programming reference</a></p>
<p><a href="/windows-hardware/drivers/ddi/_wdf/" data-raw-source="[WDF Reference](/windows-hardware/drivers/ddi/_wdf/)">WDF Reference</a></p></td>
</tr>
</tbody>
</table>

 

## Related topics
[Universal Serial Bus (USB)](./index.md)
