---
title: Component-Level Performance State Management
description: Starting with Windows 10, the power management framework (PoFx) enables a driver to define one or more sets of individually adjustable performance states for individual components within a device.
ms.assetid: D5341D6D-7C71-43CB-9C70-7E939B32C33F
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Component-Level Performance State Management


Starting with Windows 10, the power management framework (PoFx) enables a driver to define one or more sets of individually adjustable performance states for individual components within a device. The driver can use performance states to throttle a component's workload to provide just enough performance for its current needs.

## Overview of Performance States


In Windows 8 and Windows 8.1, PoFx provides idle states (F-states) for component-level power savings by power and clock rail gating when a specific F-state is entered. This model saves power when a component is in an idle state (non-F0), but does not provide any mechanism for optimizing power usage or balancing it against performance needs when the component is active. Even though a component is active (in F0) and servicing a request, it may not require the full performance of the device. For example, a graphics card may need to only update a blinking cursor and this may not need full performance.

Variable performance states address this issue by allowing the driver to throttle a device’s component to provide just enough performance for its current needs. In Windows 8 and Windows 8.1, if a component supports performance states, each driver must implement a proprietary performance state selection algorithm that is internal to the driver, and if needed, notify the platform extension plug-in (PEP) in a proprietary manner. The PEP is a software component that performs power management tasks that are specific to a particular product line of processor or System on a Chip (SoC) modules. Driver-specific proprietary performance state solutions have the disadvantage of being tightly coupled with the PEP, and cannot be easily debugged.

Starting with Windows 10, PoFx provides an API for performance state management. This API has two main goals:

-   It provides a standard way for device drivers to notify the PEP about performance state changes so that the PEP may take the appropriate action.
-   It provides a standard way for drivers to notify the OS of performance state changes for logging and analysis in Windows Performance Analyzer (WPA), without needing a custom plug-in for each driver.

## Introduction to the PoFX API for Component-Level Performance States


PoFx enables a device to define the following types of performance states for each component:

-   A discrete number of states in the units of frequency (measured in Hz), bandwidth (measured in bits per second), or an opaque index number.
-   A continuous distribution of states between a minimum and maximum value.

Performance states are organized into sets and are registered on a per-component basis. Performance states within a set must increase monotonically. Most drivers are expected to define a single set of performance states per component. For example, a driver might define one set of performance states to control the clock frequency for a component. However, some drivers may need to define more than one performance state set to control multiple dimensions of performance states for a component. For example, a driver might define two sets of performance states to control the clock frequency and bus bandwidth.

To register a device component for performance state management by PoFx, a driver follows these general steps:

1.  The driver registers the device components to be managed by PoFx. For more information, see [Component-Level Power Management](component-level-power-management.md).

2.  The driver registers support for performance states by calling [**PoFxRegisterComponentPerfStates**](https://msdn.microsoft.com/library/windows/hardware/dn939778). As part of the registration call, drivers can either define a given component’s performance state themselves or defer to the platform extension plug-in (PEP) to define them instead.

    Either the device driver or the PEP must hold knowledge of the performance states, including the number of performance state sets per component, the type of performance state (discrete or range-based), and the details of the values and count of the actual performance states. If the PEP does not support performance states, the driver may still register for performance state support with PoFx and notify the OS of performance state changes for logging and analysis in Windows Performance Analyzer (WPA).

    In either case, upon successful completion of [**PoFxRegisterComponentPerfStates**](https://msdn.microsoft.com/library/windows/hardware/dn939778), the driver has a [**PO\_FX\_COMPONENT\_PERF\_INFO**](https://msdn.microsoft.com/library/windows/hardware/dn939832) structure that contains the registered performance state sets.

3.  When the driver decides a component should change performance states, it calls [**PoFxIssueComponentPerfStateChange**](https://msdn.microsoft.com/library/windows/hardware/dn939769) or [**PoFxIssueComponentPerfStateChangeMultiple**](https://msdn.microsoft.com/library/windows/hardware/dn939772). PoFx invokes the driver-provided [**ComponentPerfStateCallback**](https://msdn.microsoft.com/library/windows/hardware/dn939353) routine when the performance state change is complete.

4.  The driver is informed by the [**ComponentPerfStateCallback**](https://msdn.microsoft.com/library/windows/hardware/dn939353) routine whether the PEP succeeded or denied the performance state change. If the PEP succeeded the change, the driver then performs whatever work it needs to take to change the performance state from its perspective. If the PEP denied the change, the driver may choose to do nothing or retry the request again with the same or an alternate performance state.

## Related topics
[Device Power Management Reference](https://msdn.microsoft.com/library/windows/hardware/hh450958)  



