---
title: Cryptographic Primitives Used by COPP
description: Cryptographic Primitives Used by COPP
keywords:
- copy protection WDK COPP , cryptography
- video copy protection WDK COPP , cryptography
- COPP WDK DirectX VA , cryptography
- protected video WDK COPP , cryptography
- cryptography WDK COPP
- encryption WDK COPP
ms.date: 11/17/2021
ms.localizationpriority: medium
---

# Cryptographic Primitives Used by COPP

This section applies only to Windows Server 2003 with SP1 and later, and Windows XP with SP2 and later.

COPP uses the following cryptographic primitives:

| Primitive | Explanation |
| --------- | ----------- |
| Public key cryptography | COPP requires the [RSA algorithm](https://www.rsa.com) with 2,048-bit keys for public key encryption and decryption. |
| Digital certificates    | COPP uses eXtensible rights Markup Language (XrML) digital certificates. |
| Message authentication code (MAC) | COPP uses a one-key Cipher Block Chaining (CBC)-mode MAC (OMAC) for message authenticity. The OMAC is based on Advanced Encryption Standard (AES). For information about AES, see the [RSA Laboratories](https://www.rsa.com) website. For more information about OMAC, see the [OMAC-1 algorithm](https://go.microsoft.com/fwlink/p/?linkid=70417).
