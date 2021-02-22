---
title: Accessing WDM Interfaces in KMDF Drivers
description: Most Kernel-Mode Driver Framework (KMDF) drivers do not need to access Windows Driver Model (WDM) interfaces directly.
keywords:
- kernel-mode drivers WDK KMDF , WDM
- KMDF WDK , WDM
- Kernel-Mode Driver Framework WDK , WDM
- framework-based drivers WDK KMDF , WDM
- WDM interfaces WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Accessing WDM Interfaces in KMDF Drivers


\[Applies to KMDF only\]

Most Kernel-Mode Driver Framework (KMDF) drivers do not need to access Windows Driver Model (WDM) interfaces directly. This section describes the limited cases when a KMDF driver requires direct access to WDM data structures, for example to obtain WDM information or manipulate an IRP.

## In this section


-   [Obtaining WDM Information](obtaining-wdm-information.md)
-   [Handling WDM IRPs Outside of the Framework](handling-wdm-irps-outside-of-the-framework.md)
-   [WDM Interface Restrictions](wdm-interface-restrictions.md)

 

 





