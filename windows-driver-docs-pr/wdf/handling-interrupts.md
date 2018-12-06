---
title: Handling interrupts in UMDF drivers
description: Handling Interrupts
ms.assetid: 5C8CB68A-EAE6-4AF9-8B10-F8B73B50DEB2
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling interrupts in UMDF drivers


[!include[UMDF 1 Deprecation](../umdf-1-deprecation.md)]

Starting in UMDF version 1.11, UMDF drivers can handle hardware interrupts. UMDF supports both line-based (both level-triggered and edge-triggered) and message-signaled (MSI) interrupts.

Line-based, level-triggered interrupts are available starting in Windows 8. MSI and line-based, edge-triggered interrupts are available on all operating systems that UMDF 1.11 supports.

Framework-based drivers manage hardware interrupts by using framework interrupt objects.

## In this section


-   [Creating an Interrupt Object](creating-an-interrupt-object-umdf.md)
-   [Enabling and Disabling Interrupts](enabling-and-disabling-interrupts-umdf.md)
-   [Servicing an Interrupt](servicing-an-interrupt-umdf.md)
-   [Using Work Items](using-workitems.md)
-   [Synchronizing Interrupt Code](synchronizing-interrupt-code-umdf.md)
-   [Deleting an Interrupt Object](deleting-an-interrupt-object.md)

 

 





