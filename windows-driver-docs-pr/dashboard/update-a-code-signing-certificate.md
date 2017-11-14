---
title: Update a code signing certificate
description: Update a code signing certificate
ms.assetid: 120AA970-D981-4E7D-A9BD-68125D90A0EE
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Update a code signing certificate

As a Hardware Dev Center dashboard administrator, you’re responsible for keeping your digital certificate information up to date. When the original certificate expires, you’ll need to get a new certificate and upload a new file signed with your new digital certificate.

If you’re registering your company on dashboard for the first time, see [Establish a new company](https://msdn.microsoft.com/windows/hardware/drivers/dashboard/establish-a-new-company).

> [!IMPORTANT]
> Starting March 13, 2014, code signing certificate requirements for Hardware Dev Center dashboard have changed to include:
* Extended validation (EV) code signing certificates. EV code signing certificates are required for:
  1. LSA plug-ins
  2. UEFI submissions (starting August 15, 2014)
* New certificate authorities: DigiCert, Entrust, GlobalSign, in addition to Symantec

For more information about code signing requirements, see [Get a code signing certificate](https://msdn.microsoft.com/windows/hardware/drivers/dashboard/get-a-code-signing-certificate). UEFI and LSA certification now require extended validation code signing certificates.

## To update a code signing certificate

**Step 1: Renew your code signing certificate**

1. Determine which type of code signing certificate you need (for more information, see [Get a code signing certificate](https://msdn.microsoft.com/windows/hardware/drivers/dashboard/get-a-code-signing-certificate)).

2. Get a new certificate or reuse an existing certificate.

3. Once you receive your verified certificate from the certificate authority, you can sign and upload the Winqual.exe file following the instructions below.

**Step 2: Sign and upload your Winqual.exe file**

1. From the Hardware Dev Center dashboard, sign in as an administrator with your Microsoft account.

2. Download the [Winqual.exe file](http://go.microsoft.com/fwlink/?LinkId=393250) from the Hardware Dev Center dashboard, and sign it with the new digital certificate for your company using the **SignTool**.

3. On the **Administration** page, in the **Digital certificates** tile, click **Upload code for digital certification**.

4. On the **Digital certificates** page, click **Browse** to locate and select the Winqual.exe file that has been signed with the correct digital certificate for your company.

## Related topics

[Before you sign in](https://msdn.microsoft.com/windows/hardware/drivers/dashboard/before-you-sign-in)

[Establish a new company](https://msdn.microsoft.com/windows/hardware/drivers/dashboard/establish-a-new-company)

[Hardware certification submissions](https://msdn.microsoft.com/en-us/windows/hardware/drivers/dashboard/hardware-certification-submissions)

[App certification submissions](https://msdn.microsoft.com/windows/hardware/drivers/dashboard/app-certification-submissions)
