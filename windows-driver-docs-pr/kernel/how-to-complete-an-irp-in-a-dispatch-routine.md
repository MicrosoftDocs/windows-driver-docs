---
title: How to Complete an IRP in a Dispatch Routine
description: How to Complete an IRP in a Dispatch Routine
ms.assetid: b29da791-e768-4f67-8e85-6cfbeca97220
keywords: ["completing IRPs WDK kernel , dispatch routines", "dispatch routines WDK kernel , completing IRPs", "status information WDK IRPs", "I/O status blocks WDK kernel", "status blocks WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# How to Complete an IRP in a Dispatch Routine





If an input IRP can be completed immediately, a dispatch routine does the following:

1.  Sets the **Status** and **Information** members of the IRP's I/O status block with appropriate values, in general:

    -   The dispatch routine sets **Status** either to STATUS\_SUCCESS or to an appropriate error (STATUS\_*XXX*), which can be the value returned by a call to a support routine or, for certain synchronous requests, by a lower driver.

        If a lower-level driver returns STATUS\_PENDING, a higher-level driver should not call [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) for the IRP, with one exception: The higher-level driver can use an event to synchronize between its [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine and its dispatch routine, in which case the *IoCompletion* routine signals the event and returns STATUS\_MORE\_PROCESSING\_REQUIRED. The dispatch routine waits for the event and then calls **IoCompleteRequest** to complete the IRP.

    -   It sets **Information** to the number of bytes successfully transferred if a request to transfer data, such as a read or write request, was satisfied.

    -   It sets **Information** to a value that varies according to the specific request for other IRPs that it completes with STATUS\_SUCCESS.

    -   It sets **Information** to a value that varies according to the specific request for IRPs that it completes with a warning STATUS\_*XXX*. For example, it would set **Information** to the number of bytes transferred for such a warning as STATUS\_BUFFER\_OVERFLOW.

    -   Usually, it sets **Information** to zero for requests that it completes with an error STATUS\_*XXX*.

2.  Calls **IoCompleteRequest** with the IRP and with *PriorityBoost* = IO\_NO\_INCREMENT.

3.  Returns the appropriate STATUS\_*XXX* that it already set in the I/O status block. Note that a call to **IoCompleteRequest** makes the given IRP inaccessible by the caller, so the return value from a dispatch routine cannot be set from the I/O status block of an already completed IRP.

**Follow this implementation guideline for calling IoCompleteRequest with an IRP:**

Always release any spin lock(s) the driver is holding before calling **IoCompleteRequest**.

It takes an indeterminate amount of time to complete an IRP, particularly in a chain of layered drivers. Moreover, a deadlock can occur if a higher-level driver's *IoCompletion* routine sends an IRP back down to a lower driver that is holding a spin lock.

 

 




