---
title: Errors in Handling Cleanup and Close Operations
description: Errors in Handling Cleanup and Close Operations
ms.assetid: 9d449974-99b1-4d38-9bbb-54938d67c23a
keywords: ["reliability WDK kernel , errors", "DispatchClose", "DispatchCleanup", "cleanup errors WDK kernel", "close errors WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Errors in Handling Cleanup and Close Operations





Some drivers fail to distinguish the tasks required in [*DispatchCleanup*](https://msdn.microsoft.com/library/windows/hardware/ff543233) and [*DispatchClose*](https://msdn.microsoft.com/library/windows/hardware/ff543255) routines. The I/O manager calls a driver's *DispatchCleanup* routine when the last handle to a file object is closed. The *DispatchClose* routine is called when the last reference is released from the file object. A driver should not attempt to free resources in its *DispatchCleanup* routine that are attached to a file object or might be used by other *Dispatch*Xxx routines.

When calling dispatch routines, the I/O manager holds a reference to the file object for normal I/O calls. As a result, a driver can receive I/O requests for a file object after its *DispatchCleanup* routine has been called but before its *DispatchClose* routine is called. For example, a user-mode caller might close the file handle while an I/O manager request is in progress from another thread. If the driver has deleted or freed necessary resources before the I/O manager calls its *DispatchClose* routine, invalid pointer references and other problems could occur.

 

 




