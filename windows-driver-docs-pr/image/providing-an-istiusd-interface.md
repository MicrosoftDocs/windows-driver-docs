---
title: Providing an IStiUSD Interface
description: Providing an IStiUSD Interface
ms.assetid: ed15b56b-0b63-4983-a4ff-df379a2b9de9
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Providing an IStiUSD Interface





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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543812" data-raw-source="[&lt;strong&gt;IStiUSD::DeviceReset&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543812)"><strong>IStiUSD::DeviceReset</strong></a></p></td>
<td><p>Resets a still image device to a known initialized state.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543814" data-raw-source="[&lt;strong&gt;IStiUSD::Diagnostic&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543814)"><strong>IStiUSD::Diagnostic</strong></a></p></td>
<td><p>Runs diagnostic tests on a still image device. A WIA minidriver must implement this method.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543815" data-raw-source="[&lt;strong&gt;IStiUSD::Escape&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543815)"><strong>IStiUSD::Escape</strong></a></p></td>
<td><p>Performs a vendor-specific I/O operation on a still image device.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543817" data-raw-source="[&lt;strong&gt;IStiUSD::GetCapabilities&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543817)"><strong>IStiUSD::GetCapabilities</strong></a></p></td>
<td><p>Returns a still image device&#39;s capabilities.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543820" data-raw-source="[&lt;strong&gt;IStiUSD::GetLastErrorInfo&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543820)"><strong>IStiUSD::GetLastErrorInfo</strong></a></p></td>
<td><p>Returns information about the last known error associated with a still image device.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543821" data-raw-source="[&lt;strong&gt;IStiUSD::GetNotificationData&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543821)"><strong>IStiUSD::GetNotificationData</strong></a></p></td>
<td><p>Returns a description of the most recent event that occurred on a still image device.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543823" data-raw-source="[&lt;strong&gt;IStiUSD::GetStatus&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543823)"><strong>IStiUSD::GetStatus</strong></a></p></td>
<td><p>Returns the status of a still image device. A WIA minidriver must implement this method if its device has objects, such as buttons, that can generate events.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543824" data-raw-source="[&lt;strong&gt;IStiUSD::Initialize&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543824)"><strong>IStiUSD::Initialize</strong></a></p></td>
<td><p>Initializes an instance of the COM object that defines the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543827" data-raw-source="[IStiUSD interface](https://msdn.microsoft.com/library/windows/hardware/ff543827)">IStiUSD interface</a>. A WIA minidriver must implement this method.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543829" data-raw-source="[&lt;strong&gt;IStiUSD::LockDevice&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543829)"><strong>IStiUSD::LockDevice</strong></a></p></td>
<td><p>Locks a device for exclusive use by the caller. A WIA minidriver must implement this method.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543831" data-raw-source="[&lt;strong&gt;IStiUSD::RawReadCommand&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543831)"><strong>IStiUSD::RawReadCommand</strong></a></p></td>
<td><p>Reads command information from a still image device.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543834" data-raw-source="[&lt;strong&gt;IStiUSD::RawReadData&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543834)"><strong>IStiUSD::RawReadData</strong></a></p></td>
<td><p>Reads data from a still image device.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543836" data-raw-source="[&lt;strong&gt;IStiUSD::RawWriteCommand&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543836)"><strong>IStiUSD::RawWriteCommand</strong></a></p></td>
<td><p>Writes command information to a still image device.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543839" data-raw-source="[&lt;strong&gt;IStiUSD::RawWriteData&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543839)"><strong>IStiUSD::RawWriteData</strong></a></p></td>
<td><p>Writes data to a still image device.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543840" data-raw-source="[&lt;strong&gt;IStiUSD::SetNotificationHandle&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543840)"><strong>IStiUSD::SetNotificationHandle</strong></a></p></td>
<td><p>Specifies an event handle that the minidriver should use to inform the caller of device events. A WIA minidriver must implement this method if its device has objects, such as buttons, that can generate events.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543843" data-raw-source="[&lt;strong&gt;IStiUSD::UnLockDevice&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543843)"><strong>IStiUSD::UnLockDevice</strong></a></p></td>
<td><p>Closes the device port. A WIA minidriver must implement this method.</p></td>
</tr>
</tbody>
</table>

 

 

 




