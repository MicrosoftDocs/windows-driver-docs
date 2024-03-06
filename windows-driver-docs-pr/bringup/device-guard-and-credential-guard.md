---
title: Hypervisor-Protected Code Integrity (HVCI) 
description: Hypervisor-Protected Code Integrity can use hardware technology and virtualization to isolate the Code Integrity (CI) decision-making function from the rest of the Windows operating system.
ms.date: 12/14/2023
---

# Memory integrity and virtualization-based security

**Memory integrity** is a [virtualization-based security (VBS)](/windows-hardware/design/device-experiences/oem-vbs) feature available in Windows 10, Windows 11, and Windows Server 2016 and later. Memory integrity and VBS improve the threat model of Windows and provide stronger protections against malware trying to exploit the Windows kernel. VBS uses the Windows hypervisor to create an isolated virtual environment that becomes the root of trust of the OS that assumes the kernel can be compromised. Memory integrity is a critical component that protects and hardens Windows by running kernel mode code integrity within the isolated virtual environment of VBS. Memory integrity also restricts kernel memory allocations that could be used to compromise the system, ensuring that kernel memory pages are only made executable after passing code integrity checks inside the secure runtime environment, and executable pages themselves are never writable.

> [!NOTE]
> Memory integrity is sometimes referred to as *hypervisor-protected code integrity (HVCI)* or *hypervisor enforced code integrity*, and was originally released as part of *Device Guard*. Device Guard is no longer used except to locate memory integrity and VBS settings in Group Policy or the Windows registry.

## Related resources

[Code integrity checking](../devtest/code-integrity-checking.md)

[Hypervisor Code Integrity Readiness Test](/windows-hardware/test/hlk/testref/b972fc52-2468-4462-9799-6a1898808c86)

[Driver compatibility with memory integrity and VBS](/windows-hardware/test/hlk/testref/driver-compatibility-with-device-guard)
