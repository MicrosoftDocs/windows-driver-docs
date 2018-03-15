---
title: LSA plug-in signing
description: LSA plug-in signing
ms.assetid: 7f0bc573-2616-499e-9a77-3e4f1d0ccbf3
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# LSA plug-in signing


LSA file signing is a service provided by Windows Dev Center hardware dashboard. This service allows you to digitally sign LSA plug-ins so that they can be installed on Windows computers.

LSA submissions require an extended validation (EV) code signing certificate. For more information about code signing certificates, see [Get a code signing certificate](https://msdn.microsoft.com/library/windows/hardware/hh801887.aspx).

## <span id="Submit_an_LSA_plug_in"></span><span id="submit_an_lsa_plug_in"></span><span id="SUBMIT_AN_LSA_PLUG_IN"></span>Submit an LSA plug in


1.  Sign in to the Hardware Dev Center dashboard with your Microsoft account, and then click **File signing services**.

2.  On the **File signing services** page, in the **Create submissions** tile, click **Create LSA submission**.

    **Note**  
    Before proceeding, you may be prompted to sign a legal agreement. To continue, review the document, add your signature, add the date, and then click **Submit**. Each organization only needs to sign this agreement once.

     

3.  On the **Create LSA submission** page, browse to the CAB file that you want to submit, click **Upload**, and then click **Submit**.

4.  When the Hardware Dev Center dashboard completes processing your submission, you’ll receive an email with the results.

**Important**  
-   All LSA submissions must be in a single, signed CAB file and contain all the LSA plug-in files for signing.

-   The CAB file signature must match the EV code signing certificate on file for your company with Hardware Dev Center dashboard. For more information about code signing certificates, see [Get a code signing certificate](https://msdn.microsoft.com/library/windows/hardware/hh801887.aspx).

-   Submission packages should be a CAB library that contains no folders and only the binary files to be signed.

 

### <span id="Manage_LSA_submissions"></span><span id="manage_lsa_submissions"></span><span id="MANAGE_LSA_SUBMISSIONS"></span>Manage LSA submissions

1.  Sign in to Hardware Dev Center dashboard with your Microsoft account, and then click **Manage submissions** in the **Hardware certification** tile.

2.  On the **Manage submissions** page, select **LSA** from the **Submission type** list, and then click **Apply**.

3.  Click the submission **ID** that you want to manage.

4.  On the submission details page, you can see the status of your submission, and, if it's complete, click the **Download** link to download the signed binaries.

## <span id="related_topics"></span>Related topics


[Get a code signing certificate](https://msdn.microsoft.com/library/windows/hardware/hh801887.aspx)

[Update a code signing certificate](https://msdn.microsoft.com/library/windows/hardware/br230783.aspx)

[Establish a new company](https://msdn.microsoft.com/library/windows/hardware/br230795.aspx)

 

 






