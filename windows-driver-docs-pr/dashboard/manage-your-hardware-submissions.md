---
title: Manage hardware submissions
description: Manage hardware submissions for the Windows Hardware Dev Center Dashboard
ms.assetid: C4C3C56F-8E92-4CB1-A57B-942E466ECD3D
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# Managing hardware submissions in the Windows Hardware Dev Center dashboard


After you submit your product for the Windows Hardware Compatibility Program for Windows 10 (or the certification program for previous Windows versions), you can manage it through the dashboard.

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

See [Create a driver only update package](https://docs.microsoft.com/windows-hardware/test/hlk/user/create-a-driver-only-update-package).

## Registering an ExtensionId

When you submit an extension INF to be signed, the dashboard checks if the specified **ExtensionId** was previously registered with a different account.
If it was, you'll see a message prompting you to provide a different ID. If not, the dashboard associates it with your account.

For more information about specifying **ExtensionId**, see [Using an extension INF file](https://docs.microsoft.com/windows-hardware/drivers/install/using-an-extension-inf-file). 

Note that in your submissions, you may only use ExtensionIDs that are registered to your account. 

## Related topics

- [Create a new hardware submission](create-a-new-hardware-submission.md)
- [Get drivers signed by Microsoft for multiple Windows versions](get-drivers-signed-by-microsoft-for-multiple-windows-versions.md)
- [Driver flighting](driver-flighting.md)


