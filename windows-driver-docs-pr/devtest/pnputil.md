---
title: PnPUtil Command Line Tool for Driver Packages
description: Learn how to use the PnPUtil command line tool to add, install, delete, and enumerate driver packages in the Windows driver store.
ms.date: 11/04/2025
ms.topic: overview
---

# PnPUtil

PnPUtil (PnPUtil.exe) is a command line tool for managing Windows driver packages. Use it to:

- Add a driver package to the [driver store](/windows-hardware/drivers/install/driver-store).
- Install a driver package on the computer.
- Delete a driver package from the driver store.
- Enumerate the driver packages that are currently in the driver store. The tool lists only driver packages that aren't in-box packages. An *in-box* driver package is one that's included in the default installation of Windows or its service packs.

## Where can I get PnPUtil?

Every version of Windows Vista and later includes PnPUtil in the `%windir%\system32` directory. There's no separate PnPUtil download package.

- Open a **Command Prompt** window (**Run as administrator**).
- Type `pnputil /?` to view command options. For more information, see [**PnPUtil Command Syntax**](pnputil-command-syntax.md).

## See also

To learn how to use PnpUtil, see [PnPUtil Command Syntax](pnputil-command-syntax.md).

For examples of how to use the PnPUtil tool, see [PnPUtil Examples](pnputil-examples.md).

## Related topics

- [PnPUtil Command Syntax](pnputil-command-syntax.md) - Learn all available commands and options
- [PnPUtil Examples](pnputil-examples.md) - See step-by-step usage examples
