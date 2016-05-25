---
title: Storport Queue Management
author: windows-driver-content
description: Storport Queue Management
ms.assetid: 29fddcac-abc9-4aa4-8485-56120805ae34
keywords: ["Storport drivers WDK , queue management", "queues WDK Storport"]
---

# Storport Queue Management


## <span id="ddk_storport_queue_management_kg"></span><span id="DDK_STORPORT_QUEUE_MANAGEMENT_KG"></span>


To take advantage of the capabilities of high-performance storage adapters, miniport drivers must exert control over their device queues, pausing and resuming these queues in ways that will maximize efficiency.

In the SCSI Port queue model, queue management is the exclusive domain of the port driver. In the Storport queue model, the port driver supplies several queue management support routines that give the miniport driver a significant amount of queue management control.

In the Storport queue model, all requests are queued in the port driver in per-logical-unit queues. Without extended SRB support, each logical unit can have a maximum of 255 outstanding requests. Otherwise, the queue depth is only limited by available system resources or the capabilities of the adapter. When limit set for the queue depth is reached, Storport holds further requests to that logical unit until the number of outstanding requests to the unit drops below the queue maximum.

There are no predefined limits from Storport on the number of outstanding requests that an adapter can have. For example, an adapter with 55 logical units attached to it with a queue depth of 255 could post up to a maximum of 14,025 (55 x 255) requests at a time. See the following diagram for a description of the port driver's queuing model.

![diagram illustrating the port driver's queuing model](images/queues.png)

Port Driver's Queuing Model

If the adapter and a logical unit are both ready to receive a request, the system calls the miniport driver's [**HwStorBuildIo**](https://msdn.microsoft.com/library/windows/hardware/ff557369) and [**HwStorStartIo**](https://msdn.microsoft.com/library/windows/hardware/ff557423) routines in that order.

Unlike SCSI Port, Storport allows miniport drivers to notify the port driver of busy conditions. These communications are handled by the following eight routines, which allow the miniport driver to signal when either the logical unit or the adapter is paused or busy.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Storport Routine</th>
<th align="left">Action Taken</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<strong>StorPortPauseDevice</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567461)</p></td>
<td align="left"><p>Pause a device for a specified period of time.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>StorPortResumeDevice</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567501)</p></td>
<td align="left"><p>Resume a paused device.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>StorPortPause</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567459)</p></td>
<td align="left"><p>Pause an adapter for a specified period of time.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>StorPortResume</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567499)</p></td>
<td align="left"><p>Resume a paused adapter.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>StorPortDeviceBusy</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567050)</p></td>
<td align="left"><p>Make a device busy until the device queue has completed a specified number of I/O requests.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>StorPortDeviceReady</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567053)</p></td>
<td align="left"><p>Make a busy device ready to receive requests again.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>StorPortBusy</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567041)</p></td>
<td align="left"><p>Make an adapter busy until it has completed a specified number of I/O requests.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>StorPortReady</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567489)</p></td>
<td align="left"><p>Make a busy adapter ready to receive requests again.</p></td>
</tr>
</tbody>
</table>

 

While a device is paused or busy, the port driver sends no requests to the device. If a miniport driver completes a request with a busy status (SRB\_STATUS\_BUSY or SCSISTAT\_BUSY), the port driver will retry the request an indefinite number of times, until the request fails or is completed.

In addition to supplying a set of explicit queue management routines that are not available in the SCSI Port queue model, the Storport queue model does not use the implicit queue management routines that the SCSI Port employed. In particular, the **NextRequest** and **NextLuRequest** notifications are ignored.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Storport%20Queue%20Management%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


