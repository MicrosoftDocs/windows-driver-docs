---
title: Bug Check 0x1F5 APPLICATION_HANG_KERNEL_LIVEDUMP
description: The APPLICATION_HANG_KERNEL_LIVEDUMP  has a value of 0x000001F5. This indicates that an application hung when attempting to be terminated. 
keywords: ["Bug Check 0x1F5 APPLICATION_HANG_KERNEL_LIVEDUMP", "APPLICATION_HANG_KERNEL_LIVEDUMP"]
ms.date: 10/28/2022
topic_type:
- apiref
api_name:
- APPLICATION_HANG_KERNEL_LIVEDUMP
api_type:
- NA
---

# Bug Check 0x1F5: APPLICATION\_HANG\_KERNEL\_LIVEDUMP

The APPLICATION\_HANG\_KERNEL\_LIVEDUMP has a value of 0x000001F5. This indicates that an application hung when attempting to be terminated.

(This code can never be used for a real BugCheck; it is used to identify live dumps.)

## APPLICATION\_HANG\_KERNEL\_LIVEDUMP Parameters


| Parameter | Description |
|-----------|-------------|
| 1         | Reserved    |
| 2         | Reserved    |
| 3         | Reserved    |
| 4         | Reserved    |
 

## Cause

After an application hang report (such as that can be created with the [WerReportHang](/windows/win32/api/errorrep/nf-errorrep-werreporthang) function) was completed, TerminateProcess was called, but the target process failed to terminate, likely because a thread is hung in kernel mode. 

This live kernel triage dump may contain the kernel thread states of the hung process. The kernel dump contains only the threads for the process which WER was unable to terminate, and only kernel, not user memory.  

## Resolution

The [**!analyze**](-analyze.md) debug extension displays information about the bug check and can be helpful in determining the root cause.


## See Also

[Kernel Live Dump Code Reference](bug-check-code-reference-live-dump.md)

[Bug Check Code Reference](bug-check-code-reference2.md)


 

 




