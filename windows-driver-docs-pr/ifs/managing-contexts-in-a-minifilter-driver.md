---
title: Managing Contexts in a Minifilter Driver
author: windows-driver-content
description: Managing Contexts in a Minifilter Driver
ms.assetid: c7186886-f083-45c9-a39d-3f8ce7df35bb
keywords: ["file system minifilter drivers WDK , contexts", "minifilter drivers WDK , context", "contexts WDK file system minifilter", "contexts WDK file system minifilter , about contexts"]
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Managing%20Contexts%20in%20a%20Minifilter%20Driver%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


