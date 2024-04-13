---
title: DevCon Dp_enum
description: Lists the third-party (OEM) driver packages in the driver store on the local computer.
keywords:
- DevCon Dp_enum Driver Development Tools
topic_type:
- apiref
ms.topic: reference
api_name:
- DevCon Dp_enum
api_type:
- NA
ms.date: 10/28/2022
---

# DevCon Dp_enum

> [!NOTE]
> [PnPUtil](pnputil.md) ships with every release of Windows and makes use of the most reliable and secure APIs available. We recommend using PnPUtil instead of DevCon. See the [Recommended replacement](#recommended-replacement) below and [Replacing DevCon](devcon-migration.md) for more information.

Lists the third-party (OEM) driver packages in the driver store on the local computer.

``` console
devcon dp_enum
```

## Recommended replacement

``` console
pnputil /enum-drivers
```

For more recommended replacements, see [Replacing DevCon](devcon-migration.md).

## Comments

A DevCon Dp_enum command lists the OEM\*.inf files in the %windir%/Inf on the local computer. For each file, this command displays the provider, class, date, and version number from the INF file.

## Sample usage

``` console
devcon dp_enum
```
