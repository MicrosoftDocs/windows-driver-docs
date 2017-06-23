---
title: Security Issues for Section Objects and Views
author: windows-driver-content
description: Security Issues for Section Objects and Views
ms.assetid: a2044ea1-c90c-4487-850b-d07ac55aea6d
keywords: ["memory sections WDK kernel", "section objects WDK kernel", "views WDK memory section", "security WDK memory section", "protocols WDK memory section"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Security Issues for Section Objects and Views


## <a href="" id="ddk-security-issues-for-section-objects-and-views-kg"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Security%20Issues%20for%20Section%20Objects%20and%20Views%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


