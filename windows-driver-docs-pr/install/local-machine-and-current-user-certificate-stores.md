---
title: Local Machine and Current User Certificate Stores
description: Local Machine and Current User Certificate Stores
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Local Machine and Current User Certificate Stores

Each of the system certificate stores has the following types:

* Local machine certificate store

    This type of certificate store is local to the computer and is global to all users on the computer. This certificate store is located in the registry under the HKEY_LOCAL_MACHINE root.

* Current user certificate store

    This type of certificate store is local to a user account on the computer. This certificate store is located in the registry under the HKEY_CURRENT_USER root.

For specific registry locations of certificate stores, see [System Store Locations](/windows/desktop/seccrypto/system-store-locations).

Be aware that all current user certificate stores *except the Current User/Personal store* inherit the contents of the local machine certificate stores. For example, if a certificate is added to the local machine [Trusted Root Certification Authorities certificate store](trusted-root-certification-authorities-certificate-store.md), all current user Trusted Root Certification Authorities certificate stores (with the above caveat) also contain the certificate.

>[!NOTE]
>The driver signing verification during Plug and Play (PnP) installation requires that root and Authenticode certificates, including [test certificates](./makecert-test-certificate.md), are located in a local machine certificate store.

For more information about how to add or delete certificates from the system certificate stores, see [**CertMgr**](../devtest/certmgr.md).
