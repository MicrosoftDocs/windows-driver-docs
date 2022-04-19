---
title: Add or update a code signing certificate
description: Add or update a code signing certificate
ms.topic: article
ms.date: 09/10/2021
---

# Manage code signing certificates

One is a code signing operation that identifies an organization to the dashboard. This is a signature on the package you plan to submit, and it’s a requirement that the dashboard imposes on partners so that the dashboard to prevent malicious people outside your organization from making submissions using your credentials – which could harm your reputation!

# Add or update a code signing certificate

As a Partner Center administrator, you're responsible for keeping your digital certificate information up to date. When the original certificate expires, you'll need to get a new certificate and upload a new file signed with your new digital certificate.

Partner Center supports multiple certificates associated with a single account.  If you want to add additional certificates using this same process.

If you're registering your company on dashboard for the first time, see [Get started with the hardware dashboard program](get-started-with-the-hardware-dashboard.md).

> [!IMPORTANT]
> The certificate uploaded and used for all Partner Center submission packages has changed:
> 
> * You must have an extended validation (EV) code signing certificate to register.
> * Your registered EV certificate must be valid at the time of submission.
> * While Microsoft strongly recommends that you sign individual submissions with an EV certificate, you can alternatively sign submissions with an Authenticode signing certificate that is also registered to your Partner Center account.
> * All certificates must be SHA2 and signed with the `/fd sha256` SignTool command line switch
> * For more information, see [Driver Signing changes in Windows 10, version 1607](https://techcommunity.microsoft.com/t5/windows-hardware-certification/driver-signing-changes-in-windows-10-version-1607/ba-p/364894) in the [Windows Hardware Certification blog](https://techcommunity.microsoft.com/t5/windows-hardware-certification/bg-p/WindowsHardwareCertification).

## To add or update a code signing certificate

### Step 1: Renew your code signing certificate

1. Determine which type of code signing certificate you need. For more information, see [code-singing-certificate](./code-signing-certificate.md).
1. Get a new certificate or reuse an existing certificate.
1. Once you receive your verified certificate from the certificate authority, proceed to **Step 2** to download and sign the "Signablefile.bin"

### Step 2: Sign and upload your Signablefile.bin file

1. Only administrators are allowed to upload or expire hardware dashboard certificates.
1. Once an administrator has signed in, you may use this direct link: [Sign and upload your file](https://partner.microsoft.com/dashboard/account/CertificateUpload), or manually navigate to the page following these steps.
1. Select the gear icon in the upper right, then select **Developer settings**, then **Manage Certificates** on the left pane.
1. Select the **Add a new certificate** button, then select the **Next** button.
1. Download the *Signablefile.bin* and sign it with the new digital certificate for your company using [SignTool](/windows/win32/seccrypto/signtool) with the `/fd sha256` switch and appropriate SHA-2 timestamp.
1. Upload the signed file to Partner Center.

## Related topics

* [Before you sign in](./get-started-with-the-hardware-dashboard.md)
* [Get started with the hardware dashboard program](get-started-with-the-hardware-dashboard.md)
* [Hardware certification submissions](./hardware-certification-submissions.md)
* [App certification submissions](https://techcommunity.microsoft.com/t5/windows-hardware-certification/bg-p/WindowsHardwareCertification)
