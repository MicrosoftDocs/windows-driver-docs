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
> * LSA submissions require an extended validation (EV) code signing certificate. For more information about code signing certificates, see [Get a code signing certificate](get-a-code-signing-certificate.md).
> * All UEFI submissions must be in a single, signed CAB file, and contain all UEFI files required for signing. 
>   * This file should contain no folders and only the binaries to be signed. 
> * The CAB file signature must match the Authenticode certificate for your organization. See [Authenticode digital signatures](https://docs.microsoft.com/windows-hardware/drivers/install/authenticode) for more information.
>   * Depending on your certificate provider, you may need to use [SignTool](https://msdn.microsoft.com/library/windows/desktop/aa387764) or an external process.
## Submit new UEFI firmware


1.  Sign in to the dashboard with your Microsoft account and click **Hardware certification**.

2.  On the **File Signing Services** page, click **Submit New UEFI**.
    > [!NOTE]  
    > You may be prompted to sign a legal agreement before creating a new LSA submission. Review and complete the agreement to continue. Every organization only needs to sign the agreement once.

3.  All UEFI submissions must be in a single, signed CAB file and contain all the UEFI files for signing. The CAB file signature must match the Authenticode certificate on file for your company with dashboard. Depending on your certificate provider, you may need to use an external web portal or use signtool.

4.  On the **Create UEFI** page, browse to find the CAB file that you want to submit, and then click **Submit**.

**Important**  
EFI ByteCode (EBC) files must be compiled using the /ALIGN:32 flag for processing to succeed.

Submission packages should be a CAB library that contains no folders and only the **\*.efi** files to be signed.

 

When the dashboard completes processing your submission, it sends a results email to the work email address on file.

## To manage your firmware


1.  Sign in to the dashboard with your Microsoft account, and then click **Hardware certification**.

2.  On the **Hardware certification** page, in the **Manage submissions** tile, click **Manage submissions**.

3.  On the **Manage submissions** page, select **UEFI** from the **Submission type** list.

4.  Select the submission that you want to manage.

5.  On the **Details** view, you can see the status of your submission, and, if it's complete, download the signed binaries.

## Related topics


[Microsoft UEFI CA Signing Policy Updates](http://blogs.msdn.com/b/windows_hardware_certification/archive/2013/12/03/microsoft-uefi-ca-signing-policy-updates.aspx)

[Pre-Submission Testing for UEFI Submissions](http://blogs.msdn.com/b/windows_hardware_certification/archive/2013/12/03/pre-submission-testing-for-uefi-submissions.aspx)

 

 






