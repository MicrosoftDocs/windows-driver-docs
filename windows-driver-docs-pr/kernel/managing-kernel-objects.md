---
title: Managing Kernel Objects
description: Managing Kernel Objects
ms.assetid: d45aca94-67b7-444d-8585-713ec982e3bc
keywords: ["kernel-mode drivers WDK , object management", "object manager WDK kernel", "object management WDK kernel", "referencing objects", "object names WDK user-mode", "object management WDK user-mode", "kernel-mode objects WDK"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Managing Kernel Objects





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

Kernel-mode objects enable you to manipulate objects in partnership with the object manager without damaging the portions of the objects that the operating system needs. This principle is called *encapsulation* and is one of the core concepts of object-oriented programming. (Because kernel-mode objects do not provide other aspects of object-orientation, kernel-mode programming is typically referred to as [*object-based*](object-based.md).) Kernel-mode objects do not follow the same rules as objects in C++ or Microsoft COM.

Kernel-mode objects can be referenced by pointers. An object may have an object name. For more information about object names, see [Object Names](object-names.md).

User-mode programmers can reference objects only through indirection, using a *handle*. If an object has a name, you can use it to obtain the handle in user mode. For more information about handles, see [Object Handles](object-handles.md).

Kernel-mode objects have a very specific life-cycle. For more information about object life-cycles, see [Life Cycle of an Object](life-cycle-of-an-object.md).

Object security is a prime concern for kernel-mode programming. For more information on object security, see [Object Security](object-security.md).

The kernel-mode environment stores objects in a virtual directory system, also known as the object namespace. This allows objects to be accessed in a hierarchical way with parent and child objects. This namespace is similar to a file system set of directories but does not exactly correspond to a particular file system on your computer. For more information about object directories, see [Object Directories](object-directories.md).

 

 




