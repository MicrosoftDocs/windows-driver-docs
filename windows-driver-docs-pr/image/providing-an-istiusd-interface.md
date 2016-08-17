---
title: Providing an IStiUSD Interface
description: Providing an IStiUSD Interface
MS-HAID:
- 'WIA\_drv\_basic\_d74fc438-8db2-4f7d-a9a5-4c3e82bbc887.xml'
- 'image.providing\_an\_istiusd\_interface'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: ed15b56b-0b63-4983-a4ff-df379a2b9de9
---

# Providing an IStiUSD Interface


## <a href="" id="ddk-providing-an-istiusd-interface-si"></a>


WIA builds on STI. In order to ensure the integration of a WIA minidriver with STI, the minidriver must implement an interface derived from the [IStiUSD interface methods](https://msdn.microsoft.com/library/windows/hardware/ff543827). This interface must be present in a WIA minidriver. The **IStiUSD** interface is used for managing devices (such as loading a driver), and is the means by which the [IStiDevice interface methods](https://msdn.microsoft.com/library/windows/hardware/ff543755) communicates with still image devices. A minidriver must fully implement an interface derived from the [**IStiUSD::Initialize**](https://msdn.microsoft.com/library/windows/hardware/ff543824) method in order to be loaded by the WIA service.

Typically, **IStiUSD** interface methods are called by similarly named methods defined by the **IStiDevice** interface. Minidrivers typically implement **IStiUSD** interface methods by calling the appropriate kernel-mode driver. Each minidriver must define all interface methods, but if a method is not needed it can simply return STIERR\_UNSUPPORTED.

See the *wiacam* camera sample minidriver file, *IStiUSD.cpp*, for an example of how a minidriver implements the **IStiUSD** interface.

The following table lists and describes all of the methods defined by the **IStiUSD** interface. Methods that must be implemented or conditionally implemented by WIA minidrivers are identified.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Method</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>IStiUSD::DeviceReset</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543812)</p></td>
<td><p>Resets a still image device to a known initialized state.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IStiUSD::Diagnostic</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543814)</p></td>
<td><p>Runs diagnostic tests on a still image device. A WIA minidriver must implement this method.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IStiUSD::Escape</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543815)</p></td>
<td><p>Performs a vendor-specific I/O operation on a still image device.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IStiUSD::GetCapabilities</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543817)</p></td>
<td><p>Returns a still image device's capabilities.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IStiUSD::GetLastErrorInfo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543820)</p></td>
<td><p>Returns information about the last known error associated with a still image device.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IStiUSD::GetNotificationData</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543821)</p></td>
<td><p>Returns a description of the most recent event that occurred on a still image device.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IStiUSD::GetStatus</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543823)</p></td>
<td><p>Returns the status of a still image device. A WIA minidriver must implement this method if its device has objects, such as buttons, that can generate events.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IStiUSD::Initialize</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543824)</p></td>
<td><p>Initializes an instance of the COM object that defines the [IStiUSD interface](https://msdn.microsoft.com/library/windows/hardware/ff543827). A WIA minidriver must implement this method.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IStiUSD::LockDevice</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543829)</p></td>
<td><p>Locks a device for exclusive use by the caller. A WIA minidriver must implement this method.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IStiUSD::RawReadCommand</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543831)</p></td>
<td><p>Reads command information from a still image device.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IStiUSD::RawReadData</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543834)</p></td>
<td><p>Reads data from a still image device.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IStiUSD::RawWriteCommand</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543836)</p></td>
<td><p>Writes command information to a still image device.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IStiUSD::RawWriteData</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543839)</p></td>
<td><p>Writes data to a still image device.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IStiUSD::SetNotificationHandle</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543840)</p></td>
<td><p>Specifies an event handle that the minidriver should use to inform the caller of device events. A WIA minidriver must implement this method if its device has objects, such as buttons, that can generate events.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IStiUSD::UnLockDevice</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543843)</p></td>
<td><p>Closes the device port. A WIA minidriver must implement this method.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Providing%20an%20IStiUSD%20Interface%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




