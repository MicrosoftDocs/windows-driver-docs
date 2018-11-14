---
title: Viewing and Editing Registers in KD
description: In KD, you can view and edit registers by entering the r (Registers) command. You can customize the display by using several options or by using the rm (Register Mask) command.
ms.assetid: 42306338-6E11-4724-B62F-D1E0BDBA7F8D
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Viewing and Editing Registers in KD


Registers are small volatile memory units that are located on the CPU. Many registers are dedicated to specific uses, and other registers are available for user-mode applications to use. The x86-based and x64-based processors have different collections of registers available. For more information about the registers on each processor, see [Processor Architecture](processor-architecture.md).

In KD, you can view and edit registers by entering the [**r (Registers)**](r--registers-.md) command. You can customize the display by using several options or by using the [**rm (Register Mask)**](rm--register-mask-.md) command.

Registers are also automatically displayed every time that the target stops. If you are stepping through your code with the [**p (Step)**](p--step-.md) or [**t (Trace)**](t--trace-.md) commands, you see a register display at every step. To stop this display, use the **r** option when you use these commands.

On an x86-based processor, the **r** option also controls several one-bit registers known as flags. To change these flags, you use a slightly different syntax than when changing regular registers. For more information about these flags and an explanation of this syntax, see [x86 Flags](x86-architecture.md#x86-flags).

 

 





