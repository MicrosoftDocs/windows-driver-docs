---
title: Create a new hardware submission
description: Create a new hardware submission
ms.date: 04/20/2017
ms.topic: article
ms.localizationpriority: medium
---

# Create a new hardware submission

To prepare your hardware for the Windows Hardware Compatibility Program for Windows 10 (or the separate certification program for previous operating systems), you must create and submit an **.hlkx** file (for Windows 10) or **.hckx** file (for previous operating systems). This file is created using the Windows HLK Studio (or Windows HCK Studio, for previous operating systems) and contains all of the test results, drivers, and symbols for your product. Submitting this file allows the dashboard to review your test results, evaluate any drivers tested, and return Microsoft digitally signed catalog files.

## To create a submission file

For information about creating and digitally signing an **.hlkx** file, see the [Windows HLK Getting Started Guide](/windows-hardware/test/hlk/getstarted/windows-hlk-getting-started).

For information about creating and digitally signing an **.hckx** file, see the [Windows HCK Getting Started Guide](/previous-versions/windows/hardware/hck/jj123537(v=vs.85)).

## To submit a file

1. Sign in to the Partner Center, and then select **Submit new hardware**. This loads the submission creation wizard.

2. In the **Packages and signing properties** section, choose a name for your driver submission. This name can be used to search for and organize your driver submissions. Note: If you share your driver with another company, they will see this name.

3. Either drag and drop, or browse to the **.hlkx/.hckx** file that you want to submit. The file will begin to upload.
   ![screenshot that shows the driver name field.](images/drivers-name.png)

4. It is at this point that the submission portal determines what Product Type is being submitted. Then, at the Submission page, the portal presents any questionnaire that may be required for a product being submitted for Windows Server certification. For all products submitted for Windows Server certification or signing where the submission portal presents a questionnaire, you must complete the questionnaire. The submission will not complete unless the questionaire is completed.

5. If you wish to test a driver prior to release, you can select the checkbox labled "Perform test-signing for Win10 and above" OR "Perform test-signing for OS below Win10 (legacy)". Test-signed drivers are similar to drivers signed for public release, but do not require HLK testing. They are also not distributed through Windows Update, but can be downloaded from the hardware submission site. They can be installed on test machines only. For more information about test-signing driver packages, see [WHQL Test Signature Program](../install/whql-test-signature-program.md) and [How to test-sign a driver package](../install/how-to-test-sign-a-driver-package.md).

7. Select Request Signatures as applicable. This option allows you to specify which operating system signatures (including allowable downlevel operating systems) should be included with your driver. Available certifications vary depending on your driver submission package, so there may not be any certifications listed. **Note** If you are signing a driver package for a single architecture, only include logs for the intended architecture. For example, to sign for x64 only, submit only the x64 logs.

   ![screenshot that shows possible certifications for a driver submission, and the finalize button.](images/additionalcertifications.png)

8. In the **Certification** section, complete the following information:

   <table>
   <colgroup>
   <col width="50%" />
   <col width="50%" />
   </colgroup>
   <thead>
   <tr class="header">
   <th>Field</th>
   <th>Description</th>
   </tr>
   </thead>
   <tbody>
   <tr class="even">
   <td><p>Device type</p></td>
   <td><p>Indicate if your device is:</p>
   <ul>
   <li><p>An internal component, if your device is part of a system and connects inside the PC.</p></li>
   <li><p>An external component, if your device is an external device (peripheral) that connects to a PC.</p></li>
   <li><p>Both, if your device can be connected internally (inside a PC) and externally (peripheral).</p></li>
   </ul></td>
   </tr>
   <tr class="odd">
   <td><p>Device metadata category</p></td>
   <td><p>Select an icon for your device from a list of default icons based on your device category. This determines which icon appears in Devices and Printers. If your device should not appear, select "Internal device".</p>
   <p>For information about delivering a rich experience with Windows Device Stage, see <a href="/windows-hardware/drivers/dashboard/" data-raw-source="[Device Metadata](./index.yml)">Device Metadata</a>.</p></td>
   </tr>
   <tr class="even">
   <td><p>Device metadata model ID</p></td>
   <td><p>These GUIDs are used to validate your Device Metadata submissions to the legacy Sysdev dashboard. If provided, they must match the model IDs in your device metadata package.</p></td>
   </tr>
   <tr class="odd">
   <td><p>Announcement date</p></td>
   <td><p>Enter the date when you want your product included on the Windows Server Catalog, the Windows Certified Product List, and the Universal Driver List.</p></td>
   </tr>
   <tr class="even">
   <td><p>Marketing names</p></td>
   <td><p>Enter the marketing name(s) for your submission. Marketing names allow you to provide aliases for your product. You can provide as many names as you want.</p></td>
   </tr>
   </tbody>
   </table>

   ![screenshot that shows the certification section.](images/drivers-certification.png)

9. Select **Submit**.

10. The **Distribution** section is used to publish your driver to Windows Update. For information about how to use the **Distribution** section, see [Manage driver distribution with shipping labels](manage-driver-distribution-by-submission.md).

11. You can monitor the progress of your submission with the progress tracker at the top of the page. Once all steps show a green check, the submission is complete and your organization will receive a notification in the dashboard header.

    ![screenshot that shows the progress tracker.](images/drivers-allgreen-new.png)

12. Review the results. If your submission failed, make any necessary changes and resubmit.

## Related topics

* [Managing hardware submissions in the Partner Center](manage-your-hardware-submissions.md)
* [Get drivers signed by Microsoft for multiple Windows versions](get-drivers-signed-by-microsoft-for-multiple-windows-versions.md)
* [Driver flighting](driver-flighting.md)
