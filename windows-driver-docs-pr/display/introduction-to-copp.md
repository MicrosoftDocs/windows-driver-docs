---
title: Introduction to COPP
description: Introduction to COPP
ms.assetid: a5f77c60-418d-4931-8922-ca2ae080da2e
keywords:
- copy protection WDK COPP , about COPP
- video copy protection WDK COPP , about COPP
- COPP WDK DirectX VA , about COPP
- protected video WDK COPP , about COPP
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Introduction to COPP


## <span id="ddk_introduction_to_the_certified_output_protection_protocol_gg"></span><span id="DDK_INTRODUCTION_TO_THE_CERTIFIED_OUTPUT_PROTECTION_PROTOCOL_GG"></span>


**This section applies only to Windows Server 2003 with SP1 and later, and Windows XP with SP2 and later.**

COPP provides a mechanism of applying copy protection to video that is output by the graphics adapter. COPP provides a common protocol for sending various link-protection requirements to the graphics adapter in a more protected fashion than by using the [**IOCTL\_VIDEO\_HANDLE\_VIDEOPARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567805) I/O control (IOCTL) code.

The following topics describe COPP:

[Cryptographic Primitives Used by COPP](cryptographic-primitives-used-by-copp.md)

[Communicating Through a Secure Channel](communicating-through-a-secure-channel.md)

[Graphics Adapter Output Requirements to Support COPP](graphics-adapter-output-requirements-to-support-copp.md)

 

 





