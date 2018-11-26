---
title: Spoofing Identity
description: Spoofing Identity
ms.assetid: adc0b986-a8c2-45ce-a4d5-9d4d867603b5
keywords:
- threat models WDK file systems , spoofing identity
- security threat models WDK file systems , spoofing identity
- spoofing identity WDK file systems
- identity spoofing WDK file systems
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Spoofing Identity


## <span id="ddk_spoofing_identity_if"></span><span id="DDK_SPOOFING_IDENTITY_IF"></span>


The concept of spoofing identity is allowing unprivileged code to use someone else's identity, and hence, their security credentials. For example, a driver that uses some form of a password mechanism is subject to this type of attack. Not all such drivers have security flaws, although, they are vulnerable to security flaws based on spoofing identity. The designers and implementers of the driver need to evaluate the level of vulnerability.

Other more subtle examples of spoofing identity exist. For example, an encryption filter driver that relies upon a smart card for the decryption key is subject to a physical spoofing attack if the smart card is lost or stolen. So, a filter driver might add some additional requirement, such as a biometric confirmation or a password, to protect against this category of attack.

A driver that attempts to perform its own security checks must be particularly vigilant to ensure that it uses the proper credentials during the security check. A failure to do so can easily provide a spoofing exploit that would allow a malicious user who discovered it to perform operations that would appear to have been done by someone else, since the security descriptor would be correct.

In general, drivers are best designed and implemented if they take advantage of the existing security mechanisms within the operating system, rather than constructing their own. This minimizes the number of potential locations where the implementation may contain errors.

 

 




