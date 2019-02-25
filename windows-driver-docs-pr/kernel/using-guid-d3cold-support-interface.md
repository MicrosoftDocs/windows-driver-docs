---
title: Using the GUID_D3COLD_SUPPORT_INTERFACE Driver Interface
description: Starting with Windows 8, drivers can call the routines in the GUID_D3COLD_SUPPORT_INTERFACE interface to determine the D3cold capabilities of devices and to enable these devices to use D3cold.
ms.assetid: 525637E8-B16F-4038-A78D-A47064E36449
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Using the GUID\_D3COLD\_SUPPORT\_INTERFACE Driver Interface


Starting with Windows 8, drivers can call the routines in the GUID\_D3COLD\_SUPPORT\_INTERFACE interface to determine the D3cold capabilities of devices and to enable these devices to use D3cold. The two primary routines in this interface are [*SetD3ColdSupport*](https://msdn.microsoft.com/library/windows/hardware/hh967716) and [*GetIdleWakeInfo*](https://msdn.microsoft.com/library/windows/hardware/hh967712).


The GUID_D3COLD_SUPPORT_INTERFACE driver interface provides support for the D3cold substate of the D3 device power state. D3 is divided into two substates, D3hot and D3cold. D3 is the lowest-powered device power state, and D3cold uses less power than D3hot. A device can enter D3cold only if the device, the parent bus driver, and the platform firmware support this state. A device that supports D3cold can enter and exit this state when the computer is in the S0 (working) system power state.

The driver that is the power policy owner (PPO) for the device calls the routines in this interface to do the following:

-    Discover whether the device, the parent bus driver, and platform firmware support transitions to the D3cold substate. 
-    Discover whether the device can signal a wake event to the processor when the device is in the D3cold substate. 
-    Enable and disable transitions to the D3cold substate by the device. 

To query for this interface, a device driver sends an IRP_MN_QUERY_INTERFACE IRP down the driver stack. For this IRP, the driver sets the InterfaceType input parameter to GUID_D3COLD_SUPPORT_INTERFACE. On successful completion of the IRP, the Interface output parameter is a pointer to a D3COLD_SUPPORT_INTERFACE structure. This structure contains pointers to the routines in the interface.

For more information about the D3cold device power state, see [Supporting D3cold in a Driver](supporting-d3cold-in-a-driver.md).


A driver calls the *SetD3ColdSupport* routine to dynamically enable and disable a device's transitions to D3cold that can occur when the computer is in S0. If the device must be able to signal a wake event from any low-power Dx state that the device enters, the driver should enable the device to enter D3cold only if the device can signal wake events from D3cold. Otherwise, after the device enters D3cold, it might be unavailable until the computer leaves the S0 state.

By default, before the first call to the *SetD3ColdSupport* routine, D3hot-to-D3cold transitions are disabled. To change this default so that D3hot-to-D3cold transitions are enabled before the first *SetD3ColdSupport* call, the driver package for the device can include the following two lines in the DDInstall.HW section of the INF file that installs the driver:

```Text
Include = machine.inf
Needs = PciD3ColdSupported
```

The *GetIdleWakeInfo* routine enables the driver for a device to discover the device power states from which the device can signal a wake event when the computer is in a particular system power state. The caller to this routine specifies a system power state as an input parameter, and, as an output parameter, the routine reports the lowest-powered device power state from which the device can signal a wait event when the computer is in the specified system power state. For example, the *GetIdleWakeInfo* routine can tell the driver whether the device can signal a wake event from D3cold when the computer is in S0.

The *GetIdleWakeInfo* routine supplies more complete device-wake information than is available from the [**IRP\_MN\_QUERY\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff551664) request. This request, which all versions of Windows support, supplies a [**DEVICE\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff543095) structure that describes the capabilities of a device. The **DeviceWake** member of this structure contains a subset of the information that is available from the *GetIdleWakeInfo* routine. This member indicates the lowest-powered device power state from which a device can signal a wait event. The information in this member is guaranteed to be accurate only if the computer is in the system low-power state that is indicated by the **SystemWake** member of the structure. If **SystemWake** = **PowerSystemSleeping3**, the information in **DeviceWake** is known to be valid for S3, might frequently be valid for S1 and S2, and might even be valid for S0.

However, as a best practice, a driver should not assume that the information in the **DeviceWake** method is valid for any system power state other than the state indicated by **SystemWake**. For some devices, the lowest Dx state from which a device can signal a wake event varies according to whether the computer is in working state S0 or in a low-power state (S1, S2, S3, or S4). For other devices, the buses to which the devices are connected can handle wake signals when the computer is in S0, but the devices cannot. Only the *GetIdleWakeInfo* routine can accurately describe the device-wake capabilities of these devices.

For example, the [PCI Express Base 3.0 Specification](http://www.pcisig.com/specifications/pciexpress/specifications/) defines two separate mechanisms to signal wake events—one mechanism is used when the PCI Express link (bus) is turned on, and the other is used when the link is turned off. When the link is turned on, the device sends a stream of PM\_PME Transaction Layer Packets (TLPs) to signal that the device should move from a low-power Dx state to D0. When the link is turned off, the device requests that the link be turned on so that the device can send PM\_PME TLPs. To request that the link be turned on, the device either asserts its WAKE\# signal (for the more common device form factor) or uses the "beaconing" mechanism (less common).

The PCI Express specification requires that all devices that advertise the ability to signal power management events (PMEs) from D3cold implement both of these device-wake mechanisms, but a driver developer might need to enable a device that does not correctly implement these mechanisms.

If the device can correctly deliver PM\_PME TLPs when the link is turned on, the driver can enable the device to enter D3hot when the computer is in S0. If the device can correctly assert its WAKE\# signal to turn the link on and then use PM\_PME TLPs to initiate the transition to D0, the driver can enable the device to enter D3cold when the computer is in S0.

However, the driver should not enable the device to enter either D3hot or D3cold if the system firmware (the BIOS) can't guarantee that the PCI Express device-wake mechanisms are correctly handled by the hardware platform. A driver can call the [*GetIdleWakeInfo*](https://msdn.microsoft.com/library/windows/hardware/hh967712) routine to discover whether the firmware claims support for these mechanisms. If a driver uses Kernel-Mode Driver Framework (KMDF) 1.11 or later, a convenient alternative to calling *GetIdleWakeInfo* is to allow the [**WdfDeviceAssignS0IdleSettings**](https://msdn.microsoft.com/library/windows/hardware/ff545903) method to enable the device to idle in the lowest-powered Dx state from which the device can signal a wake event.

 

 




