---
title: DevGen Command Syntax
description: How to run DevGen, including syntax and parameters. 
keywords:
- DevGen Command Syntax Driver Development Tools
ms.date: 12/01/2022
---

# DevGen Command Syntax

> [!NOTE]
> This tool is not allowed to be redistributed and should not be used for production scenarios.

DevGen.exe can be found in the tools folder of the WDK starting in Windows 11, version 22H2. It allows an administrator create and remove [software devices](/windows/win32/api/_swdevice) and root enumerated devices for testing purposes.

To run DevGen, open a command prompt window (Run as Administrator), navigate to the tools folder, and type a command using the following syntax and parameters.

```syntax
DEVGEN [/add [<…>] | /remove <…>| /?]
```

## Commands

### /add

Create a device.

```syntax
DEVGEN /add [/bus <SWD | ROOT>] [/instanceid <instance ID>] 
            [/parent <device instance ID>] [/hardwareid <hardware ID>] 
            [/compatibleid <compatible ID>] [/wait [<timeout in MS>]] 
            [/unplug] [/subtree]
```

Flags:

`/bus <SWD | ROOT>` - SWD enumerates a software device that will disconnect after reboot. ROOT enumerates a root device that will persist across reboot. A software device will be created by default.

`/instanceid <instance ID>` - unique instance ID to use when generating a device.

`/parent <device instance ID>` - parent device to enumerate device under. Only supported for software devices. Device is enumerated under HTREE\ROOT\0 by default.

`/hardwareid <hardware ID>` - hardware ID to set on the generated device. More than one hardware ID can be set by using this parameter multiple times.

`/compatibleid <compatible ID>` - compatible ID to set on the generated device. More than one compatible ID can be set by using this parameter multiple times.

`/wait [<timeout in MS>]` - remove device immediately after waiting for user prompt or optional timeout. Timeout specified in milliseconds.

`/unplug` - modifies /wait parameter to unplug device without removing. Device will remain as a non-present device node. Only valid when generating a software device with /wait parameter.

`/subtree` - remove entire device subtree, including any child devices.

### /remove

Remove a device specified by the device instance ID. Only devices created using DevGen can be removed with DevGen.

```syntax
DEVGEN /remove <device instance ID> [/subtree]
```

Flags:

`/subtree` - remove entire device subtree, including any child devices.

## Software Device vs Root-Enumerated Device

By default, DevGen creates a [software device](/windows/win32/api/_swdevice). Software devices are the recommended test devices, since they do not persist across reboot and will not clutter the system. Use root-enumerated devices only for test cases that require a system reboot.

## Examples

For examples, see [DevGen Examples](devgen-examples.md).