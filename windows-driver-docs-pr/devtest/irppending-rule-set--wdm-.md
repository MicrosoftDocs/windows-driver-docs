---
title: IrpPending rule set (WDM)
description: Use these rules to verify that your driver correctly pends I/O request packets (IRP).
ms.assetid: C4B5976B-7655-4FD1-B415-98C256873EBC
ms.date: 05/21/2018
ms.localizationpriority: medium
---

# IrpPending rule set (WDM)


Use these rules to verify that your driver correctly pends I/O request packets (IRP).

## In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Topic</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<strong>MarkDevicePower</strong>](wdm-markdevicepower.md)</p></td>
<td align="left"><p>The [<strong>MarkDevicePower</strong>](wdm-markdevicepower.md) rule specifies that an IRP_MJ_POWER with IRP_MN_SET_POWER for SystemPowerState IRP going to S0 is pended.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>MarkingInterlockedQueuedIrps</strong>](wdm-markinginterlockedqueuedirps.md)</p></td>
<td align="left"><p>The [<strong>MarkingInterlockedQueuedIrps</strong>](wdm-markinginterlockedqueuedirps.md) rule specifies that the driver correctly marks the IRP as pending before it queues it in an interlocked fashion for further processing.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>MarkingQueuedIrps</strong>](wdm-markingqueuedirps.md)</p></td>
<td align="left"><p>The [<strong>MarkingQueuedIrps</strong>](wdm-markingqueuedirps.md) rule specifies that the driver calls [<strong>IoMarkIrpPending</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549422) for an IRP that requires further processing only while holding a spin lock. This rule applies only when the driver adds the IRP to a driver-managed queue.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>MarkIrpPending</strong>](wdm-markirppending.md)</p></td>
<td align="left"><p>The [<strong>MarkIrpPending</strong>](wdm-markirppending.md) rule specifies that whenever a driver dispatch routine calls [<strong>IoMarkIrpPending</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549422), the driver returns STATUS_PENDING when the dispatch routine ends. See [<strong>MarkIrpPending2</strong>](wdm-markirppending2.md) for a complimentary specification.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>MarkIrpPending2</strong>](wdm-markirppending2.md)</p></td>
<td align="left"><p>The [<strong>MarkIrpPending2</strong>](wdm-markirppending2.md) rule specifies that if a dispatch routine returns STATUS_PENDING, it has called [<strong>IoMarkIrpPending</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549422) or passed the IRP to the lower driver. See [<strong>MarkIrpPending</strong>](wdm-markirppending.md) for a complimentary specification.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>MarkPower</strong>](wdm-markpower.md)</p></td>
<td align="left"><p>The [<strong>MarkPower</strong>](wdm-markpower.md) rule specifies that an IRP_MJ_POWER with IRP_MN_SET_POWER for <strong>SystemPowerState</strong> IRP going to S0 is pended. This rule only applies to FDO and FIDO drivers.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>MarkPowerDown</strong>](wdm-markpowerdown.md)</p></td>
<td align="left"><p>The [<strong>MarkPowerDown</strong>](wdm-markpowerdown.md) rule specifies that an IRP_MJ_POWER with IRP_MN_SET_POWER for <strong>SystemPowerState</strong> IRP going from s0 to [S1...S5] is pended.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>MarkQueryRelations</strong>](wdm-markqueryrelations.md)</p></td>
<td align="left"><p>The [<strong>MarkQueryRelations</strong>](wdm-markqueryrelations.md) rule specifies that the driver should pend the IRP_MN_QUERY_DEVICE_RELATIONS IRP.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>MarkStartDevice</strong>](wdm-markstartdevice.md)</p></td>
<td align="left"><p>The [<strong>MarkStartDevice</strong>](wdm-markstartdevice.md) rule specifies that the driver pends an IRP_MN_START_DEVICE IRP correctly. This rule only applies to FDO and FIDO drivers.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>PendedCompletedRequest</strong>](wdm-pendedcompletedrequest.md)</p></td>
<td align="left"><p>The [<strong>PendedCompletedRequest</strong>](wdm-pendedcompletedrequest.md) rule specifies that a driver's dispatch routine does not return STATUS_PENDING on an IRP if the driver has called [<strong>IoCompleteRequest</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548343) on the incoming IRP.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>PendedCompletedRequest2</strong>](wdm-pendedcompletedrequest2.md)</p></td>
<td align="left"><p>The [<strong>PendedCompletedRequest2</strong>](wdm-pendedcompletedrequest2.md) rule specifies that a wait is required after a call to [<strong>IoCallDriver</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548336) or [<strong>PoCallDriver</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559654) because the dispatch routine could complete a pending IRP.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>PendedCompletedRequest3</strong>](wdm-pendedcompletedrequest3.md)</p></td>
<td align="left"><p>The [<strong>PendedCompletedRequest3</strong>](wdm-pendedcompletedrequest3.md) rule specifies that a pending IRP should not be completed with a call to [<strong>IoCompleteRequest</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548343).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>PendedCompletedRequestEx</strong>](wdm-pendedcompletedrequestex.md)</p></td>
<td align="left"><p>The [<strong>PendedCompletedRequestEx</strong>](wdm-pendedcompletedrequestex.md) rule specifies that the driver should not call [<strong>IoCompleteRequest</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548343) for a pending IRP.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>StartDeviceWait</strong>](wdm-startdevicewait.md)</p></td>
<td align="left"><p>The [<strong>StartDeviceWait</strong>](wdm-startdevicewait.md) rule specifies that the driver should not call [<strong>KeWaitForSingleObject</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553350) in the context of start device IRP.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>StartDeviceWait2</strong>](wdm-startdevicewait2.md)</p></td>
<td align="left"><p>The [<strong>StartDeviceWait2</strong>](wdm-startdevicewait2.md) rule specifies that the driver should not call [<strong>KeWaitForSingleObject</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553350) in the context of start device IRP.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>StartDeviceWait3</strong>](wdm-startdevicewait3.md)</p></td>
<td align="left"><p>The [<strong>StartDeviceWait3</strong>](wdm-startdevicewait3.md) rule specifies that the driver should not call [<strong>KeWaitForSingleObject</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553350) in the context of start device IRP.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>StartDeviceWait4</strong>](wdm-startdevicewait4.md)</p></td>
<td align="left"><p>The [<strong>StartDeviceWait4</strong>](wdm-startdevicewait4.md) rule specifies that the driver should not call [<strong>KeWaitForSingleObject</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553350) in the context of start device IRP.</p></td>
</tr>
</tbody>
</table>

 

**To select the IrpPending rule set**

1.  Select your driver project (.vcxProj) in Microsoft Visual Studio. From the **Driver** menu, click **Launch Static Driver Verifier…**.

2.  Click the **Rules** tab. Under **Rule Sets**, select **IrpPending**.

    To select the default rule set from a Visual Studio developer command prompt window, specify **IrpPending.sdv** with the **/check** option. For example:

    ```
    msbuild /t:sdv /p:Inputs="/check:IrpPending.sdv" mydriver.VcxProj /p:Configuration="Win8 Release" /p:Platform=Win32
    ```

    For more information, see [Using Static Driver Verifier to Find Defects in Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454281) and [Static Driver Verifier commands (MSBuild)](https://msdn.microsoft.com/library/windows/hardware/hh466459).

 

 





