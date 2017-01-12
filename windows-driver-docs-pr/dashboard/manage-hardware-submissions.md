---
title: Manage Hardware Submissions
description: Manage Hardware Submissions
MS-HAID:
- 'p\_dashboard.manage\_hardware\_submissions'
- 'hw\_dashboard.manage\_hardware\_submissions'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 732c601f-6bd6-4a6a-b82c-5ed913bc7e62
---

# Manage Hardware Submissions


After you have submitted your product for the Windows Hardware Compatibility Program for Windows 10 (or the certification program for previous versions), you can manage it through the dashboard.

**To manage a hardware submission**

1.  Sign in to the Hardware Dev Center dashboard with your Microsoft account.

2.  In the **Hardware compatibility** tile, click **Manage submissions**.

3.  On the **Manage submissions** page, you can see all the hardware submissions that have been submitted by your company. To find a specific hardware submission, you can do the following:

    <table>
    <colgroup>
    <col width="50%" />
    <col width="50%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th>To</th>
    <th>You can</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><p>Search</p></td>
    <td><p>Select to search by ID or by name, and then enter the ID or name in the Search box.</p></td>
    </tr>
    <tr class="even">
    <td><p>Filter</p></td>
    <td><p>Select one or more parameters from the options to create a more precise list.</p></td>
    </tr>
    <tr class="odd">
    <td><p>Sort</p></td>
    <td><p>Click a column heading to sort the list by that property.</p></td>
    </tr>
    </tbody>
    </table>

     

4.  Click the submission ID to open more information about the submission. The following information is available:

    <table>
    <colgroup>
    <col width="50%" />
    <col width="50%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th>Tab</th>
    <th>Description</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><p>Submission Info</p></td>
    <td><p>Describes the product, including:</p>
    <ul>
    <li><p>Name</p></li>
    <li><p>Marketing information, such as marketing name, part number, and locales</p></li>
    <li><p>Publication and distribution dates</p></li>
    <li><p>The device metadata category and the default icon if you do not choose to submit a custom icon</p></li>
    <li><p>Model ID</p></li>
    </ul>
    <p>Editable fields can be changed. To submit the changes, click <strong>Update</strong>.</p></td>
    </tr>
    <tr class="even">
    <td><p>Summary & Tasks</p></td>
    <td><p>Outlines the tasks required for complete certification, such as:</p>
    <ul>
    <li><p>Status, including current and next step</p></li>
    <li><p>Submission details, including billing group and purchase order number</p></li>
    <li><p>Qualification achieved</p></li>
    </ul>
    <p>Actions available depend on the status of the submission:</p>
    <ol>
    <li><p>If the submission status is Pending, you can cancel the submission by clicking <strong>Cancel Submission</strong>. If it is complete, you can update it or download signed catalog files for submissions that include non-inbox drivers.</p></li>
    <li><p>If the submission status is Approved, you can complete any of the items in the bulleted list that follows this table.</p></li>
    </ol></td>
    </tr>
    <tr class="odd">
    <td><p>Submission details</p></td>
    <td><p>Shows you a list of the features you tested in your Windows Hardware Certification Kit (HCK) submission for each operating system.</p></td>
    </tr>
    </tbody>
    </table>

     

    Upon approval of your submission, you can use the dashboard to do the following:

    -   Resell a device that you created to other companies for their use, after the device has been approved for certification a.

    -   Accept or decline a submission that has been sold to you.

    -   Download signed files.

    -   View, save, or print a copy of your Certification Verification Report.

    -   Manage Publication settings.

    -   Download a copy of the **WQReady.xml** file from a previous submission.

    -   Download certification artwork and style guidelines.

**To update an HCK submission using the Driver Update Acceptable (DUA) process**

1.  From **Manage submissions**, click the appropriate submission ID.

2.  Under the **Download** heading, click **DUA shell package**, and then click **Save**.

3.  From HCK Studio, click **Connect**.

4.  Select **Package**, and then click **Browse** to open the existing DUA shell package.

5.  Under **Packaging Options**, select **Driver Update**.

6.  Click **OK**.

7.  On the **Package** tab, right-click the appropriate driver folder, and then click **Replace Driver**.

8.  Click **Create Package**.

9.  Go back to **Manage submissions** in the dashboard, search by ID, and click **Upload driver update (DUA)**.

10. Use the new **.hckx** file that was created by HCK Studio and complete the DUA wizard.

**To update a WLK submission using the Driver Update Acceptable (DUA) process**

1.  From **Manage submissions**, click the submission ID.

2.  Under the **Download** heading, click **WST File**, and then click **Save**. The XML file will be saved as **submissionID.xml**.

3.  Open the Winqual Submission Tool application and change the **Submission Type** to **Driver Update Submission**.

4.  Click **Submission**, click **Open**, and then select the downloaded submissionID.xml file.

5.  Confirm that the driver folder location and driver path is correct. If the driver path is not correct, click **Edit**, and then browse to the correct driver folder path in the **Driver Package** tab. You should not add any new driver locales.

6.  Click **Create Package**. This creates the submissionID.cab file package. The submissionID.xml file with also be updated with the new driver path.

7.  Sign the submissionID.cab file with a code signing certificate.

8.  Go back to **Manage submissions** in the dashboard and search by ID.

9.  Under the **View** heading, click **Upload driver update (DUA)**. Use the submissionID.xml and submissionID.cab files that were created by WST and complete the DUA wizard.

**To resell a submission**

1.  On the **Manage submissions** page, click the ID of the approved submission you want to resell, and then open the **Summary & Tasks** tab.

2.  Under **Manage**, click **Resell this submission**.

3.  Select the name of the company to which you want to resell the submission and click **Resell**.

4.  The status of the resold submission can be viewed on the **Summary & Tasks** tab. Under **View**, click **Resold Submissions**.

**To accept or decline a submission that has been sold to you**

1.  On the **Manage submissions** page, filter the list by setting the **Status** to **Resold**, and then click the ID to open the submission.

2.  On the **Summary & Tasks** tab, accept or decline the resale.

## <span id="related_topics"></span>Related topics


[Hardware Certification Submissions](https://msdn.microsoft.com/library/windows/hardware/br230796.aspx)

[Create a new hardware logo submission](https://msdn.microsoft.com/library/windows/hardware/br230808.aspx)

[Test-Sign Your Driver (Legacy)](https://msdn.microsoft.com/library/windows/hardware/br230772.aspx)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhw_dashboard\hw_dashboard%5D:%20Manage%20Hardware%20Submissions%20%20RELEASE:%20%281/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





