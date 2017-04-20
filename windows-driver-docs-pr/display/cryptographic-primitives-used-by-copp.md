---
title: Cryptographic Primitives Used by COPP
description: Cryptographic Primitives Used by COPP
ms.assetid: a14f6f4c-75fd-41a3-93f8-86c9908a2343
keywords:
- copy protection WDK COPP , cryptography
- video copy protection WDK COPP , cryptography
- COPP WDK DirectX VA , cryptography
- protected video WDK COPP , cryptography
- cryptography WDK COPP
- encryption WDK COPP
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Cryptographic Primitives Used by COPP


## <span id="ddk_cryptographic_primitives_used_by_copp_gg"></span><span id="DDK_CRYPTOGRAPHIC_PRIMITIVES_USED_BY_COPP_GG"></span>


This section applies only to Windows Server 2003 with SP1 and later, and Windows XP with SP2 and later.

COPP uses the following cryptographic primitives:

<span id="Public_key_cryptography"></span><span id="public_key_cryptography"></span><span id="PUBLIC_KEY_CRYPTOGRAPHY"></span>Public key cryptography  
COPP requires the RSA algorithm with 2,048-bit keys for public key encryption and decryption. For information about the RSA algorithm, see the [RSA Laboratories](http://go.microsoft.com/fwlink/p/?linkid=70411) website.

<span id="Digital_certificates"></span><span id="digital_certificates"></span><span id="DIGITAL_CERTIFICATES"></span>Digital certificates  
COPP uses eXtensible rights Markup Language (XrML) digital certificates.

<span id="Message_authentication_code__MAC_"></span><span id="message_authentication_code__mac_"></span><span id="MESSAGE_AUTHENTICATION_CODE__MAC_"></span>Message authentication code (MAC)  
COPP uses a one-key Cipher Block Chaining (CBC)-mode MAC (OMAC) for message authenticity. The OMAC is based on Advanced Encryption Standard (AES). For information about AES, see the [RSA Laboratories](http://go.microsoft.com/fwlink/p/?linkid=70411) website. For more information about OMAC, see the [OMAC-1 algorithm](http://go.microsoft.com/fwlink/p/?linkid=70417).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Cryptographic%20Primitives%20Used%20by%20COPP%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




