---
title: PnPUtil
description: PnPUtil
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# PnPUtil

PnPUtil (PnPUtil.exe) is a command line tool that lets an administrator perform actions on [driver packages](../install/driver-packages.md).  Some examples include:

- Adds a driver package to the [driver store](../install/driver-store.md).

- Installs a driver package on the computer.

- Deletes a driver package from the driver store.

- Enumerates the driver packages that are currently in the driver store. Only driver packages that are not in-box packages are listed. An *in-box* driver package is one which is included in the default installation of Windows or its service packs.

## Where can I download PnPUtil?

PnPUtil is included in every version of Windows, starting with Windows Vista (in the `%windir%\system32` directory). There isn't a separate PnPUtil download package.

- Open a **Command Prompt** window (**Run as administrator**).
- Type `pnputil /?` to view command options. See [**PnPUtil Command Syntax**](pnputil-command-syntax.md) for more information.
