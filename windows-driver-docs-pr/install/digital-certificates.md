---
title: Digital Certificates
description: Digital Certificates
ms.assetid: 90427be5-7b61-4ed6-ab5d-847b64c7dcf0
keywords: ["digital certificates WDK", "driver package digital certificates WDK", "package digital certificates WDK", "digital certificates WDK , driver packages", "certificates WDK", "certificates WDK , driver packages", "driver signing WDK , digital certificates", "signing drivers WDK , digital certificates", "device installations WDK , digital certificates", "driver signing WDK"]
---

# Digital Certificates


Digital certificates bind an entity, such as an individual, organization, or system, to a specific pair of public and private keys. Digital certificates can be thought of as electronic credentials that verify the identity of an individual, system, or organization.

Various types of digital certificates are used for a variety of purposes, such as the following:

-   Secure Multipurpose Internet Mail Extensions (S/MIME) digital certificates for signing email messages.

-   Secure Sockets Layer (SSL) and Internet Protocol security (IPSec) digital certificates for authenticating network connections.

-   Smart card digital certificates for logging on to personal computers.

Windows code-signing technologies use X.509 code-signing certificates, a standard that is owned by the Internet Engineering Task Force (IETF). Code-signing certificates allow software publishers or distributors to digitally sign software.

A certificate is contained in a digital signature and verifies the origin of the signature. The certificate owner's public key is in the certificate and is used to verify the digital signature. This practice avoids having to set up a central facility for distributing the certificates. The certificate owner's private key is kept separately and is known only to the certificate owner.

Software publishers must obtain a certificate from a certification authority (CA), which vouches for the integrity of the certificate. Typically, a CA requires the software publisher to provide unique identifying information. The CA uses this information to authenticate the identity of the requester before issuing the certificate. Software publishers must also agree to abide by the policies that are set by the CA. If they fail to do so, the CA can revoke the certificate.

Once a certificate is obtained from the CA, software publishers must store the certificate locally in the computer. For more information about this process, see [Certificate Stores](certificate-stores.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Digital%20Certificates%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




