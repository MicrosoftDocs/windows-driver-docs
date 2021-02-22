---
title: Device power management reference
description: Describes DDIs that drivers can use to divide their device hardware into multiple logical components to enable fine-grained power management
keywords: [AcceptDeviceNotification]
ms.date: 12/17/2018
ms.localizationpriority: medium
ms.custom: 19H1
---

# Device power management reference

Drivers can divide their device hardware into multiple logical components to enable fine-grained power management. A component has a set of power states that can be managed independently of the power states of other components in the same device. In the F0 state, the component is fully turned on. The component might support additional, low-power states F1, F2, and so on.

The power policy owner for a device is typically the device's function driver. To enable component-level power management, this driver registers the device with the [power management framework (PoFx)](overview-of-the-power-management-framework.md). By registering the device, the driver assumes the responsibility for informing PoFx when a component is actively being used and when the component is idle. PoFx makes intelligent idle state choices for the device based on information about the component activity, latency tolerance, expected idle durations, and wake requirements. By controlling power usage at the component level, PoFx can reduce power requirements while preserving system responsiveness. For more information, see [Component-Level Power Management](component-level-power-management.md).

## Device Power Management Routines

These routines are implemented by the power management framework (PoFx) to enable device power management. These routines are called by the driver that is the power policy owner (PPO) for a device. Typically, the function driver for a device is the PPO for this device.

|Topic|Description|
|----|----|
|[**PoFxActivateComponent**](/windows-hardware/drivers/ddi/wdm/nf-wdm-pofxactivatecomponent)|The **PoFxActivateComponent** routine increments the activation reference count on the specified component.|
|[PoFxCompleteDevicePowerNotRequired](/windows-hardware/drivers/ddi/wdm/nf-wdm-pofxcompletedevicepowernotrequired)|The **PoFxCompleteDevicePowerNotRequired** routine notifies the power management framework (PoFx) that the calling driver has completed its response to a call to the driver's [*DevicePowerNotRequiredCallback*](/windows-hardware/drivers/ddi/wdm/nc-wdm-po_fx_device_power_not_required_callback) callback routine.|
|[**PoFxCompleteIdleCondition**](/windows-hardware/drivers/ddi/wdm/nf-wdm-pofxcompleteidlecondition)|The **PoFxCompleteIdleCondition** routine informs the power management framework (PoFx) that the specified component has completed a pending change to the idle condition.|
|[**PoFxCompleteIdleState**](/windows-hardware/drivers/ddi/wdm/nf-wdm-pofxcompleteidlestate)|The PoFxCompleteIdleState routine informs the power management framework (PoFx) that the specified component has completed a pending change to an Fx state.|
|[**PoFxIdleComponent**](/windows-hardware/drivers/ddi/wdm/nf-wdm-pofxidlecomponent)|The **PoFxIdleComponent** routine decrements the activation reference count on the specified component.|
|[**PoFxIssueComponentPerfStateChange**](/windows-hardware/drivers/ddi/wdm/nf-wdm-pofxissuecomponentperfstatechange)|The **PoFxIssueComponentPerfStateChange** routine submits a request to place a device component in a particular performance state.|
|[**PoFxIssueComponentPerfStateChangeMultiple**](/windows-hardware/drivers/ddi/wdm/nf-wdm-pofxissuecomponentperfstatechangemultiple)|The **PoFxIssueComponentPerfStateChangeMultiple** routine submits a request to change the performance states in multiple performance state sets simultaneously for a device component.|
|[**PoFxNotifySurprisePowerOn**](/windows-hardware/drivers/ddi/wdm/nf-wdm-pofxnotifysurprisepoweron)|The **PoFxNotifySurprisePowerOn** routine notifies the power management framework (PoFx) that a device was turned on as a side effect of supplying power to some other device.|
|[**PoFxPowerControl**](/windows-hardware/drivers/ddi/wdm/nf-wdm-pofxpowercontrol)|The **PoFxPowerControl** routine sends a power control request to the power management framework (PoFx).|
|[**PoFxQueryCurrentComponentPerfState**](/windows-hardware/drivers/ddi/wdm/nf-wdm-pofxquerycurrentcomponentperfstate)|The **PoFxQueryCurrentComponentPerfState** routine retrieves the active performance state in a component's performance state set.|
|[**PoFxRegisterComponentPerfStates**](/windows-hardware/drivers/ddi/wdm/nf-wdm-pofxregistercomponentperfstates)|The **PoFxRegisterComponentPerfStates** routine registers a device component for performance state management by the power management framework (PoFx).|
|[**PoFxRegisterDevice**](/windows-hardware/drivers/ddi/wdm/nf-wdm-pofxregisterdevice)|The **PoFxRegisterDevice** routine registers a device with the power management framework (PoFx).|
|[**PoFxReportDevicePoweredOn**](/windows-hardware/drivers/ddi/wdm/nf-wdm-pofxreportdevicepoweredon)|The **PoFxReportDevicePoweredOn** routine notifies the power management framework (PoFx) that the device completed the requested transition to the D0 (fully on) power state.|
|[**PoFxSetComponentLatency**](/windows-hardware/drivers/ddi/wdm/nf-wdm-pofxsetcomponentlatency)|The **PoFxSetComponentLatency** routine specifies the maximum latency that can be tolerated in the transition from the idle condition to the active condition in the specified component.|
|[**PoFxSetComponentResidency**](/windows-hardware/drivers/ddi/wdm/nf-wdm-pofxsetcomponentresidency)|The **PoFxSetComponentResidency** routine sets the estimated time for how long a component is likely to remain idle after the component enters the idle condition.|
|[**PoFxSetComponentWake**](/windows-hardware/drivers/ddi/wdm/nf-wdm-pofxsetcomponentwake)|The **PoFxSetComponentWake** routine indicates whether the driver arms the specified component to wake whenever the component enters the idle condition.|
|[**PoFxSetDeviceIdleTimeout**](/windows-hardware/drivers/ddi/wdm/nf-wdm-pofxsetdeviceidletimeout)|The **PoFxSetDeviceIdleTimeout** routine specifies the minimum time interval from when the last component of the device enters the idle condition to when the power management framework (PoFx) calls the driver's [*DevicePowerNotRequiredCallback*](/windows-hardware/drivers/ddi/wdm/nc-wdm-po_fx_device_power_not_required_callback) callback routine.|
|[**PoFxStartDevicePowerManagement**](/windows-hardware/drivers/ddi/wdm/nf-wdm-pofxstartdevicepowermanagement)|The **PoFxStartDevicePowerManagement** routine completes the registration of a device with the power management framework (PoFx) and starts device power management.|
|[**PoFxUnregisterDevice**](/windows-hardware/drivers/ddi/wdm/nf-wdm-pofxunregisterdevice)|The **PoFxUnregisterDevice** routine removes the registration of a device from the power management framework (PoFx).|

## Device Power Management Callbacks

These callback routines are required by the power management framework (PoFx) to enable device power management. The driver that is the power policy owner for the device implements these callback routines. PoFx calls these routines to query and configure the power states of the components in the device.

|Topic|Description|
|----|----|
|[ComponentActiveConditionCallback](/windows-hardware/drivers/ddi/wdm/nc-wdm-po_fx_component_active_condition_callback)|The *ComponentActiveConditionCallback* callback routine notifies the driver that the specified component completed a transition from the idle condition to the active condition.|
|[ComponentIdleConditionCallback](/windows-hardware/drivers/ddi/wdm/nc-wdm-po_fx_component_idle_condition_callback)|The *ComponentIdleConditionCallback* callback routine notifies the driver that the specified component completed a transition from the active condition to the idle condition.|
|[ComponentIdleStateCallback](/windows-hardware/drivers/ddi/wdm/nc-wdm-po_fx_component_idle_state_callback)|The *ComponentIdleStateCallback* callback routine notifies the driver of a pending change to the Fx power state of the specified component.|
|[ComponentPerfStateCallback](/windows-hardware/drivers/ddi/wdm/nc-wdm-po_fx_component_perf_state_callback)|The *ComponentPerfStateCallback* callback routine notifies the driver that its request to change the performance state of a component is complete.|
|[DevicePowerNotRequiredCallback](/windows-hardware/drivers/ddi/wdm/nc-wdm-po_fx_device_power_not_required_callback)|The *DevicePowerNotRequiredCallback* callback routine notifies the device driver that the device is not required to stay in the D0 power state.|
|[DevicePowerRequiredCallback](/windows-hardware/drivers/ddi/wdm/nc-wdm-po_fx_device_power_required_callback)|The *DevicePowerRequiredCallback* callback routine notifies the device driver that the device must enter and remain in the D0 power state.|
|[PowerControlCallback](/windows-hardware/drivers/ddi/wdm/nc-wdm-po_fx_power_control_callback)|The *PowerControlCallback* callback routine performs a power control operation that is requested by the power management framework (PoFx).|

## Device Power Management Structures

The the power management framework (PoFx) defines these structures to support device power management.

|Topic|Description|
|----|----|
|[PO_FX_COMPONENT_V1](/windows-hardware/drivers/ddi/wdm/ns-wdm-_po_fx_component_v1)   [PO_FX_COMPONENT_V2](/windows-hardware/drivers/ddi/wdm/ns-wdm-_po_fx_component_v2)|The **PO_FX_COMPONENT** structure describes the power state attributes of a component in a device.|
|[PO_FX_COMPONENT_IDLE_STATE](/windows-hardware/drivers/ddi/wdm/ns-wdm-_po_fx_component_idle_state)|The **PO_FX_COMPONENT_IDLE_STATE** structure specifies the attributes of an Fx power state of a component in a device.|
|[PO_FX_COMPONENT_PERF_INFO](/windows-hardware/drivers/ddi/wdm/ns-wdm-_po_fx_component_perf_info)|The **PO_FX_COMPONENT_PERF_INFO** structure describes all the sets of performance states for a single component within a device.|
|[PO_FX_COMPONENT_PERF_SET](/windows-hardware/drivers/ddi/wdm/ns-wdm-_po_fx_component_perf_set)|The **PO_FX_COMPONENT_PERF_SET** structure represents a set of performance states for a single component within a device.|
|[PO_FX_DEVICE_V1](/windows-hardware/drivers/ddi/wdm/ns-wdm-_po_fx_device_v1)   [PO_FX_DEVICE_V2](/windows-hardware/drivers/ddi/wdm/ns-wdm-_po_fx_device_v2)   [PO_FX_DEVICE_V3](/windows-hardware/drivers/ddi/wdm/ns-wdm-po_fx_device_v3)|The **PO_FX_DEVICE** structure describes the power attributes of a device to the power management framework (PoFx).|
|[PO_FX_PERF_STATE](/windows-hardware/drivers/ddi/wdm/ns-wdm-_po_fx_perf_state)|The **PO_FX_PERF_STATE** structure represents a performance state for a single component within a device.|
|[PO_FX_PERF_STATE_CHANGE](/windows-hardware/drivers/ddi/wdm/ns-wdm-_po_fx_perf_state_change)|The **PO_FX_PERF_STATE_CHANGE** structure contains information about a change to a performance state that is being requested by calling the [PoFxIssueComponentPerfStateChange](/windows-hardware/drivers/ddi/wdm/nf-wdm-pofxissuecomponentperfstatechange) or [PoFxIssueComponentPerfStateChangeMultiple](/windows-hardware/drivers/ddi/wdm/nf-wdm-pofxissuecomponentperfstatechangemultiple) routine.

## Device Power Management Enumerations

The power management framework (PoFx) defines these enumerations to support device power management.

|Topic|Description|
|----|----|
|[PO_FX_PERF_STATE_TYPE](/windows-hardware/drivers/ddi/wdm/ne-wdm-_po_fx_perf_state_type)|The **PO_FX_PERF_STATE_TYPE** enumeration contains values that describe the type of performance states in a [PO_FX_COMPONENT_PERF_SET](/windows-hardware/drivers/ddi/wdm/ns-wdm-_po_fx_component_perf_set).|
|[PO_FX_PERF_STATE_UNIT](/windows-hardware/drivers/ddi/wdm/ne-wdm-_po_fx_perf_state_unit)|The **PO_FX_PERF_STATE_UNIT** enumeration contains values that describe the type of unit that is controlled by the performance states in a [PO_FX_COMPONENT_PERF_SET](/windows-hardware/drivers/ddi/wdm/ns-wdm-_po_fx_component_perf_set).

## Device Power Management Constants

### PO_FX_FLAG_XXX flag bits

The **PO_FX_FLAG_XXX** constants are flag bits that indicate whether a request to change the condition of component is performed synchronously or asynchronously.

```c++
#define PO_FX_FLAG_BLOCKING   0x1
#define PO_FX_FLAG_ASYNC_ONLY 0x2
```

#### PO_FX_FLAG_XXX constants

|Constant|Description|
|----|----|
|PO_FX_FLAG_BLOCKING|Make the condition change synchronous. If this flag is set, the routine that requests the condition change does not return control to the calling driver until the component hardware completes the transition to the new condition. This flag can be used only if the caller is running at IRQL < DISPATCH_LEVEL.|
|PO_FX_FLAG_ASYNC_ONLY|Make the condition change fully asynchronous. If this flag is set, the calling driver's callback routine is called from a thread other than the thread in which the routine that requests the condition change is called. Thus, the routine that requests the condition change always returns asynchronously without waiting for the callback to complete.|

#### PO_FX_FLAG_XXX remarks

The Flags parameter to the following routines can be set to a **PO_FX_FLAG_XXX** constant:

- [PoFxActivateComponent](/windows-hardware/drivers/ddi/wdm/nf-wdm-pofxactivatecomponent)
- [PoFxIdleComponent](/windows-hardware/drivers/ddi/wdm/nf-wdm-pofxidlecomponent)
- [PoFxIssueComponentPerfStateChange](/windows-hardware/drivers/ddi/wdm/nf-wdm-pofxissuecomponentperfstatechange)
- [PoFxIssueComponentPerfStateChangeMultiple](/windows-hardware/drivers/ddi/wdm/nf-wdm-pofxissuecomponentperfstatechangemultiple)

The **PO_FX_FLAG_BLOCKING** and **PO_FX_FLAG_ASYNC_ONLY** flag bits are mutually exclusive. The caller can set one or the other flag bit in the Flags parameter, but not both flag bits.

#### PO_FX_FLAG_XXX Requirements

|Version|Header|
|----|----|
|Supported starting with Windows 8.|Wdm.h|

### PO_FX_FLAG_PERF_XXX flag bits

The **PO_FX_FLAG_PERF_XXX** constants are flag bits that define how the power management framework (PoFx) manages performance states for a device component.

```c++
#define PO_FX_FLAG_PERF_PEP_OPTIONAL   0x1
#define PO_FX_FLAG_PERF_QUERY_ON_F0 0x2
#define PO_FX_FLAG_PERF_QUERY_ON_ALL_IDLE_STATES 0x4
```

|Constant|Value|Description|
|----|----|----|
|**PO_FX_FLAG_PERF_PEP_OPTIONAL**|1 (0x1)|Indicates that the driver can change performance states without assistance from the platform extension plug-in (PEP), or that the driver is registering performance states with PoFx for logging purposes only. If this flag is set, the [PoFxRegisterComponentPerfStates](/windows-hardware/drivers/ddi/wdm/nf-wdm-pofxregistercomponentperfstates) call will still succeeded if the PEP does not support performance states for the component.|
|**PO_FX_FLAG_PERF_QUERY_ON_F0**|2 (0x2)|For some devices, the PEP may need to a place a performance state set for a component into a certain performance state (known as a *nominal performance state*) when it idles the component. Drivers set this flag if the component contains nominal performance states, in which case PoFx will query the PEP to determine the current performance state when the component transitions to F0.|
|**PO_FX_FLAG_PERF_QUERY_ON_ALL_IDLE_STATES**|4 (0x4)|For some devices, the PEP may need to a place a performance state set for a component into a certain performance state (known as a *nominal performance state*) when it transitions the component between idle states. Drivers set this flag if this component contains nominal performance states, in which case PoFx will query the PEP to determine the current performance state when the component transitions between idle states.|

#### PO_FX_FLAG_PERF_XXX remarks

The Flags parameter to the [PoFxRegisterComponentPerfStates](/windows-hardware/drivers/ddi/wdm/nf-wdm-pofxregistercomponentperfstates) routine can be set to a **PO_FX_FLAG_PERF_XXX** constant.

#### PO_FX_FLAG_PERF_XXX requirements

|Requirements|Version|
|----|----|
|Supported starting with Windows 10.|Wdm.h|
