---
title: C28126 Warning
description: Warning C28126 The AccessMode parameter to ObReferenceObject* should be IRP->RequestorMode.
keywords:
- warnings listed WDK PREfast for Drivers
- errors listed WDK PREfast for Drivers
ms.date: 04/20/2017
f1_keywords: 
  - "C28126"
---

# C28126


warning C28126: The AccessMode parameter to ObReferenceObject\* should be IRP-&gt;RequestorMode

In a call to [**ObReferenceObjectByHandle**](/windows-hardware/drivers/ddi/wdm/nf-wdm-obreferenceobjectbyhandle) or [**ObReferenceObjectByPointer**](/windows-hardware/drivers/ddi/wdm/nf-wdm-obreferenceobjectbypointer), the driver is passing **UserMode** or **KernelMode** for the *AccessMode* parameter, instead of using **Irp-&gt;RequestorMode**.

The driver should use **Irp-&gt;RequestorMode**, rather than specifying **UserMode** or **KernelMode**. This allows the senders of kernel-mode IRP to supply kernel-mode handles safely.

This warning is intended for the top-level driver in the driver stack. You can ignore or suppress this warning for all other drivers.

The top-level driver in the driver stack should use **Irp-&gt;RequestorMode**, rather than specifying **UserMode** or **KernelMode**. This allows the senders of kernel-mode IRP to supply kernel-mode handles safely. All other drivers in the stack should specify **KernelMode**, which skips the access check and leaves responsibility for the access check to the top-level driver.

 

