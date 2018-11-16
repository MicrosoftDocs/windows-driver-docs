---
title: Handle Management
description: Handle Management
ms.assetid: 09d9c836-1754-4a50-92a3-229a3ae05ccb
keywords:
- handles WDK file systems
- security WDK file systems , minimizing threats
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handle Management


## <span id="ddk_handle_management_if"></span><span id="DDK_HANDLE_MANAGEMENT_IF"></span>


A significant source of security issues within drivers is the use of handles passed between user-mode and kernel-mode components. There are a number of known problems with handle usage within the kernel environment, including the following:

-   An application that passes the wrong type of handle to a kernel driver. The kernel driver might crash trying to use an event object where a file object is needed.

-   An application that passes a handle to an object for which it does not have the necessary access. The kernel driver might perform an operation that works because the call comes from kernel mode, even though the user does not have adequate permissions to do so.

-   An application that passes a value that is not a valid handle in its address space, but is marked as a system handle to perform a malicious operation against the system.

-   An application that passes a value that is not an appropriate handle for the device object (a handle that this driver didn't create).

To protect against these issues, a kernel driver must be particularly careful to ensure that handles passed to it are valid. The safest policy is to create any needed handles within the context of the driver. These handles, created by kernel drivers, should specify the OBJ\_KERNEL\_HANDLE option, which will create a handle valid in arbitrary process context and one that can only be accessed from a kernel-mode caller.

For drivers that use handles created by an application program, the use of these handles must be done with extreme care:

-   The best practice is to convert the handle to an object pointer by calling [**ObReferenceObjectByHandle**](https://msdn.microsoft.com/library/windows/hardware/ff558679), specifying the correct *AccessMode* (usually from Irp-&gt;RequestorMode), *DesiredAccess*, and *ObjectType* parameters, such as IoFileObjectType or ExEventObjectType.

-   If a handle must be used directly within a call, it is best to use the Nt variants of functions rather than the Zw variants of functions. This will enforce parameter checking and handle validation by the operating system since the previous mode will be **UserMode** and hence untrusted. Note that parameters passed to Nt functions that are pointers may fail validation if the previous mode is **UserMode**. The Nt and Zw routines return an *IoStatusBlock* parameterwith error information that you should check for errors.

-   Errors must be appropriately trapped as well using \_\_try and \_\_except as necessary. Many of the cache manager (Cc), memory manager (Mm), and file system runtime library routines (FsRtl) raise an exception when an error occurs.

No driver should ever rely on handles or parameters passed from a user-mode application without taking appropriate precautions.

Note that if the Nt variant is used to open a file, then the Nt variant must also be used to close the file.

 

 




