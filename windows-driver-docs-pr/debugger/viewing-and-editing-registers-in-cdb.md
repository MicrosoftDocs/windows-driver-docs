---
title: Viewing and Editing Registers in CDB
description: In CDB, you can view registers by entering the r (Registers) command in the Debugger Command window. You can customize the display by using several options or by using the rm (Register Mask) command.
ms.assetid: 33A2AF32-B4A6-430A-AD08-73B51D5D6301
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Viewing and Editing Registers in CDB


Registers are small volatile memory units that are located on the CPU. Many registers are dedicated to specific uses, and other registers are available for user-mode applications to use. The x86-based and x64-based processors have different collections of registers available. For more information about the registers on each processor, see [Processor Architecture](processor-architecture.md).

In CDB, you can view registers by entering the [**r (Registers)**](r--registers-.md) command in the Debugger Command window. You can customize the display by using several options or by using the [**rm (Register Mask)**](rm--register-mask-.md) command.

Registers are also automatically displayed every time that the target stops. If you are stepping through your code with the [**p (Step)**](p--step-.md) or [**t (Trace)**](t--trace-.md) commands, you see a register display at every step. To stop this display, use the **r** option when you use these commands.

On an x86-based processor, the **r** option also controls several one-bit registers known as flags. To change these flags, you use a slightly different syntax than when changing regular registers. For more information about these flags and an explanation of this syntax, see [x86 Flags](x86-architecture.md#x86-flags).

 

 





