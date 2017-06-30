---
title: Windows Kernel-Mode Object Manager
author: windows-driver-content
description: Windows Kernel-Mode Object Manager
ms.assetid: f10561a3-d831-4c13-9edf-be40fb1db403
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Windows%20Kernel-Mode%20Object%20Manager%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


