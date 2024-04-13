---
title: Identifying Source Disks and Files
description: Identifying Source Disks and Files
keywords:
- INF files WDK display , identifying source disks or files
- source disks WDK display
- source files WDK display
- identifying display source disks or files
ms.date: 04/20/2017
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

For more information about the **SourceDisksNames** and **SourceDisksFiles** sections, see [**INF SourceDisksNames Section**](../install/inf-sourcedisksnames-section.md) and [**INF SourceDisksFiles Section**](../install/inf-sourcedisksfiles-section.md).

 

