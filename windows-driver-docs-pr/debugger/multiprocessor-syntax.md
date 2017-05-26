---
title: Multiprocessor Syntax
description: This topic covers Multiprocessor Syntax
ms.assetid: 71adc522-f078-457c-8bc9-9e971e914a41
keywords: ["multiprocessor computer", "multiprocessor computer, command syntax", "dual-processor computer", "dual-processor computer, See "multiprocessor computer"", "(processor identifier)", "(processor identifier)", "syntax rules for commands, (processor identifier)", "syntax rules for commands, (processor identifier)", "processor identifier ( )"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Multiprocessor Syntax


## <span id="ddk_multiprocessor_syntax_dbg"></span><span id="DDK_MULTIPROCESSOR_SYNTAX_DBG"></span>


KD and kernel-mode WinDbg support multiple processor debugging. You can perform this kind of debugging on any multiprocessor platform.

Processors are numbered zero through *n*.

If the current processor is processor 0 (that is, if it is the processor that currently caused the debugger to be active), you can examine the other non-current processors (processors one through *n*). However, you cannot change anything in the non-current processors. You can only view their state.

### <span id="selecting_a_processor"></span><span id="SELECTING_A_PROCESSOR"></span>Selecting a Processor

You can use the [**.echocpunum (Show CPU Number)**](-echocpunum--show-cpu-number-.md) command to display the processor numbers of the current processor. The output from this command enables you to immediately tell when you are working on a multiple processor system by the text in the kernel debugging prompt.

In the following example, **0:** in front of the **kd&gt;** prompt indicates that you are debugging the first processor in the computer.

```
0: kd>
```

Use the [**~s (Change Current Processor)**](-s--change-current-processor-.md) command to switch between processors, as the following example shows.

```
0: kd> ~1s
1: kd>
```

Now you are debugging the second processor in the computer.

You might have to change processors on a multiprocessor system if you encounter a break and you cannot understand the stack trace. The break might have occurred on a different processor.

### <span id="specifying_processors_in_other_commands"></span><span id="SPECIFYING_PROCESSORS_IN_OTHER_COMMANDS"></span>Specifying Processors in Other Commands

You can add a processor number before several commands. This number is not preceded by a tilde (**~**), except in the **~S** command.

**Note**   In user-mode debugging, the tilde is used to specify threads. For more information about this syntax, see [Thread Syntax](thread-syntax.md).

 

Processor IDs do not have to be referred to explicitly. Instead, you can use a numerical expression that resolves to an integer that corresponds to a processor ID. To indicate that the expression should be interpreted as a processor, use the following syntax.

```
||[Expression]
```

In this syntax, the square brackets are required, and *Expression* stands for any numerical expression that resolves to an integer that corresponds to a processor ID.

In the following example, the processor changes depending on the value of a user-defined pseudo-register.

```
||[@$t0]
```

### <span id="examples"></span><span id="EXAMPLES"></span>Examples

The following example uses the [**k (Display Stack Backtrace)**](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md) command to display a stack trace from processor two.

```
1: kd> 2k 
```

The following example uses the [**r (Registers)**](r--registers-.md) command to display the **eax** register of processor three.

```
1: kd> 3r eax 
```

However, the following command gives a syntax error, because you cannot change the state of a processor other than the current processor.

```
1: kd> 3r eax=808080 
```

### <span id="breakpoints"></span><span id="BREAKPOINTS"></span>Breakpoints

During kernel debugging, the [**bp, bu, bm (Set Breakpoint)**](bp--bu--bm--set-breakpoint-.md) and [**ba (Break on Access)**](ba--break-on-access-.md) commands apply to all processors of a multiple processor computer.

For example, if the current processor is three, you can enter the following command to put a breakpoint at **SomeAddress**.

```
1: kd> bp SomeAddress 
```

Then, any processor (not only processor one) that executes at that address causes a breakpoint trap.

### <span id="displaying_processor_information"></span><span id="DISPLAYING_PROCESSOR_INFORMATION"></span>Displaying Processor Information

You can use the [**!running**](-running.md) extension to display the status of each processor on the target computer. For each processor, **!running** can also display the current and next thread fields from the process control block (PRCB), the state of the 16 built-in queued spinlocks, and a stack trace.

You can use the [**!cpuinfo**](-cpuinfo.md) and [**!cpuid**](-cpuid.md) extensions to display information about the processors themselves.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Multiprocessor%20Syntax%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




