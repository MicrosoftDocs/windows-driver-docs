---
title: Create a new hardware submission
description: Create a new hardware submission
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 3F433F0A-422C-46E5-B59E-8DB4AC537F01
---

# Create a new hardware submission


To prepare your hardware for the Windows Hardware Compatibility Program for Windows 10 (or the separate certification program for previous operating systems), you must create and submit an **.hlkx** file (for Windows 10) or **.hckx** file (for previous operating systems). This file is created using the Windows HLK Studio (or Windows HCK Studio, for previous operating systems) and contains all of the test results, drivers, and symbols for your product. Submitting this file allows the dashboard to review your test results, evaluate any drivers tested, and return Microsoft digitally signed catalog files.

## <span id="To_create_a_submission_file"></span><span id="to_create_a_submission_file"></span><span id="TO_CREATE_A_SUBMISSION_FILE"></span>To create a submission file


For information about creating and digitally signing an **.hlkx** file, see the [Windows HLK Getting Started Guide](https://msdn.microsoft.com/library/windows/hardware/dn915002.aspx).

For information about creating and digitally signing an **.hckx** file, see the [Windows HCK Getting Started Guide](http://go.microsoft.com/fwlink/p/?LinkId=248436).

## <span id="To_submit_a_file"></span><span id="to_submit_a_file"></span><span id="TO_SUBMIT_A_FILE"></span>To submit a file


1.  Sign in to the Windows Hardware Dev Center dashboard, and then select **Create new driver**. This loads the submission creation wizard.

2.  In the **Packages and signing properties** section, choose a name for your driver submission. This name can be used to search for and organize your driver submissions. Note: If you share your driver with another company, they will see this name.

3.  Either drag and drop, or browse to the **.hlkx/.hckx** file that you want to submit. The file will begin to upload.

4.  Select the "This is a beta driver" checkbox if applicable. This option states that your driver should be signed for pre-production and will not be broadly released.

    ![screenshot that shows the driver name field](images/drivers-name.png)

5.  Select any applicable additional certifications if available. This option allows you to specify which down-level operating system signatures should be included with your driver. Available certifications vary depending on your driver submission package, so there may not be any certifications listed.

6.  Select **Finalize**. You will not be able to select the **Finalize** button until your file upload is complete. Note: Your signature properties and name cannot be changed after you click **Finalize**.

    ![screenshot that shows possible certifications for a driver submission, and the finalize button](images/additionalcertifications.png)

7.  In the **Certification** section, complete the following information:

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
    <tr class="odd">
    <td><p>Is your driver Universal?</p></td>
    <td><p>Indicate whether or not your driver meets the Universal Windows Platform requirements. For more information, see [Getting Started with Universal Windows drivers](https://msdn.microsoft.com/windows/hardware/drivers/develop/getting-started-with-universal-drivers).</p></td>
    </tr>
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
    <td><p>Select an icon for your device from a list of default icons based on your device category. This determines which icon appears in Devices and Printers. If your device should not appear, select &quot;Internal device&quot;.</p>
    <p>For information about delivering a rich experience with Windows Device Stage, see [Device Metadata](https://msdn.microsoft.com/library/windows/hardware/br230800.aspx).</p></td>
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

     

    ![screenshot that shows the certification section](images/drivers-certification.png)

8.  Select **Submit**.

9.  The **Distribution** section is used to publish your driver to Windows Update. For information about how to use the **Distribution** section, see [Manage driver distribution with shipping labels](manage-driver-distribution-by-submission.md).

10. You can monitor the progress of your submission with the progress tracker at the top of the page. Once all steps show a green check, the submission is complete and your organization will receive a notification in the dashboard header.

    ![screenshot that shows the progress tracker](images/drivers-allgreen-new.png)

11. Review the results. If your submission failed, make any necessary changes and resubmit.

## <span id="related_topics"></span>Related topics


[Manage hardware submissions](manage-your-hardware-submissions.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhw_dashboard\hw_dashboard%5D:%20Create%20a%20new%20hardware%20submission%20%20RELEASE:%20%281/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





