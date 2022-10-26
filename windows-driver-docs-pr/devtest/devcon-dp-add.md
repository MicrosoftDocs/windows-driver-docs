---
title: DevCon Dp_add
description: Adds a third-party (OEM) driver package to the driver store on the local computer.
keywords:
- DevCon Dp_add Driver Development Tools
topic_type:
- apiref
api_name:
- DevCon Dp_add
api_type:
- NA
ms.date: 10/26/2022
---

# DevCon Dp\_add

> [!NOTE] 
> [PnPUtil](pnputil.md) ships with every release of Windows and makes use of the most reliable and secure APIs available. Its use is recommended instead of DevCon. See the [Recommended Replacement](#recommended-replacement) below and [Replacing DevCon](devcon-migration.md) for more information.

Adds a third-party (OEM) driver package to the driver store on the local computer.

```
    devcon dp_add inf
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______inf______"></span><span id="_______INF______"></span> *inf*   
The fully qualified path and name of the INF file for the driver package.

## Recommended Replacement

```
pnputil /add-driver inf
```

For more recommended replacements, see [Replacing DevCon](devcon-migration.md).

## <span id="comments"></span><span id="COMMENTS"></span>Comments

A DevCon dp\_add command copies the specified INF file to the %windir%/Inf directory and renames it OEM\*.inf. This file name is unique on the computer and you cannot specify it.

If this INF file already exists in %windir%/Inf (as determined by comparing the binary files, not by matching the file names) and the catalog (.cat) file for the INF is identical to a catalog file in the directory, the INF file is not recopied to the %windir%/Inf directory.

This command calls the **SetupCopyOEMInf** function with no *CopyStyle* flags. **SetupCopyOEMInf** is described in the Microsoft Windows SDK documentation.

## <span id="sample_usage"></span><span id="SAMPLE_USAGE"></span>Sample Usage

```
devcon dp_add C:\WinDDK\5322\src\general\toaster\inf\i386\toaster.inf
```





