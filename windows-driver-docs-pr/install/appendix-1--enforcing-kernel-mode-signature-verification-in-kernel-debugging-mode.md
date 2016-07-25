---
title: Appendix 1 Enforcing Kernel-Mode Signature Verification in Kernel Debugging Mode
description: .
ms.assetid: D7CB436F-4B89-49E7-BB53-101BDA7046F3
---

# Appendix 1: Enforcing Kernel-Mode Signature Verification in Kernel Debugging Mode


## Enforcing Kernel-Mode Signature Verification in Kernel Debugging Mode


*Excerpt from* [Installing an Unsigned Driver during Development and Test](installing-an-unsigned-driver-during-development-and-test.md):

In certain cases, developers might have to enable load-time signature enforcement when a kernel debugger is attached. An example of this is when a driver stack has an unsigned driver (such as a filter driver) that fails to load, which may invalidate the entire stack. Because attaching a debugger allows the unsigned driver to load, the problem appears to vanish as soon as the debugger is attached. Debugging this type of issue may be difficult.

In order to facilitate debugging these situations, the kernel-mode code signing policy supports the following registry value:

```
HKLM\SYSTEM\CurrentControlSet\Control\CI\DebugFlags
```

This registry value is of type REG\_DWORD, and can be assigned a value based on a bitwise OR of one or more of the following flags.

```
0x00000001
```

This flag value configures the kernel to break into the debugger if a driver is unsigned. The developer or tester can then choose to load the unsigned driver by entering g at the debugger prompt.

```
0x00000010
```

This flag value configures the kernel to ignore the presence of the debugger and to always block an unsigned driver from loading.

If this registry value does not exist in the registry or has a value that is not based on the flags described previously, the kernel always loads a driver in kernel debugging mode regardless of whether the driver is signed.

**Note**  This registry value does not exist in the registry by default. You must create the value in order to debug the kernel-mode signature verification.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Appendix%201:%20Enforcing%20Kernel-Mode%20Signature%20Verification%20in%20Kernel%20Debugging%20Mode%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




