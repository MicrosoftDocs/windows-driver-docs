---
title: Weak Authentication
author: windows-driver-content
description: Weak Authentication
ms.assetid: ff220633-31cb-4405-a0a5-c6d9e7e51f76
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# Weak Authentication


As part of the scan server installation, a server certificate will be attached to the scan server. The server certificate will be provided during the creation of the secure http connection. The device must ensure the server certificate is issued by a trusted certificate authority. It is recommended that you use standard SSL validation, Enterprise PKI root discovery, TLS 1.2 channel.

### TLS Information

For information about all the TLS RFCs, see the IETF TLS charter page at [Transport Layer Security (tls)](http://go.microsoft.com/fwlink/p/?linkid=518817).

The latest protocol version is TLS 1.2 (RFC 5246). For more information, see [The Transport Layer Security (TLS) Protocol](http://go.microsoft.com/fwlink/p/?linkid=154084)

Section 7.4 describes the SSL handshake including the certificate validation.

TLS1.2 is supported on Windows 7 and Windows Server 2008 R2. It is not supported on down-level OS.

### Certificate Path RFC

Certificate path validation RFC is RFC 5280. For more information, see [RFC 5280 Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile](http://go.microsoft.com/fwlink/p/?linkid=154086).

Refer to section 6 for basic path validation recommendations.

Windows is compliant with the RFC guidance.

### Enterprise Root Paths

For the Enterprise roots, the path is most easily discovered by using the "cerutil -store -?" command.

For example:

```
C:\Users\cmaca>certutil -store -?
Usage:
  CertUtil [Options] -store [CertificateStoreName [CertId [OutputFile]]]
  Dump certificate store
    CertificateStoreName -- Certificate store name.  Examples:
            "My", "CA" (default), "Root",
 
            "ldap:///CN=Certification Authorities,CN=Public Key Services,CN=Services,CN=Configuration,DC=corp,DC=microsoft,DC=com?cACertificate?one?objectClass=certificationAuthority" (View Root Certificates)
```

Elements are the relative top level paths in the DN: CN=Certification Authorities,CN=Public Key Services,CN=Services,CN=Configuration.

A device can get the Enterprise roots by querying this container as suggested above with the arguments: "cACertificate?one?objectClass=certificationAuthority"

 

 




