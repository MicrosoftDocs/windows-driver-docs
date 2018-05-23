---
title: UEFI Firmware Signing
description: UEFI Firmware Signing
ms.assetid: a39f65c3-9b0b-43ca-9831-ec420fb4cdca
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# UEFI firmware signing

UEFI signing is a service provided by the hardware dashboard that lets you sign UEFI firmware binaries, enabling them to be installed on Windows devices.

> [!IMPORTANT]
> Please note the following:
> * UEFI submissions require an extended validation (EV) code signing certificate. For more information about code signing certificates, see [Get a code signing certificate](get-a-code-signing-certificate.md).
> * UEFI submissions must be in a signed CAB library, and contain all UEFI files required for signing. 
>   * This file should contain no folders and only the .efi files to be signed. 
> * The CAB file signature must match the Authenticode certificate for your organization. See [Authenticode digital signatures](https://docs.microsoft.com/windows-hardware/drivers/install/authenticode) for more information.
>   * Depending on your certificate provider, you may need to use [SignTool](https://msdn.microsoft.com/library/windows/desktop/aa387764) or an external process.
> * EFI ByteCode (EBC) files must be compiled using the /ALIGN:32 flag for processing to succeed.

## Submit new UEFI firmware


1.  Sign in to the dashboard with your Microsoft account and click **Hardware certification**.

2.  On the **File Signing Services** page, click **Submit New UEFI**.
    > [!NOTE]  
    > You may be prompted to sign a legal agreement before creating a new LSA submission. Review and complete the agreement to continue. Every organization only needs to sign the agreement once.

3.  On the **New LSA submission** page, upload the CAB file you want to submit, and click **Submit**.

4. Once your submission has been processed, you’ll receive an email with your submission ID.

## Manage your firmware submission

After signing in to the Hardware Dev Center Dashboard, you can [manage your firmware submission](manage-your-hardware-submissions.md) like any other dashboard submission. 

## Related topics


[Microsoft UEFI CA Signing Policy Updates](http://blogs.msdn.com/b/windows_hardware_certification/archive/2013/12/03/microsoft-uefi-ca-signing-policy-updates.aspx)

[Pre-Submission Testing for UEFI Submissions](http://blogs.msdn.com/b/windows_hardware_certification/archive/2013/12/03/pre-submission-testing-for-uefi-submissions.aspx)

 

 






