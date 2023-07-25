---
title: findfilelockowner
description: The findfilelockowner extension attempts to find the owner of a file object lock by examining all threads for a thread that is blocked.
keywords: ["findfilelockowner Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- findfilelockowner
api_type:
- NA
---

# !findfilelockowner

The **!findfilelockowner** extension attempts to find the owner of a file object lock by examining all threads for a thread that is blocked in an IopSynchronousServiceTail assert and that has the file object as a parameter.

```dbgcmd
!findfilelockowner [FileObject]
```

## Parameters

*FileObject*

Specifies the address of a file object. If *FileObject* is omitted, the extension searches for any thread in the current process that is stuck in **IopAcquireFileObjectLock** and retrieves the file object address from the stack trace.

### DLL

Kdexts.dll

### Additional Information

For information about file objects, see the Microsoft Windows SDK documentation, the Windows Driver Kit (WDK) documentation, and *Microsoft Windows Internals* by Mark Russinovich and David Solomon.

## Remarks

This extension is most useful after a critical section timeout in which the thread that times out was waiting for the file inside **IopAcquireFileObjectLock**. After the offending thread is found, the extension attempts to recover the IRP that was used for the request and to display the driver that was processing the IRP.

The extension takes some time to complete because it walks the stack of all threads in the system until it finds the offending thread.You can stop \` at any point by pressing CTRL+BREAK (in WinDbg) or CTRL+C (in KD).

## See also

[Displaying a Critical Section](displaying-a-critical-section.md)

[Critical Section Time Outs](critical-section-time-outs.md) (user mode)
