---
title: Manage hardware submissions
description: Manage hardware submissions for the Windows Hardware Dev Center Dashboard
ms.assetid: C4C3C56F-8E92-4CB1-A57B-942E466ECD3D
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Managing hardware submissions in the Windows Hardware Dev Center dashboard


After you submit your product for the Windows Hardware Compatibility Program for Windows 10 (or the certification program for previous Windows versions), you can manage it through the dashboard.

-   [Find a hardware submission](#find-a-hardware-submission)
-   [Update an HCK hardware submission using the Driver Update Acceptable (DUA) process](#update-an-hck-hardware-submission-using-the-driver-update-acceptable-dua-process)

## Find a hardware submission

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

     

## Update an HCK hardware submission using the Driver Update Acceptable (DUA) process

1.  [Find the hardware submission](#find-a-hardware-submission) that you want to update.

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

## Registering an ExtensionId

When you submit an extension INF to be signed, the dashboard attempts to associate the **ExtensionId** with your account. If the **ExtensionId** is already registered with a different account, you'll see a message prompting you to use a different ID.

For more information about specifying **ExtensionId**, see [Using an extension INF file](https://docs.microsoft.com/en-us/windows-hardware/drivers/install/using-an-extension-inf-file). 

Note that in your submissions, you may only use ExtensionIDs that are registered to your account. 

## Related topics

   *  [Create a new hardware submission](create-a-new-hardware-submission.md)
   *  [Get drivers signed by Microsoft for multiple Windows versions](get-drivers-signed-by-microsoft-for-multiple-windows-versions.md)
   *  [Driver flighting](driver-flighting.md)


