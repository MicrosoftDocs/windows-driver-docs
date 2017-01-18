---
title: Manage hardware submissions
description: Manage hardware submissions
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: C4C3C56F-8E92-4CB1-A57B-942E466ECD3D
---

# Manage hardware submissions


After you submit your product for the Windows Hardware Compatibility Program for Windows 10 (or the certification program for previous Windows versions), you can manage it through the dashboard.

-   [Find a hardware submission](#find-submission)
-   [Update an HCK hardware submission using the Driver Update Acceptable (DUA) process](#configuration-settings)

## <span id="find_submission"></span><span id="FIND_SUBMISSION"></span>


**Find a hardware submission**

1.  Sign in to the Windows Hardware Dev Center dashboard.

2.  On the **Manage submissions** page, you can see all hardware submissions that have been submitted by your organization. To find a specific hardware submission, you can do the following:

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
    <td><p>Sort</p></td>
    <td><p>Click a column heading to sort the list by that property.</p></td>
    </tr>
    </tbody>
    </table>

     

    ![screenshot that shows the driver list](images/drivers-summary-page.png)

3.  Click the submission ID to open more information about the submission. The following information is available:

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
    <td><p>Submission info</p></td>
    <td><p>Describes the product, including:</p>
    <ul>
    <li><p>Name</p></li>
    <li><p>Certification selection</p></li>
    <li><p>Device type</p></li>
    <li><p>The device metadata category and the default icon if you do not choose to submit a custom icon</p></li>
    <li><p>Announcement date</p></li>
    <li><p>Marketing names. You can add new marketing names and select <strong>Add</strong>.</p></li>
    <li><p>If applicable, the signed driver files can be downloaded.</p></li>
    </ul></td>
    </tr>
    </tbody>
    </table>

     

## <span id="update_submission"></span><span id="UPDATE_SUBMISSION"></span>


**Update an HCK hardware submission using the Driver Update Acceptable (DUA) process**

1.  [Find the hardware submission](#find-submission) that you want to update.

2.  Select **Download DUA shell**, and then select **Save**. Note: DUA is only available for driver submissions that include a driver.

    ![screenshot of the dua download button](images/drivers-dua-upload-buttons.png)

3.  Launch HCK Studio.

4.  Select **Package**, and then select **Browse** to open the downloaded DUA shell package.

5.  Select **Open as Driver Update package**.

6.  Select **OK**.

7.  Select the **Package** tab.

8.  For each driver you want to update, right-click the appropriate driver folder and then select **Replace Driver**.

9.  Select **Create Package**.

10. You will also need to sign your package, so select "Use the certificate store".

11. Go to your hardware submission and select **Upload new** in the **Packages and signing properties** section.

    ![screenshot of the upload new button](images/drivers-dua-upload-buttons.png)

12. Choose a name for your updated driver package. You can use this name to organize your driver packages. Shipping Labels are associated to a specific driver package, so it is important to choose a unique name that you will recognize later.

13. Upload your updated driver package.

14. You can monitor the progress of your driver update with the progress tracker at the top of the page. Once all steps show a green check, the update is complete.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhw_dashboard\hw_dashboard%5D:%20Manage%20hardware%20submissions%20%20RELEASE:%20%281/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




