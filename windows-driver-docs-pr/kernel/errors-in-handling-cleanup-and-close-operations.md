---
title: Errors in Handling Cleanup and Close Operations
author: windows-driver-content
description: Errors in Handling Cleanup and Close Operations
MS-HAID:
- 'Other\_a002ad7b-1586-434a-925f-1db8ec73dc46.xml'
- 'kernel.errors\_in\_handling\_cleanup\_and\_close\_operations'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 9d449974-99b1-4d38-9bbb-54938d67c23a
keywords: ["reliability WDK kernel , errors", "DispatchClose", "DispatchCleanup", "cleanup errors WDK kernel", "close errors WDK kernel"]
---

# Errors in Handling Cleanup and Close Operations


## <a href="" id="ddk-errors-in-handling-cleanup-and-close-operations-kg"></a>


Some drivers fail to distinguish the tasks required in [*DispatchCleanup*](https://msdn.microsoft.com/library/windows/hardware/ff543233) and [*DispatchClose*](https://msdn.microsoft.com/library/windows/hardware/ff543255) routines. The I/O manager calls a driver's *DispatchCleanup* routine when the last handle to a file object is closed. The *DispatchClose* routine is called when the last reference is released from the file object. A driver should not attempt to free resources in its *DispatchCleanup* routine that are attached to a file object or might be used by other *Dispatch*Xxx routines.

When calling dispatch routines, the I/O manager holds a reference to the file object for normal I/O calls. As a result, a driver can receive I/O requests for a file object after its *DispatchCleanup* routine has been called but before its *DispatchClose* routine is called. For example, a user-mode caller might close the file handle while an I/O manager request is in progress from another thread. If the driver has deleted or freed necessary resources before the I/O manager calls its *DispatchClose* routine, invalid pointer references and other problems could occur.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Errors%20in%20Handling%20Cleanup%20and%20Close%20Operations%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


