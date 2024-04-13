---
title: DevCon Reboot
description: Stops and then starts the operating system. Valid only on the local computer.
keywords:
- DevCon Reboot Driver Development Tools
topic_type:
- apiref
ms.topic: reference
api_name:
- DevCon Reboot
api_type:
- NA
ms.date: 10/28/2022
---

# DevCon Reboot

> [!NOTE]
> [PnPUtil](pnputil.md) ships with every release of Windows and makes use of the most reliable and secure APIs available. We recommend using PnPUtil instead of DevCon. See the [Recommended replacement](#recommended-replacement) below and [Replacing DevCon](devcon-migration.md) for more information.

Stops and then starts the operating system. Valid only on the local computer.

``` console
devcon reboot
```

## Recommended replacement

``` console
shutdown /r /t 0
```

For more recommended replacements, see [Replacing DevCon](devcon-migration.md).

## Comments

Unlike the **/r** parameter, which reboots the system only if required to make a change effective, the **DevCon Reboot** operation reboots the system without determining whether a reboot is required.

DevCon uses the standard **ExitWindowsEx** function to reboot. If the user has open files on the computer or a program will not close, the system does not reboot until the user has responded to system prompts to close the files or end the process. For more information about **ExitWindowsEx**, see the Microsoft Windows SDK.

## Sample usage

``` console
devcon reboot
```

## Example

- [Example 39: Reboot the local computer](devcon-examples.md#example-39-reboot-the-local-computer)
