---
title: Power Management
description: Power Management
keywords:
- power management WDK printer
- critical shutdowns WDK printer
- shutdown power management WDK printer
- standby tests WDK printer
- hibernate tests WDK printer
ms.date: 01/30/2023
---

# Power Management

[!include[Print Support Apps](../includes/print-support-apps.md)]

Some of the most common failures of a port-connected device occur when the system is cycled through various sleep states and the device fails to correctly set device power states or to return from various device power states. A system should always act as if it was started from a completely powered-off state ("cold boot"). Special behavior that is unique to entering or waking from a sleep state is most likely a bug.

Follow these basic rules to make sure your device is working correctly.

1. Devices, ports, and their drivers should not block or prevent the system from entering a sleep state.

1. A print job in progress should not block a request to go to a lower power state.

1. When the system wakes from a sleep state, any print jobs that were in progress when the lower power state was initiated should resume gracefully.

1. Critical shutdown requests will override any attempts to veto a change in power state.

For more information, see [System Power States](../kernel/system-power-states.md).

## Testing Port-Connected Devices Across Various Power States

To begin testing a device before and after various power states, first verify the device's baseline [Plug and Play](../kernel/introduction-to-plug-and-play.md) (PnP) functionality. Next, verify that your test environment can enter and wake from all power states.

With one device connected and installed correctly, test its behavior before and after each power state S0 through S5 as follows:

- **Standby Test (S1 - S3)**

    1. Enter and wake from the Standby state with the device attached and no jobs in progress. The system should gracefully enter each Sleep and Wake state.

    1. Verify that the device functions properly both before and after entering the Sleep state. Repeat the same test without the device installed.

    1. Try installing the device after waking from the Standby state. The device should install successfully.

    1. Verify entering and waking from Standby with print jobs in progress. Jobs in progress should resume upon waking.

    1. Verify that the job can be canceled, recovered from, and restarted after entering and waking from the Standby state.

    1. Put the device into each of the error states described in [Device Error States](device-error-states.md). Verify that the job can be canceled, recovered from, and restarted after entering and waking from the Standby state.

- **Hibernate Test (S4)**

    1. Enter and wake from the Hibernate state with the device attached and no jobs in progress. The system should gracefully enter each Sleep and Wake state.

    1. Verify that the device functions properly both before and after entering the Sleep state. Repeat the same test without the device installed.

    1. Try installing the device after waking from the Hibernate state. The device should install successfully.

    1. Verify entering and waking from the Hibernate state with print jobs in progress. Jobs in progress should resume upon waking.

    1. Put the device into each of the error states described in [Device Error States](device-error-states.md). Verify that the job can be canceled, recovered from, and restarted after entering and then waking from the Hibernate state.

- **Shutdown/Restart (S5)**

    1. Shut down the system while the device is attached and no jobs are in progress. The system should gracefully shut down.

    1. Verify that the device functions properly both before and after system shutdown. Repeat the same test without the device installed.

    1. Try installing the device after you shut down and then restart the system.

    1. Shut down and restart the system with print jobs in progress. Jobs in progress should resume upon restart.

    1. Put the device into each of the error states described in [Device Error States](device-error-states.md). Verify that the job can be canceled, recovered from, and restarted after returning from a system shutdown or restart. Print jobs in an error state should remain in the queue through shutdown or restart, and the print job should resume after the error state is cleared after shutdown or restart.

- **Critical Shutdown**

    1. The computer can be in any of the above active power states (S0-S4) when a critical shutdown event can be requested (for example, when a critical battery level has been reached). Verify that the device functions properly both before and after a critical shutdown event. Repeat the same test without the device installed.

    1. Try installing the device after the critical shutdown event.

    1. Test for the condition in which devices are in use when a critical shutdown event is initiated by the power manager, and the device driver does not veto the Sleep state.

    1. With a print job in progress, initiate a critical shutdown event. When the system wakes, the print job should restart and recover gracefully.

    1. Put the device into each of the error states described in [Device Error States](device-error-states.md). Verify that the job can be canceled, recovered from, and restarted after returning from a critical shutdown event. Print jobs in an error state should remain in the queue through shutdown or restart, and the print job should resume after the error state is cleared after shutdown or restart.

    1. With the device installed and idle, use the **Power Options** application, obtained from Control Panel, to start a system sleep state. Verify that the system enters the appropriate Sleep state at the given time. Repeat this test without the device installed, and verify that the device can be installed after the system wakes.
