---
title: Bluetooth Core Driver Layer and Supported Power Transitions
description: The following table summarizes device and system power states that the Bluetooth core driver supports.
ms.date: 04/20/2017
---

# Bluetooth Core Driver Layer and Supported Power Transitions

The following table summarizes device and system power states that the Bluetooth core driver supports. A "sleep" state is used throughput this section and its subtopics to describe a very low power state in which the Bluetooth radio’s internal settings and configurations are persistent.

## Device Power States

| System power states | Device power state D0 | Device power state D2 | Device power state D3 |
|----|----|----|----|
| | D0 (Active) | D2 (sleep) – some power is maintained to the Bluetooth chip for persisting its internal state. | D3 (Off) - Power is removed (*) |
| S0 (Active) | Active | Sleep if armed for wake | Radio RM off |
| S1 | N/A | N/A | N/A |
| S2 | N/A | N/A | N/A |
| S3 (Sleep) | N/A | Sleep if armed for wake | Can be powered off |
| S4 (Hibernate) | N/A | Sleep if armed for wake | Can be powered off |
| S5 (Off) | N/A | N/A | Can be powered off |

\*Re-initialization by Bluetooth core driver is required since power is lost to the Bluetooth chip

Guidelines for system state support for SoC systems:

- S0 (on) and S5 (shutdown) support is required for all SoCs
- S4 (hibernation) is required for x86-based SoCs
- Systems that support Connected Standby do not support S3

## Active (S0/D0)

This is the state when a client application is actively using Bluetooth functionality.

## Low Duty Cycle/Sleep (S0/D2)

This is the most common state in which the system is effectively on (in S0), but the driver is in the D2 state – the controller is throttled down to a lower power state. While in this state, a controller can resume to the active state (D0) rather quickly without affecting the end-user experience.

An example of this state can be demonstrated by using a Bluetooth keyboard. When no keys are pressed for a few seconds, the Bluetooth core layer throttles to D2 to notify and allow the controller to enter an idle state while maintaining a connection in sniff mode to reduce power consumption. Upon a key press, the radio will receive a wake notification and trigger a wake event for the Bluetooth core driver to resume to D0 and then read the incoming data.

Another example is in the initial condition when there are no associations – the Bluetooth core stack can enter D2 to notify and allow the Bluetooth radio to throttle down to a sleep state. The power consumption of the radio is optimized while persistent non-volatile settings can quickly resume when the user intends to associate with a remote Bluetooth device.

Common and critical scenarios in this state:

1. Have no associations (i.e. no pairings with Bluetooth devices)
2. Have an association, be connected but in idle
3. Have an association but be disconnected

Later subtopic provide further details on the mechanisms of entering idle and resuming to active. This state also becomes the primary state in an AOAC (Always On Always Connected) system.

## System is On but Device is Off (S0/D3)

This state is currently only supported for Radio Management when the radio is in "off" mode. The state will incur a longer latency to restore a Bluetooth controller to its active state where the process includes but is not limited to device level initialization and configuration, as well as host and device initialization by the Bluetooth core driver.

## System Remote Wake-able (Sx/D2)

The support for this Sx remains unchanged for Windows 8.1, and this particular state is used to enable waking the system from a HID device. While in D2, the Bluetooth chip continues to have power so its internal volatile settings and configuration remain persistent. This capability is optional.

## System Off (Sx/D3)

The system is off, and the Bluetooth radio is assumed to be off or in a low power state. In some Sx states (except shutdown), the driver stack is still in memory (i.e. it remains loaded).

## Radio Management

Going forward, Radio Management (RM) will be standardized for Bluetooth 4.0 radios. The Bluetooth stack will send down an HCI\_RESET command, which the radio is expected to respond by putting the radio in no transmission mode and the device in D3 power state. The stack will then surprise remove all child devnodes, effectively putting the radio in "airplane" mode. The serial bus driver will stay loaded while in the Radio off state, so it can receive a request from the stack to turn the radio back on. The inbox stack will handle the re-enumeration of devnodes. For more details on implementation of radio management, please refer to the [Bluetooth Software Radio Switch Function Prototypes](bluetooth-software-radio-switch-function-prototypes.md).
