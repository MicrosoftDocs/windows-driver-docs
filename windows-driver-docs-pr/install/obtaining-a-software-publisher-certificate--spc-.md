---
title: Obtaining a Software Publisher Certificate (SPC)
description: Obtaining a Software Publisher Certificate (SPC)
ms.assetid: 50546234-e98d-40ed-b9c6-7d78cf0419ca
---

# Obtaining a Software Publisher Certificate (SPC)


Release-signing requires:

-   A Software Publisher Certificate (SPC), along with the certificate's public and private cryptographic keys.

-   An associated cross-certificate.

The SPC is obtained through a commercial certificate authority (CA). The CA will also provide private and public keys for the certificate. In order to be used for creating digital signatures, the SPC and keys must be converted to a Personal Information Exchange (*.pfx*) file. For more information about this process, see [Personal Information Exchange (.pfx) Files](personal-information-exchange---pfx--files.md).

Once the SPC and keys are stored in a *.pfx* file, they must be imported into the Personal certificate store on the signing computer. For more information, see [Importing an SPC into a Certificate Store](importing-an-spc-into-a-certificate-store.md).

Microsoft has issued one cross-certificate for each public key root certificate for CAs, which supports the use of Software Publisher Certificates for kernel-mode code signing. You must use correct cross-certificate when release-signing a driver package. To determine which cross-certificate is needed for release-signing, see [Determining an SPC's Cross-Certificate](determining-an-spc-s-cross-certificate.md).

For a list of certification authorities that provide SPCs and for more information about cross-certificates, see [Microsoft Cross-Certificates for Windows Vista Kernel Mode Code Signing](http://go.microsoft.com/fwlink/p/?linkid=66583). Follow the instructions on the CA's website for obtaining and installing the SPC and corresponding cross-certificate on the signing computer.

For more information about SPCs and their management, see [Software Publisher Certificate (SPC)](software-publisher-certificate.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Obtaining%20a%20Software%20Publisher%20Certificate%20%28SPC%29%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




