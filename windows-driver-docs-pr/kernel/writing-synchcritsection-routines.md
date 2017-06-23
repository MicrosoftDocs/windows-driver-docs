---
title: Writing SynchCritSection Routines
author: windows-driver-content
description: Writing SynchCritSection Routines
ms.assetid: b02e230e-48f1-43dc-b5aa-368cd7b5436f
keywords: ["SynchCritSection", "critical section routines WDK kernel"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Writing SynchCritSection Routines


## <a href="" id="ddk-writing-synchcritsection-routines-kg"></a>


Drivers use their [*SynchCritSection*](https://msdn.microsoft.com/library/windows/hardware/ff563928) routines for either of two basic purposes:

[Programming a device for an I/O operation](programming-a-device-for-an-i-o-operation.md)

[Accessing shared state information](accessing-shared-state-information.md)

Like an ISR, a *SynchCritSection* routine must execute as quickly as possible, doing only what is necessary to set up device registers or update context data, before returning.

Because [**KeSynchronizeExecution**](https://msdn.microsoft.com/library/windows/hardware/ff553302) holds a device driver's interrupt spin lock while its *SynchCritSection* routine runs, the driver's ISR cannot execute until the *SynchCritSection* routine returns control.

For any received IRP, a device driver should do as much I/O processing as possible either at IRQL PASSIVE\_LEVEL in its dispatch routines (or possibly [device-dedicated threads](device-dedicated-threads.md)), or at IRQL DISPATCH\_LEVEL in its [*StartIo*](https://msdn.microsoft.com/library/windows/hardware/ff563858) routine and DPC routines.

For additional information about how critical sections are synchronized, see [Using Spin Locks: An Example](using-spin-locks--an-example.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Writing%20SynchCritSection%20Routines%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


