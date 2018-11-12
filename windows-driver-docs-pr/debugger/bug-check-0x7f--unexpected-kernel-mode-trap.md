---
title: Bug Check 0x7F UNEXPECTED_KERNEL_MODE_TRAP
description: The UNEXPECTED_KERNEL_MODE_TRAP bug check has a value of 0x0000007F.
ms.assetid: f4fcc2a1-891b-44e9-94bf-e712019f538f
keywords: ["Bug Check 0x7F UNEXPECTED_KERNEL_MODE_TRAP", "UNEXPECTED_KERNEL_MODE_TRAP"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- UNEXPECTED_KERNEL_MODE_TRAP
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x7F: UNEXPECTED\_KERNEL\_MODE\_TRAP


The UNEXPECTED\_KERNEL\_MODE\_TRAP bug check has a value of 0x0000007F. This bug check indicates that the Intel CPU generated a trap and the kernel failed to catch this trap.

This trap could be a *bound trap* (a trap the kernel is not permitted to catch) or a *double fault* (a fault that occurred while processing an earlier fault, which always results in a system failure).

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## UNEXPECTED\_KERNEL\_MODE\_TRAP Parameters


The first parameter that appears on the blue screen specifies the trap number.

The most common trap codes include the following:

-   0x00000000, or Divide by Zero Error, indicates that a DIV instruction is executed and the divisor is zero. Memory corruption, other hardware problems, or software failures can cause this error.

-   0x00000004, or Overflow, occurs when the processor executes a call to an interrupt handler when the overflow (OF) flag is set.

-   0x00000005, or Bounds Check Fault, indicates that the processor, while executing a BOUND instruction, finds that the operand exceeds the specified limits. A BOUND instruction ensures that a signed array index is within a certain range.

-   0x00000006, or Invalid Opcode, indicates that the processor tries to execute an invalid instruction. This error typically occurs when the instruction pointer has become corrupted and is pointing to the wrong location. The most common cause of this error is hardware memory corruption.

-   0x00000008, or Double Fault, indicates that an exception occurs during a call to the handler for a prior exception. Typically, the two exceptions are handled serially. However, there are several exceptions that cannot be handled serially, and in this situation the processor signals a double fault. There are two common causes of a double fault:
    -   A kernel stack overflow. This overflow occurs when a guard page is hit, and the kernel tries to push a trap frame. Because there is no stack left, a stack overflow results, causing the double fault. If you think this overview has occurred, use [**!thread**](-thread.md) to determine the stack limits, and then use [**kb (Display Stack Backtrace)**](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md) with a large parameter (for example, **kb 100**) to display the full stack.
    -   A hardware problem.

The less-common trap codes include the following:

-   0x00000001 -- A system-debugger call

-   0x00000003 -- A debugger breakpoint

-   0x00000007 -- A hardware coprocessor instruction with no coprocessor present

-   0x0000000A -- A corrupted Task State Segment

-   0x0000000B -- An access to a memory segment that was not present

-   0x0000000C -- An access to memory beyond the limits of a stack

-   0x0000000D -- An exception not covered by some other exception; a protection fault that pertains to access violations for applications

For other trap numbers, see an Intel architecture manual.

Cause
-----

Bug check 0x7F typically occurs after you install a faulty or mismatched hardware (especially memory) or if installed hardware fails.

A double fault can occur when the kernel stack overflows. This overflow occurs if multiple drivers are attached to the same stack. For example, if two file system filter drivers are attached to the same stack and then the file system recurses back in, the stack overflows.

Resolution
----------

**Debugging:** Always begin with the [**!analyze**](-analyze.md) extension.

If this extension is not sufficient, use the [**kv (Display Stack Backtrace)**](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md) debugger command.

-   If **kv** shows a **taskGate**, use the [**.tss (Display Task State Segment)**](-tss--display-task-state-segment-.md) command on the part before the colon.

-   If **kv** shows a trap frame, use the [**.trap (Display Trap Frame)**](-trap--display-trap-frame-.md) command to format the frame.

-   Otherwise, use the [**.trap (Display Trap Frame)**](-trap--display-trap-frame-.md) command on the appropriate frame. (On x86-based platforms, this frame is associated with the procedure **NT!KiTrap**.)

After using one of these commands, use **kv** again to display the new stack.

**Troubleshooting:** If you recently added hardware to the computer, remove it to see if the error recurs. If existing hardware has failed, remove or replace the faulty component. Run hardware diagnostics that the system manufacturer supplies to determine which hardware component failed.

The memory scanner is especially important. Faulty or mismatched memory can cause this bug check. For more information about these procedures, see the owner's manual for your computer. Check that all adapter cards in the computer are properly seated. Use an ink eraser or an electrical contact treatment, available at electronics supply stores, to ensure adapter card contacts are clean.

If the error appears on a newly installed system, check the availability of updates for the BIOS, the SCSI controller, or network cards. These kind of updates are typically available on the Web site or BBS of the hardware manufacturer.

Confirm that all hard disk drives, hard disk controllers, and SCSI adapters are compatible with the installed version of Windows. For example, you can get information about compatibility with Windows 7 at the [Windows 7 Compatibility Center](https://go.microsoft.com/fwlink/p/?LinkID=246806).

If the error occurred after the installation of a new or updated device driver, you should remove or replace the driver. If, under this circumstance, the error occurs during the startup sequence and the system partition is formatted with NTFS, you might be able to use Safe Mode to rename or delete the faulty driver. If the driver is used as part of the system startup process in Safe Mode, you have to start the computer by using the Recovery Console in order to access the file.

Also restart your computer, and then press F8 at the character-based menu that displays the operating system choices. At the **Advanced Options** menu, select the **Last Known Good Configuration** option. This option is most effective when you add only one driver or service at a time.

Overclocking (setting the CPU to run at speeds above the rated specification) can cause this error. If you have overclocked the computer that is experiencing the error, return the CPU to the default clock speed setting.

Check the System Log in Event Viewer for additional error messages that might help identify the device or driver that is causing the error. You can also disable memory caching of the BIOS to try to resolve the problem.

If you encountered this error while upgrading to a new version of the Windows operating system, the error might be caused by a device driver, a system service, a virus scanner, or a backup tool that is incompatible with the new version. If possible, remove all third-party device drivers and system services and disable any virus scanners before you upgrade. Contact the software manufacturer to obtain updates of these tools. Also make sure that you have installed the latest Windows Service Pack.

Finally, if all the above steps do not resolve the error, take the system motherboard to a repair facility for diagnostic testing. A crack, a scratched trace, or a defective component on the motherboard can also cause this error.

 

 




