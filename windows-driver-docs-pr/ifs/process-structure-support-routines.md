---
title: Process Structure Support Routines
description: Process Structure Support Routines
ms.assetid: 2cf3ab25-9db8-4a20-982d-eda0c3c96dbc
ms.date: 09/30/2019
ms.localizationpriority: medium
---

# Process Structure Support Routines

The following table lists the subset of system-supplied process structure support routines that can be used by kernel-mode file systems and by minifilter and legacy filter drivers. These routines cannot be used by device drivers.

In addition to the routines documented here, file systems and filter drivers can also call any of the **Ps**_Xxx_ routines that are described in the Kernel-Mode Driver Architecture Reference section and that are declared in *ntifs.h*.

**Header File:** *ntifs.h*

**Prefix: Ps**_Xxx_

| Function or Macro | Description |
| ----------------- | ----------- |
| **PsChargePoolQuota** | Charges pool quota of the specified pool type to the specified process. |
| **PsDereferenceImpersonationToken** | Decrements the reference count of an impersonation token. |
| **PsDereferencePrimaryToken** | Decrements the reference count of a primary token. |
| **PsIsDiskCountersEnabled** | Returns the enabled state of the per-process disk I/O counters. |
| **PsGetProcessExitTime** | Returns the exit time for the current process. |
| **PsImpersonateClient** | Causes a server thread to impersonate a client. |
| **PsIsThreadTerminating** | Checks whether a thread is terminating. |
| **PsLookupProcessByProcessId** | Accepts the process ID of a process and returns a referenced pointer to EPROCESS structure of the process. |
| **PsLookupThreadByThreadId** | Accepts the thread ID of a thread and returns a referenced pointer to the ETHREAD structure of the thread. |
| **PsReferenceImpersonationToken** | Increments the reference count of the impersonation token for the specified thread. |
| **PsReferencePrimaryToken** | Increments the reference count of the primary token for the specified process. |
| **PsReturnPoolQuota** | Returns pool quota of the specified pool type to the specified process. |
| **PsRevertToSelf** | Ends the calling thread's impersonation of a client. |
| **PsUpdateDiskCounters** | Updates the disk I/O counters of a given process. |
