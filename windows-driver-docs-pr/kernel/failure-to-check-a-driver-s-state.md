---
title: Failure to Check a Driver's State
author: windows-driver-content
description: Failure to Check a Driver's State
ms.assetid: 963f79f6-2282-41bd-9cf4-bd5bc02a510e
keywords: ["reliability WDK kernel , driver state checking", "checking driver states", "driver state checking", "verifying driver states", "correct device states WDK kernel", "device states WDK kernel"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Failure to Check a Driver's State


## <a href="" id="ddk-failure-to-check-a-driver-s-state-kg"></a>


In the following example, the driver uses the **ASSERT** macro to check for the correct device state in the checked build, but does not check device state in the free build:

```
   case IOCTL_WAIT_FOR_EVENT:

      ASSERT((!Extension->WaitEventIrp));
      Extension->WaitEventIrp = Irp;
      IoMarkIrpPending(Irp);
      status = STATUS_PENDING;
```

In the checked build, if the driver already holds the IRP pending, the system will assert. In the free build, however, the driver does not check for this error. Two calls to the same IOCTL cause the driver to lose track of an IRP.

On a multiprocessor system, this code fragment might cause additional problems. Assume that on entry this routine has ownership of (the right to manipulate) this IRP. When the routine saves the **Irp** pointer in the global structure at **Extension-&gt;WaitEventIrp**, another thread can get the IRP address from that global structure and perform operations on the IRP. To prevent this problem, the driver should mark the IRP pending before it saves the IRP and should include both the call to [**IoMarkIrpPending**](https://msdn.microsoft.com/library/windows/hardware/ff549422) and the assignment in an interlocked sequence. A [*Cancel*](https://msdn.microsoft.com/library/windows/hardware/ff540742) routine for the IRP might also be necessary.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Failure%20to%20Check%20a%20Driver's%20State%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


