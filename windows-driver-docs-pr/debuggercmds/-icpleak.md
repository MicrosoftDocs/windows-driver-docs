---
title: icpleak (WinDbg)
description: The icpleak extension examines all I/O completion objects in the system for the object with the largest number of queued entries.
keywords: ["I/O completion", "icpleak Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- icpleak
api_type:
- NA
---

# !icpleak


The **!icpleak** extension examines all I/O completion objects in the system for the object with the largest number of queued entries.

```dbgcmd
!icpleak [HandleFlag]
```

## Parameters


<span id="_______HandleFlag______"></span><span id="_______handleflag______"></span><span id="_______HANDLEFLAG______"></span> *HandleFlag*   
If this flag is set, the display also includes all processes that have a handle to the object with the largest number of queued entries.

## DLL

Windows XP and later - Kdexts.dll

 

### Additional Information

For information about I/O completion ports, see *Microsoft Windows Internals* by Mark Russinovich and David Solomon. 

## Remarks

This extension is useful when there is a leak in the I/O completion pool. I/O completion pool leaks can occur when a process is allocating I/O completion packets by calling [**PostQueuedCompletionStatus**](/windows/desktop/FileIO/postqueuedcompletionstatus), but is not calling [**GetQueuedCompletionStatus**](/windows/win32/api/ioapiset/nf-ioapiset-getqueuedcompletionstatus) to free them, or when a process is queuing completion entries to a port, but there is no thread retrieving the entries. To detect a leak run the [**!poolused**](-poolused.md) extension and check the value of ICP pool tag. If pool use with the ICP tag is significant, a leak might have occurred.

This extension works only if the system maintains type lists. If the *HandleFlag* is set and the system has many processes, this extension will take a long time to run.

You can stop at any point by pressing CTRL+BREAK (in WinDbg) or CTRL+C (in KD).

 

