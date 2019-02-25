---
title: Target Media for INF Files
description: Target Media for INF Files
ms.assetid: f1aaea38-e500-40a9-89c1-9c4447054fb1
keywords:
- INF files WDK device installations , target media
- target media WDK INF files
- locations WDK INF files
- media WDK INF files
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Target Media for INF Files





An INF file specifies the target location for device files that have a [**DestinationDirs**](inf-destinationdirs-section.md) section. This section should always be specified in the same INF file as the section with the copy, rename, or delete statements.

A **DestinationDirs** section should include a **DefaultDestDir** entry.

If an INF has copy, rename, or delete sections but no **DestinationDirs** section and the INF includes other INF files, Windows searches the included INF files for target location information. However, the order in which Windows searches the included files is not predictable. Therefore, there is a risk that Windows will, for example, copy files to a location not intended by the INF writer. To avoid such confusion, always specify a **DestinationDirs** section in an INF that contains copy, rename, or delete sections. The **DestinationDirs** section should include at least a **DefaultDestDir** entry and can list sections in the INF that copy, rename, or delete files.

 

 





