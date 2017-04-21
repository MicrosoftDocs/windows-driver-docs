---
Description: Developing Windows drivers for USB host controllers
title: Developing Windows drivers for USB host controllers
author: windows-driver-content
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Developing Windows drivers for USB host controllers


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Purpose</strong></p>
<p>This section describes support in the Windows operating system, for developing a Universal Serial Bus (USB) host controller driver that communicates with the Microsoft-provided USB host controller extension (UCX).</p>
<p>If you are developing an xHCI host controller that is not compliant with the specification or developing a custom non-xHCI hardware (such as a virtual host controller), you can write a host controller driver that communicates with UCX. For example, consider a wireless dock that supports USB devices. The PC communicates with USB devices through the wireless dock by using USB over TCP as a transport.</p>
<p><strong>USB host controller extension (UCX)</strong></p>
<p>The USB host controller extension is a system-supplied driver (Ucx01000.sys). This driver is implemented as a framework class extension by using the [Windows Driver Framework](https://msdn.microsoft.com/library/windows/hardware/ff557565) programming interfaces. The host controller driver serves as the client driver to that class extension. While a host controller driver handles hardware operations and events, power management, and PnP events, UCX serves as an abstracted interface that queues requests to the host controller driver, and performs other tasks.</p>
<p>UCX is one of the [USB host-side drivers in Windows](usb-3-0-driver-stack-architecture.md). It is loaded as the FDO in the host controller device stack.</p>
<p><strong>USB host controller driver</strong></p>
<p>UCX is extensible and is designed to support various host controller drivers. Windows provides an xHCI driver (Usbxhci.sys) that targets USB xHCI host controllers.</p>
<p>The host controller driver is a client of UCX, written as [Kernel-Mode Driver Framework](https://msdn.microsoft.com/library/windows/hardware/ff551869) (KMDF) driver.</p>
<p><strong>Microsoft-provided binaries</strong></p>
<p>To write a host controller driver, you need UCX (Ucx01000.sys) and the stub library (Ucx01000.lib). The stub library is in the Windows Driver Kit (WDK). The library performs two main functions.</p>
<ul>
<li>Translate calls made by the host controller driver and pass them up to UCX.</li>
<li>Provides support for versioning. A host controller driver will work with UCX, only if UCX has the same Major version number as the host controller driver, and the same or higher Minor version number as the host controller driver.</li>
</ul>
<p><strong>Development tools</strong></p>
<p>The WDK contains resources that are required for driver development, such as headers, libraries, tools, and samples.</p>
<p>[Download kits and tools for Windows](http://go.microsoft.com/fwlink/p/?linkid=617155)</p></td>
<td><p><strong>Get started...</strong></p>
<p>Read the official specification that describes the expected behavior of different components (device, host controller, and hub) of the architecture.</p>
[xHCI for Universal Serial Bus: Specification]( http://go.microsoft.com/fwlink/p/?linkid=618273)
[Official Universal Serial Bus Documents]( http://go.microsoft.com/fwlink/p/?linkid=224892)
<p><strong>Understand the architecture of UCX</strong></p>
<p>Familiarize yourself with the Microsoft-provided USB driver stack:</p>
[USB host-side drivers in Windows](usb-3-0-driver-stack-architecture.md)
[Architecture: USB host controller extension (UCX)](get-started-with-host-controller-driver-development.md)
<p><strong>Familiarize yourself with UCX objects and handles</strong></p>
<p>UCX extends the WDF object functionality to define its own USB-specific UCX objects. For more details on WDF objects, see [Introduction to Framework Objects](https://msdn.microsoft.com/library/windows/hardware/ff544249).</p>
<p>For queuing requests to any underlying host controller driver, UCX uses these objects. For more information, see [UCX objects and handles used by a host controller driver](ucx-objects-and-handles-used-by-host-controller-driver.md).</p>
<p></p>
<dl>
<dt>Host controller object (UCXCONTROLLER)</dt>
<dd><p>Represents the host controller that is created by the host controller driver. The driver must create only one host controller object per host controller instance. Typically created within the [**EVT_WDF_DRIVER_DEVICE_ADD**](https://msdn.microsoft.com/library/windows/hardware/ff541693)callback by calling the [<strong>UcxControllerCreate</strong>](https://msdn.microsoft.com/library/windows/hardware/mt188033) method.</p>
</dd>
<dt>Root hub object (UCXROOTHUB)</dt>
<dd><p>Gets and controls the status of the root ports of the host controller. Created by the host controller driver typically within the [**EVT_WDF_DRIVER_DEVICE_ADD**](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback by calling the [<strong>UcxRootHubCreate</strong>](https://msdn.microsoft.com/library/windows/hardware/mt188048) method.</p>
</dd>
<dt>USB device object (UCXUSBDEVICE)</dt>
<dd><p>Represents a physical USB device connected to the bus. Created by the host controller driver typically within the [<em>EVT_UCX_CONTROLLER_USBDEVICE_ADD</em>](https://msdn.microsoft.com/library/windows/hardware/mt187823) callback by calling the [<strong>UcxUsbDeviceCreate</strong>](https://msdn.microsoft.com/library/windows/hardware/mt188052) method.</p>
</dd>
<dt>Endpoint object (UCXENDPOINT)</dt>
<dd><p>Represents an endpoint on a USB device object. Created by the host controller driver typically within the [<em>EVT_UCX_USBDEVICE_DEFAULT_ENDPOINT_ADD</em>](https://msdn.microsoft.com/library/windows/hardware/mt187839) or [<em>EVT_UCX_USBDEVICE_ENDPOINT_ADD</em>](https://msdn.microsoft.com/library/windows/hardware/mt187843) callback by calling the [<strong>UcxEndpointCreate</strong>](https://msdn.microsoft.com/library/windows/hardware/mt188039) method.</p>
</dd>
<dt>Stream object (UCXSTREAMS)</dt>
<dd><p>Represents a number of pipes to the device across a single bulk endpoint. Created by the host controller driver typically within the [<em>EVT_UCX_ENDPOINT_STATIC_STREAMS_ADD</em>](https://msdn.microsoft.com/library/windows/hardware/mt187830) callback by calling the [<strong>UcxStaticStreamsCreate</strong>](https://msdn.microsoft.com/library/windows/hardware/mt188050) method.</p>
</dd>
</dl>
<p><strong>Documentation sections</strong></p>
[Root hub callback functions of a host controller driver](manage-the-root-hub-in-a-host-controller-driver.md)
<p>UCX handles most operations related to the root hub. This allows the USB hub driver to interact with the root hub in the same way that it interacts with a regular hub. The host controller driver can register its callback functions.</p>
[Handle I/O requests in a USB host controller driver](handling-i-o-requests-in-a-host-controller-driver.md)
<p>UCX triages incoming USB request blocks (URBs), and then forwards them to the correct endpoint queue.</p>
[Configure USB endpoints in a host controller driver](configuring-usb-endpoints-in-a-host-controller-driver.md)
<p>The host controller driver plays a role in UCX’s management of the queues that are associated with its endpoints, and in the programming of endpoints into controller hardware.</p>
[USB host controller extension (UCX) reference](https://msdn.microsoft.com/library/windows/hardware/mt188009)
<p>Gives specifications for I/O requests, support routines, structures, and interfaces used by the client driver. Those routines and related data structures are defined in the WDK headers.</p>
<p>UCX is referred to as the <em>framework class extension</em>.</p>
<p>The host controller driver is referred to as the <em>client driver</em>.</p></td>
</tr>
</tbody>
</table>

 

## Related topics
[Universal Serial Bus (USB)](https://msdn.microsoft.com/library/windows/hardware/ff538930)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20Developing%20Windows%20drivers%20for%20USB%20host%20controllers%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


