---
title: Attaching to a Target Computer Running Hyper-V
description: Attaching to a Target Computer Running Hyper-V
ms.assetid: 379ebaf6-0599-41df-a57a-03a133ea0b02
keywords: ["Hyper-V debugging", "Windows hypervisor debugging", "hypervisor debugging", "root partition", "parent partition", "guest partition", "child partition"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Attaching to a Target Computer Running Hyper-V


## <span id="ddk_controlling_the_user_mode_debugger_from_the_kernel_debugger_dbg"></span><span id="DDK_CONTROLLING_THE_USER_MODE_DEBUGGER_FROM_THE_KERNEL_DEBUGGER_DBG"></span>


Windows Server 2008 Hyper-V is a virtualization platform that enables multiple operating systems to run on a single computer. Each operating system runs in an isolated virtual space known as a *partition*. The first partition, known as the *root partition* or *parent partition*, must run Windows Server 2008 or a later version of Windows. The other partitions, known as *guest partitions* or *child partitions*, may run other operating systems. Windows hypervisor, a component of Hyper-V, runs as a thin layer between these partitions and the hardware.

Debugging Tools for Windows supports kernel debugging of the root partition, as well as kernel debugging of Windows hypervisor itself. This debugging can be done across a null-modem cable or a 1394 connection.

The procedures used to perform this debugging are described in the following sections:

[Debugging Hyper-V via a Null-modem Cable Connection](debugging-hyper-v-via-a-null-modem-cable-connection.md)

[Debugging Hyper-V via a 1394 Cable Connection](debugging-hyper-v-via-a-1394-cable-connection.md)

[Troubleshooting Hyper-V Debugging](troubleshooting-hyper-v-debugging.md)

 

 





