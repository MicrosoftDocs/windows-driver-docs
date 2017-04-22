---
title: WDM Interface Restrictions
author: windows-driver-content
description: WDM Interface Restrictions
ms.assetid: 89f3793e-8561-4d8a-a01a-1ff7aecca64a
keywords:
- KMDF WDK , WDM
- Kernel-Mode Driver Framework WDK , WDM
- WDM drivers WDK KMDF
- framework-based drivers WDK KMDF , WDM
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WDM Interface Restrictions


\[Applies to KMDF only\]

## <a href="" id="ddk-framework-compatibility-with-wdm-df"></a>


If your framework-based driver accesses WDM interfaces, you must be aware of the following restrictions:

-   Framework-based drivers must not use the **Tail.Overlay.DriverContext** member of the [**IRP**](https://msdn.microsoft.com/library/windows/hardware/ff550694) structure, because the framework uses this member.

 

 





