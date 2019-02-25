---
title: WDM Interface Restrictions
description: WDM Interface Restrictions
ms.assetid: 89f3793e-8561-4d8a-a01a-1ff7aecca64a
keywords:
- KMDF WDK , WDM
- Kernel-Mode Driver Framework WDK , WDM
- WDM drivers WDK KMDF
- framework-based drivers WDK KMDF , WDM
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WDM Interface Restrictions


\[Applies to KMDF only\]




If your framework-based driver accesses WDM interfaces, you must be aware of the following restrictions:

-   Framework-based drivers must not use the **Tail.Overlay.DriverContext** member of the [**IRP**](https://msdn.microsoft.com/library/windows/hardware/ff550694) structure, because the framework uses this member.

 

 





