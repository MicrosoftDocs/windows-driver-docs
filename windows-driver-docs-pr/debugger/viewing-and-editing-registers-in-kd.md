---
title: Viewing and Editing Registers in KD
description: In KD, you can view and edit registers by entering the r (Registers) command. You can customize the display by using several options or by using the rm (Register Mask) command.
ms.assetid: 42306338-6E11-4724-B62F-D1E0BDBA7F8D
---

# Viewing and Editing Registers in KD


Registers are small volatile memory units that are located on the CPU. Many registers are dedicated to specific uses, and other registers are available for user-mode applications to use. The x86-based and x64-based processors have different collections of registers available. For more information about the registers on each processor, see [Processor Architecture](processor-architecture.md).

In KD, you can view and edit registers by entering the [**r (Registers)**](r--registers-.md) command. You can customize the display by using several options or by using the [**rm (Register Mask)**](rm--register-mask-.md) command.

Registers are also automatically displayed every time that the target stops. If you are stepping through your code with the [**p (Step)**](p--step-.md) or [**t (Trace)**](t--trace-.md) commands, you see a register display at every step. To stop this display, use the **r** option when you use these commands.

On an x86-based processor, the **r** option also controls several one-bit registers known as flags. To change these flags, you use a slightly different syntax than when changing regular registers. For more information about these flags and an explanation of this syntax, see [x86 Flags](x86-architecture.md#x86-flags).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Viewing%20and%20Editing%20Registers%20in%20KD%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




