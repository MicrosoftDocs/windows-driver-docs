---
title: LSA plug-in signing
description: LSA plug-in signing
ms.assetid: 7f0bc573-2616-499e-9a77-3e4f1d0ccbf3
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# LSA plugin signing


Local Security Authority (LSA) file signing is a hardware dashboard service that lets you to digitally sign LSA plugins, enabling them to be installed on Windows devices. For more information about LSA protection, see [Configuring additional LSA protection(https://docs.microsoft.com/windows-server/security/credentials-protection-and-management/configuring-additional-lsa-protection).


> [!IMPORTANT]
> Please note the following:
> * LSA submissions require an extended validation (EV) code signing certificate. For more information about code signing certificates, see [Get a code signing certificate](get-a-code-signing-certificate.md).
> * All LSA submissions must be in a single, signed CAB file, and contain all the LSA plug-in files required for signing. 
>   * This file should contain no folders and only the binaries to be signed. 
> * The CAB file signature must match the EV code signing certificate for your organization. 


## Submit an LSA plugin

1.  Sign in to the hardware dashboard with your Microsoft account, and then click **File signing services**.

2.  Click **Submit new LSA**.
    > [!NOTE]  
    > You may be prompted to sign a legal agreement before creating a new LSA submission. Review and complete the agreement to continue. Every organization only needs to sign the agreement once. 
  
3.  On the **New LSA submission** page, upload the CAB file you want to submit, and click **Submit**.

4.  Once your submission has been processed, you’ll receive an email with the results.



 

### <span id="Manage_LSA_submissions"></span><span id="manage_lsa_submissions"></span><span id="MANAGE_LSA_SUBMISSIONS"></span>Manage LSA submissions

1.  Sign in to Hardware Dev Center dashboard with your Microsoft account, and then click **Manage submissions** in the **Hardware certification** tile.

2.  On the **Manage submissions** page, select **LSA** from the **Submission type** list, and then click **Apply**.

3.  Click the submission **ID** that you want to manage.

4.  On the submission details page, you can see the status of your submission, and, if it's complete, click the **Download** link to download the signed binaries.