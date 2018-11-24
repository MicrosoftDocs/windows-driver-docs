---
title: Bluetooth Core Driver Layer and Supported Power Transitions
description: The following table summarizes device and system power states that the Bluetooth core driver supports.
ms.assetid: 25A3598E-51A7-4B16-92F7-9D2F39177946
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Bluetooth Core Driver Layer and Supported Power Transitions


The following table summarizes device and system power states that the Bluetooth core driver supports. A "sleep" state is used throughput this section and its subtopics to describe a very low power state in which the Bluetooth radio’s internal settings and configurations are persistent.

<table>
    <tr>
        <td></td>
        <td></td>
        <td colspan="3"><b>Device Power States</b></td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td>D0 (Active)</td>
        <td>D2 (sleep) – some power is maintained to the Bluetooth chip for persisting its internal state</td>
        <td>D3 (Off) - Power is removed (*)</td>
    </tr>
    <tr>
        <td rowspan="6"><b>System power states</b></td>
        <td>S0 (Active)</td>
        <td>Active</td>
        <td>Sleep if armed for wake</td>
        <td>Radio RM off</td>
    </tr>
    <tr>
        <td>S1</td>
        <td>N/A</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
       <td>S2</td>
        <td>N/A</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td>S3 (Sleep)</td>
        <td>N/A</td>
        <td>Sleep if armed for wake</td>
        <td>Can be powered off</td>
    </tr>
    <tr>
        <td>S4 (Hibernate)</td>
        <td>N/A</td>
        <td>Sleep if armed for wake</td>
        <td>Can be powered off</td>
    </tr>
    <tr>
        <td>S5 (Off)</td>
        <td>N/A</td>
        <td>N/A</td>
        <td>Can be powered off</td>
    </tr>
</table>



\*Re-initialization by Bluetooth core driver is required since power is lost to the Bluetooth chip

Guidelines for system state support for SoC systems:

-   S0 (on) and S5 (shutdown) support is required for all SoCs
-   S4 (hibernation) is required for x86-based SoCs
-   Systems that support Connected Standby do not support S3

## <span id="Active__S0_D0_"></span><span id="active__s0_d0_"></span><span id="ACTIVE__S0_D0_"></span>Active (S0/D0)


This is the state when a client application is actively using Bluetooth functionality.

## <span id="Low_Duty_Cycle_Sleep__S0_D2_"></span><span id="low_duty_cycle_sleep__s0_d2_"></span><span id="LOW_DUTY_CYCLE_SLEEP__S0_D2_"></span>Low Duty Cycle/Sleep (S0/D2)


This is the most common state in which the system is effectively on (in S0), but the driver is in the D2 state – the controller is throttled down to a lower power state. While in this state, a controller can resume to the active state (D0) rather quickly without affecting the end-user experience.

An example of this state can be demonstrated by using a Bluetooth keyboard. When no keys are pressed for a few seconds, the Bluetooth core layer throttles to D2 to notify and allow the controller to enter an idle state while maintaining a connection in sniff mode to reduce power consumption. Upon a key press, the radio will receive a wake notification and trigger a wake event for the Bluetooth core driver to resume to D0 and then read the incoming data.

Another example is in the initial condition when there are no associations – the Bluetooth core stack can enter D2 to notify and allow the Bluetooth radio to throttle down to a sleep state. The power consumption of the radio is optimized while persistent non-volatile settings can quickly resume when the user intends to associate with a remote Bluetooth device.

Common and critical scenarios in this state:

1.  Have no associations (i.e. no pairings with Bluetooth devices)
2.  Have an association, be connected but in idle
3.  Have an association but be disconnected

Later subtopic provide further details on the mechanisms of entering idle and resuming to active. This state also becomes the primary state in an AOAC (Always On Always Connected) system.

## <span id="System_is_On_but_Device_is_Off__S0_D3_"></span><span id="system_is_on_but_device_is_off__s0_d3_"></span><span id="SYSTEM_IS_ON_BUT_DEVICE_IS_OFF__S0_D3_"></span>System is On but Device is Off (S0/D3)


This state is currently only supported for Radio Management when the radio is in "off" mode. The state will incur a longer latency to restore a Bluetooth controller to its active state where the process includes but is not limited to device level initialization and configuration, as well as host and device initialization by the Bluetooth core driver.

## <span id="System_Remote_Wake-able__Sx_D2_"></span><span id="system_remote_wake-able__sx_d2_"></span><span id="SYSTEM_REMOTE_WAKE-ABLE__SX_D2_"></span>System Remote Wake-able (Sx/D2)


The support for this Sx remains unchanged for Windows 8.1, and this particular state is used to enable waking the system from a HID device. While in D2, the Bluetooth chip continues to have power so its internal volatile settings and configuration remain persistent. This capability is optional.

## <span id="System_Off__Sx_D3__"></span><span id="system_off__sx_d3__"></span><span id="SYSTEM_OFF__SX_D3__"></span>System Off (Sx/D3)


The system is off, and the Bluetooth radio is assumed to be off or in a low power state. In some Sx states (except shutdown), the driver stack is still in memory (i.e. it remains loaded).

## <span id="Radio_Management"></span><span id="radio_management"></span><span id="RADIO_MANAGEMENT"></span>Radio Management


Going forward, Radio Management (RM) will be standardized for Bluetooth 4.0 radios. The Bluetooth stack will send down an HCI\_RESET command, which the radio is expected to respond by putting the radio in no transmission mode and the device in D3 power state. The stack will then surprise remove all child devnodes, effectively putting the radio in "airplane" mode. The serial bus driver will stay loaded while in the Radio off state, so it can receive a request from the stack to turn the radio back on. The inbox stack will handle the re-enumeration of devnodes. For more details on implementation of radio management, please refer to the [Bluetooth Software Radio Switch Function Prototypes](https://msdn.microsoft.com/library/windows/hardware/hh450832).

 

 





