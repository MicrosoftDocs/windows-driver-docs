---
title: Advantages of the Filter Manager Model
description: Advantages of the Filter Manager Model
ms.assetid: 8e3449dc-7c78-4f78-97c4-89b20001e91b
keywords:
- filter manager WDK file system minifilter , advantages
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Advantages of the Filter Manager Model


## <span id="ddk_returning_status_from_a_minifilter_driverentry_routine_if"></span><span id="DDK_RETURNING_STATUS_FROM_A_MINIFILTER_DRIVERENTRY_ROUTINE_IF"></span>


The filter manager model offers the following advantages over the existing legacy filter driver model:

-   **Better control over filter load order.** Unlike a legacy filter driver, a minifilter driver can be loaded at any time and attached at the appropriate location as determined by its altitude.

-   **Ability to unload while system is running.** Unlike a legacy filter driver, which cannot be unloaded while the system is running, a minifilter driver can be unloaded at any time, and it can prevent itself from being unloaded if necessary. The filter manager synchronizes safe removal of all minifilter driver attachments, and it handles operations that complete after the minifilter driver is unloaded.

-   **Ability to process only necessary operations.** The filter manager uses a callback model in which a minifilter driver can choose which types of I/O operations (IRP-based, fast I/O, or FSFilter) to filter. The minifilter driver receives only I/O requests for which it has registered callback routines. A minifilter driver can register a unique preoperation or postoperation callback routine, or both, and it can ignore certain types of operations, such as paging I/O and cached I/O.

-   **More efficient use of kernel stack.** The filter manager is optimized to reduce the amount of kernel stack it uses, and the callback model greatly reduces the impact of minifilter drivers on the stack. The filter manager reduces the impact of recursive I/O by supporting filter-initiated I/O that is seen only by lower drivers in the stack.

-   **Less redundant code.** The filter manager reduces the amount of code required for a minifilter driver in a number of ways, such as providing infrastructure for name generation and caching file names for use by more than one minifilter driver. The filter manager attaches to volumes and notifies minifilter drivers when a volume is available. The filter manager is optimized to support multiprocessor systems, which makes locking both more efficient and less prone to error.

-   **Reduced complexity.** The filter manager simplifies filtering I/O requests by providing support routines for common functionality, such as naming, context management, communication between user mode and kernel mode, and masking differences between file systems. The filter manager handles certain tasks on behalf of minifilter drivers, such as pending IRPs and enumerating and attaching to file system stacks.

-   **Easier addition of new operations.** Because minifilter drivers register only for the I/O operations they will handle, support for new operations can be added to the filter manager without breaking existing minifilter drivers.

-   **Better support for multiple platforms.** A minifilter driver can run on any version of Windows that supports the filter manager. If a minifilter driver registers for an I/O operation that isn't available at runtime, the filter manager simply doesn't call the minifilter driver for that operation. A minifilter driver can determine programmatically whether functions are available, and filter manager structures are designed to be extensible.

-   **Better support for user-mode applications.** The filter manager provides common functionality for user-mode services and control programs that work with minifilter drivers. The filter manager user-mode library, Filterlib.dll, enables communication between a user-mode service or control program and a minifilter driver. Filterlib.dll also provides interfaces for management tools.

 

 




