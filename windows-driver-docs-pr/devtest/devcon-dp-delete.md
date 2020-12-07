---
title: DevCon Dp_delete
description: Deletes a third-party (OEM) driver package from the driver store on the local computer. This command deletes the INF file, the PNF file, and the associated catalog file (.cat).
keywords:
- DevCon Dp_delete Driver Development Tools
topic_type:
- apiref
api_name:
- DevCon Dp_delete
api_type:
- NA
ms.date: 04/11/2019
ms.localizationpriority: medium
---

# DevCon Dp\_delete

Deletes a third-party (OEM) driver package from the driver store on the local computer. This command deletes the INF file, the PNF file, and the associated catalog file (.cat).

```command
    devcon [-f] dp_delete inf
```

## Parameters

**-f**
This parameter deletes the driver package even if a device is using it at the time.

*inf*
The OEM\*.inf file name of the INF file. Windows assigns a file name with this format to the INF file when you add the driver package to the driver store, such as by using [**DevCon dp\_add**](devcon-dp-add.md).

## Comments

### Sample Usage

```command
devcon dp_delete oem2.inf
devcon -f dp_delete oem0.inf
```
