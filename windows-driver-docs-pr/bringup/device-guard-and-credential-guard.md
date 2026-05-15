---
title: Memory Integrity and Virtualization-Based Security (VBS)
description: Learn how memory integrity uses virtualization-based security (VBS) to protect Windows from kernel exploits. Configure HVCI to harden your system against malware.
ms.date: 11/05/2025
ms.topic: concept-article
---

# Memory integrity and virtualization-based security

**Memory integrity** is a virtualization-based security (VBS) feature that protects Windows from kernel-level malware attacks. Available in Windows 10, Windows 11, and Windows Server 2016 and later, memory integrity uses hardware virtualization to isolate code integrity validation in a secure environment, preventing attackers from compromising the kernel.

VBS uses the Windows hypervisor to create an isolated virtual environment that becomes the root of trust of the OS. Memory integrity runs kernel mode code integrity checks within this secure environment and restricts kernel memory allocations that could be used to compromise the system. This ensures that kernel memory pages are only made executable after passing code integrity validation, and executable pages themselves are never writable.

This article explains how memory integrity works, how to enable it, and how to verify driver compatibility with your system.

> [!NOTE]
> Memory integrity is sometimes referred to as *hypervisor-protected code integrity (HVCI)* or *hypervisor enforced code integrity*. It was originally released as part of *Device Guard*. Device Guard is no longer used except to locate memory integrity and VBS settings in Group Policy or the Windows registry.

## Related content

[Code integrity checking](../devtest/code-integrity-checking.md)

[Hypervisor Code Integrity Readiness Test](/windows-hardware/test/hlk/testref/b972fc52-2468-4462-9799-6a1898808c86)

[Driver compatibility with memory integrity and VBS](/windows-hardware/test/hlk/testref/driver-compatibility-with-device-guard)

[virtualization-based security (VBS)](/windows-hardware/design/device-experiences/oem-vbs)
