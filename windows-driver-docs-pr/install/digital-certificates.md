---
title: Digital Certificates
description: Digital Certificates
ms.assetid: 90427be5-7b61-4ed6-ab5d-847b64c7dcf0
keywords:
- digital certificates WDK
- driver package digital certificates WDK
- package digital certificates WDK
- digital certificates WDK , driver packages
- certificates WDK
- certificates WDK , driver packages
- driver signing WDK , digital certificates
- signing drivers WDK , digital certificates
- device installations WDK , digital certificates
- driver signing WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





