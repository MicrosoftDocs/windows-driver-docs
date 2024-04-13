---
title: Overview of the Power Management Framework
description: Starting with Windows 8, the run-time power management framework (PoFx) supports power and clock management at the component (or subdevice) level.
ms.date: 08/05/2021
---

# Overview of the Power Management Framework

Windows 7 and earlier versions of the operating system only provide support for device-level power management, which enables a driver to support D-states in a device.
The Advanced Configuration and Power Interface (ACPI) specification defines [device power states](device-power-states.md) D0 (fully on) through D3 (fully off), and defines [system power states](system-power-states.md) S0 (fully on)
 through S5 (fully off). These versions of Windows do not provide mechanisms to independently manage the power supplied to the individual components in a device. In these versions of Windows, some drivers can implement
  custom power controls for components, but these controls typically add complexity to drivers, and might be feasible only if component power settings are controlled within the device.

Starting with Windows 8, the run-time power management framework (PoFx) adds support for component-level power management.
A component, or subdevice, is a functional hardware unit in a device that can be turned on or switched to a low-power state independently of the other components in the same device.
For example, an audio device might have separate components for playback and recording whose power states can be managed independently of each other.
If the playback component is being used, but the recording component is idle, the recording component can be switched to a low-power state without interfering with the activity of the playback component.

A device driver registers with PoFx to independently manage power usage in the individual components in a device.
PoFx provides the fine-grained control necessary to extend the time that a Windows portable computer, tablet, phone, or other mobile device can run on a battery charge.
PoFx reduces power usage in a way that maintains the appearance of a mobile device that is always on and always connected.

A driver typically supports some number of component power states, F0, F1, and so on, where F0 is the fully on state. All components support
 the F0 state. The driver that is the power policy owner (PPO) for the components in a device is responsible for defining any additional, low-power Fx power states that a component might have. (Typically, the function driver for a
  device is the PPO.) This driver determines the number of low-power Fx states per component and the attributes of each Fx state. The Fx states that this driver defines might vary from component to component in the same device.

PoFx provides a device driver interface (DDI) through which a driver can supply status and capabilities information about the components in a device. This information includes:

* The current activity level of each component
* The time required by the component to change from one power state to another
* The amount of latency that can be tolerated by clients of the device when the component wakes from a low-power state

In addition, PoFx obtains system-wide information about the power and clock domains to which the component belongs.
 (The devices in a particular power domain share a common power rail; the devices in a particular clock domain share a common clock signal.)

Based on this information, PoFx makes intelligent decisions about when a component should enter a low-power state and which low-power state to enter. The decision process involves information from other components and other devices,
 and takes into account the dependencies between the devices and components in the various power and clock domains.

To get started using PoFx, see [Device power management reference](./device-power-management-reference.md) and [Component-Level Power Management](./component-level-power-management.md).
