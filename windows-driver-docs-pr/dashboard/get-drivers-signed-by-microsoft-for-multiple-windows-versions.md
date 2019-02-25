---
title: Get drivers signed by Microsoft for multiple Windows versions
description: How to get a driver signed by Microsoft for multiple versions of Windows
ms.assetid: 519384F5-986C-4109-8C91-4352DEFF46F9
ms.topic: article
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Get drivers signed by Microsoft for multiple Windows versions


## <span id="How_to_submit_to_the_dashboard"></span><span id="how_to_submit_to_the_dashboard"></span><span id="HOW_TO_SUBMIT_TO_THE_DASHBOARD"></span>How to submit to the dashboard


This topic explains how to make a submission to the dashboard, such as a driver, and have it apply to multiple versions of Windows. This topic also covers how to retrieve the submission after Microsoft signs it, and how to validate the Microsoft signature.

There are two ways to make a dashboard submission apply to Windows 10 and earlier versions of Windows:

1.  Use the Hardware Lab Kit (HLK) to test your submission against Windows 10 and use the Hardware Certification Kit (HCK) to test against earlier versions of Windows. Then create a dashboard submission that includes all the [merged HLK/HCK test results](https://msdn.microsoft.com/library/windows/hardware/dn939938.aspx). During the submission process, you can opt-in to get a free signature for Windows Vista and Windows XP, as shown later in this topic. To opt-in for Windows Server 2008, provide a submission ID from a [Windows Logo Kit (WLK)](https://www.microsoft.com/download/details.aspx?id=39359) submission. This is the only way to make a submission apply to all Windows versions.
2.  As an alternative to HLK and HCK testing, you can [cross-sign](https://msdn.microsoft.com/library/windows/hardware/dn170454.aspx) your driver yourself and submit it to the dashboard for [attestation signing](attestation-signing-a-kernel-driver-for-public-release.md) so that it also works on Windows 10. This is more complicated, but still a valid option. But it’s important to note that a submission signed this way will not work on Windows Server 2016. For more information about how to attestation sign a driver, see [Attestation signing a kernel driver for public release](attestation-signing-a-kernel-driver-for-public-release.md).
    **Important**  You must still use [Hardware Dev Center (Sysdev)](dashboard-services.md) to attestation sign a driver until driver signing is available through the new Windows Hardware Dev Center dashboard.

     

This topic will provide some background info about the dashboard for context, then walk through the process for using the HLK/HCK.

In the dashboard, there are two options related to signing submissions – either way, you can get a Microsoft-signed driver. The Hardware compatibility option means you’ve gone the extra distance and met [Windows Hardware Compatibility Program](https://msdn.microsoft.com/library/windows/hardware/dn922588.aspx) requirements. This gives you reputation with Microsoft SmartScreen, visibility on the Certified Products List, and other business benefits.

For background, there are two code signing operations to consider:

-   One is a code signing operation that identifies an organization to the dashboard. This is a signature on the package you plan to submit, and it’s a requirement that the dashboard imposes on partners so that the dashboard to prevent malicious people outside your organization from making submissions using your credentials – which could harm your reputation!
-   The other is where Microsoft actually signs the individual files within your submission, such as your driver.

You must have an EV certificate bound to your company to access submission features in the dashboard.

To confirm the certificate that is used to identify your organization within [Hardware Dev Center (Sysdev)](dashboard-services.md), you need to be logged in as an Administrator for your organization’s account. Then select **Administration** &gt; **Upload a new digital certificate**.

To confirm the certificate that is used to identify your organization within the new Windows Hardware Dev Center dashboard, see [Update a code signing certificate](https://msdn.microsoft.com/library/windows/hardware/mt786467).

After you sign in to the dashboard and you are ready to sign your submission, you can use either a standard code signing cert or an EV code signing cert. This is true for all operating system versions, not just Windows 10.

This is a [recent change in policy](http://blogs.msdn.com/b/windows_hardware_certification/archive/2015/10/20/update-on-sysdev-ev-certificate-requirement.aspx). If you have an EV cert bound to the account for your organization, you’re good to go – that is, you can continue to use a standard SHA-2 certificate when you submit your package.

## <span id="How_to_submit_HLK_test_results"></span><span id="how_to_submit_hlk_test_results"></span><span id="HOW_TO_SUBMIT_HLK_TEST_RESULTS"></span>How to submit HLK test results


Here's how to submit HLK test results to the dashboard. There are separate tabs where you can see what tests were run and the test results. For dashboard purposes, the most interesting part of an HLK project is the **Package** tab:

![hlk package](images/hlkpackage.png)

Click the file path for the project to open it. In this case, the submission is one driver.

![driver](images/capture.png)

Let’s say you want to create a submission package from scratch. In the HLK, click **Add Driver Folder**.

![add driver folder](images/adddriverfolder.png)

Now is you first chance to make declarations about the OS versions that are supported for your submission. In this case, the submission has been tested for Windows 10 x64 and earlier versions of Windows.

![os qualifications](images/osqualifications.png)

You also need to make declarations for locales. For example, depending on the design and architecture of your driver, you may choose to display different strings in different locales. In that case, you might actually have different compiled binaries for different locales. So for one device, you might have a hundred different drivers; one for each locale.

![locales](images/locales.png)

To add symbols, right-click the driver folder.

![add symbols](images/addsymbols.png)

Click **Add Supplemental Folder** to submit other files that are important to the submission but are not actually part of the submission itself. You can add any content you want to the package. This is a way for you to get other items to the Dashboard that are important for the submission, such as a readme file for a driver submission.

![add supplemental folder](images/addsupplementalfolder.png)

When you are ready, click **Create Package**.

![create package](images/createpackage.png)

The next step is to specify a certificate that you will you use to sign the package – this is the first of the two code signing operations that were covered at the start of this topic. You can click **Use a certificate file** to specify a certificate that is stored on something like a USB drive, or click **Use the certificate store** to specify a certificate that has been imported into the certificate store of the local computer.

![use the certificate store](images/usecertstore.png)

After you click **OK**, you name the package and it gets created and signed (assuming you have a certificate installed on the computer you are using for the submission), and you’ll get back a friendly success message.

And the package has a green check under **Signability**:

![signability](images/signability.png)

The next steps occur in the Windows Hardware Dev Center dashboard. Sign in and follow the instructions in [Create a new hardware submission](create-a-new-hardware-submission.md) to upload your HLK package.

## <span id="How_to_retrieve_a__submission_after_Microsoft_signs_it"></span><span id="how_to_retrieve_a__submission_after_microsoft_signs_it"></span><span id="HOW_TO_RETRIEVE_A__SUBMISSION_AFTER_MICROSOFT_SIGNS_IT"></span>How to retrieve a submission after Microsoft signs it


For an HLK or HCK submission that you submitted to the Windows Hardware Dev Center dashboard:

-   [Find the hardware submission](manage-your-hardware-submissions.md) that contains the drivers that you want to download signed files for. Select the ID to open the driver details. On that page, expand the package tab for the package containing the driver you want to download and click “Download signed files”.

For a WLK submission, system submission, or attestation signed driver that you submitted to Hardware Dev Center (Sysdev):

-   Select **Hardware Compatibility** &gt; **Manage submissions** &gt; and on the **Summary and Tasks** tab, if the status is **Approved**, the submission is ready to be retrieved. Under **Download** in the lower right corner of the screen, click **Signed driver package**. Microsoft will stream an in-memory zip file that includes the signed submission.

Inside the submission folder will be the package files. These files are signed by Microsoft. The partner does not have to sign the returned payload. Microsoft always returns a .cat file with an approved submission. If a partner includes its own .cat file. Microsoft discards it and returns its own signed .cat file.

In the past, Microsoft only signed the .cat file. Starting with Windows 10, Microsoft now signs all of the portable executables in the returned payload. For example, the .dll file is also signed by Microsoft:

![files signed by microsoft](images/filessignedbymicrosoft.png)

## <span id="How_to_validate_the_Microsoft_signature"></span><span id="how_to_validate_the_microsoft_signature"></span><span id="HOW_TO_VALIDATE_THE_MICROSOFT_SIGNATURE"></span>How to validate the Microsoft signature


There are a couple cases where you may want to validate the Microsoft signature for a submission.

1.  You aren’t sure if a driver has been signed by Microsoft or not, and you want to check.
2.  You have two drivers, and you need to determine which one was signed by attestation and which one was signed after submission of HLK/HCK results to the dashboard.

You can validate the Microsoft signature by checking the Enhanced Key Usages (EKUs) of the certificate that Microsoft signs the submission with. To check the EKU, right-click the .cat file and click **Properties**. Click the **Digital Signatures** tab, click the name of the certificate, and then click **Details**.

![eku details](images/ekudetails.png)

On the certificate **Details** tab, click **Enhanced Key Usage**. There you will see the EKUs and corresponding OID values for the certificate. In this case, the **Windows Hardware Driver Verification OID** ends with a 5, which means the driver has not been signed by attestation:

![certified](images/certified.png)

If the driver had been signed by attestation, then the OID would end with a 1:

![attestation signed](images/attested.png)

## Related topics

- [Create a new hardware submission](create-a-new-hardware-submission.md)

- [Managing hardware submissions in the Windows Hardware Dev Center dashboard](manage-your-hardware-submissions.md)

- [Driver flighting](driver-flighting.md)

 

