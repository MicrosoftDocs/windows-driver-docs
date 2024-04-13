---
title: WDM Interface Restrictions
description: WDM Interface Restrictions
keywords:
- KMDF WDK , WDM
- Kernel-Mode Driver Framework WDK , WDM
- WDM drivers WDK KMDF
- framework-based drivers WDK KMDF , WDM
ms.date: 04/20/2017
---

# WDM Interface Restrictions


\[Applies to KMDF only\]




If your framework-based driver accesses WDM interfaces, you must be aware of the following restrictions:

-   Framework-based drivers must not use the **Tail.Overlay.DriverContext** member of the [**IRP**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_irp) structure, because the framework uses this member.

 

