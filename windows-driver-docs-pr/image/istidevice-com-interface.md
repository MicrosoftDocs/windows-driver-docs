---
title: IStiDevice COM Interface
author: windows-driver-content
description: IStiDevice COM Interface
ms.assetid: b026fb74-9ce6-4d4e-8a5b-402731904064
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# IStiDevice COM Interface


## <a href="" id="ddk-istidevice-com-interface-si"></a>


The **IStiDevice** COM interface provides applications with the ability to communicate with still image devices. Interface methods allow applications to send and receive data and commands, to run diagnostic tests, to receive notifications of [Still Image Device Events](still-image-device-events.md), and to obtain device capabilities and status information.

Access to the **IStiDevice** interface is obtained by calling the **CreateDevice** method of the [IStillImage COM Interface](istillimage-com-interface.md). Many of the **IStiDevice** interface's methods are implemented by calling like-named methods defined by the [IStiUSD COM Interface](istiusd-com-interface.md).

The following table lists and describes all of the methods supplied by the **IStiDevice** interface. The table indicates the types of clients that typically must call each method.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Method</th>
<th>Description</th>
<th>Typical Callers</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>IStiDevice::DeviceReset</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543733)</p></td>
<td><p>Resets a still image device to a known state.</p></td>
<td><p>Image Acquisition APIs</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IStiDevice::Diagnostic</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543736)</p></td>
<td><p>Executes diagnostic tests on a still image device.</p></td>
<td><p>Scanners and Cameras Control Panel</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IStiDevice::Escape</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543740)</p></td>
<td><p>Sends a request for a vendor-specific I/O operation to a still image device.</p></td>
<td><p>Image Acquisition APIs</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IStiDevice::GetCapabilities</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543745)</p></td>
<td><p>Returns a still image device's capabilities.</p></td>
<td><p>Still image event monitor</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IStiDevice::GetLastError</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543747)</p></td>
<td><p>Returns the last known error associated with a still image device.</p></td>
<td><p>Image Acquisition APIs</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IStiDevice::GetLastErrorInfo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543749)</p></td>
<td><p>Returns information about the last known error associated with a still image device.</p></td>
<td><p>Image Acquisition APIs</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IStiDevice::GetLastNotificationData</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543751)</p></td>
<td><p>Returns a description of the most recent event that occurred on a still image device.</p></td>
<td><p>Image Acquisition APIs</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IStiDevice::GetStatus</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543752)</p></td>
<td><p>Returns a still image device's status information.</p></td>
<td><p>Image acquisition APIs and still image event monitor</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IStiDevice::Initialize</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543754)</p></td>
<td><p>Initializes an object instance.</p></td>
<td><p>Not called directly</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IStiDevice::LockDevice</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543756)</p></td>
<td><p>Locks a device for exclusive use by the caller.</p></td>
<td><p>All <strong>IStiDevice</strong> interface clients</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IStiDevice::RawReadCommand</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543758)</p></td>
<td><p>Reads command information from a still image device.</p></td>
<td><p>Image Acquisition APIs</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IStiDevice::RawReadData</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543760)</p></td>
<td><p>Reads data from a still image device.</p></td>
<td><p>Image Acquisition APIs</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IStiDevice::RawWriteCommand</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543762)</p></td>
<td><p>Sends command information to a still image device.</p></td>
<td><p>Image Acquisition APIs</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IStiDevice::RawWriteData</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543764)</p></td>
<td><p>Writes data to a still image device.</p></td>
<td><p>Image Acquisition APIs</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IStiDevice::Release</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543765)</p></td>
<td><p>Closes an object instance and removes access to the <strong>IStiDevice</strong> interface.</p></td>
<td><p>All <strong>IStiDevice</strong> interface clients</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IStiDevice::Subscribe</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543768)</p></td>
<td><p>Registers the caller to receive notifications of device events.</p></td>
<td><p>Image Acquisition APIs</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IStiDevice::UnLockDevice</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543770)</p></td>
<td><p>Unlocks a device.</p></td>
<td><p>All <strong>IStiDevice</strong> interface clients</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IStiDevice::UnSubscribe</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543773)</p></td>
<td><p>Removes the caller from the list of applications registered to receive notification of device events.</p></td>
<td><p>Image Acquisition APIs</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20IStiDevice%20COM%20Interface%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


