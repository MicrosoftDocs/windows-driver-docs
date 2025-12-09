---
title: What Is Secure Boot for Windows
description: Learn what Secure Boot is and how this UEFI security standard works to ensure your Windows PC boots using only trusted software.
ms.date: 12/08/2025
ms.topic: concept-article
---

# Secure boot

This article provides an overview of Secure Boot, a security standard that is part of the UEFI specification. You learn how it works to ensure your PC boots using only trusted software and find resources on its requirements for Windows.

Secure Boot is a security standard that ensures your PC boots using only software trusted by the PC manufacturer. It's part of the Unified Extensible Firmware Interface (UEFI) specification.

## How Secure Boot works

When the PC starts, the firmware checks the signature of each piece of boot software, including firmware drivers (Option ROMs) and the operating system. If the signatures are valid, the PC boots, and the firmware gives control to the operating system.

## Requirements

Secure Boot is a requirement for Windows 8, 8.1, 10, and 11. For more information on the UEFI specification, see [Section 27.1 Secure Boot](https://uefi.org/sites/default/files/resources/UEFI_2_3_1_C.pdf).

For specific Windows hardware compatibility requirements for Secure Boot, see **System.Fundamentals.Firmware.UEFISecureBoot** in the [WHCP-Systems-Specification-1607 (ZIP download)](https://download.microsoft.com/download/D/3/C/D3CAA04D-0EE6-415B-9E94-FA7BDE37C2B4/WHCP-Documents-1607.zip).

## Next steps

- To enable Secure Boot on your device, see [Enabling Secure Boot](/windows/windows-11-and-secure-boot-a8ff1202-c0d9-42f5-940f-843abef64fad).

## Related resources

- [Hardware Security Testability Specification](/windows-hardware/test/hlk/testref/hardware-security-testability-specification)
- [Windows Hardware Compatibility Program Specifications and Policies](/windows-hardware/design/compatibility/whcp-specifications-policies)
- [Secured Boot and Measured Boot: Hardening Early Boot Components Against Malware](/previous-versions/windows/hardware/design/dn653311(v=vs.85))
- [Windows 8.1 Secure Boot Key Creation and Management Guidance](/previous-versions/windows/it-pro/windows-8.1-and-8/dn747883(v=win.10))
