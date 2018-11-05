---
title: Managing the Digital Signature or Code Signing Keys
description: Managing the Digital Signature or Code Signing Keys
ms.assetid: 3aaa713b-c964-4a1e-9b2c-dee66cb4c4b2
keywords:
- driver signing WDK , cryptographic keys
- signing drivers WDK , cryptographic keys
- digital signatures WDK , cryptographic keys
- signatures WDK , cryptographic keys
- cryptography WDK driver signing
- keys WDK driver signing
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Managing the Digital Signature or Code Signing Keys


The cryptographic keys that are at the heart of the Authenticode signing process must be well protected and treated with the same care as the publisher's most valuable assets. These keys represent an organization's identity. Any code that is signed with these keys appears to Windows as if it contains a valid digital signature that can be traced to the organization. If the keys are stolen, they could be used to fraudulently sign malicious code and possibly result in the delivery of code that contains Trojan or a virus that appears to come from a legitimate publisher.


 

 





