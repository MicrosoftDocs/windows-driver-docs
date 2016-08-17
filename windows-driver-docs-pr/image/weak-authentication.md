---
title: Weak Authentication
description: Weak Authentication
MS-HAID:
- 'dsm\_des\_tut\_b4b109b2-0812-4572-b563-f6ab291c3894.xml'
- 'image.weak\_authentication'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: ff220633-31cb-4405-a0a5-c6d9e7e51f76
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Weak%20Authentication%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




