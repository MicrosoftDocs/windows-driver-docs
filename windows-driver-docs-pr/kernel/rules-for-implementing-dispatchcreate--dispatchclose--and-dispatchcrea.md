---
title: Rules for Implementing DispatchCreate, DispatchClose, and DispatchCreateClose Routines
author: windows-driver-content
description: Rules for Implementing DispatchCreate, DispatchClose, and DispatchCreateClose Routines
ms.assetid: 4ce37675-92a6-41c2-b386-6570c989e56c
keywords: ["dispatch routines WDK kernel , DispatchCreate routine", "dispatch routines WDK kernel , DispatchClose routine", "dispatch routines WDK kernel , DispatchCreateClose routine", "DispatchCreateClose routine", "DispatchClose routine", "DispatchCreate routine", "IRP_MJ_CREATE I/O function code", "IRP_MJ_CLOSE I/O function code", "create dispatch routines WDK kernel", "close dispatch routines WDK kernel"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Rules for Implementing DispatchCreate, DispatchClose, and DispatchCreateClose Routines


## <a href="" id="ddk-rules-for-implementing-dispatchcreate-dispatchclose-and-dispatchcr"></a>


Keep the following points in mind when implementing *DispatchCreate*, *DispatchClose*, and *DispatchCreateClose* routines:

-   At a minimum, the routine must do the following:
    1.  Set the **Status** field of the input IRP's I/O status block with an appropriate NTSTATUS, usually STATUS\_SUCCESS.
    2.  Set the **Information** field of the input IRP's I/O status block to zero.
    3.  Call **IoCompleteRequest** with the IRP and a *PriorityBoost* of IO\_NO\_INCREMENT.
    4.  Return the NTSTATUS that it set in the **Status** field of the IRP's I/O status block.
-   In a highest-level or intermediate driver, the routine might have to do additional work to process a create or close request, depending on the nature of its device or of the underlying device, and on the design of the driver.

-   For a create request to open a file object that represents a logical or physical device, a highest-level driver should check the **FileObject.FileName** in the I/O stack location and complete the IRP with STATUS\_SUCCESS if the Unicode string at **FileName** has a zero length. Otherwise, it should complete the IRP with STATUS\_INVALID\_PARAMETER.

-   The routines of lowest-level drivers are called only when the next-higher-level driver calls **IoAttachDeviceToDeviceStack**, **IoGetDeviceObjectPointer**, or **IoAttachDevice**. The lowest-level driver in a chain of layered drivers frequently does only the minimum required processing of a create or close request.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Rules%20for%20Implementing%20DispatchCreate,%20DispatchClose,%20and%20DispatchCreateClose%20Routines%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


