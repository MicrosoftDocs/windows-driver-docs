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
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





