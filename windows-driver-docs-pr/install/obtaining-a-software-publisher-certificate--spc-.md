---
title: Obtaining a Software Publisher Certificate (SPC)
description: Obtaining a Software Publisher Certificate (SPC)
ms.assetid: 50546234-e98d-40ed-b9c6-7d78cf0419ca
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





