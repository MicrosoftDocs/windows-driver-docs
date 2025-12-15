---
title: Create a New Hardware Submission
description: Create a new hardware submission on the Partner Center hardware dashboard for your Windows tested drivers to obtain certification.
ms.date: 10/16/2025
ms.topic: how-to
---

# Create a new hardware submission

With the Partner Center hardware dashboard, you can submit your Windows tested drivers for certification. This article describes how to create a new hardware submission in the Partner Center hardware dashboard.

All hardware submissions to the dashboard are processed within five business days, depending on whether the submission requires manual review. Manual review might be required if your submission's tests fail, if a valid filter isn't applied, or due to an internal business policy.

> [!NOTE]
> In order to make Windows 10 more secure without affecting performance, all binaries are now receiving embedded signatures. This technique applies to all submissions for certification, not only Windows 10 submissions.

## Prerequisites

- Make sure your [dashboard account](https://partner.microsoft.com/dashboard) is registered for the Windows Hardware Developer Program. For information on how to register, see [Register for the Windows Hardware Developer Program](hardware-program-register.md).

- Use the following table to determine which signed file you need to create for your submission:

   | Operating system | Required signed file type | Guidance |
   |------------------|---------------------------|----------|
   | Windows 11 and Windows 10 </br>Windows Server 2016 and later | Windows Hardware Lab Kit (WHLK) file, *.hlk* | [Find and download the correct version of the Hardware Lab Kit (HLK)](/windows-hardware/test/hlk/) based on the compatible system. You can then [merge all HLK package test results](/windows-hardware/test/hlk/user/merge-packages) into a single dashboard submission.</br></br>**Note:** The Windows 10 version 22H2 release follows the same guidelines as Windows 10, version 2004. For more information, see [Windows Hardware Compatibility Program (WHCP) guidance for Windows 10, version 22H2](https://techcommunity.microsoft.com/blog/windowshardwarecertification/whcp-guidance-for-windows-10-version-22h2/3586362). |
   | Windows 8/8.1 and earlier | Windows Hardware Certification Kit (HCK) file, *.hckx* | To learn how to create and digitally sign an *.hckx* file, see the [Windows HCK Getting Started Guide](/previous-versions/windows/hardware/hck/jj123537(v=vs.85)) |
   | Windows Server 2008 and earlier  | Windows Logo Kit (WLK) hardware submission package file, *.cab* | To learn how to create a WLK submission package, see [Create a new WLK hardware submission](hardware-submission-wlk.md). |

## Submit your new hardware

To submit your new hardware, follow these steps:

1. Go to the [Partner Center hardware dashboard](https://partner.microsoft.com/dashboard/home) and sign in with your credentials.

1. Select **Submit new hardware**:

   :::image type="content" source="./images/hardware-submission-create/hardware-list.png" alt-text="Screenshot of the list of hardware submisssions.":::

1. In the **Packages and signing properties** section, enter a product name for your driver submission. This name can be used to search for and organize your driver submissions.

   > [!NOTE]
   > The name is visible when you share your driver with another company.

1. Either drag or browse to the **.hlkx/.hckx** file that you want to submit. If you're submitting WLK hardware, you must submit a *.cab* file. To learn how to create a WLK *.cab* file submission, see [fwhqlCreate a WLK hardware submission package](hardware-submission-wlk.md).

   :::image type="content" source="./images/hardware-submission-create/hardware-submit.png" alt-text="Screenshot that shows the new hardware submission form.":::

1. If you want to test a driver before release, select **Perform test-signing**. Test-signed drivers are similar to drivers signed for public release, but don't require HLK testing. They're also not distributed through Windows Update, but can be downloaded from the hardware submission site. They can be installed on test machines only. For more information about test-signing driver packages, see [Windows Hardware Quality Labs (WHQL) test signature program](../install/whql-test-signature-program.md) and [How to test-sign a driver package](../install/how-to-test-sign-a-driver-package.md).

1. Complete any other any questionnaires that are presented. The portal presents questionnaires required for the product type being submitted for Windows Server certification.

1. Under **Request Signatures**, select which operating system signatures (including allowable downlevel operating systems) to include with your driver. Available certifications vary depending on your driver submission package, so there might not be any certifications listed.

   > [!NOTE]
   > If you're signing a driver package for a single architecture, include logs for the intended architecture only. For example, to sign for x64 only, submit only the x64 logs.

   :::image type="content" source="./images/hardware-submission-create/hardware-signatures.png" alt-text="Screenshot that shows possible signatures for a driver submission, and the finalize button.":::

1. In the **Certification** section, complete the following information:

   | Field | Description |
   |-------|-------------|
   | **Device type** | Specify your device component type: </br>- **An internal component**: Your device is part of a system and connects inside the PC. </br>- **An external component**: Your device is an external device (peripheral) that connects to a PC. </br>- **Both**: Your device can connect internally (inside a PC) and externally (peripheral). |
   | **Device metadata category** | Select an icon for your device from the list of default icons based on your device category. This selection determines which icon appears in Devices and Printers. If you don't want your device to appear, select **Internal device**.</br></br> For information about delivering a rich experience with Windows Device Stage, see [Create a Device Metadata Experience](create-a-device-metadata-experience.md). |
   | **Device metadata model ID** | These GUIDs are used to validate your Device Metadata submissions to the legacy Sysdev dashboard. If you provide GUID values, they must match the model IDs in your device metadata package. |
   | **Announcement date** | Enter the date when you want your product included on the Windows Server Catalog, the Windows Certified Product List, and the Universal Driver List. |
   | **Marketing names** | Enter one or more marketing names for your submission. Marketing names allow you to provide aliases for your product. You can provide as many names as you want.|

   :::image type="content" source="images/hardware-submission-create/hardware-certification.png" alt-text="Screenshot that shows the certification section.":::

   > [!IMPORTANT]
   > Check the announcement date. After the announcement date passes, you can't add a new name.

1. Select **Submit** at the bottom of the page.

1. Configure publication of your driver to Windows Update in the **Distribution** section. For information about how to use the **Distribution** section, see [Manage driver distribution with shipping labels](manage-driver-distribution-by-submission.md).

1. Monitor the progress of your submission with the progress tracker at the top of the page. After all steps show the green check icon, the submission is complete. Your organization receives a notification in the dashboard header.

   :::image type="content" source="images/hardware-submission-create/hardware-progress-tracker.png" alt-text="Screenshot that shows the progress tracker.":::

1. Review the results. If your submission fails, make any necessary changes and resubmit.

## Troubleshoot submission errors

The following sections provide troubleshooting suggestions to address issues with your submission.

### Error: File missing

If a file is missing, you receive one of the following errors:

> _There are files at the root of the cabinet._

> _No .inf files found in driver directory/directories: XYZ._

The failure cause is an incorrect *.cab* file structure. The *.cab* structure was created with driver files in the root folder of the *.cab* file instead of locating the files in a subfolder. For instructions on how to create a proper *.cab* file for your driver signing submissions, see [Attestation sign Windows 10 (and later) drivers](code-signing-attestation.md).

### Error: Zip64

If a Zip error occurs, you receive the error:

> _File is using Zip64(4gb+file Size)_

This error occurs when the uploaded archive's file type is *.zip64* instead of *.zip*. The most common cause is large file size.

To fix the error, repackage the submission by following these steps:

1. Rename the existing *.hckx* (or *.hlkx*) archive file to *.zip*.
1. Extract the archive file contents to a folder, and then open the folder.
1. Select all items in the folder, then right-click and select **Send to Compressed zip folder**.
1. Rename the new archive *.zip* file to *.hckx* (or *.hlkx*).
1. Upload the new archive *.hckx* (or *.hlkx*) file.

### Error: Package fails to open

If the DUA package fails to open, you receive the following error:

> _Failed to open package: Not compatible with a version (3.2.0.0) with this instance package manager_

To resolve the issue, [install standalone HLK Studio](/windows-hardware/test/hlk/user/install-standalone-hlk-studio), open the downloaded DUA shell package, and create a DUA submission.

### Other issues

For other issues, see [Support for Partner Center dashboard](technical-support.md).

## Related articles

- [View your hardware submissions](hardware-submissions-view.md)
- [Update a hardware submission](hardware-submission-update.md)
- [Validate the Microsoft signature for a hardware submission](code-signing-validate.md)
- [Get started with Windows HLK](/windows-hardware/test/hlk/getstarted/windows-hlk-getting-started)
- [Distribute your driver with Driver flighting](driver-flighting.md)
