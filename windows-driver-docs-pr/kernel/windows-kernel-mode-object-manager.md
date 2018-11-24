---
title: Windows Kernel-Mode Object Manager
description: Windows Kernel-Mode Object Manager
ms.assetid: f10561a3-d831-4c13-9edf-be40fb1db403
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Windows Kernel-Mode Object Manager


The Windows kernel-mode object manager component manages *objects*. Files, devices, synchronization mechanisms, registry keys, and so on, are all represented as objects in kernel mode. Each object has a *header* (containing information about the object such as its name, type, and location), and a *body* (containing data in a format determined by each type of object).

Windows has more than 25 types of objects. A few of the types are:

-   Files

-   Devices

-   Threads

-   Processes

-   Events

-   Mutexes

-   Semaphores

-   Registry keys

-   Jobs

-   Sections

-   Access tokens

-   Symbolic links

The object manager manages the objects in Windows by performing the following major tasks:

-   Managing the creation and destruction of objects.

-   Keeping an object namespace database for tracking object information.

-   Keeping track of resources assigned to each process.

-   Tracking access rights for specific objects to provide security.

-   Managing the lifetime of an object and determining when an object will be automatically destroyed to recycle resource space.

For more information about objects in Windows, see [Device Objects and Device Stacks](device-objects-and-device-stacks.md).

Routines that provide a direct interface to the object manager are usually prefixed with the letters "**Ob**"; for example, **ObGetObjectSecurity**. For a list of object manager routines, see [Object Manager Routines](https://msdn.microsoft.com/library/windows/hardware/ff557759).

Note that Windows uses objects as an abstraction for resources. However, Windows is not object-oriented in the classical C++ meaning of the term. Windows is *object-based*. For more information on what object-based means for Windows, see [Object-Based](object-based.md).

 

 




