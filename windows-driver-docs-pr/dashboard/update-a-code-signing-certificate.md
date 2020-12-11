---
title: Add or Update a code signing certificate
description: Add or Update a code signing certificate
ms.topic: article
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Add or Update a code signing certificate

As a Partner Center administrator, you’re responsible for keeping your digital certificate information up to date. When the original certificate expires, you’ll need to get a new certificate and upload a new file signed with your new digital certificate.

Partner Center supports multiple certificates associated with a single account.  If you want to add additional certificates using this same process.

If you’re registering your company on dashboard for the first time, see [Get started with the hardware dashboard program](get-started-with-the-hardware-dashboard.md).

> [!IMPORTANT]
> The certificate uploaded and used for all Partner Center submission packages has changed:
>
> * Extended validation (EV) code signing certificates are required for **all** submissions.  
> * All certificates must be SHA2 and signed with the **/fd sha256** signtool command line switch
> * (for more information, see this [HLK Blog post](https://techcommunity.microsoft.com/t5/Windows-Hardware-Certification/bg-p/WindowsHardwareCertification)).

## To add or update a code signing certificate

### Step 1: Renew your code signing certificate if needed  

1. Determine which type of code signing certificate you need (for more information, see [Get a code signing certificate](./get-a-code-signing-certificate.md)).

2. Get a new certificate or reuse an existing certificate.

3. Once you receive your verified certificate from the certificate authority, proceed to **Step 2** to download and sign the "Signablefile.bin"

### Step 2: Sign and upload your "Signablefile.bin file

1. Only **Administrators** are allowed to upload or expire Hardware Dashboard certificates.

2. Once an **Administrator** has signed in, you may use this direct link [Sign and upload your file](https://partner.microsoft.com/dashboard/account/CertificateUpload), or manually navigate to the page following these steps.

3. Select the gear icon in the upper right, then select **Developer settings**, then **Manage Certificates** on the left pane.

4. Select the **Add a new certificate** button, then select the **Next** button.  

5. Download the Signablefile.bin and sign it with the new digital certificate for your company using SignTool with the following switch **/fd sha256** and appropriate SHA-2 timestamp.

6. Upload the signed file to the Partner Center.

## Related topics

* [Before you sign in](./get-started-with-the-hardware-dashboard.md)

* [Get started with the hardware dashboard program](get-started-with-the-hardware-dashboard.md)

* [Hardware certification submissions](./hardware-certification-submissions.md)

* [App certification submissions](https://techcommunity.microsoft.com/t5/windows-hardware-certification/bg-p/WindowsHardwareCertification)
