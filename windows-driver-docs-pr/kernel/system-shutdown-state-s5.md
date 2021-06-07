---
title: System Shutdown State S5
description: System Shutdown State S5
keywords: ["S5 WDK power management", "system shutdown states WDK power management", "software resumption WDK power management", "resumption WDK power management", "hardware latency WDK power management", "system hardware context WDK power management", "hardware context WDK power management", "context WDK power management", "latency WDK power management", "system power states WDK kernel , shutdown state", "shutdown states WDK power management"]
ms.date: 06/07/2021
ms.localizationpriority: medium
ms.custom: contperf-fy21q4
---

# System Shutdown State S5


System power state S5 is the shutdown or off state. Similar to a system in a sleeping state (S1 through S4), a system in S5 is not performing any computational tasks and appears to be off. Unlike S1-S4, however, a system in S5 does not retain memory state.

When in state S4, the computer can restart from the hibernate file; restarting from state S5 requires rebooting the system.

State S5 has the following characteristics:

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Power consumption** | Off, except for trickle current to devices such as the power button. |
| **Software resumption** | Boot is required upon awakening. |
| **Hardware latency** | Long and undefined. Only physical interaction, such as the user pressing the ON switch, returns the system to the working state. The BIOS can also awaken from a resume timer if the system is so configured. |
| **System hardware context** | None retained. |

For a comparison between system power states and more info on S5, see [System Power States](/windows/win32/power/system-power-states).

For info on S1-S4, see [System Sleeping States](/windows-hardware/drivers/kernel/system-sleeping-states).

