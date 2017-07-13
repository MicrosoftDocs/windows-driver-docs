---
title: Using the GUID\_D3COLD\_SUPPORT\_INTERFACE Driver Interface
author: windows-driver-content
description: Starting with Windows 8, drivers can call the routines in the GUID\_D3COLD\_SUPPORT\_INTERFACE interface to determine the D3cold capabilities of devices and to enable these devices to use D3cold.
ms.assetid: 525637E8-B16F-4038-A78D-A47064E36449
---

# Using the GUID\_D3COLD\_SUPPORT\_INTERFACE Driver Interface


Starting with Windows 8, drivers can call the routines in the [GUID\_D3COLD\_SUPPORT\_INTERFACE](https://msdn.microsoft.com/library/windows/hardware/hh967714) interface to determine the D3cold capabilities of devices and to enable these devices to use D3cold. The two primary routines in this interface are [*SetD3ColdSupport*](https://msdn.microsoft.com/library/windows/hardware/hh967716) and [*GetIdleWakeInfo*](https://msdn.microsoft.com/library/windows/hardware/hh967712).

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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Using%20the%20GUID_D3COLD_SUPPORT_INTERFACE%20Driver%20Interface%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


