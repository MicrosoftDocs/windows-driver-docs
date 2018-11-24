---
title: Update a code signing certificate
description: Update a code signing certificate
ms.assetid: 120AA970-D981-4E7D-A9BD-68125D90A0EE
ms.topic: article
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Update a code signing certificate

As a Hardware Dev Center dashboard administrator, you’re responsible for keeping your digital certificate information up to date. When the original certificate expires, you’ll need to get a new certificate and upload a new file signed with your new digital certificate.

If you’re registering your company on dashboard for the first time, see [Establish a new company](https://msdn.microsoft.com/windows/hardware/drivers/dashboard/establish-a-new-company).

> [!IMPORTANT]
> The certificate uploaded and used for all Hardware Dev Center dashboard submission packages has changed:
> * Extended validation (EV) code signing certificates are required for **all** submissions.  
> * All certificates must be SHA2 and signed with the **/fd sha256** signtool command line switch 
> * (for more information, see this [HLK Blog post](https://blogs.msdn.microsoft.com/windows_hardware_certification/2017/11/13/starting-in-february-2018-packages-signed-using-a-sha-1-digest-algorithm-and-certificate-chain-will-no-longer-be-accepted/)).

## To update a code signing certificate

**Step 1: Renew your code signing certificate**

1. Determine which type of code signing certificate you need (for more information, see [Get a code signing certificate](https://msdn.microsoft.com/windows/hardware/drivers/dashboard/get-a-code-signing-certificate)).

2. Get a new certificate or reuse an existing certificate.

3. Once you receive your verified certificate from the certificate authority, proceed to **Step 2** to download and sign the "Signablefile.bin" 

**Step 2: Sign and upload your "Signablefile.bin file**

1. Only **Administrators** are allowed to upload or expire Hardware Dashboard certificates. 

2. Once an **Administrator** has signed in, you may use this direct link [Sign and upload your file](https://partner.microsoft.com/dashboard/account/CertificateUpload), or manually navigate to the page following these steps.

3. Click the gear icon in the upper right, then click **Developer settings**, then **Manage Certificates** on the left pane.

4. Click the **Add a new certificate** button, then click the **Next** button.  
   
5. Download the Signablefile.bin and sign it with the new digital certificate for your company using SignTool with the following switch **/fd sha256** and appropriate SHA-2 timestamp.

6. Upload the signed file to the Hardware Dev Center dashboard.

## Related topics

- [Before you sign in](https://msdn.microsoft.com/windows/hardware/drivers/dashboard/before-you-sign-in)

- [Establish a new company](https://msdn.microsoft.com/windows/hardware/drivers/dashboard/establish-a-new-company)

- [Hardware certification submissions](https://msdn.microsoft.com/windows/hardware/drivers/dashboard/hardware-certification-submissions)

- [App certification submissions](https://msdn.microsoft.com/windows/hardware/drivers/dashboard/app-certification-submissions)
