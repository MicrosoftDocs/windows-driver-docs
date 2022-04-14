---
title: Create a new hardware submission
description: Create a new hardware submission
ms.date: 03/25/2022
ms.topic: article
---

# Create a new hardware submission

To prepare your hardware for the Windows Hardware Compatibility Program for Windows 10 (or the separate certification program for previous operating systems), you must create and submit an **.hlkx** file (for Windows 10) or **.hckx** file (for previous operating systems). This file is created using the Windows HLK Studio (or Windows HCK Studio, for previous operating systems) and contains all of the test results, drivers, and symbols for your product. Submitting this file allows the dashboard to review your test results, evaluate any drivers tested, and return Microsoft digitally signed catalog files.

## Prerequisites

* Make sure your dashboard account is registered for the Windows Hardware Developer Program. For information on how to register, see [How to register for the Windows Hardware Developer Program](register-for-the-hardware-program.md).

* For drivers compatible with Windows 10 and above, you'll need to have a **.hlkx** file that's been digitally signed. For information about creating and digitally signing an  **.hlkx** file, see the [Windows HLK Getting Started Guide](/windows-hardware/test/hlk/getstarted/windows-hlk-getting-started).

* For drivers compatible with Windows 8/8.1 and older operating systems, you'll need to have an **.hckx** file that's been digitally signed. For information about creating and digitally signing an  **.hckx** file, see the [Windows HCK Getting Started Guide](/previous-versions/windows/hardware/hck/jj123537(v=vs.85)).

## Create a hardware submission

1. Go to [Partner Center](https://partner.microsoft.com/dashboard) and sign in using your credentials.

1. Select **Submit new hardware**.

    :::image type="content" source="./images/create-a-new-hardware-submission/hardware-list.png" alt-text="Screenshot of the the list of submitted hardware list.":::

1. In the **Packages and signing properties** section, choose a product name for your driver submission. This name can be used to search for and organize your driver submissions.

>[!NOTE]
>If you share your driver with another company, they will see this name.

1. Either drag and drop, or browse to the **.hlkx/.hckx** file that you want to submit. The file will begin to upload.

   :::image type="content" source="./images/create-a-new-hardware-submission/hardware-submit.png" alt-text="Screenshot that shows the new hardware submission form.":::

1. Complete any questionnaires that are presented.  The portal presents any questionnaire that's required for the product type being submitted for Windows Server certification. The submission won't complete until you complete the questionnaire.

1. If you wish to test a driver prior to release, you can select the checkbox labled "Perform test-signing for Win10 and above" OR "Perform test-signing for OS below Win10 (legacy)". Test-signed drivers are similar to drivers signed for public release, but do not require HLK testing. They are also not distributed through Windows Update, but can be downloaded from the hardware submission site. They can be installed on test machines only. For more information about test-signing driver packages, see [WHQL Test Signature Program](../install/whql-test-signature-program.md) and [How to test-sign a driver package](../install/how-to-test-sign-a-driver-package.md).

1. Select Request Signatures as applicable. This option allows you to specify which operating system signatures (including allowable downlevel operating systems) should be included with your driver. Available certifications vary depending on your driver submission package, so there may not be any certifications listed. **Note** If you are signing a driver package for a single architecture, only include logs for the intended architecture. For example, to sign for x64 only, submit only the x64 logs.

   :::image type="content" source="images/additionalcertifications.png" alt-text="Screenshot that shows possible certifications for a driver submission, and the finalize button.":::

1. In the **Certification** section, complete the following information:

   | Field | Description |
   |--|--|
   | Device type | Indicate if your device is:</br></br>**An internal component**, if your device is part of a system and connects inside the PC.</br></br>**An external component**, if your device is an external device (peripheral) that connects to a PC.</br></br>**Both**, if your device can be connected internally (inside a PC) and externally (peripheral). |
   | Device metadata category | Select an icon for your device from a list of default icons based on your device category. This determines which icon appears in Devices and Printers. If your device should not appear, select "Internal device".</br></br>For information about delivering a rich experience with Windows Device Stage, see [Create a Device Metadata Experience](create-a-device-metadata-experience.md). |
   | Device metadata model ID | These GUIDs are used to validate your Device Metadata submissions to the legacy Sysdev dashboard. If provided, they must match the model IDs in your device metadata package. |
   | Announcement date | Enter the date when you want your product included on the Windows Server Catalog, the Windows Certified Product List, and the Universal Driver List. |
   | Marketing names | Enter the marketing name(s) for your submission. Marketing names allow you to provide aliases for your product. You can provide as many names as you want.|

   :::image type="content" source="images/drivers-certification.png" alt-text="Screenshot that shows the certification section.":::

1. Select **Submit**.

1. The **Distribution** section is used to publish your driver to Windows Update. For information about how to use the **Distribution** section, see [Manage driver distribution with shipping labels](manage-driver-distribution-by-submission.md).

1. You can monitor the progress of your submission with the progress tracker at the top of the page. Once all steps show a green check, the submission is complete and your organization will receive a notification in the dashboard header.

   :::image type="content" source="images/drivers-allgreen-new.png" alt-text="Screenshot that shows the progress tracker.":::

1. Review the results. If your submission failed, make any necessary changes and resubmit.

## Related topics

- [Managing hardware submissions in the Partner Center](manage-your-hardware-submissions.md)
- [Get drivers signed by Microsoft for multiple Windows versions](get-drivers-signed-by-microsoft-for-multiple-windows-versions.md)
- [Driver flighting](driver-flighting.md)
