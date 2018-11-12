---
title: Live Local Debugging
description: Live Local Debugging
ms.assetid: ec76a71e-f173-4b66-beaf-d57a1c991acd
keywords: ["kernel streaming debugging, live local debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Live Local Debugging


In Microsoft Windows XP and later operating systems, it is possible to do local kernel debugging by starting the kernel debugger (KD) or WinDbg with the **-kl** command line option:

```console
kd [-y SymbolPath] -kl 
```

or

```console
windbg [-y SymbolPath] -kl 
```

In Windows Vista and later, local kernel debugging requires the computer to be booted with the **/debug** option. Open a Command Prompt Window as Administrator, and enter **bcdedit /debug on**. Reboot the computer.

> [!IMPORTANT]
> Before using BCDEdit to change boot information you may need to temporarily suspend Windows security features such as BitLocker and Secure Boot on the test PC.
> Re-enable these security features when testing is complete and appropriately manage the test PC, when the security features are disabled.

In Windows Vista and later, local kernel debugging requires the debugger to be run as Administrator.

Live local debugging is extremely useful for debugging issues that are difficult to reproduce when the debugger is attached; however, anything that requires knowledge of time sensitive information, including packet, IRP, and SRB data, is unlikely to work unless the problem is a hang or a stall.

When performing local debugging, consider the following variables:

-   **Overall states.** For example, is the stream running? Is the stream paused?

-   **Packet counts.** For example, are there IRPs queued to the stream?

-   **Changes in packet counts.** Is the stream moving?

-   **Changes in packet lists.**

-   **Hung kernel threads.**

Consider the last of these.

### <span id="examining_a_hung_thread_in_lkd"></span><span id="EXAMINING_A_HUNG_THREAD_IN_LKD"></span>Examining a Hung Thread in LKD

First, use the [**!process 0 0**](-process.md) extension to identify the process containing the hung thread. Then, issue **!process** again for more information about that thread:

```dbgcmd
lkd> !process 816a550 7
        THREAD 81705da8  Cid 0b5c.0b60  Teb: 7ffde000 Win32Thread: e1b2d890 WAIT: (Suspended)
        IRP List:
            816c9ad8: (0006,0190) Flags: 00000030  Mdl: 00000000
        Start Address kernel32!BaseProcessStartThunk (0x77e5c650)
        Win32 Start Address 0x0101c9be
        Stack Init f50bf000 Current f50bea74 Base f50bf000 Limit f50b9000 Call 0
        Priority 10 BasePriority 8 PriorityDecrement 0
```

The threads are not displayed, but the stack addresses are. Using the [**dds**](dds--dps--dqs--display-words-and-symbols-.md) (or **ddq**) command on the current address on the stack yields a starting point for further investigation, because it specifies which process is calling.

```dbgcmd
lkd> dds f50bea74
f50bea74  f50bebc4
f50bea78  00000000
f50bea7c  80805795 nt!KiSwapContext+0x25
f50beab4  8080ece0 nt!KeWaitForSingleObject
f50beabc  f942afda ks!CKsQueue::CancelAllIrps+0x14
f50bead8  f94406c4 ks!CKsQueue::SetDeviceState+0x170
f50beb00  f943f6f1 ks!CKsPipeSection::DistributeDeviceStateChange+0x1d
f50beb24  f943fb1e ks!CKsPipeSection::SetDeviceState+0xb2
```

 

 





