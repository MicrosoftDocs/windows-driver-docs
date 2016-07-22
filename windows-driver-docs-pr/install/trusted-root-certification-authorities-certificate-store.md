---
title: Trusted Root Certification Authorities Certificate Store
description: Trusted Root Certification Authorities Certificate Store
ms.assetid: c1969171-3691-4110-9530-693853728327
keywords: ["certificate stores WDK", "driver signing WDK , digital signatures", "Trusted Root Certification Authorities certificate store WDK"]
---

# Trusted Root Certification Authorities Certificate Store


Starting with Windows Vista, the Plug and Play (PnP) manager performs driver signature verification during device and driver installation. However, the PnP manager can successfully verify a digital signature only if the following statements are true:

-   The signing certificate that was used to create the signature was issued by a certification authority (CA).

-   The corresponding root certificate for the CA is installed in the *Trusted Root Certification Authorities certificate store*. Therefore, the Trusted Root Certification Authorities certificate store contains the root certificates of all CAs that Windows trusts.

By default, the Trusted Root Certification Authorities certificate store is configured with a set of public CAs that has met the requirements of the Microsoft Root Certificate Program. Administrators can configure the default set of trusted CAs and install their own private CA for verifying software.

**Note**  A private CA is unlikely to be trusted outside the network environment.

 

Having a valid digital signature ensures the authenticity and integrity of a [driver package](driver-packages.md). However, it does not mean that the end-user or a system administrator implicitly trusts the software publisher. A user or administrator must decide whether to install or run an application on a case-by-case basis, based on their knowledge of the software publisher and application. By default, a publisher is trusted only if its certificate is installed in the [Trusted Publishers certificate store](trusted-publishers-certificate-store.md).

The name of the Trusted Root Certification Authorities certificate store is *root.* You can manually install the root certificate of a private CA into the Trusted Root Certification Authorities certificate store on a computer by using the [**CertMgr**](https://msdn.microsoft.com/library/windows/hardware/ff543411) tool.

**Note**  The driver signing verification policy that is used by the PnP manager requires that the root certificate of a private CA has been previously installed in the local machine version of the Root Certification Authorities certificate store. For more information, see [Local Machine and Current User Certificate Stores](local-machine-and-current-user-certificate-stores.md).

 

For more information about certificate stores, see the [Code Signing Best Practices](http://go.microsoft.com/fwlink/p/?linkid=68250) website.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Trusted%20Root%20Certification%20Authorities%20Certificate%20Store%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




