---
title: Local Machine and Current User Certificate Stores
description: Local Machine and Current User Certificate Stores
ms.assetid: b7362f2e-c8ff-42e4-9edc-df4b9967df29
---

# Local Machine and Current User Certificate Stores


Each of the system certificate stores has the following types:

<a href="" id="local-machine-certificate-store"></a>Local machine certificate store  
This type of certificate store is local to the computer and is global to all users on the computer. This certificate store is located in the registry under the HKEY\_LOCAL\_MACHINE root.

<a href="" id="current-user-certificate-store"></a>Current user certificate store  
This type of certificate store is local to a user account on the computer. This certificate store is located in the registry under the HKEY\_CURRENT\_USER root.

Be aware that all current user certificate stores inherit the contents of the local machine certificate stores. For example, if a certificate is added to the local machine [Trusted Root Certification Authorities certificate store](trusted-root-certification-authorities-certificate-store.md), all current user Trusted Root Certification Authorities certificate stores also contain the certificate.

**Note**  The driver signing verification during Plug and Play (PnP) installation requires that root and Authenticode certificates, including [test certificates](test-certificates.md), are located in a local machine certificate store.

 

For more information about how to add or delete certificates from the system certificate stores, see [**CertMgr**](https://msdn.microsoft.com/library/windows/hardware/ff543411).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Local%20Machine%20and%20Current%20User%20Certificate%20Stores%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




