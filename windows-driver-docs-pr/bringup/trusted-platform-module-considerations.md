---
title: Trusted Platform Module (TPM) Considerations
description: Trusted Platform Module (TPM) Considerations
author: windows-driver-content
ms.author: windowsdriverdev
ms.date: 05/15/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---


# Trusted Platform Module (TPM) Considerations

New devices with TPM 2.0 should use SHA256 for all PCR banks. This may not be compatible with downlevel operating systems.

TPM 2.0 is **not** usable in legacy boot mode (with CSM enabled) for anything besides BitLocker.  There is no legacy BIOS interface to TPM 2.0. If installing Windows 7 on current hardware, you should install in x64 UEFI mode so that you can receive some benefit from the TPM 2.0 (BitLocker only). After you upgrade to later operating system (Win8 and later), depending on the firmware installed on the system, you may have the ability to enable Secure Boot. If you install a Windows operating system in legacy BIOS mode on existing hardware, you cannot receive the full benefits of TPM 2.0 or Secure Boot.

## Related resources

[TPM recommendations](https://technet.microsoft.com/itpro/windows/keep-secure/tpm-recommendations)                                        

[Trusted Platform Module 2.0: A Brief Introduction](http://www.trustedcomputinggroup.org/trusted-platform-module-2-0-brief-introduction/)

[Trusted Platform Module (TPM)](http://www.trustedcomputinggroup.org/work-groups/trusted-platform-module/)                                



--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Slicer%20settings%20%20RELEASE:%20%289/2/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


