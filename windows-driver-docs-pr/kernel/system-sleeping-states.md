---
title: System Sleeping States
author: windows-driver-content
description: System Sleeping States
MS-HAID:
- 'PwrMgmt\_62c3fe62-0434-43e7-bea2-dcf121b54ce3.xml'
- 'kernel.system\_sleeping\_states'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 2fd883b5-4e89-4ce9-b75a-b821348ac860
keywords: ["system power states WDK kernel , sleeping states", "system sleeping states WDK power management", "sleeping states WDK power management", "S1 WDK power management", "S2 WDK power management", "S3 WDK power management", "S4 WDK power management", "software resumption WDK power management", "resumption WDK power management", "hardware latency WDK power management", "system hardware context WDK power management", "hardware context WDK power management", "context WDK power management", "latency WDK power management"]
---

# System Sleeping States


## <a href="" id="ddk-system-sleeping-states-kg"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20System%20Sleeping%20States%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


