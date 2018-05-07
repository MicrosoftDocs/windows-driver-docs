---
title: Memory Overwrite Request Control (MOR) LOCK version 2
description: Memory Overwrite Request Control (MOR) LOCK version 2
author: windows-driver-content
ms.author: windowsdriverdev
ms.date: 05/15/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---


# Memory Overwrite Request Control (MOR) LOCK version 2


Windows flagship security feature Device Guard changed the threat model for secrets in memory – hypervisor secrets must now be protected from malicious OS kernels. This required extending the TCG "Platform Reset Attack Mitigations" to protect secrets in RAM from malicious administrators and kernel. Version 1 defined a UEFI variable which, when set, locks the original MOR byte, preventing it from being changed by unauthorized agents such as the OS kernel. When Device Guard is enabled, the original MOR byte is set to 0x11, indicating that the platform must wipe memory across all resets – auto-detection is prohibited. This introduced a performance penalty on Device Guard enabled platforms.

Version 2 of the lock supports a key that permits an authorized agent, for example the hypervisor, to disable the lock. The expectation is that during a normal shutdown, the hypervisor will first remove its secrets from RAM, use the Version 2 key to disable the lock, and clear the original MOR byte, enabling the platform to reboot without clearing RAM. Firmware that implements Version 2 of the MOR Lock provides protection of Device Guard secrets while avoiding the performance penalties associated with Version 1. Thus, reducing attack surface for surprise reboot attacks

Support for MOR Lock V2 is included in the following versions of Windows:

-   Windows Server Technical Preview 2016

-   Windows 10, version 1607

-   Windows 10, version 1703

## Related resources

[TCG Platform Reset Attack Mitigation Specification](https://www.trustedcomputinggroup.org/wp-content/uploads/Platform-Reset-Attack-Mitigation-Specification.pdf) 

[Secure MOR Implementation](https://msdn.microsoft.com/en-us/windows/hardware/drivers/bringup/device-guard-requirements)                                          


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Slicer%20settings%20%20RELEASE:%20%289/2/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


