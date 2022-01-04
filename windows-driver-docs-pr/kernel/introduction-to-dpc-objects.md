---
title: Introduction to DPC Objects
description: Introduction to DPC Objects
ms.date: 10/17/2018
---

# Introduction to DPC Objects





Because ISRs must execute as quickly as possible, drivers must usually postpone the completion of servicing an interrupt until after the ISR returns. Therefore, the system provides support for *deferred procedure calls* (DPCs), which can be queued from ISRs and which are executed at a later time and at a lower IRQL than the ISR.

Each DPC is associated with a system-defined *DPC object*. The system supplies one DPC object for each device object. The system initializes this DPC object when a driver registers a DPC routine known as the [*DpcForIsr*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_dpc_routine) routine. A driver can create additional DPC objects if more than one DPC is needed. These extra DPCs are known as [*CustomDpc*](/windows-hardware/drivers/ddi/wdm/nc-wdm-kdeferred_routine) routines.

DPC object contents should not be directly referenced by drivers. The object's structure is not documented. Drivers do not have access to the system-supplied DPC object assigned to each device object. Drivers allocate storage for extra DPCs, but the contents of these DPC objects should only be referenced by system routines.

DPC objects and DPCs can also be used with timers. For more information, see [Timer Objects and DPCs](timer-objects-and-dpcs.md).

 

