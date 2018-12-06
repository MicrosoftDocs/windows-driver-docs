---
title: Driver x64 Restrictions
description: Driver x64 Restrictions
ms.assetid: 717ca559-93aa-48d6-8347-bfdf223f1aa4
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Driver x64 Restrictions


On x64-based systems, kernel code and certain kernel data structures are protected from modification. Any driver that attempts to modify such code or data will cause the system to bug check (with the CRITICAL\_STRUCTURE\_CORRUPTION bug check).

Drivers for x64-based systems must avoid operations that might trigger this bug check. In particular, drivers must not:

-   Attempt to modify kernel code at run time.

-   Implement and use their own stacks.

-   Modify hardware dispatch tables, such as the interrupt dispatch table (IDT) or global descriptor table (GDT).

-   Modify undocumented kernel data structures.

Even though the preceding operations will not trigger a bug check on x86-based or Itanium-based systems, drivers should not perform any of these operations on any platform. These operations might not work in future versions of the Microsoft Windows operating system.

For more information about modifying kernel code and data structures, see the [Patching Policy for x64-based Systems](http://go.microsoft.com/fwlink/p/?linkid=50719) white paper and the [64-Bit Patching FAQ](http://go.microsoft.com/fwlink/p/?linkid=69534).

For general information about programming with a 64-bit compiler, see [64-Bit Programming with Visual C++](http://go.microsoft.com/fwlink/p/?linkid=165521).

 

 




