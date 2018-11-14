---
title: AML Debugging Examples
description: AML Debugging Examples
ms.assetid: 3a9f760f-f511-412f-aca0-3c415b3e5dc2
keywords: ["AMLI Debugger, debugging examples"]
ms.author: domars
ms.date: 11/07/2018
ms.localizationpriority: medium
---

# AML Debugging Examples


## <span id="ddk_aml_debugging_examples_dbg"></span><span id="DDK_AML_DEBUGGING_EXAMPLES_DBG"></span>


Here are examples that illustrate how to get started with AML debugging.

### <span id="investigating_a_frozen_computer"></span><span id="INVESTIGATING_A_FROZEN_COMPUTER"></span>Investigating a Frozen Computer

If the target computer has frozen and you suspect it may be an ACPI problem, begin by using the [**!amli lc**](-amli-lc.md) extension to display all the active contexts:

```dbgcmd
kd> !amli lc
*Ctxt=ffffffff8128d000, ThID=ffffffff81277880, Flgs=----R----, pbOp=ffffffff8124206c, Obj=\_SB.PCI0.ISA0.FDC0._CRS
```

If no contexts are displayed, the error is probably not ACPI-related.

If there are contexts shown, look for the one marked with an asterisk. This is the *current context* (the one that is being executed by the interpreter at the present moment).

In this example, the target computer is running Windows on a 32-bit processor. Therefore all addresses are cast to 64 bits, producing a gratuitous FFFFFFFF in the high 32 bits. The abbreviation **pbOp** indicates the instruction pointer ("pointer to binary op codes"). The **Obj** field gives the full path and name of the method as it appears in the ACPI tables. For a description of the flags, see [**!amli lc**](-amli-lc.md).

You can use the [**!amli u**](-amli-u.md) command to disassemble the \_CRS method as follows:

```dbgcmd
kd> !amli u \_SB.PCI0.ISA0.FDC0._CRS

ffffffff80e4a535 : CreateDWordFieldCRES, 0x76, RAMT)
ffffffff80e4a540 : CreateDWordField(CRES, 0x82, PCIT)
ffffffff80e4a54b : Add(MLEN(), 0x100000, RAMT)
ffffffff80e4a559 : Subtract(0xffe00000, RAMT, PCIT)
ffffffff80e4a567 : Return(CRES)
```

### <span id="breaking_into_the_amli_debugger"></span><span id="BREAKING_INTO_THE_AMLI_DEBUGGER"></span>Breaking Into the AMLI Debugger

The [**!amli debugger**](-amli-debugger.md) command causes the AML interpreter to break into the AMLI Debugger the next time any AML code is executed.

After the AMLI Debugger prompt appears, you can use any of the AMLI Debugger commands. You can also use **!amli** extension commands without prefixing them with "!amli":

```dbgcmd
kd> !amli debugger
kd> g

AMLI(? for help)-> find _crs
\_SB.LNKA._CRS
\_SB.LNKB._CRS
\_SB.LNKC._CRS
\_SB.LNKD._CRS
\_SB.PCI0._CRS
\_SB.PCI0.LPC.NCP._CRS
\_SB.PCI0.LPC.PIC._CRS
\_SB.PCI0.LPC.TIME._CRS
\_SB.PCI0.LPC.IDMA._CRS
\_SB.PCI0.LPC.RTC._CRS
\_SB.PCI0.LPC.SPKR._CRS
\_SB.PCI0.LPC.FHUB._CRS
\_SB.PCI0.SBD1._CRS
\_SB.PCI0.SBD2._CRS
\_SB.MBRD._CRS

AMLI(? for help)-> u \_SB.PCI0._CRS

ffffffff80e4a535 : CreateDWordFieldCRES, 0x76, RAMT)
ffffffff80e4a540 : CreateDWordField(CRES, 0x82, PCIT)
ffffffff80e4a54b : Add(MLEN(), 0x100000, RAMT)
ffffffff80e4a559 : Subtract(0xffe00000, RAMT, PCIT)
ffffffff80e4a567 : Return(CRES)
```

### <span id="using_breakpoints"></span><span id="USING_BREAKPOINTS"></span>Using Breakpoints

In the following example, you will break into the AMLI Debugger before the method \_BST is executed.

Even if you have located a \_BST object, you should verify that it is indeed a method. You can use the [**!amli dns**](-amli-dns.md) extension to do this.

```dbgcmd
kd> !amli dns /s \_sb.pci0.isa.bat1._bst

ACPI Name Space: \_SB.PCI0.ISA.BAT1._BST (c29c2044)
Method(_BST:Flags=0x0,CodeBuff=c29c20a5,Len=103)
```

Now you can use the [**!amli bp**](-amli-bp.md) command to place the breakpoint:

```dbgcmd
kd> !amli bp \_sb.pci0.isa.bat1._bst
```

You may also want to place breakpoints within the method. You could use the [**!amli u**](-amli-u.md) command to disassemble \_BST and then place a breakpoint on one of its steps:

```dbgcmd
kd> !amli u _sb.pci0.isa.bat1._bst

ffffffffc29c20a5: Acquire(\_SB_.PCI0.ISA_.EC0_.MUT1, 0xffff)
ffffffffc29c20c0: Store("CMBatt - _BST.BAT1", Debug)
ffffffffc29c20d7: \_SB_.PCI0.ISA_.EC0_.CPOL()
ffffffffc29c20ee: Release(\_SB_.PCI0.ISA_.EC0_.MUT1)
ffffffffc29c2107: Return(PBST)

kd> !amli bp c29c20ee
```

### <span id="responding_to_a_triggered_breakpoint"></span><span id="RESPONDING_TO_A_TRIGGERED_BREAKPOINT"></span>Responding to a Triggered Breakpoint

In the following example, the method \_WAK is running and then encounters a breakpoint:

```dbgcmd
Running \_WAK method
Hit Breakpoint 0.
```

Use the [**!amli ln**](-amli-ln.md) extension to see the nearest method to the current program counter. The following example is showing addresses in 32-bit form:

```dbgcmd
kd> !amli ln
c29accf5: \_WAK
```

The [**!amli lc**](-amli-lc.md) extension displays all the active contexts:

```dbgcmd
kd> !amli lc
 Ctxt=c18b6000, ThID=00000000, Flgs=A-QC-W----, pbOp=c29bf8fe, Obj=\_SB.PCI0.ISA.EC0._Q09
*Ctxt=c18b4000, ThID=c15a6618, Flgs=----R-----, pbOp=c29accf5, Obj=\_WAK
```

This shows that the active contexts are associated with the methods \_Q09 and \_WAK. The current context is \_WAK.

Now you can use the [**!amli r**](-amli-r.md) command to display more details about the current context. From this you can see useful thread and stack information, as well as arguments passed to \_WAK and the local data objects.

```dbgcmd
kd> !amli r
Context=c18b4000*, Queue=00000000, ResList=00000000
ThreadID=c15a6618, Flags=00000010
StackTop=c18b5eec, UsedStackSize=276 bytes, FreeStackSize=7636 bytes
LocalHeap=c18b40c0, CurrentHeap=c18b40c0, UsedHeapSize=88 bytes
Object=\_WAK, Scope=\_WAK, ObjectOwner=c18b4108, SyncLevel=0
AsyncCallBack=ff06b5d0, CallBackData=0, CallBackContext=c99efddc

MethodObject=\_WAK
c18b40e4: Arg0=Integer(:Value=0x00000001[1])
c18b5f3c: Local0=Unknown()
c18b5f54: Local1=Unknown()
c18b5f6c: Local2=Unknown()
c18b5f84: Local3=Unknown()
c18b5f9c: Local4=Unknown()
c18b5fb4: Local5=Unknown()
c18b5fcc: Local6=Unknown()
c18b5fe4: Local7=Unknown()
c18b4040: RetObj=Unknown()
```

### <span id="tracing__stepping__and_running_aml_code"></span><span id="TRACING__STEPPING__AND_RUNNING_AML_CODE"></span>Tracing, Stepping, and Running AML Code

If you want to trace through the code, you can turn on full tracing information by using the [**!amli set**](-amli-set.md) extension as follows:

```dbgcmd
kd> !amli set spewon verboseon traceon
```

Now you can step through the AML code, watching the code execute line by line. The **p** command steps over any function calls. The **t** command will step into function calls.

```dbgcmd
AMLI(? for help)-> p

c29bfcb7: Store(\_SB_.PCI0.ISA_.ACAD.CHAC(SEL0=0x10e1)
c29c17b1: {
c29c17b1: | Store(LGreater(And(Arg0=0x10e1,0xf0,)=0xe0,0x80)=0xffffffff,Local0)=0xffffffff

AMLI(? for help)-> p

c29c17bb: | If(LNot(LEqual(Local0=0xffffffff,ACP_=0xffffffff)=0xffffffff)=0x0)
c29c17ce: | {
c29c17ce: | | Return(Zero)
c29c17d0: | }
c29c17d0: },Local1)=0x0

AMLI(? for help)-> t

c29bfcd4: Store(\_SB_.PCI0.ISA_.BAT1.CHBP(SEL0=0x10e1)
c29c293d: {
c29c293d: | Store("CMBatt - CHBP.BAT1",Debug)String(:Str="CMBatt - CHBP.BAT1")="CMBatt - CHBP.BAT1"
```

You may also run methods from within the AMLI Debugger if you choose. For example, you might evaluate the status of the LNKA device by running its control method \_STA:

```dbgcmd
AMLI(? for help)-> run \_sb.lnka._sta
PCI OpRegion Access on region c29b2268 device c29b2120

\_SB.LNKA._STA completed successfully with object data:
Integer(:Value=0x0000000b[11])
```

## See Also

 [The AMLI Debugger](the-amli-debugger.md)

 





