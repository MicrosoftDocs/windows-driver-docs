---
title: Providing an IStiUSD Interface
description: Providing an IStiUSD Interface
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Providing an IStiUSD Interface





WIA builds on STI. In order to ensure the integration of a WIA minidriver with STI, the minidriver must implement an interface derived from the [IStiUSD interface methods](/windows-hardware/drivers/ddi/_image/index). This interface must be present in a WIA minidriver. The **IStiUSD** interface is used for managing devices (such as loading a driver), and is the means by which the [IStiDevice interface methods](/windows-hardware/drivers/ddi/_image/index) communicates with still image devices. A minidriver must fully implement an interface derived from the [**IStiUSD::Initialize**](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-initialize) method in order to be loaded by the WIA service.

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
<td><p><a href="/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-devicereset" data-raw-source="[&lt;strong&gt;IStiUSD::DeviceReset&lt;/strong&gt;](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-devicereset)"><strong>IStiUSD::DeviceReset</strong></a></p></td>
<td><p>Resets a still image device to a known initialized state.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-diagnostic" data-raw-source="[&lt;strong&gt;IStiUSD::Diagnostic&lt;/strong&gt;](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-diagnostic)"><strong>IStiUSD::Diagnostic</strong></a></p></td>
<td><p>Runs diagnostic tests on a still image device. A WIA minidriver must implement this method.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-escape" data-raw-source="[&lt;strong&gt;IStiUSD::Escape&lt;/strong&gt;](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-escape)"><strong>IStiUSD::Escape</strong></a></p></td>
<td><p>Performs a vendor-specific I/O operation on a still image device.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-getcapabilities" data-raw-source="[&lt;strong&gt;IStiUSD::GetCapabilities&lt;/strong&gt;](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-getcapabilities)"><strong>IStiUSD::GetCapabilities</strong></a></p></td>
<td><p>Returns a still image device's capabilities.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-getlasterrorinfo" data-raw-source="[&lt;strong&gt;IStiUSD::GetLastErrorInfo&lt;/strong&gt;](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-getlasterrorinfo)"><strong>IStiUSD::GetLastErrorInfo</strong></a></p></td>
<td><p>Returns information about the last known error associated with a still image device.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-getnotificationdata" data-raw-source="[&lt;strong&gt;IStiUSD::GetNotificationData&lt;/strong&gt;](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-getnotificationdata)"><strong>IStiUSD::GetNotificationData</strong></a></p></td>
<td><p>Returns a description of the most recent event that occurred on a still image device.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-getstatus" data-raw-source="[&lt;strong&gt;IStiUSD::GetStatus&lt;/strong&gt;](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-getstatus)"><strong>IStiUSD::GetStatus</strong></a></p></td>
<td><p>Returns the status of a still image device. A WIA minidriver must implement this method if its device has objects, such as buttons, that can generate events.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-initialize" data-raw-source="[&lt;strong&gt;IStiUSD::Initialize&lt;/strong&gt;](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-initialize)"><strong>IStiUSD::Initialize</strong></a></p></td>
<td><p>Initializes an instance of the COM object that defines the <a href="/windows-hardware/drivers/ddi/_image/index" data-raw-source="[IStiUSD interface](/windows-hardware/drivers/ddi/_image/index)">IStiUSD interface</a>. A WIA minidriver must implement this method.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-lockdevice" data-raw-source="[&lt;strong&gt;IStiUSD::LockDevice&lt;/strong&gt;](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-lockdevice)"><strong>IStiUSD::LockDevice</strong></a></p></td>
<td><p>Locks a device for exclusive use by the caller. A WIA minidriver must implement this method.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-rawreadcommand" data-raw-source="[&lt;strong&gt;IStiUSD::RawReadCommand&lt;/strong&gt;](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-rawreadcommand)"><strong>IStiUSD::RawReadCommand</strong></a></p></td>
<td><p>Reads command information from a still image device.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-rawreaddata" data-raw-source="[&lt;strong&gt;IStiUSD::RawReadData&lt;/strong&gt;](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-rawreaddata)"><strong>IStiUSD::RawReadData</strong></a></p></td>
<td><p>Reads data from a still image device.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-rawwritecommand" data-raw-source="[&lt;strong&gt;IStiUSD::RawWriteCommand&lt;/strong&gt;](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-rawwritecommand)"><strong>IStiUSD::RawWriteCommand</strong></a></p></td>
<td><p>Writes command information to a still image device.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-rawwritedata" data-raw-source="[&lt;strong&gt;IStiUSD::RawWriteData&lt;/strong&gt;](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-rawwritedata)"><strong>IStiUSD::RawWriteData</strong></a></p></td>
<td><p>Writes data to a still image device.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-setnotificationhandle" data-raw-source="[&lt;strong&gt;IStiUSD::SetNotificationHandle&lt;/strong&gt;](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-setnotificationhandle)"><strong>IStiUSD::SetNotificationHandle</strong></a></p></td>
<td><p>Specifies an event handle that the minidriver should use to inform the caller of device events. A WIA minidriver must implement this method if its device has objects, such as buttons, that can generate events.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-unlockdevice" data-raw-source="[&lt;strong&gt;IStiUSD::UnLockDevice&lt;/strong&gt;](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-unlockdevice)"><strong>IStiUSD::UnLockDevice</strong></a></p></td>
<td><p>Closes the device port. A WIA minidriver must implement this method.</p></td>
</tr>
</tbody>
</table>

 

