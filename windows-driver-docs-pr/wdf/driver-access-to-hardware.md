---
title: Driver Access to Hardware
description: Driver Access to Hardware
ms.assetid: 66743284-6cdd-467e-b3b4-3d588cd296a5
keywords:
- PnP WDK KMDF , hardware access
- Plug and Play WDK KMDF , hardware access
- power management WDK KMDF , hardware access
- hardware access WDK KMDF
- framework objects WDK KMDF , device objects
- framework objects WDK KMDF , hardware access
- device objects WDK KMDF
- event callback functions WDK KMDF
- callback functions WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Driver Access to Hardware


The following table lists all of the event callback functions that the framework device object defines, in alphabetical order. The table shows you the callback functions in which your driver can access the hardware that the callback function's WDFDEVICE handle represents. You can access the hardware because the device is in its working (D0) state.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Event callbacks functionsfor framework device objects</th>
<th align="left">Is hardware accessible?</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540843" data-raw-source="[&lt;em&gt;EvtDeviceArmWakeFromS0&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540843)"><em>EvtDeviceArmWakeFromS0</em></a></p></td>
<td align="left"><p>Yes</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540844" data-raw-source="[&lt;em&gt;EvtDeviceArmWakeFromSx&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540844)"><em>EvtDeviceArmWakeFromSx</em></a></p></td>
<td align="left"><p>Yes</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540846" data-raw-source="[&lt;em&gt;EvtDeviceArmWakeFromSxWithReason&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540846)"><em>EvtDeviceArmWakeFromSxWithReason</em></a></p></td>
<td align="left"><p>Yes</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540848" data-raw-source="[&lt;em&gt;EvtDeviceD0Entry&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540848)"><em>EvtDeviceD0Entry</em></a></p></td>
<td align="left"><p>Yes</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540855" data-raw-source="[&lt;em&gt;EvtDeviceD0Exit&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540855)"><em>EvtDeviceD0Exit</em></a></p></td>
<td align="left"><p>Yes</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540858" data-raw-source="[&lt;em&gt;EvtDeviceDisableWakeAtBus&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540858)"><em>EvtDeviceDisableWakeAtBus</em></a></p></td>
<td align="left"><p>Parent bus might be at D0. The device might be at D0.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540860" data-raw-source="[&lt;em&gt;EvtDeviceDisarmWakeFromS0&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540860)"><em>EvtDeviceDisarmWakeFromS0</em></a></p></td>
<td align="left"><p>Yes</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540862" data-raw-source="[&lt;em&gt;EvtDeviceDisarmWakeFromSx&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540862)"><em>EvtDeviceDisarmWakeFromSx</em></a></p></td>
<td align="left"><p>Yes</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540863" data-raw-source="[&lt;em&gt;EvtDeviceEject&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540863)"><em>EvtDeviceEject</em></a></p></td>
<td align="left"><p>No</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540866" data-raw-source="[&lt;em&gt;EvtDeviceEnableWakeAtBus&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540866)"><em>EvtDeviceEnableWakeAtBus</em></a></p></td>
<td align="left"><p>Parent bus is at D0, but the device might not be.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540868" data-raw-source="[&lt;em&gt;EvtDeviceFileCreate&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540868)"><em>EvtDeviceFileCreate</em></a></p></td>
<td align="left"><p>Maybe</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540870" data-raw-source="[&lt;em&gt;EvtDeviceFilterAddResourceRequirements&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540870)"><em>EvtDeviceFilterAddResourceRequirements</em></a></p></td>
<td align="left"><p>No</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540872" data-raw-source="[&lt;em&gt;EvtDeviceFilterRemoveResourceRequirements&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540872)"><em>EvtDeviceFilterRemoveResourceRequirements</em></a></p></td>
<td align="left"><p>No</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540880" data-raw-source="[&lt;em&gt;EvtDevicePrepareHardware&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540880)"><em>EvtDevicePrepareHardware</em></a></p></td>
<td align="left"><p>Yes</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540886" data-raw-source="[&lt;em&gt;EvtDeviceRelationsQuery&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540886)"><em>EvtDeviceRelationsQuery</em></a></p></td>
<td align="left"><p>Yes, but the device might be in a sleeping state.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540890" data-raw-source="[&lt;em&gt;EvtDeviceReleaseHardware&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540890)"><em>EvtDeviceReleaseHardware</em></a></p></td>
<td align="left"><p>No</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540892" data-raw-source="[&lt;em&gt;EvtDeviceRemoveAddedResources&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540892)"><em>EvtDeviceRemoveAddedResources</em></a></p></td>
<td align="left"><p>Yes, but resources have not been assigned to the device.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540894" data-raw-source="[&lt;em&gt;EvtDeviceResourceRequirementsQuery&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540894)"><em>EvtDeviceResourceRequirementsQuery</em></a></p></td>
<td align="left"><p>No</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540895" data-raw-source="[&lt;em&gt;EvtDeviceResourcesQuery&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540895)"><em>EvtDeviceResourcesQuery</em></a></p></td>
<td align="left"><p>No</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540898" data-raw-source="[&lt;em&gt;EvtDeviceSelfManagedIoCleanup&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540898)"><em>EvtDeviceSelfManagedIoCleanup</em></a></p></td>
<td align="left"><p>No</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540901" data-raw-source="[&lt;em&gt;EvtDeviceSelfManagedIoFlush&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540901)"><em>EvtDeviceSelfManagedIoFlush</em></a></p></td>
<td align="left"><p>No</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540902" data-raw-source="[&lt;em&gt;EvtDeviceSelfManagedIoInit&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540902)"><em>EvtDeviceSelfManagedIoInit</em></a></p></td>
<td align="left"><p>Yes</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540905" data-raw-source="[&lt;em&gt;EvtDeviceSelfManagedIoRestart&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540905)"><em>EvtDeviceSelfManagedIoRestart</em></a></p></td>
<td align="left"><p>Yes</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540907" data-raw-source="[&lt;em&gt;EvtDeviceSelfManagedIoSuspend&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540907)"><em>EvtDeviceSelfManagedIoSuspend</em></a></p></td>
<td align="left"><p>No, if device has been surprise-removed; otherwise, yes.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540909" data-raw-source="[&lt;em&gt;EvtDeviceSetLock&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540909)"><em>EvtDeviceSetLock</em></a></p></td>
<td align="left"><p>No</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540913" data-raw-source="[&lt;em&gt;EvtDeviceSurpriseRemoval&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540913)"><em>EvtDeviceSurpriseRemoval</em></a></p></td>
<td align="left"><p>No</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540915" data-raw-source="[&lt;em&gt;EvtDeviceUsageNotification&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540915)"><em>EvtDeviceUsageNotification</em></a></p></td>
<td align="left"><p>Yes</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540919" data-raw-source="[&lt;em&gt;EvtDeviceWakeFromS0Triggered&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540919)"><em>EvtDeviceWakeFromS0Triggered</em></a></p></td>
<td align="left"><p>Yes</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540923" data-raw-source="[&lt;em&gt;EvtDeviceWakeFromSxTriggered&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540923)"><em>EvtDeviceWakeFromSxTriggered</em></a></p></td>
<td align="left"><p>Yes</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540925" data-raw-source="[&lt;em&gt;EvtDeviceWdmIrpPreprocess&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540925)"><em>EvtDeviceWdmIrpPreprocess</em></a></p></td>
<td align="left"><p>Depends on the IRP.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540874" data-raw-source="[&lt;em&gt;EvtDevicePnpStateChange&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540874)"><em>EvtDevicePnpStateChange</em></a></p></td>
<td align="left"><p>Depends on the state.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540876" data-raw-source="[&lt;em&gt;EvtDevicePowerPolicyStateChange&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540876)"><em>EvtDevicePowerPolicyStateChange</em></a></p></td>
<td align="left"><p>Depends on the state.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540878" data-raw-source="[&lt;em&gt;EvtDevicePowerStateChange&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540878)"><em>EvtDevicePowerStateChange</em></a></p></td>
<td align="left"><p>Depends on the state.</p></td>
</tr>
</tbody>
</table>

 

 

 





