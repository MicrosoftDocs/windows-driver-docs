---
title: Driver x64 Restrictions
description: Provides information about driver x64 restrictions.
ms.date: 01/15/2025
ms.topic: concept-article
---

# Driver x64 restrictions

On x64-based systems, kernel code and certain kernel data structures are protected from modification. Any driver that attempts to modify such code or data will cause the system to bug check (with the CRITICAL_STRUCTURE_CORRUPTION bug check).

Drivers for x64-based systems must avoid operations that might trigger this bug check. In particular, drivers must not:

- Attempt to modify kernel code at run time.

- Implement and use their own stacks.

- Modify hardware dispatch tables, such as the interrupt dispatch table (IDT) or global descriptor table (GDT).

- Modify undocumented kernel data structures.

Even though the preceding operations won't trigger a bug check on x86-based or Itanium-based systems, drivers shouldn't perform any of these operations on any platform. These operations might not work in future versions of the Microsoft Windows operating system.

For general information about programming with a 64-bit compiler, see [64-Bit Programming with Visual C++](/cpp/build/configuring-programs-for-64-bit-visual-cpp).
