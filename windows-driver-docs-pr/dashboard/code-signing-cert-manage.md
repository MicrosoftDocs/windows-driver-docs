---
title: Manage Code Signing Certificates
description: This article describes how to get, add, and update code signing certificates to the hardware dashboard.
ms.date: 05/29/2025
ms.topic: how-to
---

# Manage code signing certificates

As a Partner Center administrator, you're responsible for adding, updating, and retiring driver certificates when they expire. This article describes how to get, add, and update code signing certificates to the hardware dashboard.

For more information on rules for driver signing, see [Driver signing changes in Windows 10, version 1607](https://techcommunity.microsoft.com/blog/windowshardwarecertification/driver-signing-changes-in-windows-10-version-1607/364894) in the [Windows Hardware Certification blog](https://techcommunity.microsoft.com/category/winhec-online/blog/windowshardwarecertification).

## Prerequisites

Register for the Hardware Developer program. If you're not registered, follow the steps in [Register for the Microsoft Windows Hardware Developer Program](hardware-program-register.md).

## Get or renew a code signing certificate

To get a new code signing certificate:

1. Determine which certificate you need. To help you choose a certificate, see [Driver signing requirements](code-signing-reqs.md).

1. If you're reusing a certificate, move on to step 5.

1. If your organization doesn't have a certificate, you need to [purchase an EV certificate from a trusted vendor](code-signing-reqs.md#where-to-get-ev-code-signing-certificates).

1. After the certificate authority verifies your contact information and your certificate purchase is approved, follow their directions to retrieve the certificate.

1. Go to [Partner Center](https://partner.microsoft.com/dashboard) and sign in by using your administrator credentials.

1. Select the gear icon in the upper right, select **Account Settings**, and then select **Manage Certificates** on the left side of the screen.

1. Select **Add a new certificate**, and then select **Next**.

1. Download *Signablefile.bin*. Sign it with the new digital certificate for your company by using [SignTool](/windows/win32/seccrypto/signtool) with the `/fd sha256` switch and the appropriate SHA-2 timestamp.

1. Upload the signed file to Partner Center.

## Retire a code signing certificate

1. Go to [Partner Center](https://partner.microsoft.com/dashboard) and sign in by using your administrator credentials.

1. Select the gear icon in the upper right, select **Developer settings**, and then select **Manage Certificates** on the left pane.

1. Find the certificate that you want to remove.

1. Under the **Action** column of the certificate, select **Remove**.
