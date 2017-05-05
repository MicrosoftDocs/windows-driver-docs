---
title: Introduction to COPP
description: Introduction to COPP
ms.assetid: a5f77c60-418d-4931-8922-ca2ae080da2e
keywords:
- copy protection WDK COPP , about COPP
- video copy protection WDK COPP , about COPP
- COPP WDK DirectX VA , about COPP
- protected video WDK COPP , about COPP
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Introduction to COPP


## <span id="ddk_introduction_to_the_certified_output_protection_protocol_gg"></span><span id="DDK_INTRODUCTION_TO_THE_CERTIFIED_OUTPUT_PROTECTION_PROTOCOL_GG"></span>


**This section applies only to Windows Server 2003 with SP1 and later, and Windows XP with SP2 and later.**

COPP provides a mechanism of applying copy protection to video that is output by the graphics adapter. COPP provides a common protocol for sending various link-protection requirements to the graphics adapter in a more protected fashion than by using the [**IOCTL\_VIDEO\_HANDLE\_VIDEOPARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567805) I/O control (IOCTL) code.

The following topics describe COPP:

[Cryptographic Primitives Used by COPP](cryptographic-primitives-used-by-copp.md)

[Communicating Through a Secure Channel](communicating-through-a-secure-channel.md)

[Graphics Adapter Output Requirements to Support COPP](graphics-adapter-output-requirements-to-support-copp.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Introduction%20to%20COPP%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




