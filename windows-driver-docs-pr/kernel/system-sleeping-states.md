---
title: System Sleeping States
description: System Sleeping States
ms.assetid: 2fd883b5-4e89-4ce9-b75a-b821348ac860
keywords: ["system power states WDK kernel , sleeping states", "system sleeping states WDK power management", "sleeping states WDK power management", "S1 WDK power management", "S2 WDK power management", "S3 WDK power management", "S4 WDK power management", "software resumption WDK power management", "resumption WDK power management", "hardware latency WDK power management", "system hardware context WDK power management", "hardware context WDK power management", "context WDK power management", "latency WDK power management"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# System Sleeping States





States S1, S2, S3, and S4 are the sleeping states. A system in one of these states is not performing any computational tasks and appears to be off. Unlike a system in the shutdown state (S5), however, a sleeping system retains memory state, either in the hardware or on disk. The operating system need not be rebooted to return the computer to the working state.

Some devices can wake the system from a sleeping state when certain events occur, such as an incoming call to a modem. In addition, on some computers, an external indicator tells the user that the system is merely sleeping.

With each successive sleep state, from S1 to S4, more of the computer is shut down. All ACPI-compliant computers shut off their processor clocks at S1 and lose system hardware context at S4 (unless a hibernate file is written before shutdown), as listed in the sections below. Details of the intermediate sleep states can vary depending on how the manufacturer has designed the machine. For example, on some machines certain chips on the motherboard might lose power at S3, while on others such chips retain power until S4. Furthermore, some devices might be able to wake the system only from S1 and not from deeper sleep states.

### System Power State S1

System power state S1 is a sleeping state with the following characteristics:

<a href="" id="power-consumption"></a>**Power consumption**  
Less consumption than in S0 and greater than in the other sleep states. Processor clock is off and bus clocks are stopped.

<a href="" id="software-resumption"></a>**Software resumption**  
Control restarts where it left off.

<a href="" id="hardware-latency"></a>**Hardware latency**  
Typically no more than two seconds.

<a href="" id="system-hardware-context"></a>**System hardware context**  
All context retained and maintained by hardware.

### System Power State S2

System power state S2 is similar to S1 except that the CPU context and contents of the system cache are lost because the processor loses power. State S2 has the following characteristics:

<a href="" id="power-consumption"></a>**Power consumption**  
Less consumption than in state S1 and greater than in S3. Processor is off. Bus clocks are stopped; some buses might lose power.

<a href="" id="software-resumption"></a>**Software resumption**  
After wake-up, control starts from the processor's reset vector.

<a href="" id="hardware-latency"></a>**Hardware latency**  
Two seconds or more; greater than or equal to the latency for S1.

<a href="" id="system-hardware-context"></a>**System hardware context**  
CPU context and system cache contents are lost.

### System Power State S3

System power state S3 is a sleeping state with the following characteristics:

<a href="" id="power-consumption"></a>**Power consumption**  
Less consumption than in state S2. Processor is off and some chips on the motherboard also might be off.

<a href="" id="software-resumption"></a>**Software resumption**  
After the wake-up event, control starts from the processor's reset vector.

<a href="" id="hardware-latency"></a>**Hardware latency**  
Almost indistinguishable from S2.

<a href="" id="system-hardware-context"></a>**System hardware context**  
Only system memory is retained. CPU context, cache contents, and chipset context are lost.

### System Power State S4

System power state S4, the hibernate state, is the lowest-powered sleeping state and has the longest wake-up latency. To reduce power consumption to a minimum, the hardware powers off all devices. Operating system context, however, is maintained in a hibernate file (an image of memory) that the system writes to disk before entering the S4 state. Upon restart, the loader reads this file and jumps to the system's previous, prehibernation location.

If a computer in state S1, S2, or S3 loses all AC or battery power, it loses system hardware context and therefore must reboot to return to S0. A computer in state S4, however, can restart from its previous location even after it loses battery or AC power because operating system context is retained in the hibernate file. A computer in the hibernate state uses no power (with the possible exception of trickle current).

State S4 has the following characteristics:

<a href="" id="power-consumption"></a>**Power consumption**  
Off, except for trickle current to the power button and similar devices.

<a href="" id="software-resumption"></a>**Software resumption**  
System restarts from the saved hibernate file. If the hibernate file cannot be loaded, rebooting is required. Reconfiguring the hardware while the system is in the S4 state might result in changes that prevent the hibernate file from loading correctly.

<a href="" id="hardware-latency"></a>**Hardware latency**  
Long and undefined. Only physical interaction returns the system to the working state. Such interaction might include the user pressing the ON switch or, if the appropriate hardware is present and wake-up is enabled, an incoming ring for the modem or activity on a LAN. The machine can also awaken from a resume timer if the hardware supports it.

<a href="" id="system-hardware-context"></a>**System hardware context**  
None retained in hardware. The system writes an image of memory in the hibernate file before powering down. When the operating system is loaded, it reads this file and jumps to its previous location.

 

 




