---
title: Security Issues for Section Objects and Views
description: Security Issues for Section Objects and Views
ms.assetid: a2044ea1-c90c-4487-850b-d07ac55aea6d
keywords: ["memory sections WDK kernel", "section objects WDK kernel", "views WDK memory section", "security WDK memory section", "protocols WDK memory section"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Security Issues for Section Objects and Views





Drivers that create sections and views that are not to be shared with user mode must use the following protocol when they are working with sections and views:

-   The driver must use a kernel handle when it is opening a handle to the section object. Drivers can make sure that a handle is a kernel handle by either creating it in the system process, or specifying the OBJ\_KERNEL\_HANDLE attribute for the handle. For more information, see [Object Handles](object-handles.md).

-   The view must be mapped only from a system thread. (Otherwise, the view is accessible from the process whose context it is created in.) A driver can make sure that the view is mapped from the system process by using a system worker thread to perform the mapping operation. For more information, see [System Worker Threads](system-worker-threads.md) and [Driver Thread Context](driver-thread-context.md).

Drivers that share a view with a user-mode process must use the following protocol when they are working with sections and views:

-   The driver, not the user-mode process, must create the section object and map the views.

-   As mentioned earlier, the driver must use a kernel handle when it is opening a handle to the section object. Drivers can make sure that a handle is a kernel handle by either creating it in the system process, or specifying the OBJ\_KERNEL\_HANDLE attribute for the handle. For more information, see [Object Handles](object-handles.md).

-   The view is mapped in the thread context of the process that shares the view. A highest-level driver can guarantee the view is mapped in the current process context by performing the mapping operation in a dispatch routine, such [*DispatchDeviceControl*](https://msdn.microsoft.com/library/windows/hardware/ff543287). Dispatch routines of lower-level drivers run in an arbitrary thread context, and thus cannot safely map a view in a dispatch routine. For more information, see [Driver Thread Context](driver-thread-context.md).

-   All memory accesses to the view within the driver must be protected by **try**-**except** blocks. A malicious user-mode application could unmap the view or change the protection state of the view. Either would cause a system crash unless protected by a **try**-**except** block. For more information, see [Handling Exceptions](handling-exceptions.md).

The driver must also validate the contents of the view as necessary. The driver writer cannot assume that only a trusted user-mode component will have access to the view.

A driver that must share a section object with a user-mode application (that must be able to create its own views) must use the following protocol:

-   The driver, not the user-mode process, must create the section object. Drivers must never use a handle that was passed from user mode.

-   Before passing the handle to user mode, the driver must call [**ObReferenceObjectByHandle**](https://msdn.microsoft.com/library/windows/hardware/ff558679) to obtain a reference to the section object. This prevents a malicious application from deleting the section object by closing the handle. The object reference should be stored in the driver's device extension.

-   After the driver is no longer using the section object, it must call [**ObDereferenceObject**](https://msdn.microsoft.com/library/windows/hardware/ff557724) to release the object reference.

On systems that run Microsoft Windows Server 2003 with Service Pack 1 (SP1) and later versions, only kernel-mode drivers can open \\**Device**\\**PhysicalMemory**. However, drivers can decide to give a handle to a user application. To prevent security issues, only user applications that the driver trusts should be given access to \\**Device**\\**PhysicalMemory**.

 

 




