---
title: Driver Access to Hardware
description: Driver Access to Hardware
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
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_arm_wake_from_s0" data-raw-source="[&lt;em&gt;EvtDeviceArmWakeFromS0&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_arm_wake_from_s0)"><em>EvtDeviceArmWakeFromS0</em></a></p></td>
<td align="left"><p>Yes</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_arm_wake_from_sx" data-raw-source="[&lt;em&gt;EvtDeviceArmWakeFromSx&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_arm_wake_from_sx)"><em>EvtDeviceArmWakeFromSx</em></a></p></td>
<td align="left"><p>Yes</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_arm_wake_from_sx_with_reason" data-raw-source="[&lt;em&gt;EvtDeviceArmWakeFromSxWithReason&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_arm_wake_from_sx_with_reason)"><em>EvtDeviceArmWakeFromSxWithReason</em></a></p></td>
<td align="left"><p>Yes</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_entry" data-raw-source="[&lt;em&gt;EvtDeviceD0Entry&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_entry)"><em>EvtDeviceD0Entry</em></a></p></td>
<td align="left"><p>Yes</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_exit" data-raw-source="[&lt;em&gt;EvtDeviceD0Exit&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_exit)"><em>EvtDeviceD0Exit</em></a></p></td>
<td align="left"><p>Yes</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdfpdo/nc-wdfpdo-evt_wdf_device_disable_wake_at_bus" data-raw-source="[&lt;em&gt;EvtDeviceDisableWakeAtBus&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfpdo/nc-wdfpdo-evt_wdf_device_disable_wake_at_bus)"><em>EvtDeviceDisableWakeAtBus</em></a></p></td>
<td align="left"><p>Parent bus might be at D0. The device might be at D0.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_disarm_wake_from_s0" data-raw-source="[&lt;em&gt;EvtDeviceDisarmWakeFromS0&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_disarm_wake_from_s0)"><em>EvtDeviceDisarmWakeFromS0</em></a></p></td>
<td align="left"><p>Yes</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_disarm_wake_from_sx" data-raw-source="[&lt;em&gt;EvtDeviceDisarmWakeFromSx&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_disarm_wake_from_sx)"><em>EvtDeviceDisarmWakeFromSx</em></a></p></td>
<td align="left"><p>Yes</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdfpdo/nc-wdfpdo-evt_wdf_device_eject" data-raw-source="[&lt;em&gt;EvtDeviceEject&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfpdo/nc-wdfpdo-evt_wdf_device_eject)"><em>EvtDeviceEject</em></a></p></td>
<td align="left"><p>No</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdfpdo/nc-wdfpdo-evt_wdf_device_enable_wake_at_bus" data-raw-source="[&lt;em&gt;EvtDeviceEnableWakeAtBus&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfpdo/nc-wdfpdo-evt_wdf_device_enable_wake_at_bus)"><em>EvtDeviceEnableWakeAtBus</em></a></p></td>
<td align="left"><p>Parent bus is at D0, but the device might not be.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_file_create" data-raw-source="[&lt;em&gt;EvtDeviceFileCreate&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_file_create)"><em>EvtDeviceFileCreate</em></a></p></td>
<td align="left"><p>Maybe</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdffdo/nc-wdffdo-evt_wdf_device_filter_resource_requirements" data-raw-source="[&lt;em&gt;EvtDeviceFilterAddResourceRequirements&lt;/em&gt;](/windows-hardware/drivers/ddi/wdffdo/nc-wdffdo-evt_wdf_device_filter_resource_requirements)"><em>EvtDeviceFilterAddResourceRequirements</em></a></p></td>
<td align="left"><p>No</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdffdo/nc-wdffdo-evt_wdf_device_filter_resource_requirements" data-raw-source="[&lt;em&gt;EvtDeviceFilterRemoveResourceRequirements&lt;/em&gt;](/windows-hardware/drivers/ddi/wdffdo/nc-wdffdo-evt_wdf_device_filter_resource_requirements)"><em>EvtDeviceFilterRemoveResourceRequirements</em></a></p></td>
<td align="left"><p>No</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_prepare_hardware" data-raw-source="[&lt;em&gt;EvtDevicePrepareHardware&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_prepare_hardware)"><em>EvtDevicePrepareHardware</em></a></p></td>
<td align="left"><p>Yes</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_relations_query" data-raw-source="[&lt;em&gt;EvtDeviceRelationsQuery&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_relations_query)"><em>EvtDeviceRelationsQuery</em></a></p></td>
<td align="left"><p>Yes, but the device might be in a sleeping state.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_release_hardware" data-raw-source="[&lt;em&gt;EvtDeviceReleaseHardware&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_release_hardware)"><em>EvtDeviceReleaseHardware</em></a></p></td>
<td align="left"><p>No</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdffdo/nc-wdffdo-evt_wdf_device_remove_added_resources" data-raw-source="[&lt;em&gt;EvtDeviceRemoveAddedResources&lt;/em&gt;](/windows-hardware/drivers/ddi/wdffdo/nc-wdffdo-evt_wdf_device_remove_added_resources)"><em>EvtDeviceRemoveAddedResources</em></a></p></td>
<td align="left"><p>Yes, but resources have not been assigned to the device.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdfpdo/nc-wdfpdo-evt_wdf_device_resource_requirements_query" data-raw-source="[&lt;em&gt;EvtDeviceResourceRequirementsQuery&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfpdo/nc-wdfpdo-evt_wdf_device_resource_requirements_query)"><em>EvtDeviceResourceRequirementsQuery</em></a></p></td>
<td align="left"><p>No</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdfpdo/nc-wdfpdo-evt_wdf_device_resources_query" data-raw-source="[&lt;em&gt;EvtDeviceResourcesQuery&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfpdo/nc-wdfpdo-evt_wdf_device_resources_query)"><em>EvtDeviceResourcesQuery</em></a></p></td>
<td align="left"><p>No</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_self_managed_io_cleanup" data-raw-source="[&lt;em&gt;EvtDeviceSelfManagedIoCleanup&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_self_managed_io_cleanup)"><em>EvtDeviceSelfManagedIoCleanup</em></a></p></td>
<td align="left"><p>No</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_self_managed_io_flush" data-raw-source="[&lt;em&gt;EvtDeviceSelfManagedIoFlush&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_self_managed_io_flush)"><em>EvtDeviceSelfManagedIoFlush</em></a></p></td>
<td align="left"><p>No</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_self_managed_io_init" data-raw-source="[&lt;em&gt;EvtDeviceSelfManagedIoInit&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_self_managed_io_init)"><em>EvtDeviceSelfManagedIoInit</em></a></p></td>
<td align="left"><p>Yes</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_self_managed_io_restart" data-raw-source="[&lt;em&gt;EvtDeviceSelfManagedIoRestart&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_self_managed_io_restart)"><em>EvtDeviceSelfManagedIoRestart</em></a></p></td>
<td align="left"><p>Yes</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_self_managed_io_suspend" data-raw-source="[&lt;em&gt;EvtDeviceSelfManagedIoSuspend&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_self_managed_io_suspend)"><em>EvtDeviceSelfManagedIoSuspend</em></a></p></td>
<td align="left"><p>No, if device has been surprise-removed; otherwise, yes.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdfpdo/nc-wdfpdo-evt_wdf_device_set_lock" data-raw-source="[&lt;em&gt;EvtDeviceSetLock&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfpdo/nc-wdfpdo-evt_wdf_device_set_lock)"><em>EvtDeviceSetLock</em></a></p></td>
<td align="left"><p>No</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_surprise_removal" data-raw-source="[&lt;em&gt;EvtDeviceSurpriseRemoval&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_surprise_removal)"><em>EvtDeviceSurpriseRemoval</em></a></p></td>
<td align="left"><p>No</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_usage_notification" data-raw-source="[&lt;em&gt;EvtDeviceUsageNotification&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_usage_notification)"><em>EvtDeviceUsageNotification</em></a></p></td>
<td align="left"><p>Yes</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_wake_from_s0_triggered" data-raw-source="[&lt;em&gt;EvtDeviceWakeFromS0Triggered&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_wake_from_s0_triggered)"><em>EvtDeviceWakeFromS0Triggered</em></a></p></td>
<td align="left"><p>Yes</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_wake_from_sx_triggered" data-raw-source="[&lt;em&gt;EvtDeviceWakeFromSxTriggered&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_wake_from_sx_triggered)"><em>EvtDeviceWakeFromSxTriggered</em></a></p></td>
<td align="left"><p>Yes</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_preprocess" data-raw-source="[&lt;em&gt;EvtDeviceWdmIrpPreprocess&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_preprocess)"><em>EvtDeviceWdmIrpPreprocess</em></a></p></td>
<td align="left"><p>Depends on the IRP.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_pnp_state_change_notification" data-raw-source="[&lt;em&gt;EvtDevicePnpStateChange&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_pnp_state_change_notification)"><em>EvtDevicePnpStateChange</em></a></p></td>
<td align="left"><p>Depends on the state.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_power_policy_state_change_notification" data-raw-source="[&lt;em&gt;EvtDevicePowerPolicyStateChange&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_power_policy_state_change_notification)"><em>EvtDevicePowerPolicyStateChange</em></a></p></td>
<td align="left"><p>Depends on the state.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_power_state_change_notification" data-raw-source="[&lt;em&gt;EvtDevicePowerStateChange&lt;/em&gt;](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_power_state_change_notification)"><em>EvtDevicePowerStateChange</em></a></p></td>
<td align="left"><p>Depends on the state.</p></td>
</tr>
</tbody>
</table>

 

