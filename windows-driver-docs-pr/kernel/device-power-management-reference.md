---
title: Device power management reference
description: Describes DDIs that drivers can use to divide their device hardware into multiple logical components to enable fine-grained power management
keywords: [AcceptDeviceNotification]
ms.date: 12/17/2018
ms.localizationpriority: medium
---

# Device power management reference

Drivers can divide their device hardware into multiple logical components to enable fine-grained power management. A component has a set of power states that can be managed independently of the power states of other components in the same device. In the F0 state, the component is fully turned on. The component might support additional, low-power states F1, F2, and so on.

The power policy owner for a device is typically the device's function driver. To enable component-level power management, this driver registers the device with the [power management framework (PoFx)](overview-of-the-power-management-framework.md). By registering the device, the driver assumes the responsibility for informing PoFx when a component is actively being used and when the component is idle. PoFx makes intelligent idle state choices for the device based on information about the component activity, latency tolerance, expected idle durations, and wake requirements. By controlling power usage at the component level, PoFx can reduce power requirements while preserving system responsiveness. For more information, see [Component-Level Power Management](component-level-power-management.md).

## Device Power Management Routines

These routines are implemented by the power management framework (PoFx) to enable device power management. These routines are called by the driver that is the power policy owner (PPO) for a device. Typically, the function driver for a device is the PPO for this device.

|Topic|Description|
|----|----|
|[**PoFxActivateComponent**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-pofxactivatecomponent)|The **PoFxActivateComponent** routine increments the activation reference count on the specified component.|
|[PoFxCompleteDevicePowerNotRequired](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-pofxcompletedevicepowernotrequired)|The **PoFxCompleteDevicePowerNotRequired** routine notifies the power management framework (PoFx) that the calling driver has completed its response to a call to the driver's [*DevicePowerNotRequiredCallback*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-po_fx_device_power_not_required_callback) callback routine.|
|[**PoFxCompleteIdleCondition**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-pofxcompleteidlecondition)|The **PoFxCompleteIdleCondition** routine informs the power management framework (PoFx) that the specified component has completed a pending change to the idle condition.|
|[**PoFxCompleteIdleState**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-pofxcompleteidlestate)|The PoFxCompleteIdleState routine informs the power management framework (PoFx) that the specified component has completed a pending change to an Fx state.|
|[**PoFxIdleComponent**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-pofxidlecomponent)|The **PoFxIdleComponent** routine decrements the activation reference count on the specified component.|
|[**PoFxIssueComponentPerfStateChange**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-pofxissuecomponentperfstatechange)|The **PoFxIssueComponentPerfStateChange** routine submits a request to place a device component in a particular performance state.|
|[**PoFxIssueComponentPerfStateChangeMultiple**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-pofxissuecomponentperfstatechangemultiple)|The **PoFxIssueComponentPerfStateChangeMultiple** routine submits a request to change the performance states in multiple performance state sets simultaneously for a device component.|
|[**PoFxNotifySurprisePowerOn**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-pofxnotifysurprisepoweron)|The **PoFxNotifySurprisePowerOn** routine notifies the power management framework (PoFx) that a device was turned on as a side effect of supplying power to some other device.|
|[**PoFxPowerControl**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-pofxpowercontrol)|The **PoFxPowerControl** routine sends a power control request to the power management framework (PoFx).|
|[**PoFxQueryCurrentComponentPerfState**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-pofxpowercontrol)|The **PoFxQueryCurrentComponentPerfState** routine retrieves the active performance state in a component's performance state set.|
|[**PoFxRegisterComponentPerfStates**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-pofxregistercomponentperfstates)|The **PoFxRegisterComponentPerfStates** routine registers a device component for performance state management by the power management framework (PoFx).|
|[**PoFxRegisterDevice**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-pofxregisterdevice)|The **PoFxRegisterDevice** routine registers a device with the power management framework (PoFx).|
|[**PoFxReportDevicePoweredOn**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-pofxreportdevicepoweredon)|The **PoFxReportDevicePoweredOn** routine notifies the power management framework (PoFx) that the device completed the requested transition to the D0 (fully on) power state.|
|[**PoFxSetComponentLatency**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-pofxsetcomponentlatency)|The **PoFxSetComponentLatency** routine specifies the maximum latency that can be tolerated in the transition from the idle condition to the active condition in the specified component.|
|[**PoFxSetComponentResidency**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-pofxsetcomponentresidency)|The **PoFxSetComponentResidency** routine sets the estimated time for how long a component is likely to remain idle after the component enters the idle condition.|
|[**PoFxSetComponentWake**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-pofxsetcomponentwake)|The **PoFxSetComponentWake** routine indicates whether the driver arms the specified component to wake whenever the component enters the idle condition.|
|[**PoFxSetDeviceIdleTimeout**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-pofxsetdeviceidletimeout)|The **PoFxSetDeviceIdleTimeout** routine specifies the minimum time interval from when the last component of the device enters the idle condition to when the power management framework (PoFx) calls the driver's [*DevicePowerNotRequiredCallback*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-po_fx_device_power_not_required_callback) callback routine.|
|[**PoFxStartDevicePowerManagement**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-pofxstartdevicepowermanagement)|The **PoFxStartDevicePowerManagement** routine completes the registration of a device with the power management framework (PoFx) and starts device power management.|
|[**PoFxUnregisterDevice**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-pofxunregisterdevice)|The **PoFxUnregisterDevice** routine removes the registration of a device from the power management framework (PoFx).|

## 