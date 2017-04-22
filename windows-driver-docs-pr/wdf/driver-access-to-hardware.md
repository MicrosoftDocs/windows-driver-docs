---
title: Driver Access to Hardware
author: windows-driver-content
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
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
<td align="left"><p>[<em>EvtDeviceArmWakeFromS0</em>](https://msdn.microsoft.com/library/windows/hardware/ff540843)</p></td>
<td align="left"><p>Yes</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>EvtDeviceArmWakeFromSx</em>](https://msdn.microsoft.com/library/windows/hardware/ff540844)</p></td>
<td align="left"><p>Yes</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>EvtDeviceArmWakeFromSxWithReason</em>](https://msdn.microsoft.com/library/windows/hardware/ff540846)</p></td>
<td align="left"><p>Yes</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>EvtDeviceD0Entry</em>](https://msdn.microsoft.com/library/windows/hardware/ff540848)</p></td>
<td align="left"><p>Yes</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>EvtDeviceD0Exit</em>](https://msdn.microsoft.com/library/windows/hardware/ff540855)</p></td>
<td align="left"><p>Yes</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>EvtDeviceDisableWakeAtBus</em>](https://msdn.microsoft.com/library/windows/hardware/ff540858)</p></td>
<td align="left"><p>Parent bus might be at D0. The device might be at D0.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>EvtDeviceDisarmWakeFromS0</em>](https://msdn.microsoft.com/library/windows/hardware/ff540860)</p></td>
<td align="left"><p>Yes</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>EvtDeviceDisarmWakeFromSx</em>](https://msdn.microsoft.com/library/windows/hardware/ff540862)</p></td>
<td align="left"><p>Yes</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>EvtDeviceEject</em>](https://msdn.microsoft.com/library/windows/hardware/ff540863)</p></td>
<td align="left"><p>No</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>EvtDeviceEnableWakeAtBus</em>](https://msdn.microsoft.com/library/windows/hardware/ff540866)</p></td>
<td align="left"><p>Parent bus is at D0, but the device might not be.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>EvtDeviceFileCreate</em>](https://msdn.microsoft.com/library/windows/hardware/ff540868)</p></td>
<td align="left"><p>Maybe</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>EvtDeviceFilterAddResourceRequirements</em>](https://msdn.microsoft.com/library/windows/hardware/ff540870)</p></td>
<td align="left"><p>No</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>EvtDeviceFilterRemoveResourceRequirements</em>](https://msdn.microsoft.com/library/windows/hardware/ff540872)</p></td>
<td align="left"><p>No</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>EvtDevicePrepareHardware</em>](https://msdn.microsoft.com/library/windows/hardware/ff540880)</p></td>
<td align="left"><p>Yes</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>EvtDeviceRelationsQuery</em>](https://msdn.microsoft.com/library/windows/hardware/ff540886)</p></td>
<td align="left"><p>Yes, but the device might be in a sleeping state.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>EvtDeviceReleaseHardware</em>](https://msdn.microsoft.com/library/windows/hardware/ff540890)</p></td>
<td align="left"><p>No</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>EvtDeviceRemoveAddedResources</em>](https://msdn.microsoft.com/library/windows/hardware/ff540892)</p></td>
<td align="left"><p>Yes, but resources have not been assigned to the device.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>EvtDeviceResourceRequirementsQuery</em>](https://msdn.microsoft.com/library/windows/hardware/ff540894)</p></td>
<td align="left"><p>No</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>EvtDeviceResourcesQuery</em>](https://msdn.microsoft.com/library/windows/hardware/ff540895)</p></td>
<td align="left"><p>No</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>EvtDeviceSelfManagedIoCleanup</em>](https://msdn.microsoft.com/library/windows/hardware/ff540898)</p></td>
<td align="left"><p>No</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>EvtDeviceSelfManagedIoFlush</em>](https://msdn.microsoft.com/library/windows/hardware/ff540901)</p></td>
<td align="left"><p>No</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>EvtDeviceSelfManagedIoInit</em>](https://msdn.microsoft.com/library/windows/hardware/ff540902)</p></td>
<td align="left"><p>Yes</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>EvtDeviceSelfManagedIoRestart</em>](https://msdn.microsoft.com/library/windows/hardware/ff540905)</p></td>
<td align="left"><p>Yes</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>EvtDeviceSelfManagedIoSuspend</em>](https://msdn.microsoft.com/library/windows/hardware/ff540907)</p></td>
<td align="left"><p>No, if device has been surprise-removed; otherwise, yes.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>EvtDeviceSetLock</em>](https://msdn.microsoft.com/library/windows/hardware/ff540909)</p></td>
<td align="left"><p>No</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>EvtDeviceSurpriseRemoval</em>](https://msdn.microsoft.com/library/windows/hardware/ff540913)</p></td>
<td align="left"><p>No</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>EvtDeviceUsageNotification</em>](https://msdn.microsoft.com/library/windows/hardware/ff540915)</p></td>
<td align="left"><p>Yes</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>EvtDeviceWakeFromS0Triggered</em>](https://msdn.microsoft.com/library/windows/hardware/ff540919)</p></td>
<td align="left"><p>Yes</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>EvtDeviceWakeFromSxTriggered</em>](https://msdn.microsoft.com/library/windows/hardware/ff540923)</p></td>
<td align="left"><p>Yes</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>EvtDeviceWdmIrpPreprocess</em>](https://msdn.microsoft.com/library/windows/hardware/ff540925)</p></td>
<td align="left"><p>Depends on the IRP.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>EvtDevicePnpStateChange</em>](https://msdn.microsoft.com/library/windows/hardware/ff540874)</p></td>
<td align="left"><p>Depends on the state.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>EvtDevicePowerPolicyStateChange</em>](https://msdn.microsoft.com/library/windows/hardware/ff540876)</p></td>
<td align="left"><p>Depends on the state.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>EvtDevicePowerStateChange</em>](https://msdn.microsoft.com/library/windows/hardware/ff540878)</p></td>
<td align="left"><p>Depends on the state.</p></td>
</tr>
</tbody>
</table>

 

 

 





