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
<td align="left"><p><a href="wdm-markdevicepower.md" data-raw-source="[&lt;strong&gt;MarkDevicePower&lt;/strong&gt;](wdm-markdevicepower.md)"><strong>MarkDevicePower</strong></a></p></td>
<td align="left"><p>The <a href="wdm-markdevicepower.md" data-raw-source="[&lt;strong&gt;MarkDevicePower&lt;/strong&gt;](wdm-markdevicepower.md)"><strong>MarkDevicePower</strong></a> rule specifies that an IRP_MJ_POWER with IRP_MN_SET_POWER for SystemPowerState IRP going to S0 is pended.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="wdm-markinginterlockedqueuedirps.md" data-raw-source="[&lt;strong&gt;MarkingInterlockedQueuedIrps&lt;/strong&gt;](wdm-markinginterlockedqueuedirps.md)"><strong>MarkingInterlockedQueuedIrps</strong></a></p></td>
<td align="left"><p>The <a href="wdm-markinginterlockedqueuedirps.md" data-raw-source="[&lt;strong&gt;MarkingInterlockedQueuedIrps&lt;/strong&gt;](wdm-markinginterlockedqueuedirps.md)"><strong>MarkingInterlockedQueuedIrps</strong></a> rule specifies that the driver correctly marks the IRP as pending before it queues it in an interlocked fashion for further processing.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="wdm-markingqueuedirps.md" data-raw-source="[&lt;strong&gt;MarkingQueuedIrps&lt;/strong&gt;](wdm-markingqueuedirps.md)"><strong>MarkingQueuedIrps</strong></a></p></td>
<td align="left"><p>The <a href="wdm-markingqueuedirps.md" data-raw-source="[&lt;strong&gt;MarkingQueuedIrps&lt;/strong&gt;](wdm-markingqueuedirps.md)"><strong>MarkingQueuedIrps</strong></a> rule specifies that the driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff549422" data-raw-source="[&lt;strong&gt;IoMarkIrpPending&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549422)"><strong>IoMarkIrpPending</strong></a> for an IRP that requires further processing only while holding a spin lock. This rule applies only when the driver adds the IRP to a driver-managed queue.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="wdm-markirppending.md" data-raw-source="[&lt;strong&gt;MarkIrpPending&lt;/strong&gt;](wdm-markirppending.md)"><strong>MarkIrpPending</strong></a></p></td>
<td align="left"><p>The <a href="wdm-markirppending.md" data-raw-source="[&lt;strong&gt;MarkIrpPending&lt;/strong&gt;](wdm-markirppending.md)"><strong>MarkIrpPending</strong></a> rule specifies that whenever a driver dispatch routine calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff549422" data-raw-source="[&lt;strong&gt;IoMarkIrpPending&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549422)"><strong>IoMarkIrpPending</strong></a>, the driver returns STATUS_PENDING when the dispatch routine ends. See <a href="wdm-markirppending2.md" data-raw-source="[&lt;strong&gt;MarkIrpPending2&lt;/strong&gt;](wdm-markirppending2.md)"><strong>MarkIrpPending2</strong></a> for a complimentary specification.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="wdm-markirppending2.md" data-raw-source="[&lt;strong&gt;MarkIrpPending2&lt;/strong&gt;](wdm-markirppending2.md)"><strong>MarkIrpPending2</strong></a></p></td>
<td align="left"><p>The <a href="wdm-markirppending2.md" data-raw-source="[&lt;strong&gt;MarkIrpPending2&lt;/strong&gt;](wdm-markirppending2.md)"><strong>MarkIrpPending2</strong></a> rule specifies that if a dispatch routine returns STATUS_PENDING, it has called <a href="https://msdn.microsoft.com/library/windows/hardware/ff549422" data-raw-source="[&lt;strong&gt;IoMarkIrpPending&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549422)"><strong>IoMarkIrpPending</strong></a> or passed the IRP to the lower driver. See <a href="wdm-markirppending.md" data-raw-source="[&lt;strong&gt;MarkIrpPending&lt;/strong&gt;](wdm-markirppending.md)"><strong>MarkIrpPending</strong></a> for a complimentary specification.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="wdm-markpower.md" data-raw-source="[&lt;strong&gt;MarkPower&lt;/strong&gt;](wdm-markpower.md)"><strong>MarkPower</strong></a></p></td>
<td align="left"><p>The <a href="wdm-markpower.md" data-raw-source="[&lt;strong&gt;MarkPower&lt;/strong&gt;](wdm-markpower.md)"><strong>MarkPower</strong></a> rule specifies that an IRP_MJ_POWER with IRP_MN_SET_POWER for <strong>SystemPowerState</strong> IRP going to S0 is pended. This rule only applies to FDO and FIDO drivers.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="wdm-markpowerdown.md" data-raw-source="[&lt;strong&gt;MarkPowerDown&lt;/strong&gt;](wdm-markpowerdown.md)"><strong>MarkPowerDown</strong></a></p></td>
<td align="left"><p>The <a href="wdm-markpowerdown.md" data-raw-source="[&lt;strong&gt;MarkPowerDown&lt;/strong&gt;](wdm-markpowerdown.md)"><strong>MarkPowerDown</strong></a> rule specifies that an IRP_MJ_POWER with IRP_MN_SET_POWER for <strong>SystemPowerState</strong> IRP going from s0 to [S1...S5] is pended.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="wdm-markqueryrelations.md" data-raw-source="[&lt;strong&gt;MarkQueryRelations&lt;/strong&gt;](wdm-markqueryrelations.md)"><strong>MarkQueryRelations</strong></a></p></td>
<td align="left"><p>The <a href="wdm-markqueryrelations.md" data-raw-source="[&lt;strong&gt;MarkQueryRelations&lt;/strong&gt;](wdm-markqueryrelations.md)"><strong>MarkQueryRelations</strong></a> rule specifies that the driver should pend the IRP_MN_QUERY_DEVICE_RELATIONS IRP.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="wdm-markstartdevice.md" data-raw-source="[&lt;strong&gt;MarkStartDevice&lt;/strong&gt;](wdm-markstartdevice.md)"><strong>MarkStartDevice</strong></a></p></td>
<td align="left"><p>The <a href="wdm-markstartdevice.md" data-raw-source="[&lt;strong&gt;MarkStartDevice&lt;/strong&gt;](wdm-markstartdevice.md)"><strong>MarkStartDevice</strong></a> rule specifies that the driver pends an IRP_MN_START_DEVICE IRP correctly. This rule only applies to FDO and FIDO drivers.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="wdm-pendedcompletedrequest.md" data-raw-source="[&lt;strong&gt;PendedCompletedRequest&lt;/strong&gt;](wdm-pendedcompletedrequest.md)"><strong>PendedCompletedRequest</strong></a></p></td>
<td align="left"><p>The <a href="wdm-pendedcompletedrequest.md" data-raw-source="[&lt;strong&gt;PendedCompletedRequest&lt;/strong&gt;](wdm-pendedcompletedrequest.md)"><strong>PendedCompletedRequest</strong></a> rule specifies that a driver&#39;s dispatch routine does not return STATUS_PENDING on an IRP if the driver has called <a href="https://msdn.microsoft.com/library/windows/hardware/ff548343" data-raw-source="[&lt;strong&gt;IoCompleteRequest&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548343)"><strong>IoCompleteRequest</strong></a> on the incoming IRP.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="wdm-pendedcompletedrequest2.md" data-raw-source="[&lt;strong&gt;PendedCompletedRequest2&lt;/strong&gt;](wdm-pendedcompletedrequest2.md)"><strong>PendedCompletedRequest2</strong></a></p></td>
<td align="left"><p>The <a href="wdm-pendedcompletedrequest2.md" data-raw-source="[&lt;strong&gt;PendedCompletedRequest2&lt;/strong&gt;](wdm-pendedcompletedrequest2.md)"><strong>PendedCompletedRequest2</strong></a> rule specifies that a wait is required after a call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff548336" data-raw-source="[&lt;strong&gt;IoCallDriver&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548336)"><strong>IoCallDriver</strong></a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff559654" data-raw-source="[&lt;strong&gt;PoCallDriver&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff559654)"><strong>PoCallDriver</strong></a> because the dispatch routine could complete a pending IRP.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="wdm-pendedcompletedrequest3.md" data-raw-source="[&lt;strong&gt;PendedCompletedRequest3&lt;/strong&gt;](wdm-pendedcompletedrequest3.md)"><strong>PendedCompletedRequest3</strong></a></p></td>
<td align="left"><p>The <a href="wdm-pendedcompletedrequest3.md" data-raw-source="[&lt;strong&gt;PendedCompletedRequest3&lt;/strong&gt;](wdm-pendedcompletedrequest3.md)"><strong>PendedCompletedRequest3</strong></a> rule specifies that a pending IRP should not be completed with a call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff548343" data-raw-source="[&lt;strong&gt;IoCompleteRequest&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548343)"><strong>IoCompleteRequest</strong></a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="wdm-pendedcompletedrequestex.md" data-raw-source="[&lt;strong&gt;PendedCompletedRequestEx&lt;/strong&gt;](wdm-pendedcompletedrequestex.md)"><strong>PendedCompletedRequestEx</strong></a></p></td>
<td align="left"><p>The <a href="wdm-pendedcompletedrequestex.md" data-raw-source="[&lt;strong&gt;PendedCompletedRequestEx&lt;/strong&gt;](wdm-pendedcompletedrequestex.md)"><strong>PendedCompletedRequestEx</strong></a> rule specifies that the driver should not call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548343" data-raw-source="[&lt;strong&gt;IoCompleteRequest&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548343)"><strong>IoCompleteRequest</strong></a> for a pending IRP.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="wdm-startdevicewait.md" data-raw-source="[&lt;strong&gt;StartDeviceWait&lt;/strong&gt;](wdm-startdevicewait.md)"><strong>StartDeviceWait</strong></a></p></td>
<td align="left"><p>The <a href="wdm-startdevicewait.md" data-raw-source="[&lt;strong&gt;StartDeviceWait&lt;/strong&gt;](wdm-startdevicewait.md)"><strong>StartDeviceWait</strong></a> rule specifies that the driver should not call <a href="https://msdn.microsoft.com/library/windows/hardware/ff553350" data-raw-source="[&lt;strong&gt;KeWaitForSingleObject&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553350)"><strong>KeWaitForSingleObject</strong></a> in the context of start device IRP.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="wdm-startdevicewait2.md" data-raw-source="[&lt;strong&gt;StartDeviceWait2&lt;/strong&gt;](wdm-startdevicewait2.md)"><strong>StartDeviceWait2</strong></a></p></td>
<td align="left"><p>The <a href="wdm-startdevicewait2.md" data-raw-source="[&lt;strong&gt;StartDeviceWait2&lt;/strong&gt;](wdm-startdevicewait2.md)"><strong>StartDeviceWait2</strong></a> rule specifies that the driver should not call <a href="https://msdn.microsoft.com/library/windows/hardware/ff553350" data-raw-source="[&lt;strong&gt;KeWaitForSingleObject&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553350)"><strong>KeWaitForSingleObject</strong></a> in the context of start device IRP.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="wdm-startdevicewait3.md" data-raw-source="[&lt;strong&gt;StartDeviceWait3&lt;/strong&gt;](wdm-startdevicewait3.md)"><strong>StartDeviceWait3</strong></a></p></td>
<td align="left"><p>The <a href="wdm-startdevicewait3.md" data-raw-source="[&lt;strong&gt;StartDeviceWait3&lt;/strong&gt;](wdm-startdevicewait3.md)"><strong>StartDeviceWait3</strong></a> rule specifies that the driver should not call <a href="https://msdn.microsoft.com/library/windows/hardware/ff553350" data-raw-source="[&lt;strong&gt;KeWaitForSingleObject&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553350)"><strong>KeWaitForSingleObject</strong></a> in the context of start device IRP.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="wdm-startdevicewait4.md" data-raw-source="[&lt;strong&gt;StartDeviceWait4&lt;/strong&gt;](wdm-startdevicewait4.md)"><strong>StartDeviceWait4</strong></a></p></td>
<td align="left"><p>The <a href="wdm-startdevicewait4.md" data-raw-source="[&lt;strong&gt;StartDeviceWait4&lt;/strong&gt;](wdm-startdevicewait4.md)"><strong>StartDeviceWait4</strong></a> rule specifies that the driver should not call <a href="https://msdn.microsoft.com/library/windows/hardware/ff553350" data-raw-source="[&lt;strong&gt;KeWaitForSingleObject&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553350)"><strong>KeWaitForSingleObject</strong></a> in the context of start device IRP.</p></td>
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

 

 





