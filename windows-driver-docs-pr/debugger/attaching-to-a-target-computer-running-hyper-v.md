---
title: Attaching to a Target Computer Running Hyper-V
description: Attaching to a Target Computer Running Hyper-V
ms.assetid: 379ebaf6-0599-41df-a57a-03a133ea0b02
keywords: ["Hyper-V debugging", "Windows hypervisor debugging", "hypervisor debugging", "root partition", "parent partition", "guest partition", "child partition"]
---

# Attaching to a Target Computer Running Hyper-V


## <span id="ddk_controlling_the_user_mode_debugger_from_the_kernel_debugger_dbg"></span><span id="DDK_CONTROLLING_THE_USER_MODE_DEBUGGER_FROM_THE_KERNEL_DEBUGGER_DBG"></span>


Windows Server 2008 Hyper-V is a virtualization platform that enables multiple operating systems to run on a single computer. Each operating system runs in an isolated virtual space known as a *partition*. The first partition, known as the *root partition* or *parent partition*, must run Windows Server 2008 or a later version of Windows. The other partitions, known as *guest partitions* or *child partitions*, may run other operating systems. Windows hypervisor, a component of Hyper-V, runs as a thin layer between these partitions and the hardware.

Debugging Tools for Windows supports kernel debugging of the root partition, as well as kernel debugging of Windows hypervisor itself. This debugging can be done across a null-modem cable or a 1394 connection.

The procedures used to perform this debugging are described in the following sections:

[Debugging Hyper-V via a Null-modem Cable Connection](debugging-hyper-v-via-a-null-modem-cable-connection.md)

[Debugging Hyper-V via a 1394 Cable Connection](debugging-hyper-v-via-a-1394-cable-connection.md)

[Troubleshooting Hyper-V Debugging](troubleshooting-hyper-v-debugging.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Attaching%20to%20a%20Target%20Computer%20Running%20Hyper-V%20%20RELEASE:%20%284/24/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




