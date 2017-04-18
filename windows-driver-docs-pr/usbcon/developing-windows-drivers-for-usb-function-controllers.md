---
Description: Developing Windows drivers for USB function controllers
title: Developing Windows drivers for USB function controllers
author: windows-driver-content
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
<p>[Download kits and tools for Windows](http://go.microsoft.com/fwlink/p/?linkid=617155)</p>
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
[USB device-side drivers in Windows](usb-device-side-drivers-in-windows.md)
<p><strong>Familiarize yourself with UFX objects and handles</strong></p>
<p>UFX extends the WDF object functionality to define its own USB-specific UCX objects. For more details on WDF objects, see [Introduction to Framework Objects](https://msdn.microsoft.com/library/windows/hardware/ff544249).</p>
<p>For queuing requests, UFX uses USB-specific objects. For more information, [UFX objects and handles used by a USB function client driver](ufx-objects-and-handles-used-by-a-usb-function-controller.md).</p>
<p><strong>Writing a function controller client driver</strong></p>
<p>Understand the behavior of UFX, how it interacts with the client driver, and the features that the client driver is expected to implement.</p>
<p>[Tasks for a function controller client driver](function-client-driver.md)</p>
<p><strong>Programming reference sections</strong></p>
<p>[User mode services to UFX programming reference](https://msdn.microsoft.com/library/windows/hardware/mt188014)</p>
<p>[USB function class driver to UFX programming reference](https://msdn.microsoft.com/library/windows/hardware/mt188008)</p>
<p>[USB function controller client driver programming reference](https://msdn.microsoft.com/library/windows/hardware/mt188010)</p>
<p>[USB filter driver for supporting proprietary chargers](https://msdn.microsoft.com/library/windows/hardware/mt188012)</p></td>
</tr>
</tbody>
</table>

 

## Related topics
[Universal Serial Bus (USB)](https://msdn.microsoft.com/library/windows/hardware/ff538930)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20Developing%20Windows%20drivers%20for%20USB%20function%20controllers%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


