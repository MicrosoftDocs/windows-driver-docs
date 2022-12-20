---
title: Bug check 0x1E KMODE_EXCEPTION_NOT_HANDLED
description: The 0x0000001E KMODE_EXCEPTION_NOT_HANDLED bug check indicates that a kernel-mode program generated an exception the error handler didn't catch.
keywords: ["Bug check 0x1E KMODE_EXCEPTION_NOT_HANDLED", "KMODE_EXCEPTION_NOT_HANDLED"]
ms.date: 12/08/2022
topic_type:
- apiref
api_name:
- KMODE_EXCEPTION_NOT_HANDLED
api_type:
- NA
---

# Bug check 0x1E: KMODE_EXCEPTION_NOT_HANDLED

The KMODE_EXCEPTION_NOT_HANDLED bug check has a value of 0x0000001E. The bug check indicates that a kernel-mode program generated an exception that the error handler didn't catch.

> [!IMPORTANT]
> This article is for programmers. If you're a Microsoft customer and your computer displays a blue screen error code, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).

## KMODE_EXCEPTION_NOT_HANDLED parameters

| Parameter | Description |
|---|---|
| 1 | The exception code that wasn't handled. |
| 2 | The address where the exception occurred. |
| 3 | Exception information parameter 0 of the exception record. |
| 4 | Exception information parameter 0 of the exception record. |

## Cause

To interpret this bug check, you must identify which exception was generated.

Common exception codes include:

- 0x80000002: STATUS_DATATYPE_MISALIGNMENT

  An unaligned data reference was encountered.

- 0x80000003: STATUS_BREAKPOINT

  A breakpoint or ASSERT was encountered when no kernel debugger was attached to the system.

- 0xC0000005: STATUS_ACCESS_VIOLATION

  A memory access violation occurred. (Parameter 4 of the bug check is the address that the driver attempted to access.)

For a complete list of exception codes, see [NTSTATUS values](/openspecs/windows_protocols/ms-erref/596a1078-e883-4972-9bbc-49e60bebca55). The exception codes are defined in *ntstatus.h*, a header file that's in the [Windows Driver Kit](../index.yml). For more information, see [Header files in the Windows Driver Kit](../gettingstarted/header-files-in-the-windows-driver-kit.md).

## Remarks

If you're not equipped to debug this problem, you can use some basic troubleshooting techniques that are described in [Blue screen data](blue-screen-data.md). If a driver is identified in the bug check message, disable the driver or check with the manufacturer for driver updates.

### Hardware incompatibility

Confirm that any new hardware that's installed is compatible with the installed version of Windows. For example, you can get information about required hardware at [Windows 10 specifications](https://www.microsoft.com/windows/windows-10-specifications).

### Faulty device driver or system service

A faulty device driver or system service might cause this error. Hardware issues, such as BIOS incompatibilities, memory conflicts, and IRQ conflicts, can also generate this error.

If a driver is listed by name in the bug check message, disable or remove that driver. Disable or remove any drivers or services that were recently added. If the error occurs during the startup sequence and the system partition is formatted as an NTFS file system, you might be able to use Safe Mode to disable the driver in Device Manager.

Check System Log in Event Viewer for more error messages that might help you identify the device or driver that's causing bug check 0x1E. Also run hardware diagnostics that are supplied by the system manufacturer, especially the memory scanner. For more information about these troubleshooting steps, see the owner's manual for your computer.

The error that generates this message might occur after the first restart during Windows Setup or after Setup is finished. A possible cause of the error is a system BIOS incompatibility. You can resolve BIOS problems by upgrading the system BIOS version.

## Resolution

You might find it difficult to get a stack trace when you debug this problem. The exception address (parameter 2) should identify the driver or function that caused the problem.

Exception code 0x80000003 indicates that a hard-coded breakpoint or assertion was hit, but the system was started with the `/NODEBUG` switch. This problem should occur rarely. If it occurs repeatedly, make sure that a kernel debugger is connected and that the system is started with the `/DEBUG` switch.

If exception code 0x80000002 occurs, the trap frame supplies more information.

### Unknown cause

If the specific cause of the exception is unknown, consider using the following procedure to get a stack trace.

> [!NOTE]
> This procedure assumes that you can locate `NT!PspUnhandledExceptionInSystemThread`. However, in some cases, like in an access violation crash, you won't be able to find `NT!PspUnhandledExceptionInSystemThread`. In that case, look for `ntoskrnl!KiDispatchException`. The third parameter that's passed to this function is a trap frame address. Use the [.trap (display trap frame)](-trap--display-trap-frame-.md) command with this address to set the register context to the correct value. Then you can do stack traces and issue other commands.

#### Get a stack trace

To get a stack trace if normal stack tracing procedures fail:

1. Use the [kb (display stack backtrace)](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md) command to display parameters in the stack trace. Look for the call to `NT!PspUnhandledExceptionInSystemThread`. (If this function isn't listed, see the preceding note.)

1. The first parameter to `NT!PspUnhandledExceptionInSystemThread` is a pointer to a structure. The pointer contains pointers to an `except` statement:

    ```cpp
    typedef struct _EXCEPTION_POINTERS {
        PEXCEPTION_RECORD ExceptionRecord;
        PCONTEXT ContextRecord;
        } EXCEPTION_POINTERS, *PEXCEPTION_POINTERS;

    ULONG PspUnhandledExceptionInSystemThread(
        IN PEXCEPTION_POINTERS ExceptionPointers
        )
    ```

    Use the [dd (display memory)](d--da--db--dc--dd--dd--df--dp--dq--du--dw--dw--dyb--dyd--display-memor.md) command on that address to display the data you need.

1. The first retrieved value is an exception record. For the exception record, use the [.exr (display exception record)](-exr--display-exception-record-.md) command.

   The second value is a context record. For the context record, use the [.cxr (display context record)](-cxr--display-context-record-.md) command.

1. After the `.cxr` command executes, use the `kb` command to display a stack trace that's based on the context record information. This stack trace indicates the calling stack where the unhandled exception occurred.

### Example bug check

The following example shows a bug check 0x1E on an x86 processor:

```dbgcmd
kd> .bugcheck                 get the bug check data
Bugcheck code 0000001e
Arguments c0000005 8013cd0a 00000000 0362cffff

kd> kb                        start with a stack trace 
FramePtr  RetAddr   Param1   Param2   Param3   Function Name 
8013ed5c  801263ba  00000000 00000000 fe40cb00 NT!_DbgBreakPoint 
8013eecc  8013313c  0000001e c0000005 8013cd0a NT!_KeBugCheckEx+0x194
fe40cad0  8013318e  fe40caf8 801359ff fe40cb00 NT!PspUnhandledExceptionInSystemThread+0x18
fe40cad8  801359ff  fe40cb00 00000000 fe40cb00 NT!PspSystemThreadStartup+0x4a
fe40cf7c  8013cb8e  fe43a44c ff6ce388 00000000 NT!_except_handler3+0x47
00000000  00000000  00000000 00000000 00000000 NT!KiThreadStartup+0xe

kd> dd fe40caf8 L2            dump EXCEPTION_POINTERS structure
0xFE40CAF8  fe40cd88 fe40cbc4                   ..@...@.

kd> .exr fe40cd88             first DWORD is the exception record
Exception Record @ FE40CD88:
   ExceptionCode: c0000005
  ExceptionFlags: 00000000
  Chained Record: 00000000
ExceptionAddress: 8013cd0a
NumberParameters: 00000002
   Parameter[0]: 00000000
   Parameter[1]: 0362cfff

kd> .cxr fe40cbc4             second DWORD is the context record
CtxFlags: 00010017
eax=00087000 ebx=00000000 ecx=03ff0000 edx=ff63d000 esi=0362cfff edi=036b3fff
eip=8013cd0a esp=fe40ce50 ebp=fe40cef8 iopl=0         nv dn ei pl nz ac po cy
vip=0    vif=0
cs=0008  ss=0010  ds=0023  es=0023  fs=0030  gs=0000             efl=00010617
0x8013cd0a  f3a4             rep movsb

kd> kb                        kb gives stack for context record
ChildEBP RetAddr  Args to Child
fe40ce54 80402e09 ff6c4000 ff63d000 03ff0000 NT!_RtlMoveMemory@12+0x3e
fe40ce68 80403c18 ffbc0c28 ff6ce008 ff6c4000 HAL!_HalpCopyBufferMap@20+0x49
fe40ce9c fe43b1e4 ff6cef90 ffbc0c28 ff6ce009 HAL!_IoFlushAdapterBuffers@24+0x148
fe40ceb8 fe4385b4 ff6ce388 6cd00800 ffbc0c28 QIC117!_kdi_FlushDMABuffers@20+0x28
fe40cef8 fe439894 ff6cd008 ffb6c820 fe40cf4c QIC117!_cqd_CmdReadWrite@8+0x26e
fe40cf18 fe437d92 ff6cd008 ffb6c820 ff6e4e50 QIC117!_cqd_DispatchFRB@8+0x210
fe40cf30 fe43a4f5 ff6cd008 ffb6c820 00000000 QIC117!_cqd_ProcessFRB@8+0x134
fe40cf4c 80133184 ff6ce388 00000000 00000000 QIC117!_kdi_ThreadRun@4+0xa9
fe40cf7c 8013cb8e fe43a44c ff6ce388 00000000 NT!_PspSystemThreadStartup@8+0x40
```
