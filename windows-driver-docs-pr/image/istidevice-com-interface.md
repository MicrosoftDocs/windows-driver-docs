---
title: IStiDevice COM Interface
description: IStiDevice COM Interface
ms.assetid: b026fb74-9ce6-4d4e-8a5b-402731904064
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# IStiDevice COM Interface





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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543733" data-raw-source="[&lt;strong&gt;IStiDevice::DeviceReset&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543733)"><strong>IStiDevice::DeviceReset</strong></a></p></td>
<td><p>Resets a still image device to a known state.</p></td>
<td><p>Image Acquisition APIs</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543736" data-raw-source="[&lt;strong&gt;IStiDevice::Diagnostic&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543736)"><strong>IStiDevice::Diagnostic</strong></a></p></td>
<td><p>Executes diagnostic tests on a still image device.</p></td>
<td><p>Scanners and Cameras Control Panel</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543740" data-raw-source="[&lt;strong&gt;IStiDevice::Escape&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543740)"><strong>IStiDevice::Escape</strong></a></p></td>
<td><p>Sends a request for a vendor-specific I/O operation to a still image device.</p></td>
<td><p>Image Acquisition APIs</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543745" data-raw-source="[&lt;strong&gt;IStiDevice::GetCapabilities&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543745)"><strong>IStiDevice::GetCapabilities</strong></a></p></td>
<td><p>Returns a still image device&#39;s capabilities.</p></td>
<td><p>Still image event monitor</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543747" data-raw-source="[&lt;strong&gt;IStiDevice::GetLastError&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543747)"><strong>IStiDevice::GetLastError</strong></a></p></td>
<td><p>Returns the last known error associated with a still image device.</p></td>
<td><p>Image Acquisition APIs</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543749" data-raw-source="[&lt;strong&gt;IStiDevice::GetLastErrorInfo&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543749)"><strong>IStiDevice::GetLastErrorInfo</strong></a></p></td>
<td><p>Returns information about the last known error associated with a still image device.</p></td>
<td><p>Image Acquisition APIs</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543751" data-raw-source="[&lt;strong&gt;IStiDevice::GetLastNotificationData&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543751)"><strong>IStiDevice::GetLastNotificationData</strong></a></p></td>
<td><p>Returns a description of the most recent event that occurred on a still image device.</p></td>
<td><p>Image Acquisition APIs</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543752" data-raw-source="[&lt;strong&gt;IStiDevice::GetStatus&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543752)"><strong>IStiDevice::GetStatus</strong></a></p></td>
<td><p>Returns a still image device&#39;s status information.</p></td>
<td><p>Image acquisition APIs and still image event monitor</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543754" data-raw-source="[&lt;strong&gt;IStiDevice::Initialize&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543754)"><strong>IStiDevice::Initialize</strong></a></p></td>
<td><p>Initializes an object instance.</p></td>
<td><p>Not called directly</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543756" data-raw-source="[&lt;strong&gt;IStiDevice::LockDevice&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543756)"><strong>IStiDevice::LockDevice</strong></a></p></td>
<td><p>Locks a device for exclusive use by the caller.</p></td>
<td><p>All <strong>IStiDevice</strong> interface clients</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543758" data-raw-source="[&lt;strong&gt;IStiDevice::RawReadCommand&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543758)"><strong>IStiDevice::RawReadCommand</strong></a></p></td>
<td><p>Reads command information from a still image device.</p></td>
<td><p>Image Acquisition APIs</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543760" data-raw-source="[&lt;strong&gt;IStiDevice::RawReadData&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543760)"><strong>IStiDevice::RawReadData</strong></a></p></td>
<td><p>Reads data from a still image device.</p></td>
<td><p>Image Acquisition APIs</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543762" data-raw-source="[&lt;strong&gt;IStiDevice::RawWriteCommand&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543762)"><strong>IStiDevice::RawWriteCommand</strong></a></p></td>
<td><p>Sends command information to a still image device.</p></td>
<td><p>Image Acquisition APIs</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543764" data-raw-source="[&lt;strong&gt;IStiDevice::RawWriteData&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543764)"><strong>IStiDevice::RawWriteData</strong></a></p></td>
<td><p>Writes data to a still image device.</p></td>
<td><p>Image Acquisition APIs</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543765" data-raw-source="[&lt;strong&gt;IStiDevice::Release&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543765)"><strong>IStiDevice::Release</strong></a></p></td>
<td><p>Closes an object instance and removes access to the <strong>IStiDevice</strong> interface.</p></td>
<td><p>All <strong>IStiDevice</strong> interface clients</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543768" data-raw-source="[&lt;strong&gt;IStiDevice::Subscribe&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543768)"><strong>IStiDevice::Subscribe</strong></a></p></td>
<td><p>Registers the caller to receive notifications of device events.</p></td>
<td><p>Image Acquisition APIs</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543770" data-raw-source="[&lt;strong&gt;IStiDevice::UnLockDevice&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543770)"><strong>IStiDevice::UnLockDevice</strong></a></p></td>
<td><p>Unlocks a device.</p></td>
<td><p>All <strong>IStiDevice</strong> interface clients</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543773" data-raw-source="[&lt;strong&gt;IStiDevice::UnSubscribe&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543773)"><strong>IStiDevice::UnSubscribe</strong></a></p></td>
<td><p>Removes the caller from the list of applications registered to receive notification of device events.</p></td>
<td><p>Image Acquisition APIs</p></td>
</tr>
</tbody>
</table>

 

 

 




