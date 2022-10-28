---
title: DevCon Classes
description: Lists all device setup classes, including classes that devices on the system do not use.
keywords:
- DevCon Classes Driver Development Tools
topic_type:
- apiref
api_name:
- DevCon Classes
api_type:
- NA
ms.date: 10/28/2022
---

# DevCon Classes

> [!NOTE]
> [PnPUtil](pnputil.md) ships with every release of Windows and makes use of the most reliable and secure APIs available. We recommend using PnPUtil instead of DevCon. See the [Recommended replacement](#recommended-replacement) below and [Replacing DevCon](devcon-migration.md) for more information.

Lists all [device setup classes](../install/overview-of-device-setup-classes.md), including classes that devices on the system do not use.

``` console
devcon classes
```

## Recommended replacement

``` console
pnputil /enum-classes
```

For more recommended replacements, see [Replacing DevCon](devcon-migration.md).

## Comments

In the DevCon display, classes are listed in the order that they appear in the registry (alphanumeric order by GUID).

To find the devices in a setup class, use the **[DevCon ListClass](devcon-listclass.md)** operation. To find the setup class of a particular device, use the **[DevCon Stack](devcon-stack.md)** operation.

## Sample usage

``` console
devcon classes
devcon classes > setupclasses.txt
```

## Examples

- [Example 4: List classes on the local computer](devcon-examples.md#example-4-list-classes-on-the-local-computer)
