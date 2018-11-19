---
title: Memory Overwrite Request Control (MOR) LOCK version 2
description: Memory Overwrite Request Control (MOR) LOCK version 2
ms.date: 05/15/2018
ms.localizationpriority: medium
---


# Memory Overwrite Request Control (MOR) LOCK version 2


Windows flagship security feature Device Guard changed the threat model for secrets in memory – hypervisor secrets must now be protected from malicious OS kernels. This required extending the TCG "Platform Reset Attack Mitigations" to protect secrets in RAM from malicious administrators and kernel. Version 1 defined a UEFI variable which, when set, locks the original MOR byte, preventing it from being changed by unauthorized agents such as the OS kernel. When Device Guard is enabled, the original MOR byte is set to 0x11, indicating that the platform must wipe memory across all resets – auto-detection is prohibited. This introduced a performance penalty on Device Guard enabled platforms.

Version 2 of the lock supports a key that permits an authorized agent, for example the hypervisor, to disable the lock. The expectation is that during a normal shutdown, the hypervisor will first remove its secrets from RAM, use the Version 2 key to disable the lock, and clear the original MOR byte, enabling the platform to reboot without clearing RAM. Firmware that implements Version 2 of the MOR Lock provides protection of Device Guard secrets while avoiding the performance penalties associated with Version 1. Thus, reducing attack surface for surprise reboot attacks

Support for MOR Lock V2 is included in the following versions of Windows:

-   Windows Server Technical Preview 2016

-   Windows 10, version 1607 and later


## Related resources

[TCG Platform Reset Attack Mitigation Specification](https://www.trustedcomputinggroup.org/wp-content/uploads/Platform-Reset-Attack-Mitigation-Specification.pdf)

[Secure MOR Implementation](https://docs.microsoft.com/windows-hardware/drivers/bringup/device-guard-requirements)



