---
title: Device Power Management (DPM) Notifications
description: Each device power management (DPM) notification that the PEP's AcceptDeviceNotification callback routine receives is accompanied by a Notification parameter that indicates the type of notification, and a Data parameter that points to a data structure that contains the information for the specified notification type.
keywords: [AcceptDeviceNotification]
ms.date: 01/17/2018
---

# Device power management (DPM) notifications

Each device power management (DPM) notification that the PEP's AcceptDeviceNotification callback routine receives is accompanied by a Notification parameter that indicates the type of notification, and a Data parameter that points to a data structure that contains the information for the specified notification type.

In this call, the Notification parameter is set to a PEP_DPM_XXX constant value that indicates the notification type. The Data parameter points to a PEP_XXX structure type that is associated with this notification type.

|Notification ID|Value|Associated structure|
|----|----|----|
|[PEP_DPM_PREPARE_DEVICE](#pep_dpm_prepare_device)|0x01|[PEP_PREPARE_DEVICE](/windows-hardware/drivers/ddi/pepfx/ns-pepfx-_pep_prepare_device)|
|[PEP_DPM_ABANDON_DEVICE](#pep_dpm_abandon_device)|0x02|[PEP_ABANDON_DEVICE](/windows-hardware/drivers/ddi/pepfx/ns-pepfx-_pep_abandon_device)|
|[PEP_DPM_REGISTER_DEVICE](#pep_dpm_register_device)|0x03|[PEP_REGISTER_DEVICE_V2](/windows-hardware/drivers/ddi/pepfx/ns-pepfx-_pep_register_device_v2)|
|[PEP_DPM_UNREGISTER_DEVICE](#pep_dpm_unregister_device)|0x04|[PEP_UNREGISTER_DEVICE](/windows-hardware/drivers/ddi/pepfx/ns-pepfx-_pep_unregister_device)|
|[PEP_DPM_DEVICE_POWER_STATE](#pep_dpm_device_power_state)|0x05|[PEP_DEVICE_POWER_STATE](/windows-hardware/drivers/ddi/pepfx/ns-pepfx-_pep_device_power_state)|
|[PEP_DPM_COMPONENT_ACTIVE](#pep_dpm_component_active)|0x07|[PEP_COMPONENT_ACTIVE](/windows-hardware/drivers/ddi/pep_x/ns-pep_x-_pep_component_active)|
|[PEP_DPM_WORK](#pep_dpm_work)|0x0D|[PEP_WORK](/windows-hardware/drivers/ddi/pepfx/ns-pepfx-_pep_work)|
|[PEP_DPM_POWER_CONTROL_REQUEST](#pep_dpm_power_control_request)|0x0E|[PEP_POWER_CONTROL_REQUEST](/windows-hardware/drivers/ddi/pepfx/ns-pepfx-_pep_power_control_request)|
|[PEP_DPM_POWER_CONTROL_COMPLETE](#pep_dpm_power_control_complete)|0x0F|[PEP_POWER_CONTROL_COMPLETE](/windows-hardware/drivers/ddi/pepfx/ns-pepfx-_pep_power_control_complete)|
|[PEP_DPM_SYSTEM_LATENCY_UPDATE](#pep_dpm_system_latency_update)|0x10|[PEP_SYSTEM_LATENCY](/windows-hardware/drivers/ddi/pepfx/ns-pepfx-_pep_system_latency)|
|[PEP_DPM_DEVICE_STARTED](#pep_dpm_device_started)|0x12|[PEP_DEVICE_STARTED](/windows-hardware/drivers/ddi/pepfx/ns-pepfx-_pep_device_started)|
|[PEP_DPM_NOTIFY_COMPONENT_IDLE_STATE](#pep_dpm_notify_component_idle_state)|0x13|[PEP_NOTIFY_COMPONENT_IDLE_STATE](/windows-hardware/drivers/ddi/pepfx/ns-pepfx-_pep_notify_component_idle_state)|
|[PEP_DPM_REGISTER_DEBUGGER](#pep_dpm_register_debugger)|0x15|[PEP_REGISTER_DEBUGGER](/windows-hardware/drivers/ddi/pepfx/ns-pepfx-_pep_register_debugger)|
|[PEP_DPM_LOW_POWER_EPOCH](#pep_dpm_low_power_epoch)|0x18|[PEP_LOW_POWER_EPOCH](/windows-hardware/drivers/ddi/pepfx/ns-pepfx-_pep_low_power_epoch)|
|[PEP_DPM_REGISTER_CRASHDUMP_DEVICE](#pep_dpm_register_crashdump_device)|0x19|[PEP_REGISTER_CRASHDUMP_DEVICE](/windows-hardware/drivers/ddi/pepfx/ns-pepfx-_pep_register_crashdump_device)|
|[PEP_DPM_DEVICE_IDLE_CONSTRAINTS](#pep_dpm_device_idle_constraints)|0x1A|[PEP_DEVICE_PLATFORM_CONSTRAINTS](/windows-hardware/drivers/ddi/pepfx/ns-pepfx-_pep_device_platform_constraints)|
|[PEP_DPM_COMPONENT_IDLE_CONSTRAINTS](#pep_dpm_component_idle_constraints)|0x1B|[PEP_COMPONENT_PLATFORM_CONSTRAINTS](/windows-hardware/drivers/ddi/pepfx/ns-pepfx-_pep_component_platform_constraints)|
|[PEP_DPM_QUERY_COMPONENT_PERF_CAPABILITIES](#pep_dpm_query_component_perf_capabilities)|0x1C|[PEP_QUERY_COMPONENT_PERF_CAPABILITIES](/windows-hardware/drivers/ddi/pepfx/ns-pepfx-_pep_query_component_perf_capabilities)|
|[PEP_DPM_QUERY_COMPONENT_PERF_SET](#pep_dpm_query_component_perf_set)|0x1D|[PEP_QUERY_COMPONENT_PERF_SET](/windows-hardware/drivers/ddi/pepfx/ns-pepfx-_pep_query_component_perf_set)|
|[PEP_DPM_QUERY_COMPONENT_PERF_SET_NAME](#pep_dpm_query_component_perf_set_name)|0x1E|[PEP_QUERY_COMPONENT_PERF_SET_NAME](/windows-hardware/drivers/ddi/pepfx/ns-pepfx-_pep_query_component_perf_set_name)|
|[PEP_DPM_QUERY_COMPONENT_PERF_STATES](#pep_dpm_query_component_perf_states)|0x1F|[PEP_QUERY_COMPONENT_PERF_STATES](/windows-hardware/drivers/ddi/pepfx/ns-pepfx-_pep_query_component_perf_states)|
|[PEP_DPM_REGISTER_COMPONENT_PERF_STATES](#pep_dpm_register_component_perf_states)|0x20|[PEP_REGISTER_COMPONENT_PERF_STATES](/windows-hardware/drivers/ddi/pepfx/ns-pepfx-_pep_register_component_perf_states)|
|[PEP_DPM_REQUEST_COMPONENT_PERF_STATE](#pep_dpm_request_component_perf_state)|0x21|[PEP_REQUEST_COMPONENT_PERF_STATE](/windows-hardware/drivers/ddi/pepfx/ns-pepfx-_pep_request_component_perf_state)|
|[PEP_DPM_QUERY_CURRENT_COMPONENT_PERF_STATE](#pep_dpm_query_current_component_perf_state)|0x22|[PEP_QUERY_CURRENT_COMPONENT_PERF_STATE](/windows-hardware/drivers/ddi/pepfx/ns-pepfx-_pep_query_current_component_perf_state)|
|[PEP_DPM_QUERY_DEBUGGER_TRANSITION_REQUIREMENTS](#pep_dpm_query_debugger_transition_requirements)|0x23|[PEP_DEBUGGER_TRANSITION_REQUIREMENTS](/windows-hardware/drivers/ddi/pepfx/ns-pepfx-_pep_debugger_transition_requirements)|
|[PEP_DPM_QUERY_SOC_SUBSYSTEM_COUNT](#pep_dpm_query_soc_subsystem_count)|0x24|[PEP_QUERY_SOC_SUBSYSTEM_COUNT](/windows-hardware/drivers/ddi/pepfx/ns-pepfx-_pep_query_soc_subsystem_count)|
|[PEP_DPM_QUERY_SOC_SUBSYSTEM](#pep_dpm_query_soc_subsystem)|0x25|[PEP_QUERY_SOC_SUBSYSTEM](/windows-hardware/drivers/ddi/pepfx/ns-pepfx-_pep_query_soc_subsystem)|
|[PEP_DPM_RESET_SOC_SUBSYSTEM_ACCOUNTING](#pep_dpm_reset_soc_subsystem_accounting)|0x26|[PEP_RESET_SOC_SUBSYSTEM_ACCOUNTING](/windows-hardware/drivers/ddi/pepfx/ns-pepfx-_pep_reset_soc_subsystem_accounting)|
|[PEP_DPM_QUERY_SOC_SUBSYSTEM_BLOCKING_TIME](#pep_dpm_query_soc_subsystem_blocking_time)|0x27|[PEP_QUERY_SOC_SUBSYSTEM_BLOCKING_TIME](/windows-hardware/drivers/ddi/pepfx/ns-pepfx-_pep_query_soc_subsystem_blocking_time)|
|[PEP_DPM_QUERY_SOC_SUBSYSTEM_METADATA](#pep_dpm_query_soc_subsystem_metadata)|0x28|[PEP_QUERY_SOC_SUBSYSTEM_METADATA](/windows-hardware/drivers/ddi/pepfx/ns-pepfx-_pep_query_soc_subsystem_metadata)|

## Notification Ids

The following DPM notification IDs are used by the AcceptDeviceNotification callback routine.

### PEP_DPM_PREPARE_DEVICE

#### Notification (PEP_DPM_PREPARE_DEVICE)

The value PEP_DPM_PREPARE_DEVICE.

#### Data (PEP_DPM_PREPARE_DEVICE)

A pointer to a [PEP_PREPARE_DEVICE](/windows-hardware/drivers/ddi/pepfx/ns-pepfx-_pep_prepare_device) structure. Tells the PEP that owns the specified device to configure the device to operate in the D0 (working) device power state.

The Windows power management framework (PoFx) sends this notification to the PEP before a device's driver stack is started for the first time by the operating system. This notification allows the PEP to turn on any external power or clock resources that are required to operate the device.

To send a PEP_DPM_PREPARE_DEVICE notification, the operating system calls the PEP's AcceptDeviceNotification callback routine. In this call, the Notification parameter value is PEP_DPM_PREPARE_DEVICE, and the Data parameter points to a PEP_PREPARE_DEVICE structure. On entry, the DeviceId member of this structure is a device identification string that uniquely identifies a device. Before returning, the PEP sets the DeviceAccepted member of this structure to TRUE to claim ownership of the device, or to FALSE to indicate that it does not own the device.

The PEP that owns the power management for a device is responsible for managing power and clock resources that are external to the device and that are needed to operate the device. This PEP enables the clock signal and power to the device in response to a PEP_DPM_PREPARE_DEVICE notification, and removes the clock signal and power from the device in response to a PEP_DPM_ABANDON_DEVICE notification.

The following table shows the preconditions that are in effect when this operating system sends a PEP_DPM_PREPARE_DEVICE notification to the PEP, and the postconditions that must be in effect after the PEP handles this notification for a device that it owns.

|Preconditions|Postconditions|
|----|----|
|The device can be in any power state.|If the PEP claims ownership of the device, the device and all its components must be turned on, and clocks to the device must ungated.</br>The PEP can receive PEP_DPM_PREPARE_DEVICE notifications for multiple devices as the power manager tries to find PEP owners for these devices. The PEP should set the DeviceAccepted member of the PEP_PREPARE_DEVICE structure to FALSE for all devices that the PEP does not own.

No PEP_DPM_PREPARE_DEVICE notifications are sent for core devices.

For a PEP_DPM_PREPARE_DEVICE notification, the AcceptDeviceNotification routine is always called at IRQL = PASSIVE_LEVEL.

### PEP_DPM_ABANDON_DEVICE

#### Notification (PEP_DPM_ABANDON_DEVICE)

The value PEP_DPM_ABANDON_DEVICE.

#### Data (PEP_DPM_ABANDON_DEVICE)

A pointer to a [PEP_ABANDON_DEVICE](/windows-hardware/drivers/ddi/pepfx/ns-pepfx-_pep_abandon_device) structure.
 Tells the PEP that the specified device is no longer being used by the operating system.

The Windows power management framework (PoFx) sends this notification to the PEP after the operating system removes a device's driver stack. This notification allows the PEP to turn off any external power or clock resources that are used to operate the device, and to remove this device from future decision-making processes. If the device must be started again later, the PEP will first receive a PEP_DPM_PREPARE_DEVICE notification.

To send a PEP_DPM_ABANDON_DEVICE notification, the operating system calls the PEP's AcceptDeviceNotification callback routine. In this call, the Notification parameter value is PEP_DPM_ABANDON_DEVICE, and the Data parameter points to a PEP_ABANDON_DEVICE structure. On entry, the DeviceId member of this structure is a device identification string that uniquely identifies a device. Before returning, the PEP sets the DeviceAccepted member of this structure to TRUE to claim ownership of the device, or to FALSE to indicate that it does not own the device.

The PEP that owns the power management for a device is responsible for managing power and clock resources that are external to the device and that are needed to operate the device.

The following table shows the preconditions that are in effect when this operating system sends a PEP_DPM_ABANDON_DEVICE notification to the PEP, and the postconditions that must be in effect after the PEP handles this notification for a device that it owns.

|Preconditions|Postconditions|
|----|----|
|The PEP has received a PEP_DPM_PREPARE_DEVICE notification for the device and accepted ownership of the device.</br>If the PEP has received a PEP_DPM_REGISTER_DEVICE notification for the device and accepted the device registration, it has subsequently received a PEP_DPM_UNREGISTER_DEVICE notification for the device.|Any resources that were allocated in response to the PEP_DPM_PREPARE_DEVICE notification must be freed.</br>For a PEP_DPM_PREPARE_DEVICE notification, the AcceptDeviceNotification routine is always called at IRQL = PASSIVE_LEVEL.|

### PEP_DPM_REGISTER_DEVICE

#### Notification (PEP_DPM_REGISTER_DEVICE)

The value PEP_DPM_REGISTER_DEVICE.

#### Data (PEP_DPM_REGISTER_DEVICE)

A pointer to a [PEP_REGISTER_DEVICE_V2](/windows-hardware/drivers/ddi/pepfx/ns-pepfx-_pep_register_device_v2) structure.

Tells the PEP that the driver stack for the specified device has registered with the Windows power management framework (PoFx).

PoFx sends this notification when the device's driver stack calls the PoFxRegisterDevice routine to register the device. This notification allows the PEP to copy the device's registration information to the PEP's internal storage for later reference.

To send a PEP_DPM_REGISTER_DEVICE notification, the operating system calls the PEP's AcceptDeviceNotification callback routine. In this call, the Notification parameter value is PEP_DPM_REGISTER_DEVICE, and the Data parameter points to a PEP_REGISTER_DEVICE_V2 structure that contains the device's kernel handle and other registration information. On entry, the DeviceId member of this structure is a device identification string that uniquely identifies a device. Before returning, the PEP sets the DeviceAccepted member of this structure to TRUE to claim ownership of the device, or to FALSE to indicate that it does not own the device. For information about the other members of this structure, see PEP_REGISTER_DEVICE_V2.

The following table shows the preconditions that are in effect when this operating system sends a PEP_DPM_REGISTER_DEVICE notification to the PEP, and the postconditions that must be in effect after the PEP handles this notification for a device that it owns.

|Preconditions|Postconditions|
|----|----|
|The PEP has received a PEP_DPM_PREPARE_DEVICE notification for a device that it owns.|The PEP is ready to receive other device power management (DPM) notifications associated with this device.|

For a PEP_DPM_REGISTER_DEVICE notification, the AcceptDeviceNotification routine is always called at IRQL = PASSIVE_LEVEL.

### PEP_DPM_UNREGISTER_DEVICE

#### Notification (PEP_DPM_UNREGISTER_DEVICE)

The value PEP_DPM_UNREGISTER_DEVICE.

#### Data (PEP_DPM_UNREGISTER_DEVICE)

A pointer to a [PEP_UNREGISTER_DEVICE](/windows-hardware/drivers/ddi/pepfx/ns-pepfx-_pep_unregister_device) structure.

Tells the PEP that owns the specified device that the device's driver stack has withdrawn its registration from the Windows power management framework (PoFx).

PoFx sends this notification to inform the PEP that any registration information that the PEP stored for the device during the previous PEP_DPM_REGISTER_DEVICE notification is no longer valid. In response, the PEP can clean up any internal state used for power management of this device.

To send a PEP_DPM_UNREGISTER_DEVICE notification, the operating system calls the PEP's AcceptDeviceNotification callback routine. In this call, the Notification parameter value is PEP_DPM_UNREGISTER_DEVICE, and the Data parameter points to a PEP_UNREGISTER_DEVICE structure. This structure contains the handle that the PEP created in response to the previous PEP_DPM_REGISTER_DEVICE notification for the device.

The following table shows the preconditions that are in effect when this operating system sends a PEP_DPM_UNREGISTER_DEVICE notification to the PEP, and the postconditions that must be in effect after the PEP handles this notification for a device that it owns.

|Preconditions|Postconditions|
|----|----|
|If the PEP has received a PEP_DPM_REGISTER_DEVICE notification for the device and accepted device registration.</br>The PEP can receive any device power management (DPM) notifications associated with this device.</br>The PEP can report "work" associated with this device.|The PEP can no longer receive any device power management (DPM) notifications associated with this device, except for PEP_DPM_ABANDON_DEVICE.</br>The PEP cannot report "work" associated with this device.|

For a PEP_DPM_UNREGISTER_DEVICE notification, the AcceptDeviceNotification routine is always called at IRQL = PASSIVE_LEVEL.

### PEP_DPM_DEVICE_POWER_STATE

#### Notification (PEP_DPM_DEVICE_POWER_STATE)

The value PEP_DPM_DEVICE_POWER_STATE.

#### Data (PEP_DPM_DEVICE_POWER_STATE)

A pointer to a [PEP_DEVICE_POWER_STATE](/windows-hardware/drivers/ddi/pepfx/ns-pepfx-_pep_device_power_state) structure.

Sent to the PEP each time the device's driver stack either requests a change to a new Dx power state, or a previously requested transition to a Dx power state completes.

After the PEP calls the RequestWorker routine to request a work item, PoFx responds by sending the PEP a PEP_DPM_DEVICE_POWER_STATE notification. However, this notification is not sent until the resources (that is, the worker thread) necessary to process the work item are available. In this way, PoFx guarantees that the work request that the PEP passes to PoFx during the notification can never fail due to lack of resources.

To send a PEP_DPM_DEVICE_POWER_STATE notification, the operating system calls the PEP's AcceptDeviceNotification callback routine. In this call, the Notification parameter value is PEP_DPM_DEVICE_POWER_STATE, and the Data parameter points to a PEP_DEVICE_POWER_STATE structure. On entry, the PEP should assume that the contents of this structure are uninitialized. To handle this notification, the PEP should set the WorkInformation member to point to a PEP-allocated PEP_WORK_INFORMATION structure that describes the work that is being requested. In addition, the PEP should set the NeedWork member of the PEP_WORK structure to TRUE to confirm that the PEP has handled the PEP_DEVICE_POWER_STATE notification and that the WorkInformation member points to a valid PEP_WORK_INFORMATION structure. If the PEP fails to handle the notification or is unable to allocate the PEP_WORK_INFORMATION structure, the PEP should set the WorkInformation member to NULL and set the NeedWork member to FALSE.

For a PEP_DPM_DEVICE_POWER_STATE notification, the AcceptDeviceNotification routine is always called at IRQL = PASSIVE_LEVEL.

### PEP_DPM_COMPONENT_ACTIVE

#### Notification (PEP_DPM_COMPONENT_ACTIVE)

The value PEP_DPM_COMPONENT_ACTIVE.

#### Data (PEP_DPM_COMPONENT_ACTIVE)

A pointer to a [PEP_COMPONENT_ACTIVE](/windows-hardware/drivers/ddi/pep_x/ns-pep_x-_pep_component_active) structure that identifies the component and that indicates whether this component is making a transition to the active condition or to the idle condition.

Informs the PEP that a component needs to make a transition from the idle condition to the active condition, or vice versa.

The Windows power management framework (PoFx) sends this notification when a transition is pending either to the active condition or to the idle condition.

To send a PEP_DPM_COMPONENT_ACTIVE notification, PoFx calls the PEP's AcceptDeviceNotification callback routine. In this call, the Notification parameter value is PEP_DPM_COMPONENT_ACTIVE, and the Data parameter points to a PEP_COMPONENT_ACTIVE structure.

A component that is accessible is in the active condition. A component that is inaccessible is in the idle condition. A component that is in the active condition is always in the F0 component power state. The component cannot leave F0 until it enters the idle condition. A component that is in the idle condition might be in F0 or in a low-power Fx state. The active/idle condition of a component is the only reliable means for a driver to determine whether a component is accessible. A component that is in F0 but is also in the idle condition might be about to switch to a low-power Fx state.

When an active component is ready to enter the idle condition, the transition occurs immediately. During the handling of the PEP_DPM_COMPONENT_ACTIVE notification, the PEP might, for example, request a transition from F0 to a low-power Fx state for the component.

If a component is in a low-power Fx state when a PEP_DPM_COMPONENT_ACTIVE notification requests a transition from the idle condition to the active condition, the PEP must first switch the component to F0 before the component can enter the active condition. The PEP might need to finish preparing the component for the transition to the active condition asynchronously, after returning from the AcceptDeviceNotification callback for the PEP_DPM_COMPONENT_ACTIVE notification. After the component is fully configured to operate in the active condition, the PEP must call the RequestWorker routine and then handle the resulting PEP_DPM_WORK notification by setting WorkType = PepWorkActiveComplete in the PEP_WORK_INFORMATION structure.

If the PEP receives a PEP_DPM_COMPONENT_ACTIVE notification for a component that is in F0 and is already fully configured to operate in the active condition, the PEP might be able to finish handling this notification synchronously. If "fast path" handling of the notification is supported, the WorkInformation member of the PEP_COMPONENT_ACTIVE structure for this notification contains a pointer to a PEP_WORK_INFORMATION structure, and the PEP can set the WorkType member of this structure to PepWorkActiveComplete to complete the transition. However, if WorkInformation = NULL, no "fast path" is available and the PEP must complete the transition asynchronously by calling RequestWorker, as described in the preceding paragraph.

For more information about the active and idle conditions, see [Component-Level Power Management](component-level-power-management.md).

For a PEP_DPM_COMPONENT_ACTIVE notification, the AcceptDeviceNotification routine is called at IRQL <= DISPATCH_LEVEL.

### PEP_DPM_WORK

#### Notification (PEP_DPM_WORK)

The value PEP_DPM_WORK.

#### Data (PEP_DPM_WORK)

A pointer to a [PEP_WORK](/windows-hardware/drivers/ddi/pepfx/ns-pepfx-_pep_work) structure.

Sent to the PEP once each time the PEP calls the RequestWorker routine to request an item of work from the Windows power management framework (PoFx).

After the PEP calls the RequestWorker routine to request a work item, PoFx responds by sending the PEP a PEP_DPM_WORK notification. However, this notification is not sent until the resources (that is, the worker thread) necessary to process the work item are available. In this way, PoFx guarantees that the work request that the PEP passes to PoFx during the notification can never fail due to lack of resources.

To send a PEP_DPM_WORK notification, the operating system calls the PEP's AcceptDeviceNotification callback routine. In this call, the Notification parameter value is PEP_DPM_WORK, and the Data parameter points to a PEP_WORK structure. On entry, the PEP should assume that the contents of this structure are uninitialized. To handle this notification, the PEP should set the WorkInformation member to point to a PEP-allocated PEP_WORK_INFORMATION structure that describes the work that is being requested. In addition, the PEP should set the NeedWork member of the PEP_WORK structure to TRUE to confirm that the PEP has handled the PEP_DPM_WORK notification and that the WorkInformation member points to a valid PEP_WORK_INFORMATION structure. If the PEP fails to handle the notification or is unable to allocate the PEP_WORK_INFORMATION structure, the PEP should set the WorkInformation member to NULL and set the NeedWork member to FALSE.

For a PEP_DPM_WORK notification, the AcceptDeviceNotification routine is always called at IRQL = PASSIVE_LEVEL.

### PEP_DPM_POWER_CONTROL_REQUEST

#### Notification (PEP_DPM_POWER_CONTROL_REQUEST)

The value PEP_DPM_POWER_CONTROL_REQUEST.

#### Data (PEP_DPM_POWER_CONTROL_REQUEST)

A pointer to a [PEP_POWER_CONTROL_REQUEST](/windows-hardware/drivers/ddi/pepfx/ns-pepfx-_pep_power_control_request) structure.

Informs the PEP that a driver has called the PoFxPowerControl API to send a control code directly to the PEP.

The Windows power management framework (PoFx) sends this notification to the PEP when a driver calls the PoFxPowerControl API to send a control code directly to the PEP. The notification Data pointer in this case points to the PEP_POWER_CONTROL_REQUEST structure

Power control requests and their semantics are defined between the PEP writer and the device class owner. Typically such an interface is for device class specific communication that is not captured in the generalized power management framework. For example, the UART controller may communicate baud rate information to the PEP to modify some platform clock rails / dividers and such communication would likely leverage a power control request.

>![NOTE]
>The PEP can only request to send a control code to the device after it receives either a PEP_DPM_DEVICE_STARTED notification or PEP_DPM_POWER_CONTROL_REQUEST notification.

For a PEP_DPM_POWER_CONTROL_REQUEST notification, the AcceptDeviceNotification routine is called at IRQL <= DISPATCH_LEVEL.

### PEP_DPM_POWER_CONTROL_COMPLETE

#### Notification (PEP_DPM_POWER_CONTROL_COMPLETE)

The value PEP_DPM_POWER_CONTROL_COMPLETE.

#### Data (PEP_DPM_POWER_CONTROL_COMPLETE)

A pointer to a [PEP_POWER_CONTROL_COMPLETE](/windows-hardware/drivers/ddi/pepfx/ns-pepfx-_pep_power_control_complete) structure.

Informs the PEP that a driver has completed a power control request that was previously issued by the PEP

The Windows power management framework (PoFx) sends this notification to the PEP when a driver completes a power control request issued previously by the PEP.

>![NOTE]
>The PEP can ignore this notification if it does not issue any power control requests.

For a PEP_DPM_POWER_CONTROL_COMPLETE notification, the AcceptDeviceNotification routine is called at IRQL <= DISPATCH_LEVEL.

### PEP_DPM_SYSTEM_LATENCY_UPDATE

#### Notification (PEP_DPM_SYSTEM_LATENCY_UPDATE)

The value PEP_DPM_SYSTEM_LATENCY_UPDATE.

#### Data (PEP_DPM_SYSTEM_LATENCY_UPDATE)

A pointer to a [PEP_SYSTEM_LATENCY](/windows-hardware/drivers/ddi/pepfx/ns-pepfx-_pep_system_latency) structure.

Informs the PEP that the OS has updated the overall system latency tolerance.

The Windows power management framework (PoFx) sends this notification when the OS updates the overall system latency tolerance.

In earlier versions of PoFx, this notification was used by the PEP for processor and platform idle state selection. With the latest PEP interfaces, the selection process is entirely handled by the OS and as such this notification is no longer useful. It is included here for completeness and the PEP should ignore it.

To send a PEP_DPM_SYSTEM_LATENCY_UPDATE notification, PoFx calls the PEP's AcceptDeviceNotification callback routine. For this notification, the AcceptDeviceNotification routine is called at IRQL <= DISPATCH_LEVEL.

### PEP_DPM_DEVICE_STARTED

#### Notification (PEP_DPM_DEVICE_STARTED)

The value PEP_DPM_DEVICE_STARTED.

#### Data (PEP_DPM_DEVICE_STARTED)

A pointer to a [PEP_DEVICE_STARTED](/windows-hardware/drivers/ddi/pepfx/ns-pepfx-_pep_device_started) structure.

Informs the PEP that the device has started so that it is available to receive power control transactions.

Device stacks register with the OS for runtime power management in a two-step process. The driver first calls PoFxRegisterDevice to provide information about the number of components, their idle states and corresponding attributes. In response to this call, the PEP receives a PEP_DPM_REGISTER_DEVICE notification.

After registration succeeds, the driver has the opportunity to initialize its components (i.e. set active, update latency requirements, update expected idle residency, etc.). Once the driver has completed any initialization tasks, it notifies the power manager by calling PoFxStartDevicePowerManagement. In response, the PEP will receive a PEP_DPM_DEVICE_STARTED notification. At this point, the device is considered to be fully enabled for runtime power management.

As a result, the PEP cannot issue any power control requests to the driver unless it has either first received a PEP_DPM_DEVICE_STARTED notification or a PEP_DPM_POWER_CONTROL_REQUEST notification.

>[!NOTE]
>The PEP can ignore this notification if it does not issue any power control requests.

For a PEP_DPM_DEVICE_STARTED notification, the AcceptDeviceNotification routine is called at IRQL <= DISPATCH_LEVEL.

### PEP_DPM_NOTIFY_COMPONENT_IDLE_STATE

#### Notification (PEP_DPM_NOTIFY_COMPONENT_IDLE_STATE)

The value PEP_DPM_NOTIFY_COMPONENT_IDLE_STATE.

#### Data (PEP_DPM_NOTIFY_COMPONENT_IDLE_STATE)

A pointer to a [PEP_NOTIFY_COMPONENT_IDLE_STATE](/windows-hardware/drivers/ddi/pepfx/ns-pepfx-_pep_notify_component_idle_state) structure.

Sent to the PEP when the OS issues an idle state transition for a given component.

The Windows power management framework (PoFx) sends this notification when the OS issues an idle state transition for a given component.

>[!IMPORTANT]
>The PEP must handle this notification.

For each idle state transition, the PEP is notified before and after the driver is notified. The PEP distinguishes between pre and post notifications by examining the DriverNotified member of the PEP_NOTIFY_COMPONENT_IDLE_STATE structure. For a post-notification, the DriverNotified member will be TRUE.

Pre-notifications are generally used when transitioning to F0. In this case the PEP may need to re-enable clock or power resources such that when the driver handles the F0 notification, the hardware is available. Accordingly, post-notifications are generally used when transitioning from F0 to a deeper idle state. After a driver has handled the idle state notification, the PEP can safely turn off clock and power resources.

Handling an idle state transition for a given component may require asynchronous processing if the operation takes a significant amount of time or the IRQL is too high to complete the transition synchronously. As a result, the PEP can complete this notification synchronously or asynchronously by setting the Completed member to TRUE or FALSE respectively.

If the notification is to be completed asynchronously, the PEP notifies the OS on completion by requesting a worker (see RequestWorker) and filling out the provided work information structure in the resulting PEP_DPM_WORK notification using a work type of PepWorkCompleteIdleState.

To send a PEP_DPM_NOTIFY_COMPONENT_IDLE_STATE notification, PoFx calls the PEP's AcceptDeviceNotification callback routine. This routine is called at IRQL <= DISPATCH_LEVEL.

### PEP_DPM_REGISTER_DEBUGGER

#### Notification (PEP_DPM_REGISTER_DEBUGGER)

The value PEP_DPM_REGISTER_DEBUGGER.

#### Data (PEP_DPM_REGISTER_DEBUGGER)

A pointer to a [PEP_REGISTER_DEBUGGER](/windows-hardware/drivers/ddi/pepfx/ns-pepfx-_pep_register_debugger) structure.

Informs the PEP that a registered device may be used as a debug port.

The Windows power management framework (PoFx) sends this notification to notify the PEP that a registered device may be used as a debug port.

For a PEP_DPM_REGISTER_DEBUGGER notification, the AcceptDeviceNotification routine is called at IRQL <= DISPATCH_LEVEL.

### PEP_DPM_LOW_POWER_EPOCH

#### Notification (PEP_DPM_LOW_POWER_EPOCH)

The value PEP_DPM_LOW_POWER_EPOCH.

#### Data (PEP_DPM_LOW_POWER_EPOCH)

A pointer to a [PEP_LOW_POWER_EPOCH](/windows-hardware/drivers/ddi/pepfx/ns-pepfx-_pep_low_power_epoch) structure.

This notification is deprecated.

### PEP_DPM_REGISTER_CRASHDUMP_DEVICE

#### Notification (PEP_DPM_REGISTER_CRASHDUMP_DEVICE)

The value PEP_DPM_REGISTER_CRASHDUMP_DEVICE.

#### Data (PEP_DPM_REGISTER_CRASHDUMP_DEVICE)

A pointer to a [PEP_REGISTER_CRASHDUMP_DEVICE](/windows-hardware/drivers/ddi/pepfx/ns-pepfx-_pep_register_crashdump_device) structure.

The Windows power management framework (PoFx) sends this notification when a device registers as a crashdump handler.

The ability to generate a memory dump (crashdump) when the system encounters a fatal error is invaluable toward determining the cause of the crash. Windows, by default, will generate a crashdump when the system encounters a bugcheck. In this context, the system is under a very constrained operating environment with interrupts disabled and the system IRQL at HIGH_LEVEL.

Since devices involved in writing a crashdump to disk (i.e. storage controller, PCI controller, etc. ) may be powered down at the time of the crash, the OS must call into the PEP to power on the device. As such, the OS requests a callback (PowerOnDumpDeviceCallback) from the PEP for every device on the crashdump stack and invokes the callback when generating the dump file.

Given the constrained environment at the time of the crash, the callback provided by the PEP must not access paged code, block on any events or invoke any code that may do the same. Furthermore, the process of powering up any required resources cannot rely on interrupts. As a result, the PEP may have to revert to polling should it need to wait for various resources to be enabled. If the PEP cannot power on the device under these constraints, it should either not handle the notification or not supply a callback routine.

To send a PEP_DPM_REGISTER_CRASHDUMP_DEVICE notification, PoFx calls the PEP's AcceptDeviceNotification callback routine. For this notification, the AcceptDeviceNotification routine is called at IRQL <= HIGH_LEVEL.

### PEP_DPM_DEVICE_IDLE_CONSTRAINTS

#### Notification (PEP_DPM_DEVICE_IDLE_CONSTRAINTS)

The value PEP_DPM_DEVICE_IDLE_CONSTRAINTS.

#### Data (PEP_DPM_DEVICE_IDLE_CONSTRAINTS)

A pointer to a [PEP_DEVICE_PLATFORM_CONSTRAINTS](/windows-hardware/drivers/ddi/pepfx/ns-pepfx-_pep_device_platform_constraints) structure.
 Sent to the PEP to query for dependencies between device D-states and platform idle states.

The Windows power management framework (PoFx) sends this notification to the PEP to query for dependencies between device D-states and platform idle states. The PEP uses this notification to return the lightest D-state the device can still be in and enter each platform idle state. The OS will guarantee the device is in the minimum D-state before entering an associated platform idle state. If a platform idle state does not depend on this device being in any D-state, the PEP should specify a minimum D-state of PowerDeviceD0. If no platform idle states depend on this device being in a particular D-state, this notification can be ignored.

This notification is sent to each device after the PEP has received the  PEP_NOTIFY_PPM_QUERY_PLATFORM_STATES notification.

To send a PEP_DPM_DEVICE_IDLE_CONSTRAINTS notification, PoFx calls the PEP's AcceptDeviceNotification callback routine. In this call, the Notification parameter value is PEP_DPM_DEVICE_IDLE_CONSTRAINTS, and the Data parameter points to a PEP_DEVICE_PLATFORM_CONSTRAINTS structure.

For a PEP_DPM_DEVICE_IDLE_CONSTRAINTS notification, the AcceptDeviceNotification routine is always called at IRQL = DISPATCH_LEVEL.

### PEP_DPM_COMPONENT_IDLE_CONSTRAINTS

#### Notification (PEP_DPM_COMPONENT_IDLE_CONSTRAINTS)

The value PEP_DPM_COMPONENT_IDLE_CONSTRAINTS.

#### Data (PEP_DPM_COMPONENT_IDLE_CONSTRAINTS)

A pointer to a [PEP_COMPONENT_PLATFORM_CONSTRAINTS](/windows-hardware/drivers/ddi/pepfx/ns-pepfx-_pep_component_platform_constraints) structure.

Sent to the PEP to query for dependencies between component F-states and platform idle states.

The Windows power management framework (PoFx) sends this notification to the PEP to query for dependencies between component F-states and platform idle states. The PEP uses this notification to return the lightest F-state the component can still be in and enter each platform idle state. The OS will guarantee the component is in the minimum F-state before entering an associated platform idle state. If a platform idle state does not depend on this component being in any F-state, the PEP should specify a minimum F-state of 0. If no platform idle states depend on this component being in a particular F-state, this notification can be ignored.

Device idle constraints deeper than D0 are more constraining than component idle states for components on the device. For a given platform idle state index, if the device specified a device idle constraint, the corresponding component idle constraint for all components associated with the device are ignored.

This notification is sent to each component on each device after the PEP receives a PEP_NOTIFY_PPM_QUERY_PLATFORM_STATES notification.

To send a PEP_DPM_COMPONENT_IDLE_CONSTRAINTS notification, PoFx calls the PEP's AcceptDeviceNotification callback routine. The AcceptDeviceNotification routine is always called at IRQL = DISPATCH_LEVEL.

### PEP_DPM_QUERY_COMPONENT_PERF_CAPABILITIES

#### Notification (PEP_DPM_QUERY_COMPONENT_PERF_CAPABILITIES)

The value PEP_DPM_QUERY_COMPONENT_PERF_CAPABILITIES.

#### Data (PEP_DPM_QUERY_COMPONENT_PERF_CAPABILITIES)

A pointer to a [PEP_QUERY_COMPONENT_PERF_CAPABILITIES](/windows-hardware/drivers/ddi/pepfx/ns-pepfx-_pep_query_component_perf_capabilities) structure.

Informs the PEP that it is being queried for the number of performance state (P-state) sets that are defined for a component.

To send a PEP_DPM_QUERY_COMPONENT_PERF_CAPABILITIES notification, PoFx calls the PEP's AcceptDeviceNotification callback routine. In this call, the Notification parameter value is PEP_DPM_QUERY_COMPONENT_PERF_CAPABILITIES, and the Data parameter points to a PEP_QUERY_COMPONENT_PERF_CAPABILITIES structure.

For a PEP_DPM_QUERY_COMPONENT_PERF_CAPABILITIES notification, the AcceptDeviceNotification routine is always called at IRQL = PASSIVE_LEVEL.

### PEP_DPM_QUERY_COMPONENT_PERF_SET

#### Notification (PEP_DPM_QUERY_COMPONENT_PERF_SET)

The value PEP_DPM_QUERY_COMPONENT_PERF_SET.

#### Data (PEP_DPM_QUERY_COMPONENT_PERF_SET)

A pointer to a [PEP_QUERY_COMPONENT_PERF_SET](/windows-hardware/drivers/ddi/pepfx/ns-pepfx-_pep_query_component_perf_set) structure.

Informs the PEP that it is being queried for information about a set of performance state values (P-state set) for a component.

To send a PEP_DPM_QUERY_COMPONENT_PERF_SET notification, PoFx calls the PEP's AcceptDeviceNotification callback routine. In this call, the Notification parameter value is PEP_DPM_QUERY_COMPONENT_PERF_SET, and the Data parameter points to a PEP_QUERY_COMPONENT_PERF_SET structure.

For a PEP_DPM_QUERY_COMPONENT_PERF_SET notification, the AcceptDeviceNotification routine is always called at IRQL = PASSIVE_LEVEL.

### PEP_DPM_QUERY_COMPONENT_PERF_SET_NAME

#### Notification (OPEP_DPM_QUERY_COMPONENT_PERF_SET_NAME)

The value PEP_DPM_QUERY_COMPONENT_PERF_SET_NAME.

#### Data (OPEP_DPM_QUERY_COMPONENT_PERF_SET_NAME)

A pointer to a [PEP_QUERY_COMPONENT_PERF_SET_NAME](/windows-hardware/drivers/ddi/pepfx/ns-pepfx-_pep_query_component_perf_set_name) structure.

Informs the PEP that it is being queried for information about a set of performance state values (P-state set) for a component.

To send a PEP_DPM_QUERY_COMPONENT_PERF_SET_NAME notification, PoFx calls the PEP's AcceptDeviceNotification callback routine. In this call, the Notification parameter value is PEP_DPM_QUERY_COMPONENT_PERF_SET_NAME, and the Data parameter points to a PEP_QUERY_COMPONENT_PERF_SET_NAME structure.

For a PEP_DPM_QUERY_COMPONENT_PERF_SET_NAME notification, the AcceptDeviceNotification routine is always called at IRQL = PASSIVE_LEVEL.

### PEP_DPM_QUERY_COMPONENT_PERF_STATES

#### Notification (PEP_DPM_QUERY_COMPONENT_PERF_STATES)

The value PEP_DPM_QUERY_COMPONENT_PERF_STATES.

#### Data (PEP_DPM_QUERY_COMPONENT_PERF_STATES)

A pointer to a [PEP_QUERY_COMPONENT_PERF_STATES](/windows-hardware/drivers/ddi/pepfx/ns-pepfx-_pep_query_component_perf_states) structure.

Informs the PEP that it is being queried for a list of discrete performance state (P-state) values for a specified P-state set.

To send a PEP_DPM_QUERY_COMPONENT_PERF_STATES notification, PoFx calls the PEP's AcceptDeviceNotification callback routine. In this call, the Notification parameter value is PEP_DPM_QUERY_COMPONENT_PERF_STATES, and the Data parameter points to a PEP_QUERY_COMPONENT_PERF_STATES structure.

For a PEP_DPM_QUERY_COMPONENT_PERF_STATES notification, the AcceptDeviceNotification routine is always called at IRQL = PASSIVE_LEVEL.

### PEP_DPM_REGISTER_COMPONENT_PERF_STATES

#### Notification (PEP_DPM_REGISTER_COMPONENT_PERF_STATES)

The value PEP_DPM_REGISTER_COMPONENT_PERF_STATES.

#### Data (PEP_DPM_REGISTER_COMPONENT_PERF_STATES)

A pointer to a [PEP_REGISTER_COMPONENT_PERF_STATES](/windows-hardware/drivers/ddi/pepfx/ns-pepfx-_pep_register_component_perf_states) structure.

Informs the PEP about the performance states (P-states) of the specified component.

To send a PEP_DPM_REGISTER_COMPONENT_PERF_STATES notification, PoFx calls the PEP's AcceptDeviceNotification callback routine. In this call, the Notification parameter value is PEP_DPM_REGISTER_COMPONENT_PERF_STATES, and the Data parameter points to a PEP_REGISTER_COMPONENT_PERF_STATES structure.

For a PEP_DPM_REGISTER_COMPONENT_PERF_STATES notification, the AcceptDeviceNotification routine is always called at IRQL = PASSIVE_LEVEL.

### PEP_DPM_REQUEST_COMPONENT_PERF_STATE

#### Notification (PEP_DPM_REQUEST_COMPONENT_PERF_STATE)

The value PEP_DPM_REQUEST_COMPONENT_PERF_STATE.

#### Data (PEP_DPM_REQUEST_COMPONENT_PERF_STATE)

A pointer to a PEP_REQUEST_COMPONENT_PERF_STATE structure.

Informs the PEP that one or more performance state (P-state) changes are requested by the Windows power management framework (PoFx).

To send a PEP_DPM_REQUEST_COMPONENT_PERF_STATE notification, PoFx calls the PEP's AcceptDeviceNotification callback routine. In this call, the Notification parameter value is PEP_DPM_REQUEST_COMPONENT_PERF_STATE, and the Data parameter points to a PEP_REQUEST_COMPONENT_PERF_STATE structure.

For a PEP_DPM_REQUEST_COMPONENT_PERF_STATE notification, the AcceptDeviceNotification routine is always called at IRQL = PASSIVE_LEVEL.

### PEP_DPM_QUERY_CURRENT_COMPONENT_PERF_STATE

#### Notification (PEP_DPM_QUERY_CURRENT_COMPONENT_PERF_STATE)

The value PEP_DPM_QUERY_CURRENT_COMPONENT_PERF_STATE.

#### Data (PEP_DPM_QUERY_CURRENT_COMPONENT_PERF_STATE)

A pointer to a PEP_QUERY_CURRENT_COMPONENT_PERF_STATE structure.

Informs the PEP that it is being queried for information about the current P-state in the specified P-state set.

To send a PEP_DPM_QUERY_CURRENT_COMPONENT_PERF_STATE notification, PoFx calls the PEP's AcceptDeviceNotification callback routine. In this call, the Notification parameter value is PEP_DPM_QUERY_CURRENT_COMPONENT_PERF_STATE, and the Data parameter points to a PEP_QUERY_CURRENT_COMPONENT_PERF_STATE structure.

For a PEP_DPM_QUERY_CURRENT_COMPONENT_PERF_STATE notification, the AcceptDeviceNotification routine is always called at IRQL = PASSIVE_LEVEL.

### PEP_DPM_QUERY_DEBUGGER_TRANSITION_REQUIREMENTS

#### Notification (PEP_DPM_QUERY_DEBUGGER_TRANSITION_REQUIREMENTS)

The value PEP_DPM_QUERY_DEBUGGER_TRANSITION_REQUIREMENTS.

#### Data (PEP_DPM_QUERY_DEBUGGER_TRANSITION_REQUIREMENTS)

A pointer to a [PEP_DEBUGGER_TRANSITION_REQUIREMENTS](/windows-hardware/drivers/ddi/pepfx/ns-pepfx-_pep_debugger_transition_requirements) structure.

Sent to the PEP to query for the set of coordinated or platform states which require the debugger to be powered off.

The Windows power management framework (PoFx) sends this notification to the PEP to query for the set of coordinated or platform states which require the debugger to be powered off. If this notification is accepted, the OS will perform all debugger power transitions for the PEP, and the PEP may not use TransitionCriticalResource to power manage the debugger.

This notification is sent to each debugger device after the PEP has accepted a PEP_NOTIFY_PPM_QUERY_PLATFORM_STATE or PEP_NOTIFY_PPM_QUERY_COORDINATED_STATES notification.

To send a PEP_DPM_QUERY_DEBUGGER_TRANSITION_REQUIREMENTS notification, PoFx calls the PEP's AcceptDeviceNotification callback routine. For this notification, the AcceptDeviceNotification routine is always called at IRQL = DISPATCH_LEVEL.

### PEP_DPM_QUERY_SOC_SUBSYSTEM

#### Notification (PEP_DPM_QUERY_SOC_SUBSYSTEM)

The value PEP_DPM_QUERY_SOC_SUBSYSTEM.

#### Data (PEP_DPM_QUERY_SOC_SUBSYSTEM)

A pointer to a [PEP_QUERY_SOC_SUBSYSTEM](/windows-hardware/drivers/ddi/pepfx/ns-pepfx-_pep_query_soc_subsystem) structure.

Sent to the PEP to collect basic information about a particular system on a chip (SoC) subsystem.

The Windows power management framework (PoFx) sends this notification to the PEP after platform idle states have been initialized in order to collect basic information about a particular SoC subsystem. A PEP that does not implement SoC subsystem accounting, or does not implement it for the specified platform idle state, returns FALSE. This directs the OS to stop sending diagnostic notifications to the PEP for this platform idle state.

A system's SubsystemCount and a subsystem's MetadataCount can change with PEP/BSP updates. SubsystemIndex can change every time the OS boots.

>[!IMPORTANT]
>The PEP cannot ignore this notification. The PEP is receiving this notification because it responded to the PEP_DPM_QUERY_SOC_SUBSYSTEM_COUNT notification for this PlatformIdleStateIndex with a non-zero SubsystemCount.

To send a PEP_DPM_QUERY_SOC_SUBSYSTEM notification, PoFx calls the PEP's AcceptDeviceNotification callback routine at IRQL < DISPATCH_LEVEL.

### PEP_DPM_QUERY_SOC_SUBSYSTEM_BLOCKING_TIME

#### Notification (PEP_DPM_QUERY_SOC_SUBSYSTEM_BLOCKING_TIME)

The value PEP_DPM_QUERY_SOC_SUBSYSTEM_BLOCKING_TIME.

#### Data (PEP_DPM_QUERY_SOC_SUBSYSTEM_BLOCKING_TIME)

A pointer to a [PEP_QUERY_SOC_SUBSYSTEM_BLOCKING_TIME](/windows-hardware/drivers/ddi/pepfx/ns-pepfx-_pep_query_soc_subsystem_blocking_time) structure.

Sent to the PEP when the OS wants to collect the tally of time a particular system on a chip (SoC) subsystem has blocked entry into a particular platform idle state without the OS's knowledge.

Typically the OS calls this notification at the end of an extended connected standby session where the OS attempted to enter the specified platform idle state. The PEP_QUERY_SOC_SUBSYSTEM_COUNT.SubsystemCount value, filled in earlier by the PEP during subcomponent initialization, specifies how many PEP_DPM_QUERY_SOC_SUBSYSTEM_BLOCKING_TIME notifications are sent to the PEP at a time. A PEP can receive multiple PEP_DPM_QUERY_SOC_SUBSYSTEM_BLOCKING_TIME notifications for a given subsystem. These notifications may or may not be interleaved with PEP_DPM_RESET_SOC_SUBSYSTEM_ACCOUNTING notifications.

>[!IMPORTANT]
>The PEP cannot ignore this notification. The PEP is receiving this notification because it responded to the PEP_DPM_QUERY_SOC_SUBSYSTEM_COUNT notification for this PlatformIdleStateIndex with a non-zero SubsystemCount.

To send a PEP_DPM_QUERY_SOC_SUBSYSTEM_BLOCKING_TIME notification, PoFx calls the PEP's AcceptDeviceNotification callback routine at IRQL < DISPATCH_LEVEL.

### PEP_DPM_QUERY_SOC_SUBSYSTEM_COUNT

#### Notification (PEP_DPM_QUERY_SOC_SUBSYSTEM_COUNT)

The value PEP_DPM_QUERY_SOC_SUBSYSTEM_COUNT.

#### Data (PEP_DPM_QUERY_SOC_SUBSYSTEM_COUNT)

A pointer to a [PEP_QUERY_SOC_SUBSYSTEM_COUNT](/windows-hardware/drivers/ddi/pepfx/ns-pepfx-_pep_query_soc_subsystem_count) structure.

Sent to the PEP after platform idle states have been initialized to tell the OS whether the PEP supports system on a chip (SoC) subsystem accounting for a given platform idle state.

This is the first SoC subsystem diagnostic notification sent to the PEP. A PEP that does not implement SoC subsystem accounting, or does not implement it for the specified platform idle state, returns FALSE, in which case the OS will not send the PEP any more SoC subsystem diagnostic notifications for this platform idle state.

>[!NOTE]
>The PEP can ignore this notification if it does not implement SoC diagnostic notifications for the specified platform idle state.

To send a PEP_DPM_QUERY_SOC_SUBSYSTEM_COUNT notification, PoFx calls the PEP's AcceptDeviceNotification callback routine at IRQL < DISPATCH_LEVEL.

### PEP_DPM_QUERY_SOC_SUBSYSTEM_METADATA

#### Notification (PEP_DPM_QUERY_SOC_SUBSYSTEM_METADATA)

The value PEP_DPM_QUERY_SOC_SUBSYSTEM_METADATA.

#### Data (PEP_DPM_QUERY_SOC_SUBSYSTEM_METADATA)

A pointer to a PEP_QUERY_SOC_SUBSYSTEM_METADATA structure.

Sent to the PEP to collect optional metadata about the subsystem whose blocking time has just been queried.

This notification is typically sent to the PEP immediately following a PEP_DPM_QUERY_SOC_SUBSYSTEM_BLOCKING_TIME notification. One PEP_DPM_QUERY_SOC_SUBSYSTEM_METADATA notification collects all key-value metadata pairs describing the subsystem.

>[!IMPORTANT]
>The PEP cannot ignore this notification. The PEP is receiving this notification because it responded to the PEP_DPM_QUERY_SOC_SUBSYSTEM_COUNT notification for this PlatformIdleStateIndex with a non-zero SubsystemCount.

To send a PEP_DPM_QUERY_SOC_SUBSYSTEM_METADATA notification, PoFx calls the PEP's AcceptDeviceNotification callback routine. For this notification, the AcceptDeviceNotification routine is called at IRQL < DISPATCH_LEVEL.

### PEP_DPM_RESET_SOC_SUBSYSTEM_ACCOUNTING

#### Notification (PEP_DPM_RESET_SOC_SUBSYSTEM_ACCOUNTING)

The value PEP_DPM_RESET_SOC_SUBSYSTEM_ACCOUNTING.

#### Data (PEP_DPM_RESET_SOC_SUBSYSTEM_ACCOUNTING)

A pointer to a A pointer to a [PEP_RESET_SOC_SUBSYSTEM_ACCOUNTING](/windows-hardware/drivers/ddi/pepfx/ns-pepfx-_pep_reset_soc_subsystem_accounting) structure. structure.

Sent to the PEP to clear all subsystem blocking time and metadata accounting, perform any additional initialization required, and restart the accounting.

The Windows power management framework (PoFx) sends this notification to the PEP anytime after all subsystems are initialized with the OS. Typically, this notification is called when the OS begins a new period of analysis around what is keeping the system on a chip (SoC) out of the specified platform idle state (targeting DRIPS upon entering connected standby). The OS only sends this notification for platform idle states for which the PEP initialized one or more SoC subsystems.

To send a PEP_DPM_RESET_SOC_SUBSYSTEM_ACCOUNTING notification, PoFx calls the PEP's AcceptDeviceNotification callback routine at IRQL < DISPATCH_LEVEL.
