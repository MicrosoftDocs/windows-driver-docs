---
title: WDM Reader Driver
description: WDM Reader Driver
ms.assetid: ead76f5f-1d28-4343-99c0-e7974fa4c3da
keywords:
- vendor-supplied drivers WDK smart card , required routines
- WDM WDK smart card
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WDM Reader Driver


## <span id="_ntovr_wdm_reader_driver"></span><span id="_NTOVR_WDM_READER_DRIVER"></span>


The following table lists the routines that are required by a WDM reader driver.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Routine</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff544113" data-raw-source="[&lt;strong&gt;DriverEntry&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff544113)"><strong>DriverEntry</strong></a></p></td>
<td align="left"><p>Initializes the driver object and the dispatch table.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540521" data-raw-source="[&lt;em&gt;AddDevice&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540521)"><em>AddDevice</em></a></p></td>
<td align="left"><p>Creates a device object for the smart card reader. In addition, <a href="https://msdn.microsoft.com/library/windows/hardware/ff540521" data-raw-source="[&lt;em&gt;AddDevice&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540521)"><em>AddDevice</em></a> can call any of the following driver library routines:</p>
<ul>
<li><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff548944" data-raw-source="[&lt;strong&gt;SmartcardInitialize (WDM)&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548944)"><strong>SmartcardInitialize (WDM)</strong></a> to complete driver initialization. Calling this routine in <a href="https://msdn.microsoft.com/library/windows/hardware/ff540521" data-raw-source="[&lt;em&gt;AddDevice&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540521)"><em>AddDevice</em></a> is obligatory.</p></li>
<li><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff548947" data-raw-source="[&lt;strong&gt;SmartcardLogError (WDM)&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548947)"><strong>SmartcardLogError (WDM)</strong></a> to log an error. Drivers must call this routine in <a href="https://msdn.microsoft.com/library/windows/hardware/ff540521" data-raw-source="[&lt;em&gt;AddDevice&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540521)"><em>AddDevice</em></a> if <a href="https://msdn.microsoft.com/library/windows/hardware/ff548944" data-raw-source="[&lt;strong&gt;SmartcardInitialize (WDM)&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548944)"><strong>SmartcardInitialize (WDM)</strong></a> fails.</p></li>
<li><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff548935" data-raw-source="[&lt;strong&gt;SmartcardCreateLink (WDM)&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548935)"><strong>SmartcardCreateLink (WDM)</strong></a> to create a symbolic link for the reader device in the registry.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564886" data-raw-source="[&lt;em&gt;Unload&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564886)"><em>Unload</em></a></p></td>
<td align="left"><p>Removes the driver from the system.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543266" data-raw-source="[&lt;em&gt;DispatchCreate&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543266)"><em>DispatchCreate</em></a></p>
<p>-and-</p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543255" data-raw-source="[&lt;em&gt;DispatchClose&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543255)"><em>DispatchClose</em></a></p></td>
<td align="left"><p>Supports <a href="https://msdn.microsoft.com/library/windows/hardware/ff550729" data-raw-source="[&lt;strong&gt;IRP_MJ_CREATE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550729)"><strong>IRP_MJ_CREATE</strong></a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff550720" data-raw-source="[&lt;strong&gt;IRP_MJ_CLOSE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550720)"><strong>IRP_MJ_CLOSE</strong></a>, respectively. To establish a connection to the reader, the resource manager sends <strong>IRP_MJ_CREATE</strong> to the reader driver. To sever the connection, the resource manager sends <strong>IRP_MJ_CLOSE</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543233" data-raw-source="[&lt;em&gt;DispatchCleanup&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543233)"><em>DispatchCleanup</em></a></p></td>
<td align="left"><p>Supports <a href="https://msdn.microsoft.com/library/windows/hardware/ff550718" data-raw-source="[&lt;strong&gt;IRP_MJ_CLEANUP&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550718)"><strong>IRP_MJ_CLEANUP</strong></a>, which the resource manager sends to the reader driver to cancel pending I/O requests.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543341" data-raw-source="[&lt;em&gt;DispatchPnP&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543341)"><em>DispatchPnP</em></a></p></td>
<td align="left"><p>Supports <a href="https://msdn.microsoft.com/library/windows/hardware/ff550772" data-raw-source="[&lt;strong&gt;IRP_MJ_PNP&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550772)"><strong>IRP_MJ_PNP</strong></a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543354" data-raw-source="[&lt;em&gt;DispatchPower&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543354)"><em>DispatchPower</em></a></p></td>
<td align="left"><p>Supports <a href="https://msdn.microsoft.com/library/windows/hardware/ff550784" data-raw-source="[&lt;strong&gt;IRP_MJ_POWER&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550784)"><strong>IRP_MJ_POWER</strong></a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543287" data-raw-source="[&lt;em&gt;DispatchDeviceControl&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543287)"><em>DispatchDeviceControl</em></a></p></td>
<td align="left"><p>Supports <a href="https://msdn.microsoft.com/library/windows/hardware/ff550744" data-raw-source="[&lt;strong&gt;IRP_MJ_DEVICE_CONTROL&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550744)"><strong>IRP_MJ_DEVICE_CONTROL</strong></a> and is the main entry point for smart card requests. Upon receiving IRP_MJ_DEVICE_CONTROL, <a href="https://msdn.microsoft.com/library/windows/hardware/ff543287" data-raw-source="[&lt;em&gt;DispatchDeviceControl&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543287)"><em>DispatchDeviceControl</em></a> must immediately call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548939" data-raw-source="[&lt;strong&gt;SmartcardDeviceControl (WDM)&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548939)"><strong>SmartcardDeviceControl (WDM)</strong></a>, which is the smart card driver library routine that handles device-control requests. The following code example shows how to call this library routine from a WDM driver:</p>
<pre space="preserve"><code>NTSTATUS
DriverDeviceControl(
    PDEVICE_OBJECT DeviceObject,
    PIRP Irp
    )
{
    PDEVICE_EXTENSION deviceExtension = DeviceObject -&gt; DeviceExtension;

    return SmartcardDeviceControl(
        &(deviceExtension-&gt;SmartcardExtension),
        Irp
        );
}</code></pre>
<p>If it is unable to handle the particular IOCTL that is indicated in the call, <strong>SmartcardDeviceControl</strong> will call the driver&#39;s callback for unknown IOCTL requests.</p></td>
</tr>
</tbody>
</table>

 

 

 





