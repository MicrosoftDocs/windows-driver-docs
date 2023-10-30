---
title: DevGen
description: DevGen
ms.date: 12/01/2022
---

# DevGen

> [!NOTE]
> This tool is not allowed to be redistributed and should not be used for production scenarios.

DevGen (DevGen.exe) is a command line tool that lets an administrator create [software devices](/windows/win32/api/_swdevice) and root-enumerated devices for testing purposes.

## Where can I download DevGen?

DevGen is included in the %WindowsSdkDir%\\Tools subdirectory after installation of the [Windows Driver Kit (WDK)](../download-the-wdk.md) starting in Windows 11, version 22H2.

- Open a **Command Prompt** window (**Run as administrator**).
- Navigate to the WDK tools folder for the desired architecture.
- Type `devgen /?` to view command options. See [**DevGen Command Syntax**](devgen-command-syntax.md) for more information.
