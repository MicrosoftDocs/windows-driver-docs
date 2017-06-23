---
title: Managing Kernel Objects
author: windows-driver-content
description: Managing Kernel Objects
ms.assetid: d45aca94-67b7-444d-8585-713ec982e3bc
keywords: ["kernel-mode drivers WDK , object management", "object manager WDK kernel", "object management WDK kernel", "referencing objects", "object names WDK user-mode", "object management WDK user-mode", "kernel-mode objects WDK"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Managing Kernel Objects


## <a href="" id="ddk-object-management-kg"></a>


The Windows Object Manager controls *objects* that are part of the kernel-mode operating system. An object is a collection of data that the operating system manages.

Typical kernel-mode objects include the following objects:

-   Device objects (See [Device Objects and Device Stacks](device-objects-and-device-stacks.md).)

-   File objects.

-   Symbolic links.

-   Registry keys.

-   Threads and processes.

-   Kernel dispatcher objects, such as event objects and mutex objects. (See [Kernel Dispatcher Objects](kernel-dispatcher-objects.md).)

-   Callback objects. (See [Callback Objects](callback-objects.md).)

-   Section objects. (See [Section Objects and Views](section-objects-and-views.md).)

Kernel-mode objects enable you to manipulate objects in partnership with the object manager without damaging the portions of the objects that the operating system needs. This principle is called *encapsulation* and is one of the core concepts of object-orientated programming. (Because kernel-mode objects do not provide other aspects of object-orientation, kernel-mode programming is typically referred to as [*object-based*](object-based.md).) Kernel-mode objects do not follow the same rules as objects in C++ or Microsoft COM.

Kernel-mode objects can be referenced by pointers. An object may have an object name. For more information about object names, see [Object Names](object-names.md).

User-mode programmers can reference objects only through indirection, using a *handle*. If an object has a name, you can use it to obtain the handle in user mode. For more information about handles, see [Object Handles](object-handles.md).

Kernel-mode objects have a very specific life-cycle. For more information about object life-cycles, see [Life Cycle of an Object](life-cycle-of-an-object.md).

Object security is a prime concern for kernel-mode programming. For more information on object security, see [Object Security](object-security.md).

The kernel-mode environment stores objects in a virtual directory system, also known as the object namespace. This allows objects to be accessed in a hierarchical way with parent and child objects. This namespace is similar to a file system set of directories but does not exactly correspond to a particular file system on your computer. For more information about object directories, see [Object Directories](object-directories.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Managing%20Kernel%20Objects%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


