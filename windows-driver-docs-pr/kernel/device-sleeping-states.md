---
title: Device Low-Power States
description: Device Low-Power States
ms.assetid: f594a63f-10ce-439d-abe3-d342555d98f0
keywords: ["device power states WDK kernel", "device low-power states WDK power management", "sleep power management WDK kernel", "Dx names WDK power management", "asleep devices WDK power management", "lowest-powered device state WDK kernel", "highest-powered device low-power state WDK kernel", "intermediate sleeping state WDK kernel", "low power modes WDK kernel", "power saving modes WDK kernel", "continuous power WDK kernel", "delays WDK power management", "state transition delays WDK power management"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Device Low-Power States





Device power states D1, D2, and D3 are the device low-power states. Starting with Windows 8, D3 is divided into two substates, [D3hot](#d3hot) and [D3cold](#d3cold).

D1 and D2 are intermediate low-power states. Many classes of devices do not define these states. All devices must define D3hot.

The following sections describe D1, D2, and D3:

-   [Device Power State D1](#d1)
-   [Device Power State D2](#d2)
-   [Device Power State D3](#d3)

### <a href="" id="d1"></a>Device Power State D1

Device power state D1 is the highest-powered device low-power state. It has the following characteristics:

<a href="" id="power-consumption"></a>*Power consumption*  
Consumption is less than in the D0 state but greater than or equal to that in the D2 state. Frequently, D1 is a clock-gated state in which the device receives just enough power to preserve the device's hardware context. Typically, the specification for a bus or device class that supports D1 describes this state in more detail.

<a href="" id="device-context"></a>*Device context*  
In general, device context is preserved by the hardware and need not be restored by the driver. The specification for a bus or device class that supports D1 typically provides detailed requirements for preserving this context.

<a href="" id="device-driver-behavior"></a>*Device driver behavior*  
Drivers must save and restore or reinitialize any context lost by the hardware. Typically, however, devices lose little context upon entering this state.

<a href="" id="restore-time"></a>*Restore time*  
In general, the time required to restore the device to D0 from D1 should be less than restoration from D2 to D0.

<a href="" id="wake-up-capability"></a>*Wake-up capability*  
A device in D1 might be able to request wake-up. To supply information about whether this state can support a wake signal, a bus driver uses the [**DEVICE\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff543095) structure or, starting with Windows 8, the [GUID\_D3COLD\_SUPPORT\_INTERFACE](https://msdn.microsoft.com/library/windows/hardware/hh967714) driver interface.

Typically, devices that use D1 do so because resuming from this state does not require the driver to restore the device's full hardware context. To minimize the user's perception of delay, restoring a device to D0 from D1 should incur the least possible delay. Minimizing delay in the state transition is more important than reducing power consumption.

### <a href="" id="d2"></a>Device Power State D2

D2 is an intermediate device low-power state with the following characteristics:

<a href="" id="power-consumption"></a>*Power consumption*  
Consumption is less than or equal to that in the D1 state.

<a href="" id="device-context"></a>*Device context*  
In general, most device context is lost by the hardware. Frequently, this state preserves the part of the context that is used to signal wake events. The specification for a bus or device class that supports D2 typically provides detailed requirements for preserving this context.

<a href="" id="device-driver-behavior"></a>*Device driver behavior*  
Device drivers must save and restore or reinitialize any context lost by the hardware. A typical device loses most context when it enters D2.

<a href="" id="restore-time"></a>*Restore time*  
Restoring the device from D2 to D0 takes at least as long as restoring the device from D1 to D0. A graphics adapter that has a large frame buffer is an example of a device that has a large amount of hardware context to restore after a transition from D2 to D0. For such a device, the restore time from D2 might be much greater than the restore time from D1.

<a href="" id="wake-up-capability"></a>*Wake-up capability*  
A device in D2 might be able to request wake-up. To supply information about whether this state can support a wake signal, a bus driver uses the [**DEVICE\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff543095) structure or, starting with Windows 8, the [GUID\_D3COLD\_SUPPORT\_INTERFACE](https://msdn.microsoft.com/library/windows/hardware/hh967714) driver interface.

Typically, drivers that support D2 do so because their devices cannot support wake from D3. For these devices, power consumption in the D2 state drops to the lowest level from which the device can recover in response to a wake signal. In contrast to the D1 state, which is implemented to reduce the delay perceived by the user, the goal in implementing the D2 state is to conserve power. As a result, the restore time from D2 to D0 typically exceeds that from D1 to D0. In the D2 state, for example, reduced power on the bus might cause a device to turn off some of its functionality, thus requiring additional time to restart and restore the device.

Many classes of device do not define this state.

### <a href="" id="d3"></a>Device Power State D3

D3 is the lowest-powered device low-power state. All devices must support this state.

Starting with Windows 8, the operating system subdivides D3 into two separate and distinct substates, D3hot and D3cold. Earlier versions of Windows define the D3 state, but not the D3hot and D3cold substates. However, all versions of the [PCI Bus Power Management Interface Specification](http://www.pcisig.com/specifications/conventional/) define separate D3hot and D3cold substates, and versions 4 and later of the [Advanced Configuration and Power Interface Specification](http://go.microsoft.com/fwlink/p/?linkid=57185) define D3hot and D3cold substates.

Although versions of Windows before Windows 8 do not explicitly define the D3hot and D3cold substates of D3, these substates exist implicitly in these earlier versions of Windows. A device is implicitly in the D3hot substate if the device is explicitly in the D3 state, and the computer is in the S0 system power state. In D3hot, a device is connected to a power source (although the device might be configured to draw low current), and the presence of the device on the bus can be detected. A device is implicitly in the D3cold substate if it is explicitly in the D3 state, and the computer is in a low-power Sx state (a state other than S0). In this implicit D3cold substate, the device might receive a trickle current, but the device and the computer are effectively turned off until a wake event occurs.

Starting with Windows 8, a device can enter and leave the D3cold substate while the computer remains in the S0 state. To support this new behavior, D3hot and D3cold must be explicitly defined as distinct substates of D3.

D3hot is the only substate of D3 that the device can enter directly from D0. A device makes a transition from D0 to D3hot under software control by the device driver. In D3hot, the device can be detected on the bus that it connects to. The bus must remain in the D0 state while the device is in the D3hot substate. From D3hot, the device can either return to D0 or enter D3cold. D3cold can be entered only from D3hot.

D3cold is a substate of D3 in which the device is physically connected to the bus but the presence of the device on the bus cannot be detected (that is, until the device is turned on again). In D3cold, one or both of the following is true:

-   The bus that the device connects to is in a low-power state.
-   The device is in a low-power state in which the device does not respond when the bus driver tries to detect its presence on the bus.

The transition from D3hot to D3cold occurs with no device driver interaction. Instead, the device driver indicates whether it is prepared for a D3cold transition before it initiates the transition from D0 to D3hot. Subsequently, a transition from D3hot to D3cold may or may not occur, depending on whether all of the conditions are right to enable this transition.

Two such conditions are that all of the devices that use the same power source are in D3hot and are prepared for a D3cold transition. When the last of these devices enters D3hot, the parent bus driver or ACPI filter driver turns off the power source to these devices, which is to say that the devices enter D3cold.

A device that is in D3cold can leave this substate only by entering D0. There is no direct transition from D3cold to D3hot.

When the computer is in the S0 state and a device enters the D3hot substate, the device driver is typically unable to determine in advance whether the device's next transition will be to D3cold or D0. The one exception is when the computer is preparing to leave the S0 state. In this case, the next transition is to D3cold.

The following sections describe D3hot and D3cold:

-   [D3hot substate](#d3hot)
-   [D3cold substate](#d3cold)

For more information, see [Supporting D3cold in a Driver](supporting-d3cold-in-a-driver.md).

### <a href="" id="d3hot"></a>D3hot substate

D3hot has the following characteristics:

<a href="" id="power-consumption"></a>*Power consumption*  
Power is mostly removed from the device, but not from the computer as a whole. The computer, which is in the S0 state, might continue running in this state, or it might be preparing to move from S0 to a low-power Sx state.

<a href="" id="device-context"></a>*Device context*  
The device driver is solely responsible for restoring device context. The driver must preserve and then restore all device context or must reinitialize the device upon transition to the D0 state.

<a href="" id="device-driver-behavior"></a>*Device driver behavior*  
The device driver is solely responsible for restoring device context, typically from the most recent working configuration.

<a href="" id="restore-time"></a>*Restore time*  
Total restore time is the highest of any of the device power states, except for D3cold, but is typically not much greater than the restore time from D2.

<a href="" id="wake-up-capability"></a>*Wake-up capability*  
A device in the D3hot substate may or may not be able to request wake-up. To supply information about whether this substate can support a wake signal, a bus driver uses the [**DEVICE\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff543095) structure or, starting with Windows 8, the [GUID\_D3COLD\_SUPPORT\_INTERFACE](https://msdn.microsoft.com/library/windows/hardware/hh967714) driver interface.

In D3hot, only minimal trickle current is available. Drivers and hardware must be prepared for the absence of power. The specification for a bus that supports D3hot typically provides detailed requirements for power sources that can be used in this state. To return the device to the working state, the device's drivers must be able to restore and reinitialize the device without depending on the BIOS to run any code in the option ROM that might be available for the device.

The parent bus driver will not remove system power from the parent bus of any device that enters D3hot unless the computer as a whole transitions to the S0 state.

All classes of device define the D3hot substate.

### <a href="" id="d3cold"></a>D3cold substate

D3cold has the following characteristics:

<a href="" id="power-consumption"></a>*Power consumption*  
Power has been fully removed from the device and possibly from the entire system. The device may be able to draw current from side-band sources, depending on its construction.

<a href="" id="device-context"></a>*Device context*  
The device driver is solely responsible for restoring device context. The driver must preserve and then restore device context or must reinitialize the device upon transition to the D0 state.

<a href="" id="device-driver-behavior"></a>*Device driver behavior*  
The device driver is solely responsible for restoring device context, typically from the most recent working configuration.

<a href="" id="restore-time"></a>*Restore time*  
Total restore time is the highest of any of the device power states.

<a href="" id="wake-up-capability"></a>*Wake-up capability*  
In the D3cold substate, a device might be able to trigger a wake signal to wake a sleeping computer. This capability is reported in the [**DEVICE\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff543095) structure and, starting with Windows 8, by the [*GetIdleWakeInfo*](https://msdn.microsoft.com/library/windows/hardware/hh967712) routine in the [GUID\_D3COLD\_SUPPORT\_INTERFACE](https://msdn.microsoft.com/library/windows/hardware/hh967714) driver interface. After the signal wakes the computer, the device driver initiates the device's transition from D3cold to D0. For more information, see the following remarks.

Starting with Windows 8, a device in the D3cold substate might be able to trigger a wake signal to a computer that is in the S0 system power state. This capability is reported by the *GetIdleWakeInfo* routine. The **DEVICE\_CAPABILITIES** structure does not contain information about this capability. After the wake signal arrives, the device driver initiates the device's transition from D3cold to D0. In this case, the computer is awake when the signal arrives, and only the device needs to wake.

In many existing hardware platforms, a device that is in a low-power Dx state can trigger a wake signal to wake a sleeping computer. However, the same device might not be able to trigger a wake signal if the computer is running in the S0 state. Thus, the driver for this device must not initiate the device's transition from D0 to a low-power Dx state when the computer is in the S0 state. Otherwise, after the device leaves D0, it will be unavailable until the computer leaves the S0 state. This device should leave the D0 state only when the computer is preparing to leave the S0 state.

If a device that is in a low-power Dx state can trigger a wake signal to a computer that is running in the S0 state, the device is not required to remain in D0 when the computer is in S0. If the computer is in S0, and the device is in D0 but is idle, the driver can arm the device to trigger a wake signal, and then initiate the device's transition from D0 to this low-power Dx state.

Some classes of device define the D3cold substate.

For more information, see [Supporting D3cold in a Driver](supporting-d3cold-in-a-driver.md).

 

 




