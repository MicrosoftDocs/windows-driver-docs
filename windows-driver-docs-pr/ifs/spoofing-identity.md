---
title: Spoofing Identity
description: Spoofing Identity
ms.assetid: adc0b986-a8c2-45ce-a4d5-9d4d867603b5
keywords: ["threat models WDK file systems , spoofing identity", "security threat models WDK file systems , spoofing identity", "spoofing identity WDK file systems", "identity spoofing WDK file systems"]
---

# Spoofing Identity


## <span id="ddk_spoofing_identity_if"></span><span id="DDK_SPOOFING_IDENTITY_IF"></span>


The concept of spoofing identity is allowing unprivileged code to use someone else's identity, and hence, their security credentials. For example, a driver that uses some form of a password mechanism is subject to this type of attack. Not all such drivers have security flaws, although, they are vulnerable to security flaws based on spoofing identity. The designers and implementers of the driver need to evaluate the level of vulnerability.

Other more subtle examples of spoofing identity exist. For example, an encryption filter driver that relies upon a smart card for the decryption key is subject to a physical spoofing attack if the smart card is lost or stolen. So, a filter driver might add some additional requirement, such as a biometric confirmation or a password, to protect against this category of attack.

A driver that attempts to perform its own security checks must be particularly vigilant to ensure that it uses the proper credentials during the security check. A failure to do so can easily provide a spoofing exploit that would allow a malicious user who discovered it to perform operations that would appear to have been done by someone else, since the security descriptor would be correct.

In general, drivers are best designed and implemented if they take advantage of the existing security mechanisms within the operating system, rather than constructing their own. This minimizes the number of potential locations where the implementation may contain errors.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Spoofing%20Identity%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




