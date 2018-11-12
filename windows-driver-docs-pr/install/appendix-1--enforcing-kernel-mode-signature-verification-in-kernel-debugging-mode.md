---
title: Enforce Kernel-Mode Signature Verification in Kernel Debugging
description: Describes how to enable load-time signature enforcement when a kernel debugger is attached.
ms.assetid: D7CB436F-4B89-49E7-BB53-101BDA7046F3
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Appendix 1: Enforcing Kernel-Mode Signature Verification in Kernel Debugging Mode


## Enforcing Kernel-Mode Signature Verification in Kernel Debugging Mode


*Excerpt from* [Installing an Unsigned Driver during Development and Test](installing-an-unsigned-driver-during-development-and-test.md):

In certain cases, developers might have to enable load-time signature enforcement when a kernel debugger is attached. An example of this is when a driver stack has an unsigned driver (such as a filter driver) that fails to load, which may invalidate the entire stack. Because attaching a debugger allows the unsigned driver to load, the problem appears to vanish as soon as the debugger is attached. Debugging this type of issue may be difficult.

In order to facilitate debugging these situations, the kernel-mode code signing policy supports the following registry value:

```cpp
HKLM\SYSTEM\CurrentControlSet\Control\CI\DebugFlags
```

This registry value is of type [REG_DWORD](https://docs.microsoft.com/windows/desktop/SysInfo/registry-value-types), and can be assigned a value based on a bitwise OR of one or more of the following flags.

```cpp
0x00000001
```

This flag value configures the kernel to break into the debugger if a driver is unsigned. The developer or tester can then choose to load the unsigned driver by entering g at the debugger prompt.

```cpp
0x00000010
```

This flag value configures the kernel to ignore the presence of the debugger and to always block an unsigned driver from loading.

If this registry value does not exist in the registry or has a value that is not based on the flags described previously, the kernel always loads a driver in kernel debugging mode regardless of whether the driver is signed.

**Note**  This registry value does not exist in the registry by default. You must create the value in order to debug the kernel-mode signature verification.

 

 

 





