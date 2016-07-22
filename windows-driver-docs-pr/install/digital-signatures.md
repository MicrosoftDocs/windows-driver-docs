---
title: Digital Signatures
description: Digital Signatures
ms.assetid: 637212b2-bc57-414b-9a06-07f79d9264f9
keywords: ["driver package digital signatures WDK", "package digital signatures WDK", "digital signatures WDK , driver packages", "signatures WDK , driver packages", "driver signing WDK , driver packages", "signing drivers WDK , driver packages", "device installations WDK , digital signatures", "driver signing WDK", "certificates WDK , about digital signatures"]
---

# Digital Signatures


Digital signatures are based on Microsoft public key infrastructure technology, which is based on Microsoft [Authenticode](authenticode.md) combined with an infrastructure of trusted certification authorities (CAs). Authenticode, which is based on industry standards, allows vendors, or *software publishers*, to sign either a file or a collection of files (such as a [driver package](driver-packages.md)) by using a code-signing [digital certificate](digital-certificates.md) that is issued by a CA.

Windows uses a valid digital signature to verify the following:

-   The file, or the collection of files, is signed.

-   The signer is trusted.

-   The certification authority that authenticated the signer is trusted.

-   The collection of files was not altered after it was published.

For example, this signing process for a [driver package](driver-packages.md) involves the following:

-   A publisher obtains an *X.509 digital certificate* from a CA. An Authenticode certificate is also referred to as a *signing certificate*. A signing certificate is a set of data that identifies a publisher, and is issued by a CA only after the CA has verified the identity of the publisher. A CA can be a Microsoft CA, a third-party commercial CA, or an Enterprise CA.

    The signing certificate is used to sign the [catalog file](catalog-files.md) of a driver package or to [embed a signature](embedded-signatures-in-a-driver-file.md) in a driver file. Certificates that identify trusted publishers and trusted CAs are installed in [certificate stores](certificate-stores.md) that are maintained by Windows.

-   The signing certificate includes a private key and a public key, which is known as the *key pair*. The private key is used to sign the catalog file of a [driver package](driver-packages.md) or to embed a signature in a driver file. The public key is used to verify the signature of a driver package's catalog file or a signature that is embedded in a driver file.

-   To sign a catalog file or to embed a signature in a file, the signing process first generates a cryptographic hash, or *thumbprint*, of the file. The signing process then encrypts the file thumbprint with a private key and adds the thumbprint to the file.

    The signing process also adds information about the publisher and the CA that issued the signing certificate. The digital signature is added to the file in a section of the file that is not processed when the file thumbprint is generated.

-   To verify the digital signature of a file, Windows extracts the information about the publisher and the CA and uses the public key to decrypt the encrypted file thumbprint.

    Windows accepts the integrity of the file and the authenticity of the publisher only if the following are true:

    -   The decrypted thumbprint matches the thumbprint of the file.
    -   The certificate of the publisher is installed in the [Trusted Publishers certificate store](trusted-publishers-certificate-store.md).
    -   The root certificate of the CA that issued the publisher's certificate is installed in the [Trusted Root Certification Authorities certificate store](trusted-root-certification-authorities-certificate-store.md).

For more information about how the Plug and Play (PnP) device installation uses the digital signature of a [driver package's](driver-packages.md) [catalog file](catalog-files.md), see [Digital Signatures and PnP Device Installation](digital-signatures-and-pnp-device-installation.md).

For more information about Microsoft public key infrastructure technology, code signing, and digital signatures, see [Introduction to Code Signing](http://go.microsoft.com/fwlink/p/?linkid=104071) and [Code Signing Best Practices](http://go.microsoft.com/fwlink/p/?linkid=68250).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Digital%20Signatures%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




