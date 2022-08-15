---
title: Memory Overwrite Request Control (MOR) LOCK version 2
description: Provides information about Memory Overwrite Request Control (MOR) LOCK version 2.
ms.date: 08/19/2021
---

# Memory Overwrite Request Control (MOR) lock version 2

To prevent advanced memory attacks, the existing system BIOS security mitigation MemoryOverwriteRequestControl is improved to support locking to defend against new threats.

Version 1 defined a UEFI variable which, when set, locks the original MOR byte, preventing it from being changed by unauthorized agents such as the OS kernel. When MOR lock is enabled, the original MOR byte is set to 0x11, indicating that the platform must wipe memory across all resets – auto-detection is prohibited. This introduced a performance penalty when enabled platforms.

Version 2 of the lock supports a key that permits an authorized agent, for example the hypervisor, to disable the lock. The expectation is that during a normal shutdown, the hypervisor will first remove its secrets from RAM, use the Version 2 key to disable the lock, and clear the original MOR byte, enabling the platform to reboot without clearing RAM. Firmware that implements Version 2 of the MOR Lock provides additional protection while avoiding the performance penalties associated with Version 1.

Support for MOR Lock V2 is included in the following versions of Windows:

- Windows Server Technical Preview 2016

- Windows 10, version 1607 and later

## Related resources

[TCG Platform Reset Attack Mitigation Specification](https://www.trustedcomputinggroup.org/wp-content/uploads/Platform-Reset-Attack-Mitigation-Specification.pdf)

[Secure MOR Implementation](./device-guard-requirements.md)
