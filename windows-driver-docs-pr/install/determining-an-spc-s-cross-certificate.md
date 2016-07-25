---
title: Determining an SPC's Cross-Certificate
description: Determining an SPC's Cross-Certificate
ms.assetid: e54c6c69-6b80-4a03-b4ff-e46d565a56d9
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Determining%20an%20SPC's%20Cross-Certificate%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




