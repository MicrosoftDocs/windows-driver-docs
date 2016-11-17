---
title: WDM Reader Driver
description: WDM Reader Driver
ms.assetid: ead76f5f-1d28-4343-99c0-e7974fa4c3da
keywords: ["vendor-supplied drivers WDK smart card , required routines", "WDM WDK smart card"]
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
<td align="left"><p>[<strong>DriverEntry</strong>](https://msdn.microsoft.com/library/windows/hardware/ff544113)</p></td>
<td align="left"><p>Initializes the driver object and the dispatch table.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>AddDevice</em>](https://msdn.microsoft.com/library/windows/hardware/ff540521)</p></td>
<td align="left"><p>Creates a device object for the smart card reader. In addition, [<em>AddDevice</em>](https://msdn.microsoft.com/library/windows/hardware/ff540521) can call any of the following driver library routines:</p>
<ul>
<li><p>[<strong>SmartcardInitialize (WDM)</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548944) to complete driver initialization. Calling this routine in [<em>AddDevice</em>](https://msdn.microsoft.com/library/windows/hardware/ff540521) is obligatory.</p></li>
<li><p>[<strong>SmartcardLogError (WDM)</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548947) to log an error. Drivers must call this routine in [<em>AddDevice</em>](https://msdn.microsoft.com/library/windows/hardware/ff540521) if [<strong>SmartcardInitialize (WDM)</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548944) fails.</p></li>
<li><p>[<strong>SmartcardCreateLink (WDM)</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548935) to create a symbolic link for the reader device in the registry.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>Unload</em>](https://msdn.microsoft.com/library/windows/hardware/ff564886)</p></td>
<td align="left"><p>Removes the driver from the system.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>DispatchCreate</em>](https://msdn.microsoft.com/library/windows/hardware/ff543266)</p>
<p>-and-</p>
<p>[<em>DispatchClose</em>](https://msdn.microsoft.com/library/windows/hardware/ff543255)</p></td>
<td align="left"><p>Supports [<strong>IRP_MJ_CREATE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550729) and [<strong>IRP_MJ_CLOSE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550720), respectively. To establish a connection to the reader, the resource manager sends <strong>IRP_MJ_CREATE</strong> to the reader driver. To sever the connection, the resource manager sends <strong>IRP_MJ_CLOSE</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>DispatchCleanup</em>](https://msdn.microsoft.com/library/windows/hardware/ff543233)</p></td>
<td align="left"><p>Supports [<strong>IRP_MJ_CLEANUP</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550718), which the resource manager sends to the reader driver to cancel pending I/O requests.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>DispatchPnP</em>](https://msdn.microsoft.com/library/windows/hardware/ff543341)</p></td>
<td align="left"><p>Supports [<strong>IRP_MJ_PNP</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550772).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>DispatchPower</em>](https://msdn.microsoft.com/library/windows/hardware/ff543354)</p></td>
<td align="left"><p>Supports [<strong>IRP_MJ_POWER</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550784).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>DispatchDeviceControl</em>](https://msdn.microsoft.com/library/windows/hardware/ff543287)</p></td>
<td align="left"><p>Supports [<strong>IRP_MJ_DEVICE_CONTROL</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550744) and is the main entry point for smart card requests. Upon receiving IRP_MJ_DEVICE_CONTROL, [<em>DispatchDeviceControl</em>](https://msdn.microsoft.com/library/windows/hardware/ff543287) must immediately call [<strong>SmartcardDeviceControl (WDM)</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548939), which is the smart card driver library routine that handles device-control requests. The following code example shows how to call this library routine from a WDM driver:</p>
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
<p>If it is unable to handle the particular IOCTL that is indicated in the call, <strong>SmartcardDeviceControl</strong> will call the driver's callback for unknown IOCTL requests.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[smartcrd\smartcrd]:%20WDM%20Reader%20Driver%20%20RELEASE:%20%287/20/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




