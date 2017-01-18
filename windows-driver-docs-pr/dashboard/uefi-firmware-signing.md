---
title: UEFI Firmware Signing
description: UEFI Firmware Signing
MS-HAID:
- 'p\_dashboard.uefi\_firmware\_signing'
- 'hw\_dashboard.uefi\_firmware\_signing'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: a39f65c3-9b0b-43ca-9831-ec420fb4cdca
---

# UEFI Firmware Signing


UEFI signing is a service provided by the Dashboard that lets you to sign UEFI firmware binaries targeted to x86 or x64 computers, so they can be installed on Windows PCs.

## <span id="To_submit_your_firmware"></span><span id="to_submit_your_firmware"></span><span id="TO_SUBMIT_YOUR_FIRMWARE"></span>To submit your firmware


1.  Sign in to the dashboard with your Microsoft account, and then click **Hardware certification**.

2.  On the **Hardware certification** page, in the **Create submissions** tile, click **Create UEFI submission**.

    **Note**  
    Before proceeding, you may be prompted to sign a legal agreement. To continue, review the document, add your signature, add the date, and then click **Submit**. Each organization only needs to sign this agreement once.

     

3.  All UEFI submissions must be in a single, signed CAB file and contain all the UEFI files for signing. The CAB file signature must match the Authenticode certificate on file for your company with dashboard. Depending on your certificate provider, you may need to use an external web portal or use signtool.

4.  On the **Create UEFI** page, browse to find the CAB file that you want to submit, and then click **Submit**.

**Important**  
EFI ByteCode (EBC) files must be compiled using the /ALIGN:32 flag for processing to succeed.

Submission packages should be a CAB library that contains no folders and only the **\*.efi** files to be signed.

 

When the dashboard completes processing your submission, it sends a results email to the work email address on file.

## <span id="To_manage_your_firmware"></span><span id="to_manage_your_firmware"></span><span id="TO_MANAGE_YOUR_FIRMWARE"></span>To manage your firmware


1.  Sign in to the dashboard with your Microsoft account, and then click **Hardware certification**.

2.  On the **Hardware certification** page, in the **Manage submissions** tile, click **Manage submissions**.

3.  On the **Manage submissions** page, select **UEFI** from the **Submission type** list.

4.  Select the submission that you want to manage.

5.  On the **Details** view, you can see the status of your submission, and, if it's complete, download the signed binaries.

## <span id="related_topics"></span>Related topics


[Microsoft UEFI CA Signing Policy Updates:](http://blogs.msdn.com/b/windows_hardware_certification/archive/2013/12/03/microsoft-uefi-ca-signing-policy-updates.aspx)

[Pre-Submission Testing for UEFI Submissions](http://blogs.msdn.com/b/windows_hardware_certification/archive/2013/12/03/pre-submission-testing-for-uefi-submissions.aspx)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhw_dashboard\hw_dashboard%5D:%20UEFI%20Firmware%20Signing%20%20RELEASE:%20%281/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





