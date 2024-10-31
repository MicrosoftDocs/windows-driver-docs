---
title: Kernel Address Sanitizer
description: The Kernel Address Sanitizer is a bug detection technology supported by Windows drivers that enables you to detect several classes of illegal memory accesses.
keywords:
- Kernel Address Sanitizer
- KASAN
- verifying drivers WDK
ms.date: 10/31/2024
---

# Kernel Address Sanitizer (KASAN)

The Kernel Address Sanitizer (KASAN) is a bug detection technology supported on Windows kernel drivers that enables you to detect several classes of illegal memory accesses, such as buffer overflows and use-after-free events. It requires you to enable KASAN on your system, and recompile your kernel driver with a specific MSVC compiler flag.

## Pre-requisites

In order to use KASAN, you need:

 - OS version of the target system, on which your kernel driver will be loaded:
    - Client: Windows 11 24H2 or above.
    - Server: Windows Server 2025 or above.
 - VisualStudio: version 17.11 or above.
 - WDK: version 10.0.26100.2161 or above.

## How to enable KASAN on your kernel driver

1. Enter the following command line in an administrator **Command Prompt** window on the target system:

   ```console
   reg add "HKLM\System\CurrentControlSet\Control\Session Manager\Kernel" /v KasanEnabled /t REG_DWORD /d 1
   ```

1. Reboot your target system for the change to take effect.

1. Recompile your kernel driver with KASAN instrumentation enabled by passing a new flag to the MSVC compiler. Use either of the following methods:

    - **GUI**: in VisualStudio, navigate to the **Solution Explorer**, right-click on your kernel driver project, and select **Properties**. In the property page, navigate to **Configuration Properties** >> **C/C++** >> **General**, and set **Enable Kernel Address Sanitizer** to *Yes*. Then rebuild your solution.
    - **Command prompt**: add the */fsanitize=kernel-address* parameter to your compiler command line. Then, rebuild your solution.

1. Load your recompiled kernel driver on your target system, and stress-test it as you usually would. KASAN operates at runtime and reports illegal memory access events via **Bug Check 0x1F2: KASAN_ILLEGAL_ACCESS**.

## How to verify that KASAN is enabled on your kernel driver

The kernel drivers compiled with KASAN have a PE section called "`KASAN`". Verify that KASAN is enabled on your driver by running the following command in a **Developer Command Prompt**:

```console
dumpbin /ALL YourDriver.sys
```

If the output contains a section called "`KASAN`", then KASAN is enabled on your driver.

## How to analyze KASAN reports

When KASAN detects an illegal memory access in your driver, it issues **Bug Check 0x1F2: KASAN_ILLEGAL_ACCESS**. Inspect the generated kernel memory dump to determine where exactly your driver performed an illegal memory access.

Use KASAN with a kernel debugger attached to the target system so that the memory can be inspected dynamically as soon as the bug check is issued, rather than post-mortem with a memory dump.

### Bug check parameters

The parameters of **Bug Check 0x1F2: KASAN_ILLEGAL_ACCESS** are:

 1. Parameter 1: Address being accessed illegally.
 1. Parameter 2: Size of the memory access.
 1. Parameter 3: Address of the caller performing the illegal memory access.
 1. Parameter 4: Extra information on the memory access:
     - Bits [0:7]: the KASAN shadow code. See the table below.
     - Bit 8: `1` if the access was a write, `0` if it was a read.

### KASAN shadow codes

In KASAN, we consider that all of the kernel memory is divided in contiguous chunks of eight-byte-aligned, eight-byte *cells*. With KASAN, each eight-byte cell in kernel memory has a *shadow code* associated with it, which is an one-byte integer that indicates the validity of the cell. The encoding of the shadow codes is the following:

| Value | Meaning |
|--|--|
| `0x00` | The cell is entirely valid: accesses to all eight bytes of the cell are legal. |
| `0x01` -> `0x07` | The cell is partially valid: the first *value* bytes in the cell are valid, but the rest are invalid. |
| >= `0x80` | The cell is entirely invalid: accesses to all eight bytes of the cell are illegal. |

Several sub-codes are used for the entirely invalid cells to further indicate what type of memory the cell is associated to, and why it is invalid:

 - `0x81`: left redzone of alloca.
 - `0x82`: middle redzone of alloca.
 - `0x83`: right redzone of alloca.
 - `0x84`: right redzone of global variable.
 - `0x85`: generic redzone.
 - `0x86`: right redzone of pool memory.
 - `0x87`: freed memory.
 - `0x8A`: left redzone of contiguous memory.
 - `0x8B`: right redzone of contiguous memory.
 - `0x8C`: freed lookasidelist memory.
 - `0x8D`: left redzone of pool memory.
 - `0xF1`: left redzone of stack variable.
 - `0xF2`: middle redzone of stack variable.
 - `0xF3`: right redzone of stack variable.
 - `0xF5`: used-after-ret stack variable.
 - `0xF8`: out-of-scope stack variable.

### Understand KASAN bug checks: an example

Assume that KASAN issued a bug check when your driver was executing, with these parameters:

 1. Parameter 1: `0xFFFFFFFFFFFFABCD`
 1. Parameter 2: `0x0000000000000004`
 1. Parameter 3: `0xFFFFFFFF12345678`
 1. Parameter 4: `0x0000000000000184`

*Parameter 1* tells you that your driver tried to access address `0xFFFFFFFFFFFFABCD` and that this access was illegal. *Parameter 2* tells you that it was a four-byte access. *Parameter 3* gives you the address of the instruction pointer at which your driver performed the illegal access. *Parameter 4* tells you that this was a write access, and that the memory being touched was the right redzone of a global variable.

In other words, your driver likely tried to perform a write buffer overflow on a global variable. Use this information to investigate and determine where and how to fix this bug in your driver.

## Performance impact of KASAN

KASAN increases kernel memory consumption and introduces an approximate two-times slowdown in drivers compiled with KASAN enabled.

## Resources

- [Microsoft: Introducing kernel sanitizers on Microsoft platforms](https://www.microsoft.com/en-us/security/blog/2023/01/26/introducing-kernel-sanitizers-on-microsoft-platforms/)
