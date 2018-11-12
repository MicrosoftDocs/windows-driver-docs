---
title: Determining an SPC's Cross-Certificate
description: Determining an SPC's Cross-Certificate
ms.assetid: e54c6c69-6b80-4a03-b4ff-e46d565a56d9
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Determining an SPC's Cross-Certificate


In addition to obtaining a Software Publisher Certificate (SPC) from a commercial certificate authority (CA), you must obtain a cross-certificate that Microsoft issues. The cross certificate is used to verify that the CA that issued an SPC is a trusted root authority. Both a cross-certificate and an SPC are required for release-signing.

A cross-certificate is an X.509 certificate issued by a CA that signs the public key for the root certificate of another CA. Cross-certificates allow the kernel to have a single trusted Microsoft root authority, but also provide the flexibility to extend the chain of trust to commercial CAs that issue SPCs.

Before you can determine which cross-certificate is needed for release-signing, you must first import the Personal Information Exchange (.*pfx*) file, which stores a Software Publisher Certificate (SPC) and its private and public keys, into the Personal certificate store. For more information about this process, see [Importing an SPC into a Certificate Store](importing-an-spc-into-a-certificate-store.md).

Once the *.pfx* file is imported into the Personal store on the signing computer, do the following to determine which cross-certificate you can use with your SPC for release-signing.

1.  Click **Start** and then click **Run**.

2.  To start the MMC Certificates snap-in, type Certmgr.msc and press the **Enter** key.

3.  Locate the signing certificate in the certificate store. The certificate should be listed in one of the following locations, depending on how it was installed:

    -   Current User-&gt;Personal-&gt;Certificates store
    -   Local Machine-&gt;Certificates store

4.  To open the **Certificate** dialog box, double click the certificate.

5.  In the **Certificate** dialog box, select the **Certification Path** tab, and then select the top-most certificate in the certification path.

    This is the CA that is the issuing root authoring for your certificate.

6.  To view the root authority certificate, select **View Certificate**, and then click the **Details** property tab.

7.  Find the **Issuer Name** and **Thumbprint** for the issuing CA of this certificate. Locate the corresponding cross-certificate in the "Root Authority Cross Certificate List" section of the [Microsoft Cross-Certificates for Windows Vista Kernel Mode Code Signing](http://go.microsoft.com/fwlink/p/?linkid=190544) white paper.

8.  Download the related cross-certificate from the "Root Authority Cross Certificate List" section and use this cross-certificate when digitally signing [driver packages](driver-packages.md).

For more information about SPCs and their management, see [Software Publisher Certificate (SPC)](software-publisher-certificate.md).

 

 





