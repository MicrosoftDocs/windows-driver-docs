---
title: Remove Section in a Network INF File
description: Remove Section in a Network INF File
ms.assetid: c9be4e98-fa35-4966-895a-aebe29f16289
keywords:
- INF files WDK network , Remove section
- network INF files WDK , Remove section
- Remove section WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Remove Section in a Network INF File





**Remove** sections are supported for **NetClient**, **NetTrans**, and **NetService** components but not for **Net** components (adapters).

**Note**  **NetClient** components are deprecated in Windows 8.1, Windows Server 2012 R2, and later.

 

The network class installer does not keep track of adapter instances. A **Remove** section that removes files that are shared by other adapters or by multiple instances of an adapter could render those adapters or adapter instances inoperative.
If it is necessary to remove a driver file that is used by a **Net** component, use a co-installer that keeps track of all drivers that are using the file. Such a co-installer should also track multiple instances of the same device, as well as drivers for multiple devices. For more information about co-installers, see [Creating an INF File](https://msdn.microsoft.com/library/windows/hardware/ff549520).

 

 





