---
Description: Developing Windows drivers for USB function controllers
title: Developing Windows drivers for USB function controllers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Developing Windows drivers for USB function controllers


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Purpose</strong></p>
<p>This section describes support in the Windows operating system, for developing a Universal Serial Bus (USB) 3.0 function controller driver that communicates with the Microsoft-provided USB function controller extension (UFX).</p>
<p><strong>Development tools and Microsoft-provided binaries</strong></p>
<p>The Windows Driver Kit (WDK) contains resources that are required for driver development, such as headers, libraries, tools, and samples.</p>
<p><a href="http://go.microsoft.com/fwlink/p/?linkid=617155" data-raw-source="[Download kits and tools for Windows](http://go.microsoft.com/fwlink/p/?linkid=617155)">Download kits and tools for Windows</a></p>
<p>To write a function controller driver, you need:</p>
<ul>
<li>UFX (Ufx01000.sys) loaded as the FDO. This driver is included in Windows.</li>
<li>Link to the stub library (Ufx01000.lib). The stub library is in the WDK. The library translates calls made by the function controller driver and pass them up to UFX.</li>
<li>Include Ufxclient.h provided in the WDK.</li>
</ul>
<p>To send requests from user mode, you need:</p>
<ul>
<li>GenericUSBFn.sys loaded as the USB function class driver. This driver is included in Windows.</li>
<li>Include Genericusbfnioctl.h provided in the WDK.</li>
</ul>
<p>To send requests from your USB class driver, you need:</p>
<ul>
<li>UFX (Ufx01000.sys) loaded as the FDO. This driver is included in Windows.</li>
<li>Include Usbfnioctl.h provided in the WDK.</li>
</ul>
To write a filter driver that handles charging through proprietary chargers, you need:
<ul>
<li>Either UfxChipidea.sys or Ufxsynopsys.sys loaded as the client driver to UFX.</li>
<li>Include Ufxproprietarycharger.h provided in the WDK.</li>
</ul></td>
<td><p><strong>Architecture of UFX</strong></p>
<p>Familiarize yourself with the Microsoft-provided USB driver stack:</p>
<a href="usb-device-side-drivers-in-windows.md" data-raw-source="[USB device-side drivers in Windows](usb-device-side-drivers-in-windows.md)">USB device-side drivers in Windows</a>
<p><strong>Familiarize yourself with UFX objects and handles</strong></p>
<p>UFX extends the WDF object functionality to define its own USB-specific UCX objects. For more details on WDF objects, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff544249" data-raw-source="[Introduction to Framework Objects](https://msdn.microsoft.com/library/windows/hardware/ff544249)">Introduction to Framework Objects</a>.</p>
<p>For queuing requests, UFX uses USB-specific objects. For more information, <a href="ufx-objects-and-handles-used-by-a-usb-function-controller.md" data-raw-source="[UFX objects and handles used by a USB function client driver](ufx-objects-and-handles-used-by-a-usb-function-controller.md)">UFX objects and handles used by a USB function client driver</a>.</p>
<p><strong>Writing a function controller client driver</strong></p>
<p>Understand the behavior of UFX, how it interacts with the client driver, and the features that the client driver is expected to implement.</p>
<p><a href="function-client-driver.md" data-raw-source="[Tasks for a function controller client driver](function-client-driver.md)">Tasks for a function controller client driver</a></p>
<p><strong>Programming reference sections</strong></p>
<p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/_usbref/#function-class-driver-reference" data-raw-source="[USB function class driver to UFX programming reference](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/_usbref/#function-class-driver-reference)">USB function class driver to UFX programming reference</a></p>
<p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/_usbref/#usb-function-controller-client-driver-reference" data-raw-source="[USB function controller client driver programming reference](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/_usbref/#usb-function-controller-client-driver-reference)">USB function controller client driver programming reference</a></p>
<p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/_usbref/#filter-driver-for-supporting-usb-chargers" data-raw-source="[USB filter driver for supporting proprietary chargers](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/_usbref/#filter-driver-for-supporting-usb-chargers)">USB filter driver for supporting proprietary chargers</a></p></td>
</tr>
</tbody>
</table>

 

## Related topics
[Universal Serial Bus (USB)](https://msdn.microsoft.com/library/windows/hardware/ff538930)  



