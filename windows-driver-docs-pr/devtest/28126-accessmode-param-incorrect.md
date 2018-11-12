---
title: C28126
description: Warning C28126 The AccessMode parameter to ObReferenceObject* should be IRP->RequestorMode.
ms.assetid: be8f909e-2d4a-4e22-b457-81a048d90df8
keywords:
- warnings listed WDK PREfast for Drivers
- errors listed WDK PREfast for Drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# C28126


warning C28126: The AccessMode parameter to ObReferenceObject\* should be IRP-&gt;RequestorMode

In a call to [**ObReferenceObjectByHandle**](https://msdn.microsoft.com/library/windows/hardware/ff558679) or [**ObReferenceObjectByPointer**](https://msdn.microsoft.com/library/windows/hardware/ff558686), the driver is passing **UserMode** or **KernelMode** for the *AccessMode* parameter, instead of using **Irp-&gt;RequestorMode**.

The driver should use **Irp-&gt;RequestorMode**, rather than specifying **UserMode** or **KernelMode**. This allows the senders of kernel-mode IRP to supply kernel-mode handles safely.

This warning is intended for the top-level driver in the driver stack. You can ignore or suppress this warning for all other drivers.

The top-level driver in the driver stack should use **Irp-&gt;RequestorMode**, rather than specifying **UserMode** or **KernelMode**. This allows the senders of kernel-mode IRP to supply kernel-mode handles safely. All other drivers in the stack should specify **KernelMode**, which skips the access check and leaves responsibility for the access check to the top-level driver.

 

 





