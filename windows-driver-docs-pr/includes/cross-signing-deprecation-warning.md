---
description: "Warning about deprecation of cross signing for driver signing"
title: Warning about deprecation of cross signing for driver signing
ms.date: 09/19/2023
ms.topic: include
---

> [!WARNING]
> Cross-signing is no longer accepted for driver signing. Using cross certificates to sign kernel-mode drivers is a violation of the [Microsoft Trusted Root Program](/security/trusted-root/program-requirements) (TRP) policy. The TRP no longer supports root certificates that have kernel mode signing capabilities.
> Certificates in violation of Microsoft TRP policies will be revoked by the CA.
