---
title: Debugging an Application Failure
description: Debugging an Application Failure
keywords: ["application failures"]
ms.date: 05/23/2017
---

# Debugging an Application Failure

There are a variety of errors possible in user-mode applications.

The most common kinds of failures include access violations, alignment faults, exceptions, critical section time-outs (deadlocks), and in-page I/O errors.

Access violations and data type misalignments are among the most common. They usually occur when an invalid pointer is dereferenced. The blame could lie with the function that caused the fault, or with an earlier function that passed an invalid parameter to the faulting function.

User-mode exceptions have many possible causes. If an unknown exception occurs, locate it in ntstatus.h or winerror.h if possible.

Critical section timeouts (or possible deadlocks) occur when one thread is waiting for a critical section for a long time. These are difficult to debug and require an in-depth analysis of the stack trace.

In-page I/O errors are almost always hardware failures. You can double-check the status code in ntstatus.h to verify.

## See also

[Displaying a Critical Section](displaying-a-critical-section.md)

[Critical Section Time Outs](critical-section-time-outs.md) (user mode)
