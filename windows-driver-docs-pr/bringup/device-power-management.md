---
title: Device power management
description: The ACPI 5.0 specification defines a set of namespace objects to specify device power information for a device.
ms.assetid: F57AD5A0-F459-4A20-BDBE-87C30CF957B3
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Device power management


The [ACPI 5.0 specification](https://www.uefi.org/specifications) defines a set of namespace objects to specify device power information for a device. For example, one set of objects can specify the power resources that a device requires in each supported device power state. Another object type can describe the ability of the device to wake from a low-power state in response to hardware events.

## Device power management in Windows


While a system is running (that is, the system is in the ACPI-defined working state, S0), individual devices can make transitions between device power states, depending on activity, to save power. In traditional PC systems, ACPI-defined sleeping states (S1 through S4) are also used to save power, but these disconnected, high-latency sleep states are not used on Windows SoC platforms. Therefore, battery life is highly dependent on how platforms implement run-time device power management.

Devices that are integrated into the SoC can be power-managed through the Windows Power Framework (PoFx). These framework-integrated devices are power-managed by PoFx through a SoC-specific power engine plug-in (microPEP) that knows the specifics of the SoC's power and clock controls. For more information about PoFx, see [Overview of the Power Management Framework](https://msdn.microsoft.com/library/windows/hardware/hh406637).

For peripheral devices that are not integrated into the SoC, Windows uses ACPI Device Power Management. For these ACPI-managed devices, the power policy owner in a device driver stack (typically the function or class driver) makes device power state transition decisions, and the [Windows ACPI driver](https://msdn.microsoft.com/library/windows/hardware/ff540493), Acpi.sys, invokes ASL control methods to apply the required platform-specific power controls.

**Note**  It is possible to, and some device stacks do, use ACPI Device Power Management—alone, or in combination with the microPEP—for on-SoC device power management.

 

As described in [Device power management in ACPI](#acpi), Windows supports the D3cold power management capabilities that are defined in the ACPI 5.0 specification. By using this support, devices, platforms and drivers can opt-in to having device power completely removed during run-time idle periods. This capability can significantly improve battery life. However, removing power must be supported by all affected components in order to be able to return to D0 successfully. For this reason, drivers (bus and function), as well as the platform itself, must indicate that they support it. For more information about D3cold driver opt-in, see [Supporting D3cold in a Driver](https://msdn.microsoft.com/library/windows/hardware/hh967717).

## Device power management in ACPI


Namespace devices support up to four device power states, numbered D0 (full-function, or "on") to D3 (no function, or "off"). Each state can have different power requirements, with higher-numbered states consuming less power than lower-numbered states. In addition, the D3 (off) state has two sub-states, D3hot and D3cold. The D3hot sub-state requires the device to remain accessible on its parent bus so that it can respond to bus-specific software commands. This requirement, and the power used to meet it, are removed in D3cold. Finally, a device can be armed to wake itself from a low-power state due to a hardware event, and, if necessary, to also bring the platform out of an idle state.

The platform indicates its support for D3cold by granting the OS control of the "\_PR3 Support" feature (bit 2) when requested by using the platform-wide OSPM Capabilities Method. For more information, see section 6.2.10.2, "Platform-wide OSPM Capabilities", in the [ACPI 5.0 specification](https://www.uefi.org/specifications).

Power-managed devices use child objects to describe their power capabilities to the operating system. The following sections describe these capabilities and objects.

### Power resources and states

A device declares its support for a power state by listing the set of power resources it requires in order to be in that state. ACPI Power Resources represent the voltage rails that power devices and the clock signals that drive them. These resources are declared at the root of the namespace. Each power resource has an \_ON and an \_OFF method through which it is controlled, and an \_STA method to report its state. For more information, see section 7.1, "Declaring a Power Resource Object", of the [ACPI 5.0 specification](https://www.uefi.org/specifications).

The [Windows ACPI driver](https://msdn.microsoft.com/library/windows/hardware/ff540493), Acpi.sys, monitors the power dependencies among devices that share resources, and, as these devices transition between power states, ensures that only the power resources that are actually needed by a device are turned on at any particular time.

**Power Resource Requirements (\_PRx)**

There is a Power Resource Requirements (\_PRx) object, where x = 0, 1, 2, or 3, for each supported device power state. When the device driver decides to transition to a new power state, Acpi.sys ensures that any power resources required for the new state are turned on, and that any resources no longer in use are turned off.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Device state supported</th>
<th>Resource requirements object to use</th>
<th>Resources to include in requirements object</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>D0 (required)</td>
<td>_PR0</td>
<td><p>All power and clocks required for full function of the device.</p></td>
</tr>
<tr class="even">
<td>D1</td>
<td>_PR1</td>
<td><p>Any power or clocks required for the class-defined reduced-functionality of this state.</p></td>
</tr>
<tr class="odd">
<td>D2</td>
<td>_PR2</td>
<td><p>Any power or clocks required for the class-defined reduced-functionality of this state.</p></td>
</tr>
<tr class="even">
<td>D3hot (required)</td>
<td>_PR2</td>
<td><p>The same resources as the next higher state that is supported (D2, D1, or D0).</p></td>
</tr>
<tr class="odd">
<td>D3cold</td>
<td>_PR3</td>
<td><p>Only the power or clocks required for the device to appear on its bus and respond to a bus-specific command.</p></td>
</tr>
</tbody>
</table>

 

**Note**  If a particular platform supports the D3cold feature, and the device driver for a device opts-in to D3cold, the device's \_PR3 power resources will, if they are not being used by any other device, be turned off sometime after the transition to D3hot.

 

For more information about the power resource requirements for a device that supports D3cold, see [Firmware Requirements for D3cold](firmware-requirements-for-d3cold.md).

**Device Power State (\_PSx)**

There is a Power State method, \_PSx, where x = 0, 1, 2, or 3, for each supported device power state Dx. This method is optional, but, if it is present, it is invoked before the power resources for the state are turned off, and after the power resources for the state are turned on. \_PSx is intended to perform any platform-specific actions required around the power cycle. \_PSx must not access device registers that are assigned to the function driver, access bus-standard registers that are assigned to the bus driver, or switch power resources on or off, which is an operation reserved for Acpi.sys.

### Wake capabilities

Power-managed devices might be able to detect events when in a low-power state and cause the platform to wake up to handle them. To enable this feature, Windows needs information about the capabilities of both the platform and the device.

**Sx Device Wake State (\_SxW)**

On a given platform, there is a specific mapping between device states that support the wake capability and system states that can respond to wake events. ACPI defines the \_SxW object to provide this information to the operating system. There is an SxW object for each supported system power state, Sx. Because SoC platforms are always in S0, the only object of interest here is \_S0W. This object specifies the platform's ability to wake from a low-power idle state in response to a device's wake signal. The object is used by Windows to determine the target D-state for the device during system low-power idle. For more information about \_S0W, see section 7.2.20, "\_S0W (S0 Device Wake State)", in the [ACPI 5.0 specification](https://www.uefi.org/specifications).

For most SoC platforms, devices are aggressively power-managed to the D3 state when idle, and the system is capable of waking from low-power idle while the device is in this state. For such a system, the \_S0W object returns 3 (or 4, if it also supports D3cold). However, any D-state can be designated as the lowest-powered wake-capable state, and some device classes or buses use different values. For instance, SDIO- and USB-connected devices use state D2 for this state.

**Note**  To facilitate the migration of device drivers from Windows 7 to Windows 8 or Windows 8.1, your device might be required to supply \_S4W as well. Currently, the only device class that has this requirement is networking (Ndis.sys).

 

**Wake-capable interrupts (\_CRS)**

The resource description for a device indicates that the device is capable of detecting and signaling a wake event by marking an interrupt as "wake-capable" (either ExclusiveAndWake or SharedAndWake). Windows and device drivers provide special handling of such interrupts to ensure that they are enabled when the device transitions to a low-power state. For more information, see the descriptions of the Interrupt and GpioInt resource descriptors in section 6.4.3.6, "Extended Interrupt Descriptor", and section 6.4.3.8.1 , "GPIO Connection Descriptors", of the [ACPI 5.0 specification](https://www.uefi.org/specifications).

### Wake enablement

Depending on user scenario or system policy, wake-capable devices may or may not actually be armed for wake. Therefore, wake-capable interrupts may or may not be enabled when the device is idle. In addition to enabling interrupts, Windows uses the following mechanisms to enable wake on a device.

**Device Sleep Wake (\_DSW)**

ACPI defines the \_DSW object as a way for the operating system to inform the ACPI platform firmware about the next sleep or low-power idle period. This object is optional, and is used only if the platform has a need to configure platform-specific wake hardware in advance. The target D-state for the device and the target S-state for the system are both provided. The D-state and S-state combination will always comply with the information provided by the device's \_SxW object(s).

**Power Resources for Wake (\_PRW)**

In some cases, additional power resources must be turned on for a device to be enabled for wake. In this case, the device can provide the \_PRW object to list those additional power resources. The [Windows ACPI driver](https://msdn.microsoft.com/library/windows/hardware/ff540493), Acpi.sys, will manage these power resources as it normally does, making sure that they are turned on when they are needed by a device (that is, a wake-enabled device), and are turned off otherwise.

\_PRW is also used to define the wake capability for traditional (full-ACPI hardware) PC platforms.

 

 




