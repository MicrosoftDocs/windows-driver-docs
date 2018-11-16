---
title: Managing Contexts in a Minifilter Driver
description: Managing Contexts in a Minifilter Driver
ms.assetid: c7186886-f083-45c9-a39d-3f8ce7df35bb
keywords:
- file system minifilter drivers WDK , contexts
- minifilter drivers WDK , context
- contexts WDK file system minifilter
- contexts WDK file system minifilter , about contexts
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Managing Contexts in a Minifilter Driver


## <span id="ddk_writing_a_driverentry_routine_for_a_minifilter_driver_if"></span><span id="DDK_WRITING_A_DRIVERENTRY_ROUTINE_FOR_A_MINIFILTER_DRIVER_IF"></span>


A *context* is a structure that is defined by the minifilter driver and that can be associated with a filter manager object. Minifilter drivers can create and set contexts for the following objects:

-   Files (Windows Vista and later only.)

-   Instances

-   Volumes

-   Streams

-   Stream handles (file objects)

-   Transactions (Windows Vista and later only.)

Except for volume contexts, which must be allocated from nonpaged pool, contexts can be allocated from paged or nonpaged pool.

The filter manager deletes contexts automatically when the objects that they are attached to are deleted, when a minifilter driver instance is detached from a volume, or when the minifilter driver is unloaded.

This section includes:

[Registering Context Types](registering-context-types.md)

[Creating Contexts](creating-contexts.md)

[Setting Contexts](setting-contexts.md)

[Getting Contexts](getting-contexts.md)

[Referencing Contexts](referencing-contexts.md)

[Releasing Contexts](releasing-contexts.md)

[Deleting Contexts](deleting-contexts.md)

[Freeing Contexts](freeing-contexts.md)

[File System Support for Contexts](file-system-support-for-contexts.md)

[Best Practices](best-practices.md)

 

 




