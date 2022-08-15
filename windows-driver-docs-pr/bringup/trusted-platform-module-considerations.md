---
title: Trusted Platform Module (TPM) Considerations
description: Provides information about Trusted Platform Module (TPM) considerations.
ms.date: 05/07/2018
---

# Trusted Platform Module (TPM) Considerations

New devices with TPM 2.0 should use SHA256 for all PCR banks. This may not be compatible with downlevel operating systems.

There is no legacy BIOS interface to TPM 2.0. Though in these scenarios TPM 2.0 can be utilized by Bitlocker.  If installing Windows 7 on current hardware, you should install in x64 UEFI boot mode (though you will still need a CSM due to Windows 7 boot requirements) so that you can receive some benefit from TPM 2.0.

After you upgrade to later operating system (Win8 and later), depending on the firmware installed on the system, you may have the ability to enable Secure Boot. If you install a Windows operating system in legacy BIOS mode on existing hardware, you cannot receive the full benefits of TPM 2.0 or Secure Boot.

## Related resources

[TPM recommendations](/windows/security/hardware-protection/tpm/tpm-recommendations)

[Trusted Platform Module 2.0: A Brief Introduction](https://trustedcomputinggroup.org/resource/trusted-platform-module-2-0-a-brief-introduction/)

[Trusted Platform Module (TPM)](https://trustedcomputinggroup.org/work-groups/trusted-platform-module/)
