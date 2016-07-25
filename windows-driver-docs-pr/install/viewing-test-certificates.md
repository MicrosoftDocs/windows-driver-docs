---
title: Viewing Test Certificates
description: Viewing Test Certificates
ms.assetid: bdfa8970-fdba-4d65-8a9c-960e5f6844d6
keywords: ["driver signing WDK , viewing test certificates"]
---

# Viewing Test Certificates


After the certificate is created and a copy is put in the certificate store, the Microsoft Management Console (MMC) Certificates snap-in can be used to view it. Do the following to view a certificate through the MMC **Certificates** snap-in:

1.  Click **Start** and then click Start Search.

2.  To start the Certificates snap-in, type Certmgr.msc and press the **Enter** key.

3.  In the left pane of the Certificates snap-in, expand the PrivateCertStore certificate store folder and double-click Certificates.

The following screen shot shows the Certificates snap-in view of the **PrivateCertStore** certificate store folder.

![screen shot of the certificate store showing the test certificate ](images/certstore.png)

To view the details about the Contoso.com(Test) certificate, double-click the certificate in the right pane. The following screen shot shows the details about the certificate.

![screen shot of the certificate window displaying the details of the contoso.com (test) certificate](images/certinfo.png)

Notice that the Certificate dialog box states: "This CA Root certificate is not trusted. To enable trust, install this certificate in the Trusted Root Certification Authorities store." This is the expected behavior. The certificate cannot be verified because Windows does not trust the issuing authority, "Contoso.com(Test)" by default.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Viewing%20Test%20Certificates%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




