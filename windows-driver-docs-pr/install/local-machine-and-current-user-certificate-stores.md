---
title: Local Machine and Current User Certificate Stores
description: Learn about the local machine certificate and current user certificate stores, and how stores inherit certificates.
ms.date: 10/30/2025
ms.topic: concept-article
#customer intent: As a developer or administrator, I need to understand the relationship between local machine and current user certificate stores. 
---

# Local machine and current user certificate stores

Each of the system certificate stores has the following types:

- Local machine certificate store

  This type of certificate store is local to the computer and global to all users on the computer. It's located under the `HKEY_LOCAL_MACHINE` root in the registry.

- Current user certificate store

  This type of certificate store is local to a user account on the computer. It's located under the `HKEY_CURRENT_USER` registry root.

For specific registry locations of certificate stores, see [System Store Locations](/windows/desktop/seccrypto/system-store-locations).

All current user certificate stores *except the Current User or Personal store* inherit the contents of the local machine certificate stores. For example, if a certificate is added to the local machine [Trusted Root Certification Authorities certificate store](trusted-root-certification-authorities-certificate-store.md), all current user Trusted Root Certification Authorities certificate stores (with the previous caveat) also contain the certificate.

> [!NOTE]
> The driver signing verification during Plug and Play (PnP) installation requires that root and Authenticode certificates, including [test certificates](./makecert-test-certificate.md), are located in a local machine certificate store.

For more information about how to add or delete certificates from the system certificate stores, see [CertMgr](../devtest/certmgr.md).
