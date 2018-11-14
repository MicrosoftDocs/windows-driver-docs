---
title: Identifying Source Disks and Files
description: Identifying Source Disks and Files
ms.assetid: 0eb8fe7f-1e44-4f3d-8567-31a2cd659805
keywords:
- INF files WDK display , identifying source disks or files
- source disks WDK display
- source files WDK display
- identifying display source disks or files
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Identifying Source Disks and Files


You must specify all in-box display drivers in the **SourceDisksNames** and **SourceDisksFiles** sections. The following example shows how to identify the CD-ROM discs and the names of the source files that are contained on the disks. The source files are transferred to the target computer during installation.

```inf
[SourceDisksNames]
3426=windows cd

[SourceDisksFiles]
DisplayMiniportDriverName.sys  = 3426
UserModeDriverName1.dll  = 3426
UserModeDriverName2.dll  = 3426
```

For more information about the **SourceDisksNames** and **SourceDisksFiles** sections, see [**INF SourceDisksNames Section**](https://msdn.microsoft.com/library/windows/hardware/ff547478) and [**INF SourceDisksFiles Section**](https://msdn.microsoft.com/library/windows/hardware/ff547472).

 

 





