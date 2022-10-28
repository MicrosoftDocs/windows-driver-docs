---
title: DevCon Rescan
description: Uses Windows Plug and Play features to update the device list for the computer.
keywords:
- DevCon Rescan Driver Development Tools
topic_type:
- apiref
api_name:
- DevCon Rescan
api_type:
- NA
ms.date: 10/28/2022
---

# DevCon Rescan

> [!NOTE]
> [PnPUtil](pnputil.md) ships with every release of Windows and makes use of the most reliable and secure APIs available. We recommend using PnPUtil instead of DevCon. See the [Recommended replacement](#recommended-replacement) below and [Replacing DevCon](devcon-migration.md) for more information.

Uses Windows Plug and Play features to update the device list for the computer.

``` console
devcon [/r] rescan
```

## Parameters

**/r**

Conditional reboot. Reboots the system after completing an operation only if a reboot is required to make a change effective.

## Recommended replacement

``` console
pnputil /scan-devices
```

For more recommended replacements, see [Replacing DevCon](devcon-migration.md).

## Comments

Rescanning can cause the Plug and Play manager to detect new devices and to install device drivers without warning.

Rescanning can detect some non-Plug and Play devices, particularly those that cannot notify the system when they are installed, such as parallel-port devices and serial-port devices. As a result, you must have Administrator privileges to run **DevCon Rescan** commands.

## Sample usage

``` console
devcon rescan
```

## Example

- [Example 37: Scan the computer for new devices](devcon-examples.md#example-37-scan-the-computer-for-new-devices)
