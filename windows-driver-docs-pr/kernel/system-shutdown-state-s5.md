---
title: System Shutdown State S5
description: System Shutdown State S5
ms.assetid: c08d688d-c31a-4d57-a343-406edfa35e8f
keywords: ["S5 WDK power management", "system shutdown states WDK power management", "software resumption WDK power management", "resumption WDK power management", "hardware latency WDK power management", "system hardware context WDK power management", "hardware context WDK power management", "context WDK power management", "latency WDK power management", "system power states WDK kernel , shutdown state", "shutdown states WDK power management"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# System Shutdown State S5





In the S5, or shutdown, state, the machine has no memory state and is not performing any computational tasks.

The only difference between states S4 and S5 is that the computer can restart from the hibernate file in state S4, while restarting from state S5 requires rebooting the system.

State S5 has the following characteristics:

<a href="" id="power-consumption"></a>**Power consumption**  
Off, except for trickle current to devices such as the power button.

<a href="" id="software-resumption"></a>**Software resumption**  
Boot is required upon awakening.

<a href="" id="hardware-latency"></a>**Hardware latency**  
Long and undefined. Only physical interaction, such as the user pressing the ON switch, returns the system to the working state. The BIOS can also awaken from a resume timer if the system is so configured.

<a href="" id="system-hardware-context"></a>**System hardware context**  
None retained.

 

 




