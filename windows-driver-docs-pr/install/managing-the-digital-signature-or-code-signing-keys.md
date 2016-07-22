---
title: Managing the Digital Signature or Code Signing Keys
description: Managing the Digital Signature or Code Signing Keys
ms.assetid: 3aaa713b-c964-4a1e-9b2c-dee66cb4c4b2
keywords: ["driver signing WDK , cryptographic keys", "signing drivers WDK , cryptographic keys", "digital signatures WDK , cryptographic keys", "signatures WDK , cryptographic keys", "cryptography WDK driver signing", "keys WDK driver signing"]
---

# Managing the Digital Signature or Code Signing Keys


The cryptographic keys that are at the heart of the Authenticode signing process must be well protected and treated with the same care as the publisher's most valuable assets. These keys represent an organization's identity. Any code that is signed with these keys appears to Windows as if it contains a valid digital signature that can be traced to the organization. If the keys are stolen, they could be used to fraudulently sign malicious code and possibly result in the delivery of code that contains Trojan or a virus that appears to come from a legitimate publisher.

For detailed information on safe-guarding private keys, see the [Code-Signing Best Practices](http://go.microsoft.com/fwlink/p/?linkid=74265) website.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Managing%20the%20Digital%20Signature%20or%20Code%20Signing%20Keys%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




