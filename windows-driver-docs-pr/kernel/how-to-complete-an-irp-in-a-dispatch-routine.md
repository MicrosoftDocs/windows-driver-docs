---
title: How to Complete an IRP in a Dispatch Routine
author: windows-driver-content
description: How to Complete an IRP in a Dispatch Routine
MS-HAID:
- 'IRPs\_95ce4d15-44b7-44a2-b2bb-1e773c179198.xml'
- 'kernel.how\_to\_complete\_an\_irp\_in\_a\_dispatch\_routine'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: b29da791-e768-4f67-8e85-6cfbeca97220
keywords: ["completing IRPs WDK kernel , dispatch routines", "dispatch routines WDK kernel , completing IRPs", "status information WDK IRPs", "I/O status blocks WDK kernel", "status blocks WDK kernel"]
---

# How to Complete an IRP in a Dispatch Routine


## <a href="" id="ddk-how-to-complete-an-irp-in-a-dispatch-routine-kg"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20How%20to%20Complete%20an%20IRP%20in%20a%20Dispatch%20Routine%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


