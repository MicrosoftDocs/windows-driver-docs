---
title: Bug check 0x7F UNEXPECTED_KERNEL_MODE_TRAP
description: Learn about the UNEXPECTED_KERNEL_MODE_TRAP bug check, value 0x0000007F. It indicates that the Intel CPU generated a trap that the kernel failed to catch.
keywords: ["Bug Check 0x7F UNEXPECTED_KERNEL_MODE_TRAP", "UNEXPECTED_KERNEL_MODE_TRAP"]
ms.date: 02/16/2022
topic_type:
- apiref
ms.topic: reference
api_name:
- UNEXPECTED_KERNEL_MODE_TRAP
api_type:
- NA
---

# Bug check 0x7F: UNEXPECTED_KERNEL_MODE_TRAP

The UNEXPECTED_KERNEL_MODE_TRAP bug check has a value of 0x0000007F. This bug check indicates that the Intel CPU generated a trap and the kernel failed to catch this trap.

This trap could be either of the following types:

- A *bound trap*, which is a trap the kernel isn't permitted to catch.
- A *double fault*, which is a fault that occurred while processing an earlier fault, which always results in a system failure.

> [!IMPORTANT]
> This topic is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).

### Parameter 1

The first parameter that appears on the blue screen specifies the trap number.

The most common trap numbers are the following codes:

| Parameter | Trap code  | Description                 |  
|-----------|------------|-----------------------------|
| 0x00000000 | Divide by Zero Error | Indicates that a DIV instruction is executed and the divisor is zero. Memory corruption, other hardware problems, or software failures can cause this error. |
| 0x00000004 | Overflow           | Occurs when the processor executes a call to an interrupt handler when the overflow (OF) flag is set. |
| 0x00000005 | Bounds Check Fault | Indicates that the processor, while executing a BOUND instruction, finds that the operand exceeds the specified limits. A BOUND instruction ensures that a signed array index is within a certain range. |
| 0x00000006 | Invalid Opcode     | Indicates that the processor tries to execute an invalid instruction. This error typically occurs when the instruction pointer has become corrupted and is pointing to the wrong location. The most common cause of this error is hardware memory corruption. |
| 0x00000008 | Double Fault       | Indicates that an exception occurs during a call to the handler for a prior exception. Typically, the two exceptions are handled serially. There are several exceptions that can't be handled serially, so the processor signals a double fault. |

There are two common causes of a double fault:

- The first cause is a kernel stack overflow. This overflow occurs when a guard page is hit, and the kernel tries to push a trap frame. Because there's no stack left, a stack overflow results, causing the double fault. If you think this situation has occurred, use the [!thread](../debuggercmds/-thread.md) extension to determine the stack limits, and then use the [kb (Display Stack Backtrace)](../debuggercmds/k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md) command with a large value, for example, kb 100, to display the full stack.
- The second common cause is a hardware problem.

The less-common trap codes include the following values:

- 0x00000001: A system-debugger call (DEBUG)
- 0x00000003: A debugger breakpoint (INT3)
- 0x00000007: A hardware coprocessor instruction with no coprocessor present (NXP_NOT_AVAILABLE)
- 0x0000000A: A corrupted Task State Segment (INVALID_TSS)
- 0x0000000B: An access to a memory segment that wasn't present (SEGMENT_NOT_PRESENT)
- 0x0000000C: An access to memory beyond the limits of a stack (STACK_FAULT)
- 0x0000000D: An exception not covered by some other exception, a protection fault that pertains to access violations for applications (GP_FAULT)
- 0x0000000F: A reserved trap exception (RESERVED_TRAP)
- 0x00000010: A hardware coprocessor exception (NPX_ERROR)
- 0x00000011: An alignment check exception (ALIGNMENT_CHECK)

For other trap numbers, refer to the Intel processor architecture manual for the processor you're troubleshooting.

## Cause

Bug check 0x7F typically occurs after you install faulty or mismatched hardware, especially memory, or if installed hardware fails.

A double fault can occur when the kernel stack overflows. This overflow occurs if multiple drivers are attached to the same stack. For example, if two file system filter drivers are attached to the same stack and then the file system recurses back in, the stack overflows.

## Debug

Always begin with the [!analyze](../debuggercmds/-analyze.md) extension with the **-v** option, verbose. Examine the output and the faulting code. Look for reoccurring trends in multiple dumps.

After you try **!analyze**, use the [kv (Display Stack Backtrace)](../debuggercmds/k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md) debugger command.

- If **kv** shows a task gate, use the [.tss (Display Task State Segment)](../debuggercmds/-tss--display-task-state-segment-.md) command on the part before the colon.
- If **kv** shows a trap frame, use the [.trap (Display Trap Frame)](../debuggercmds/-trap--display-trap-frame-.md) command to format the frame.
- Otherwise, use the [.trap (Display Trap Frame)](../debuggercmds/-trap--display-trap-frame-.md) command on the appropriate frame. On x86-based platforms, this frame is associated with the procedure **NT!KiTrap**.

After using one of these commands, use **kv** again to display the new stack.

## Troubleshoot

### Hardware

If you recently added hardware to the computer, remove it to see if the error recurs. If existing hardware has failed, remove or replace the faulty component. Run hardware diagnostics that the system manufacturer supplies to determine which hardware component failed.

Faulty or mismatched memory can cause this bug check. Use the memory diagnostic program in Windows to test all of the system memory.

Confirm that all hard disk drives and hard disk controllers are compatible with the installed version of Windows.

The system motherboard might have issues, such as a scratched trace or a defective component. A failing power supply can also cause issues.

*Overclocking* is setting the CPU to run at speeds above the rated specification, which can cause this error. If you've overclocked the computer that's experiencing the error, return the CPU to the default clock speed setting. Disable memory caching of the BIOS to try to resolve the problem if that option is available.

### Software

Check the **System Log** in Event Viewer for other error messages that might help identify the device or driver that's causing the error.

Check the availability of updates for the ACPI/BIOS, the hard driver controller, or network cards from the hardware manufacturer.

If the error occurred after the installation of a new or updated device driver, remove or replace the driver. If, under this circumstance, the error occurs during the startup sequence, use Safe Mode to rename or delete the faulty driver. If the driver is used as part of the system startup process in Safe Mode, start the computer by using the Recovery Console in order to access the file. Try the *Last Known Good Configuration* option. This option is most effective when you add only one driver or service at a time.

If you encounter this error while upgrading to a new version of the Windows operating system, the error might be caused by incompatible software. Examples include a device driver, a system service, a virus scanner, or a backup tool. If possible, remove all third-party device drivers and system services and disable any virus scanners before you upgrade. Contact the software manufacturer to obtain updates of these tools. Also, make sure that you've installed the latest Windows updates.

## See also

- [!analyze](../debuggercmds/-analyze.md)
- [Bug check code reference](bug-check-code-reference2.md)
