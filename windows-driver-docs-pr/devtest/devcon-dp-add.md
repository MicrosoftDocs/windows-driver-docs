---
title: DevCon Dp_add
description: Adds a third-party (OEM) driver package to the driver store on the local computer.
keywords:
- DevCon Dp_add Driver Development Tools
topic_type:
- apiref
ms.topic: reference
api_name:
- DevCon Dp_add
api_type:
- NA
ms.date: 10/28/2022
---

# DevCon Dp_add

> [!NOTE]
> [PnPUtil](pnputil.md) ships with every release of Windows and makes use of the most reliable and secure APIs available. We recommend using PnPUtil instead of DevCon. See the [Recommended replacement](#recommended-replacement) below and [Replacing DevCon](devcon-migration.md) for more information.

Adds a third-party (OEM) driver package to the driver store on the local computer.

``` console
devcon dp_add inf
```

## Parameters

*inf*

The fully qualified path and name of the INF file for the driver package.

## Recommended replacement

``` console
pnputil /add-driver inf
```

For more recommended replacements, see [Replacing DevCon](devcon-migration.md).

## Comments

A DevCon dp_add command copies the specified INF file to the %windir%/Inf directory and renames it OEM\*.inf. This file name is unique on the computer and you cannot specify it.

If this INF file already exists in %windir%/Inf (as determined by comparing the binary files, not by matching the file names) and the catalog (.cat) file for the INF is identical to a catalog file in the directory, the INF file is not recopied to the %windir%/Inf directory.

This command calls the **SetupCopyOEMInf** function with no *CopyStyle* flags. **SetupCopyOEMInf** is described in the Microsoft Windows SDK documentation.

## Sample usage

``` console
devcon dp_add C:\WinDDK\5322\src\general\toaster\inf\i386\toaster.inf
```
