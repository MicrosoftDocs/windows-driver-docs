---
title: Rules for Implementing DispatchCreate, DispatchClose, and DispatchCreateClose Routines
description: Rules for Implementing DispatchCreate, DispatchClose, and DispatchCreateClose Routines
ms.assetid: 4ce37675-92a6-41c2-b386-6570c989e56c
keywords: ["dispatch routines WDK kernel , DispatchCreate routine", "dispatch routines WDK kernel , DispatchClose routine", "dispatch routines WDK kernel , DispatchCreateClose routine", "DispatchCreateClose routine", "DispatchClose routine", "DispatchCreate routine", "IRP_MJ_CREATE I/O function code", "IRP_MJ_CLOSE I/O function code", "create dispatch routines WDK kernel", "close dispatch routines WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Rules for Implementing DispatchCreate, DispatchClose, and DispatchCreateClose Routines





Keep the following points in mind when implementing *DispatchCreate*, *DispatchClose*, and *DispatchCreateClose* routines:

-   At a minimum, the routine must do the following:
    1.  Set the **Status** field of the input IRP's I/O status block with an appropriate NTSTATUS, usually STATUS\_SUCCESS.
    2.  Set the **Information** field of the input IRP's I/O status block to zero.
    3.  Call **IoCompleteRequest** with the IRP and a *PriorityBoost* of IO\_NO\_INCREMENT.
    4.  Return the NTSTATUS that it set in the **Status** field of the IRP's I/O status block.
-   In a highest-level or intermediate driver, the routine might have to do additional work to process a create or close request, depending on the nature of its device or of the underlying device, and on the design of the driver.

-   For a create request to open a file object that represents a logical or physical device, a highest-level driver should check the **FileObject.FileName** in the I/O stack location and complete the IRP with STATUS\_SUCCESS if the Unicode string at **FileName** has a zero length. Otherwise, it should complete the IRP with STATUS\_INVALID\_PARAMETER.

-   The routines of lowest-level drivers are called only when the next-higher-level driver calls **IoAttachDeviceToDeviceStack**, **IoGetDeviceObjectPointer**, or **IoAttachDevice**. The lowest-level driver in a chain of layered drivers frequently does only the minimum required processing of a create or close request.

 

 




