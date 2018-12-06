---
Description: Developing Windows drivers for USB host controllers
title: Developing Windows drivers for USB host controllers
ms.date: 04/20/2017
ms.localizationpriority: medium
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
<p>The USB host controller extension is a system-supplied driver (Ucx01000.sys). This driver is implemented as a framework class extension by using the <a href="https://docs.microsoft.com/windows-hardware/drivers/wdf/" data-raw-source="[Windows Driver Framework](https://docs.microsoft.com/windows-hardware/drivers/wdf/)">Windows Driver Framework</a> programming interfaces. The host controller driver serves as the client driver to that class extension. While a host controller driver handles hardware operations and events, power management, and PnP events, UCX serves as an abstracted interface that queues requests to the host controller driver, and performs other tasks.</p>
<p>UCX is one of the <a href="usb-3-0-driver-stack-architecture.md" data-raw-source="[USB host-side drivers in Windows](usb-3-0-driver-stack-architecture.md)">USB host-side drivers in Windows</a>. It is loaded as the FDO in the host controller device stack.</p>
<p><strong>USB host controller driver</strong></p>
<p>UCX is extensible and is designed to support various host controller drivers. Windows provides an xHCI driver (Usbxhci.sys) that targets USB xHCI host controllers.</p>
<p>The host controller driver is a client of UCX, written as <a href="https://msdn.microsoft.com/library/windows/hardware/ff551869" data-raw-source="[Kernel-Mode Driver Framework](https://msdn.microsoft.com/library/windows/hardware/ff551869)">Kernel-Mode Driver Framework</a> (KMDF) driver.</p>
<p><strong>Microsoft-provided binaries</strong></p>
<p>To write a host controller driver, you need UCX (Ucx01000.sys) and the stub library (Ucx01000.lib). The stub library is in the Windows Driver Kit (WDK). The library performs two main functions.</p>
<ul>
<li>Translate calls made by the host controller driver and pass them up to UCX.</li>
<li>Provides support for versioning. A host controller driver will work with UCX, only if UCX has the same Major version number as the host controller driver, and the same or higher Minor version number as the host controller driver.</li>
</ul>
<p><strong>Development tools</strong></p>
<p>The WDK contains resources that are required for driver development, such as headers, libraries, tools, and samples.</p>
<p><a href="http://go.microsoft.com/fwlink/p/?linkid=617155" data-raw-source="[Download kits and tools for Windows](http://go.microsoft.com/fwlink/p/?linkid=617155)">Download kits and tools for Windows</a></p></td>
<td><p><strong>Get started...</strong></p>
<p>Read the official specification that describes the expected behavior of different components (device, host controller, and hub) of the architecture.</p>
<a href="http://go.microsoft.com/fwlink/p/?linkid=618273" data-raw-source="[xHCI for Universal Serial Bus: Specification]( http://go.microsoft.com/fwlink/p/?linkid=618273)">xHCI for Universal Serial Bus: Specification</a>
<a href="http://go.microsoft.com/fwlink/p/?linkid=224892" data-raw-source="[Official Universal Serial Bus Documents]( http://go.microsoft.com/fwlink/p/?linkid=224892)">Official Universal Serial Bus Documents</a>
<p><strong>Understand the architecture of UCX</strong></p>
<p>Familiarize yourself with the Microsoft-provided USB driver stack:</p>
<a href="usb-3-0-driver-stack-architecture.md" data-raw-source="[USB host-side drivers in Windows](usb-3-0-driver-stack-architecture.md)">USB host-side drivers in Windows</a>
<a href="get-started-with-host-controller-driver-development.md" data-raw-source="[Architecture: USB host controller extension (UCX)](get-started-with-host-controller-driver-development.md)">Architecture: USB host controller extension (UCX)</a>
<p><strong>Familiarize yourself with UCX objects and handles</strong></p>
<p>UCX extends the WDF object functionality to define its own USB-specific UCX objects. For more details on WDF objects, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff544249" data-raw-source="[Introduction to Framework Objects](https://msdn.microsoft.com/library/windows/hardware/ff544249)">Introduction to Framework Objects</a>.</p>
<p>For queuing requests to any underlying host controller driver, UCX uses these objects. For more information, see <a href="ucx-objects-and-handles-used-by-host-controller-driver.md" data-raw-source="[UCX objects and handles used by a host controller driver](ucx-objects-and-handles-used-by-host-controller-driver.md)">UCX objects and handles used by a host controller driver</a>.</p>
<p></p>
<dl>
<dt>Host controller object (UCXCONTROLLER)</dt>
<dd><p>Represents the host controller that is created by the host controller driver. The driver must create only one host controller object per host controller instance. Typically created within the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541693" data-raw-source="[**EVT_WDF_DRIVER_DEVICE_ADD**](https://msdn.microsoft.com/library/windows/hardware/ff541693)"><strong>EVT_WDF_DRIVER_DEVICE_ADD</strong></a>callback by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/mt188033" data-raw-source="[&lt;strong&gt;UcxControllerCreate&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/mt188033)"><strong>UcxControllerCreate</strong></a> method.</p>
</dd>
<dt>Root hub object (UCXROOTHUB)</dt>
<dd><p>Gets and controls the status of the root ports of the host controller. Created by the host controller driver typically within the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541693" data-raw-source="[**EVT_WDF_DRIVER_DEVICE_ADD**](https://msdn.microsoft.com/library/windows/hardware/ff541693)"><strong>EVT_WDF_DRIVER_DEVICE_ADD</strong></a> callback by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/mt188048" data-raw-source="[&lt;strong&gt;UcxRootHubCreate&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/mt188048)"><strong>UcxRootHubCreate</strong></a> method.</p>
</dd>
<dt>USB device object (UCXUSBDEVICE)</dt>
<dd><p>Represents a physical USB device connected to the bus. Created by the host controller driver typically within the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187823" data-raw-source="[&lt;em&gt;EVT_UCX_CONTROLLER_USBDEVICE_ADD&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/mt187823)"><em>EVT_UCX_CONTROLLER_USBDEVICE_ADD</em></a> callback by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/mt188052" data-raw-source="[&lt;strong&gt;UcxUsbDeviceCreate&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/mt188052)"><strong>UcxUsbDeviceCreate</strong></a> method.</p>
</dd>
<dt>Endpoint object (UCXENDPOINT)</dt>
<dd><p>Represents an endpoint on a USB device object. Created by the host controller driver typically within the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187839" data-raw-source="[&lt;em&gt;EVT_UCX_USBDEVICE_DEFAULT_ENDPOINT_ADD&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/mt187839)"><em>EVT_UCX_USBDEVICE_DEFAULT_ENDPOINT_ADD</em></a> or <a href="https://msdn.microsoft.com/library/windows/hardware/mt187843" data-raw-source="[&lt;em&gt;EVT_UCX_USBDEVICE_ENDPOINT_ADD&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/mt187843)"><em>EVT_UCX_USBDEVICE_ENDPOINT_ADD</em></a> callback by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/mt188039" data-raw-source="[&lt;strong&gt;UcxEndpointCreate&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/mt188039)"><strong>UcxEndpointCreate</strong></a> method.</p>
</dd>
<dt>Stream object (UCXSTREAMS)</dt>
<dd><p>Represents a number of pipes to the device across a single bulk endpoint. Created by the host controller driver typically within the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187830" data-raw-source="[&lt;em&gt;EVT_UCX_ENDPOINT_STATIC_STREAMS_ADD&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/mt187830)"><em>EVT_UCX_ENDPOINT_STATIC_STREAMS_ADD</em></a> callback by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/mt188050" data-raw-source="[&lt;strong&gt;UcxStaticStreamsCreate&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/mt188050)"><strong>UcxStaticStreamsCreate</strong></a> method.</p>
</dd>
</dl>
<p><strong>Documentation sections</strong></p>
<a href="manage-the-root-hub-in-a-host-controller-driver.md" data-raw-source="[Root hub callback functions of a host controller driver](manage-the-root-hub-in-a-host-controller-driver.md)">Root hub callback functions of a host controller driver</a>
<p>UCX handles most operations related to the root hub. This allows the USB hub driver to interact with the root hub in the same way that it interacts with a regular hub. The host controller driver can register its callback functions.</p>
<a href="handling-i-o-requests-in-a-host-controller-driver.md" data-raw-source="[Handle I/O requests in a USB host controller driver](handling-i-o-requests-in-a-host-controller-driver.md)">Handle I/O requests in a USB host controller driver</a>
<p>UCX triages incoming USB request blocks (URBs), and then forwards them to the correct endpoint queue.</p>
<a href="configuring-usb-endpoints-in-a-host-controller-driver.md" data-raw-source="[Configure USB endpoints in a host controller driver](configuring-usb-endpoints-in-a-host-controller-driver.md)">Configure USB endpoints in a host controller driver</a>
<p>The host controller driver plays a role in UCX’s management of the queues that are associated with its endpoints, and in the programming of endpoints into controller hardware.</p>
<a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/_usbref/#host-controller-driver-reference" data-raw-source="[USB host controller extension (UCX) reference](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/_usbref/#host-controller-driver-reference)">USB host controller extension (UCX) reference</a>
<p>Gives specifications for I/O requests, support routines, structures, and interfaces used by the client driver. Those routines and related data structures are defined in the WDK headers.</p>
<p>UCX is referred to as the <em>framework class extension</em>.</p>
<p>The host controller driver is referred to as the <em>client driver</em>.</p></td>

</tr>
</tbody>
</table>

 

## Related topics
[Universal Serial Bus (USB)](https://msdn.microsoft.com/library/windows/hardware/ff538930)  



