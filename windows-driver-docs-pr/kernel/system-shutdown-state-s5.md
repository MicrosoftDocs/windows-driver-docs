---
title: System Shutdown State S5
author: windows-driver-content
description: System Shutdown State S5
MS-HAID:
- 'PwrMgmt\_a73ceed5-59d6-4b69-9525-e49e1fe09192.xml'
- 'kernel.system\_shutdown\_state\_s5'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: c08d688d-c31a-4d57-a343-406edfa35e8f
keywords: ["S5 WDK power management", "system shutdown states WDK power management", "software resumption WDK power management", "resumption WDK power management", "hardware latency WDK power management", "system hardware context WDK power management", "hardware context WDK power management", "context WDK power management", "latency WDK power management", "system power states WDK kernel , shutdown state", "shutdown states WDK power management"]
---

# System Shutdown State S5


## <a href="" id="ddk-system-shutdown-state-s5-kg"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20System%20Shutdown%20State%20S5%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


