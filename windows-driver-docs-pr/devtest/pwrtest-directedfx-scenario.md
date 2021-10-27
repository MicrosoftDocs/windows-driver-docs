---
title: PwrTest DirectedFx Scenario
description: The PwrTest Directed Power Framework Scenario is designed to test PoFx v3 functionality.
ms.date: 10/27/2021
ms.custom: 19H1
---

# PwrTest DirectedFx Scenario

The PwrTest DirectedFx Scenario is designed to test devices with drivers that use the [Directed Power Management Framework (DFx)](../kernel/introduction-to-the-directed-power-management-framework.md).

The user provides the instance path of the device(s) to test and optionally a device power state to verify.

If no D-state is specified, the test verifies that the device(s) did not stay in D0.  To find the instance path, examine the device's properties in Device Manager.  Alternately, run the test with no options to get a list of the instance paths of all DFx-capable devices on the system.

This test can be run on any [Modern Standby](/windows-hardware/design/device-experiences/modern-standby) system regardless of its network connectivity settings during standby or whether it is on AC or DC power.

For the specified device, the test verifies that:

- The device and any child devices that must be powered down before the parent support DFx.
- The device successfully completes at least one directed power down/up.
- The device enters the correct D-state after completing a directed power down. (optional)

For each cycle, the test shows:

- Time the system was in idle resiliency
 
- Time that Directed [Deepest Runtime Idle Platform State (DRIPS)](/windows-hardware/design/device-experiences/prepare-hardware-for-modern-standby) was disengaged
    - Time each individual reason was active

- Individual statistics and an optional fail reason for all test devices
    - `Device {Test Device} failed because device {Failed Device} {Failed Reason}`.
        - Is either a paging device or the debugging device
        - Does not support DFx
        - Has a constraint on a component
        - Failed its DFx power down call

- Each broadcast tree and all participant devices

Running the test for three cycles is recommended to ensure the device(s) can undergo multiple directed power transitions.  Once all cycles are complete, the test outputs the total number of success/failure cycles.

If no devices on the system support DFx, the test returns `Error retrieving list of available Directed Fx devices`.

## Syntax

```
pwrtest /directedfx [/c:n] [/d:n] [/p:n] [/device(:n):path] [/?] 
```

**/c:**<em>n</em>  
Specifies the number of cycles (1 is the default) to run.

**/d:**<em>n</em>  
Specifies the delay time between cycles (in seconds; 60 is default).

**/p:**<em>n</em>  
Specifies the time to remain in Connected Standby (in seconds; 300 is default).

**/device:**<em>n</em>  
Path supplies the instance path of a device to test.  
N supplies an optional device power state the device should enter due to a Directed Fx transition.

**Examples**

```
pwrtest /directedfx
```

## Related topics

[PwrTest Syntax](pwrtest-syntax.md)

[Introduction to the Directed Power Management Framework](/windows-hardware/drivers/kernel/introduction-to-the-directed-power-management-framework)

[Directed FX System Verification Test](/windows-hardware/test/hlk/testref/def16163-9118-4d4a-b559-37873befa12e)

[PwrTest DirectedFx Scenario](/windows-hardware/drivers/devtest/pwrtest-directedfx-scenario)