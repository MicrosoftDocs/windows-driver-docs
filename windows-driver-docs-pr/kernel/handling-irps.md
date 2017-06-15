---
title: Handling IRPs
author: windows-driver-content
description: Handling IRPs
MS-HAID:
- 'IRPs\_ac1b8c23-bbc5-4d81-bbdd-255977d3b85c.xml'
- 'kernel.handling\_irps'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 5fb6d2b9-17ee-4e76-95e9-dd5a7d1e79de
keywords: ["kernel-mode drivers WDK , IRPs", "IRPs WDK kernel", "I/O request packets WDK kernel See IRPs WDK kernel", "IRP WDK See IRPs WDK"]
---

# Handling IRPs


## <a href="" id="ddk-handling-irps-kg"></a>


This section describes how kernel-mode drivers handle *I/O request packets* (IRPs). It contains the following sections:

[Overview of the Windows I/O Model](overview-of-the-windows-i-o-model.md)

[End-User I/O Requests and File Objects](end-user-i-o-requests-and-file-objects.md)

[The Life of an I/O Request](the-life-of-an-i-o-request.md)

[I/O Stack Locations](i-o-stack-locations.md)

[I/O Status Blocks](i-o-status-blocks.md)

[Passing IRPs down the Driver Stack](passing-irps-down-the-driver-stack.md)

[Creating IRPs for Lower-Level Drivers](creating-irps-for-lower-level-drivers.md)

[Queuing and Dequeuing IRPs](queuing-and-dequeuing-irps.md)

[Completing IRPs](completing-irps.md)

[Canceling IRPs](canceling-irps.md)

[Reusing IRPs](reusing-irps.md)

[Device Type-Specific I/O Requests](device-type-specific-i-o-requests.md)

[Using I/O Control Codes](using-i-o-control-codes.md)

[Using IRP Priority Hints](using-irp-priority-hints.md)

[IRP Processing Examples](irp-processing-examples.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Handling%20IRPs%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


