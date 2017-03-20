---
title: LSA plug-in signing
description: LSA plug-in signing
MS-HAID:
- 'p\_dashboard.lsa\_plug\_in\_signing'
- 'hw\_dashboard.lsa\_plug\_in\_signing'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 7f0bc573-2616-499e-9a77-3e4f1d0ccbf3
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhw_dashboard\hw_dashboard%5D:%20LSA%20plug-in%20signing%20%20RELEASE:%20%281/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





