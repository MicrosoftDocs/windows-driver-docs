---
title: Debugging an Interrupt Storm
description: Debugging an Interrupt Storm
ms.assetid: b863cb9c-dce0-4572-b0ed-6f7d3a6ba472
keywords: ["pending IRPs", "I/O Request Packet (IRP), pending"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Debugging an Interrupt Storm


## <span id="ddk_debugging_pending_irps_dbg"></span><span id="DDK_DEBUGGING_PENDING_IRPS_DBG"></span>


One of the most common examples of a stalled system is an interrupt storm. An *interrupt storm* is a level-triggered interrupt signal that remains in the asserted state.

The following events can cause an interrupt storm:

-   A hardware device does not release its interrupt signal after being directed to do so by the device driver.

-   A device driver does not instruct its hardware to release the interrupt signal, because it does not detect that the interrupt was initiated from its hardware.

-   A device driver claims the interrupt even though the interrupt was not initiated from its hardware. This situation can only occur when multiple devices are sharing the same IRQ.

-   The edge level control register (ELCR) is not set correctly.

-   Edge and level interrupt-triggered devices share an IRQ (for example, a COM port and a PCI SCSI controller).

This example demonstrates one method for detecting and debugging an interrupt storm.

When the machine hangs, use a kernel debugger to break in. Use the **!irpfind** extension command to look for pending IRPs. Then, use the **!irp** extension to obtain details about any pending IRPs. For example:

```dbgcmd
kd> !irp 81183468 
Irp is active with 2 stacks 2 is current (= 0x811834fc)
 No Mdl Thread 00000000:  Irp stack trace.
     cmd  flg cl Device   File     Completion-Context
 [  0, 0]   0  0 8145f470 00000000 00000000-00000000
               \Driver\E100B
                        Args: 00000000 00000000 00000000 00000000
>[ 16, 2]   0 e1 8145f470 00000000 8047f744-814187a8 Success Error Cancel pending
               \Driver\E100B    ntoskrnl!PopCompleteSystemPowerIrp
                        Args: 00000000 00000000 00000002 00000002 
```

This example shows that \\driver\\e100b has not returned the IRP for **ntoskrnl!PopCompleteSystemPowerIrp**. It appears to be stuck and might be experiencing an interrupt storm.

To investigate, use the **kb** command to request a stack trace. For example:

```dbgcmd
kd> kb
ChildEBP RetAddr  Args to Child
f714ee68 8046355a 00000001 80068c10 00000030 ntoskrnl!RtlpBreakWithStatusInstruction
f714ee68 80067a4f 00000001 80068c10 00000030 ntoskrnl!KeUpdateSystemTime+0x13e
f714eeec 8046380b 01001010 0000003b f714ef00 halacpi!HalBeginSystemInterrupt+0x83
f714eeec 80463c50 01001010 0000003b f714ef00 ntoskrnl!KiChainedDispatch+0x1b
f714ef78 80067cc2 00000000 00000240 8000017c ntoskrnl!KiDispatchInterrupt
f714ef78 80501cb5 00000000 00000240 8000017c halacpi!HalpDispatchInterrupt2ndEnt  
```

Notice that the section in bold is an interrupt dispatch. If you use the **g** command and break in again, you will very likely see a different stack trace, but you will still see an interrupt dispatch. To determine which interrupt is responsible for the system stall, look at the second parameter passed into **HalBeginSystemInterrupt** (in this case, 0x3B). The standard rule is that the interrupt vector displayed (0x3B) is the IRQ line plus 0x30, so the interrupt is number 0xB. Running another stack trace may provide more information about which device issued the interrupt service request (ISR). In this case, a second stack trace has the following result:

```dbgcmd
kd> kb
ChildEBP RetAddr  Args to Child
f714ee24 8046355a 00000001 00000010 00000030 ntoskrnl!RtlpBreakWithStatusInstruction
f714ee24 bfe854b9 00000001 00000010 00000030 ntoskrnl!KeUpdateSystemTime+0x13e
f714eed8 f7051796 00000000 80463850 8143ec88 atimpab!AtiInterrupt+0x109
f714eee0 80463850 8143ec88 81444038 8046380b VIDEOPRT!pVideoPortInterrupt+0x16
f714eef8 80463818 00000202 0000003b 80450bb8 ntoskrnl!KiChainedDispatch2ndLvl+0x28
f714eef8 80463c50 00000202 0000003b 80450bb8 ntoskrnl!KiChainedDispatch+0x28
f714ef78 80067cc2 00000000 00000240 8000017c ntoskrnl!KiDispatchInterrupt
f714ef78 80501cb5 00000000 00000240 8000017c halacpi!HalpDispatchInterrupt2ndEntry+0x1b
f714f084 8045f744 f714f16c 00020019 f714f148 ntoskrnl!NtCreateKey+0x113
f714f084 8042e487 f714f16c 00020019 f714f148 ntoskrnl!KiSystemService+0xc4
f714f118 804ab556 f714f16c 00020019 f714f148 ntoskrnl!ZwCreateKey+0xb
f714f184 8041f75b f714f1e8 8000017c f714f1d0 ntoskrnl!IopCreateRegistryKeyEx+0x4e
f714f204 804965cd 8145f630 00000000 00000001 ntoskrnl!IopProcessSetInterfaceState+0x93
f714f220 bfee1eb9 8145f630 00000000 8145f5a0 ntoskrnl!IoSetDeviceInterfaceState+0x2b
f714f254 bfedb416 00000004 00000800 0045f570 NDIS!ndisMCommonHaltMiniport+0x1f
f714f268 bfed4ddb bfed0660 811a2708 811a2708 NDIS!ndisPmHaltMiniport+0x9a
f714f288 bfed5146 811a2708 00000004 8145f570 NDIS!ndisSetPower+0x1d1
f714f2a8 8041c60f 81453a30 811a2708 80475b18 NDIS!ndisPowerDispatch+0x84
f714f2bc 8044cc52 80475b18 811a2708 811a279c ntoskrnl!IopfCallDriver+0x35
f714f2d4 8044cb89 811a279c 811a2708 811a27c0 ntoskrnl!PopPresentIrp+0x62 
```

The system is currently running the ISR for the video card. The system will run the ISR for each of the devices sharing IRQ 0xB. If no process claims the interrupt, the operating system will wait infinitely, requesting the driver ISRs to handle the interrupt. It is also possible that a process might handle the interrupt and stop it, but if the hardware is broken the interrupt may simply be re-asserted.

Use the **!arbiter 4** extension to determine which devices are on IRQ 0xB. If there is only one device on IRQ 0xB, you have found the cause of the problem.. If there is more than one device sharing the interrupt (99% of the cases), you will need to isolate the device either by manually programming LNK nodes (which is destructive to the system state), or by removing or disabling hardware.

```dbgcmd
kd> !arbiter 4 
DEVNODE 8149a008 (HTREE\ROOT\0)
  Interrupt Arbiter "RootIRQ" at 80472a20
    Allocated ranges:
      0000000000000000 - 0000000000000000   B   8149acd0
      0000000000000001 - 0000000000000001   B   8149acd0
      0000000000000002 - 0000000000000002   B   8149acd0
      0000000000000003 - 0000000000000003   B   8149acd0
      0000000000000004 - 0000000000000004   B   8149acd0
      0000000000000005 - 0000000000000005   B   8149acd0
      0000000000000006 - 0000000000000006   B   8149acd0
      0000000000000007 - 0000000000000007   B   8149acd0
      0000000000000008 - 0000000000000008   B   8149acd0
      0000000000000009 - 0000000000000009   B   8149acd0
      000000000000000a - 000000000000000a   B   8149acd0
      000000000000000b - 000000000000000b   B   8149acd0
      000000000000000c - 000000000000000c   B   8149acd0
 000000000000000d - 000000000000000d   B   8149acd0
      000000000000000e - 000000000000000e   B   8149acd0
 000000000000000f - 000000000000000f   B   8149acd0
      0000000000000010 - 0000000000000010   B   8149acd0
      0000000000000011 - 0000000000000011   B   8149acd0
      0000000000000012 - 0000000000000012   B   8149acd0
      0000000000000013 - 0000000000000013   B   8149acd0
      0000000000000014 - 0000000000000014   B   8149acd0
      0000000000000015 - 0000000000000015   B   8149acd0
      0000000000000016 - 0000000000000016   B   8149acd0
      0000000000000017 - 0000000000000017   B   8149acd0
      0000000000000018 - 0000000000000018   B   8149acd0
      0000000000000019 - 0000000000000019   B   8149acd0
      000000000000001a - 000000000000001a   B   8149acd0
      000000000000001b - 000000000000001b   B   8149acd0
      000000000000001c - 000000000000001c   B   8149acd0
      000000000000001d - 000000000000001d   B   8149acd0
 000000000000001e - 000000000000001e   B   8149acd0
      000000000000001f - 000000000000001f   B   8149acd0
 0000000000000020 - 0000000000000020   B   8149acd0
      0000000000000021 - 0000000000000021   B   8149acd0
      0000000000000022 - 0000000000000022   B   8149acd0
      0000000000000023 - 0000000000000023   B   8149acd0
      0000000000000024 - 0000000000000024   B   8149acd0
      0000000000000025 - 0000000000000025   B   8149acd0
      0000000000000026 - 0000000000000026   B   8149acd0
      0000000000000027 - 0000000000000027   B   8149acd0
      0000000000000028 - 0000000000000028   B   8149acd0
      0000000000000029 - 0000000000000029   B   8149acd0
      000000000000002a - 000000000000002a   B   8149acd0
      000000000000002b - 000000000000002b   B   8149acd0
      000000000000002c - 000000000000002c   B   8149acd0
 000000000000002d - 000000000000002d   B   8149acd0
      000000000000002e - 000000000000002e   B   8149acd0
 000000000000002f - 000000000000002f   B   8149acd0
      0000000000000032 - 0000000000000032   B   8149acd0
      0000000000000039 - 0000000000000039 S     814776d0  (ACPI)
    Possible allocation:
      < none >

    DEVNODE 81476f28 (ACPI_HAL\PNP0C08\0)
      Interrupt Arbiter "ACPI_IRQ" at bfff10e0
        Allocated ranges:
          0000000000000000 - 0000000000000000   B   81495bb0
          0000000000000001 - 0000000000000001       814952b0  (i8042prt)
          0000000000000003 - 0000000000000003 S     81495610  (Serial)
          0000000000000004 - 0000000000000004   B   8149acd0
          0000000000000006 - 0000000000000006       81495730  (fdc)
          0000000000000008 - 0000000000000008       81495a90
          0000000000000009 - 0000000000000009 S     814776d0  (ACPI)
          000000000000000b - 000000000000000b S
            000000000000000b - 000000000000000b S     81453c30  (ds1)
            000000000000000b - 000000000000000b S     81453a30  (E100B)
            000000000000000b - 000000000000000b S     81493c30  (uhcd)
            000000000000000b - 000000000000000b S     8145c390  (atirage3)
          000000000000000c - 000000000000000c       814953d0  (i8042prt)
 000000000000000d - 000000000000000d   B   81495850
          000000000000000e - 000000000000000e       8145bb50  (atapi)
 000000000000000f - 000000000000000f       8145b970  (atapi)
        Possible allocation:
          < none > 
```

In this case, the audio, Universal Serial Bus (USB), network interface card (NIC), and video are all using the same IRQ.

To find out which ISR claims ownership of the interrupt, examine the return value from the ISR. Simply disassemble the ISR using the **U** command with address given in the **!arbiter** display, and set a breakpoint on the last instruction of the ISR (which will be a 'ret' instruction). Note that using the command **g &lt;address&gt;** is the equivalent of setting a breakpoint on that address:

```dbgcmd
kd> g bfe33e7b 
ds1wdm!AdapterIsr+ad:
bfe33e7b c20800           ret     0x8 
```

Use the **r** command to examine the registers. In particular, look at the EAX register. If the portion of the register contents in bold (in the following code example) is anything other then zero, this ISR claimed the interrupt. Otherwise, the interrupt was not claimed, and the operating system will call the next ISR. This example shows that the video card is not claiming the interrupt:

```dbgcmd
kd> r 
eax=00000000 ebx=813f4ff0 ecx=00000010 edx=ffdff848 esi=8145d168 edi=813f4fc8
eip=bfe33e7b esp=f714eec4 ebp=f714eee0 iopl=0         nv up ei pl zr na po nc
cs=0008  ss=0010  ds=0023  es=0023  fs=0030  gs=0000             efl=00000246
ds1wdm!AdapterIsr+ad:
bfe33e7b c20800           ret     0x8 
```

In fact, in this case, the interrupt is not claimed by any of the devices on IRQ 0xb. When you encounter this problem, you should also check to see if each piece of hardware associated with the interrupt is actually enabled. For PCI, this is easy -- look at the CMD register displayed by the **!pci** extension output:

```dbgcmd
kd> !pci 0 0 
PCI Bus 0
00:0  8086:7190.03  Cmd[0006:.mb...]  Sts[2210:c....]  Device  Host bridge
01:0  8086:7191.03  Cmd[0107:imb..s]  Sts[0220:.6...]  PciBridge 0->1-1  PCI-PCI bridge
03:0  1073:000c.03  Cmd[0000:......]  Sts[0210:c....]  Device  SubID:1073:000c Audio device
04:0  8086:1229.05  Cmd[0007:imb...]  Sts[0290:c....]  Device  SubID:8086:0008 Ethernet
07:0  8086:7110.02  Cmd[000f:imb...]  Sts[0280:.....]  Device  ISA bridge
07:1  8086:7111.01  Cmd[0005:i.b...]  Sts[0280:.....]  Device  IDE controller
07:2  8086:7112.01  Cmd[0005:i.b...]  Sts[0280:.....]  Device  USB host controller
07:3  8086:7113.02  Cmd[0003:im....]  Sts[0280:.....]  Device  Class:6:80:0 
```

Note that the audio chip's CMD register is zero. This means the audio chip is effectively disabled at this time. This also means that the audio chip will not be capable of responding to accesses by the driver.

In this case, the audio chip needs to be manually re-enabled.

 

 





