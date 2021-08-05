---
title: Component-Level Power Management
description: Starting with Windows 8, the power management framework (PoFx) enables a driver to manage the power states of the individual components in a device. Component-level power management exists side-by-side with device-level power management.
ms.localizationpriority: medium
ms.custom: contperf-fy22q1
ms.date: 08/05/2021
---

# Component-Level Power Management


Starting with Windows 8, the power management framework (PoFx) enables a driver to manage the power states of the individual components in a device.
Component-level power management exists side-by-side with device-level power management. For an introduction, see [Overview of the Power Management Framework](/windows-hardware/drivers/kernel/overview-of-the-power-management-framework).


This page describes the PoFx API for Component-Level Power Management.


To register a device to be managed by PoFx, the driver calls the [**PoFxRegisterDevice**](/windows-hardware/drivers/ddi/wdm/nf-wdm-pofxregisterdevice) routine. The driver passes this routine a
 [**PO\_FX\_DEVICE**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_po_fx_device_v1) structure that, among other data, contains an array of [**PO\_FX\_COMPONENT**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_po_fx_component_v1) structures.
  Each element in this array describes the Fx power states of a component in the device and the attributes of each Fx state.
   (At minimum, a component that does not support component-level power management implements only the F0 state.) The attributes of a particular Fx power state in a particular component are described by
    a [**PO\_FX\_COMPONENT\_IDLE\_STATE**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_po_fx_component_idle_state) structure, which contains the following values:

-   The transition latency, which is the time required to make a transition from this Fx state to the F0 (fully on) state.
-   The residency requirement, which is the time that a component must spend in this Fx state to make a transition to the state worthwhile.
-   The nominal power, which is the power that is consumed by the component in this Fx state.

PoFx uses this information (in addition to other system-wide inputs and dependencies) to make intelligent decisions about which Fx power state a component should be in at any particular time.
 PoFx must balance two competing objectives. First, a component that is idle should be configured to consume as little power as possible.
  Second, a component must be prepared to switch from a low-power Fx state to F0 quickly enough to maintain the appearance of a device that is always on and always connected.

Component-level power management can be performed only when a device is in the D0 (fully on) power state. When a device is in the D1 (almost on), D2 (almost off), or D3 power state, the device is inaccessible.
 When the device is in the D0 state, only components that the driver is actively using need to remain in the F0 state. Idle components can potentially switch to low-power Fx states to reduce power consumption.

While a device is in the D0 power state, the driver follows a simple protocol to enable component-level power management. When the driver needs to access a component, the driver calls the
 [**PoFxActivateComponent**](/windows-hardware/drivers/ddi/wdm/nf-wdm-pofxactivatecomponent) routine to request access to the component.
  If the component is in a low-power Fx state when this call occurs, PoFx initiates a transition to the F0 state and notifies the driver when this transition is complete.
   The driver can then access the component. When the driver no longer needs to access the component, the driver calls the [**PoFxIdleComponent**](/windows-hardware/drivers/ddi/wdm/nf-wdm-pofxidlecomponent) routine to notify PoFx.
    In response to this call, PoFx can potentially switch the component to a low-power Fx state.

A component that is accessible is in the *active condition*. A component that is inaccessible is in the *idle condition*.
 To track the accessibility of the components in a device, PoFx maintains an activation reference count on each component.
  A **PoFxActivateComponent** call increments the count on the specified component by one, and a **PoFxIdleComponent** call decrements the count by one.

If a **PoFxActivateComponent** call increments the count from zero to one, PoFx initiates a transition from the idle condition to the active condition, and notifies the driver when this transition completes.
 If a **PoFxActivateComponent** occurs when the component is already in the active condition, the component stays in the active condition and the driver receives no notification.

If a **PoFxIdleComponent** call decrements the count from one to zero, PoFx initiates a transition from the active condition to the idle condition, and notifies the driver when this transition is complete.
 If a **PoFxIdleComponent** call decrements the count but the count remains nonzero, the component stays in the active condition and the driver receives no notification.

The activation reference count conveniently handles situations in which two or more code paths in the same driver might need to concurrently access the same component in a device. By maintaining this count,
 PoFx enables the various parts of the driver to independently maintain access to the component without requiring the driver to centrally manage access to the component.

The active/idle condition of a component is the only reliable means for a driver to determine whether a component is accessible. A component that is in the F0 power state but is in the idle condition might
 be about to switch to a low-power Fx state.

A component that is in the active condition is always in the F0 state. The component cannot leave F0 until it enters the idle condition.
 A component that is in the idle condition might be in F0 or in a low-power Fx state.
  If a component is in a low-power Fx state when a **PoFxActivateComponent** call initiates a transition from the idle condition to the active condition, PoFx must first switch the component to F0 before the component can
   enter the active condition.

## Related topics

[Device Power Management Reference](device-power-management-reference.md)
