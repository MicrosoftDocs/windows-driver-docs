---
title: Failure to Check a Driver's State
description: Failure to Check a Driver's State
keywords: ["reliability WDK kernel , driver state checking", "checking driver states", "driver state checking", "verifying driver states", "correct device states WDK kernel", "device states WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Failure to Check a Driver's State





In the following example, the driver uses the **ASSERT** macro to check for the correct device state in a debug version of a driver image, but does not check device state in the retail build of the same driver source:

```cpp
   case IOCTL_WAIT_FOR_EVENT:

      ASSERT((!Extension->WaitEventIrp));
      Extension->WaitEventIrp = Irp;
      IoMarkIrpPending(Irp);
      status = STATUS_PENDING;
```

In the debug driver image, if the driver already holds the IRP pending, the system will assert. In a retail build, however, the driver does not check for this error. Two calls to the same IOCTL cause the driver to lose track of an IRP.

On a multiprocessor system, this code fragment might cause additional problems. Assume that on entry this routine has ownership of (the right to manipulate) this IRP. When the routine saves the **Irp** pointer in the global structure at **Extension-&gt;WaitEventIrp**, another thread can get the IRP address from that global structure and perform operations on the IRP. To prevent this problem, the driver should mark the IRP pending before it saves the IRP and should include both the call to [**IoMarkIrpPending**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iomarkirppending) and the assignment in an interlocked sequence. A [*Cancel*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_cancel) routine for the IRP might also be necessary.

 

