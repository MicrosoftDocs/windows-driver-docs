---
title: How to use the hardware dashboard
description: How to use the hardware dashboard
ms.topic: article
ms.date: 04/25/2022
---

# How to use the hardware dashboard

This article describes how to use the hardware dashboard during the Hardware submission process. If you haven't yet begun the submission process, see [Getting started with the hardware submission process](get-started-hardware-submissions.md).


## Hardware submission page

A hardware submission page contains information about a specific hardware submission, including status, packages, certification info, and shipping labels. For information about how to create a hardware submission, see [Create a new hardware submission](create-a-new-hardware-submission.md).

![screenshot that shows a hardware submission page.](images/hardware-submission-page.png)

The left side of the page contains a list of the 10 most recently viewed submissions.

You can monitor the progress of your submission with the progress tracker at the top of the page. Once all steps show a green check, the submission is complete and your company will receive a notification.

### Packages and signing properties

This section shows you how to manage your packages.

Select **Upload new** to upload a new package.

Select **Download DUA shell** to download the DUA shell package. For information about how to update a submission using DUA, see [Manage hardware submissions](manage-your-hardware-submissions.md).

The uploaded package list displays your uploaded packages for this submission. Select the caret to expand a package. This shows you the submission ID and allows you to select **Download package** to download the package.

**Additional certifications** displays any chosen additional certifications.

### Certification

This section displays certification information. Select **See more info** to expand this section. You can review the certification information you provided, which includes the following:

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
<td><p>Retpoline Compiled</p></td>
<td><p>Indicates whether or not your driver was compiled with the Retpoline flag.  A Check mark = True and an X = False.  For more information about this change see our <a href="https://techcommunity.microsoft.com/t5/Hardware-Dev-Center/Upcoming-Hardware-Dev-Center-changes-that-enable-support-for/ba-p/504574">blog post</a>. </p></td>
</tr><tr class="even">
<td><p>Is this a Universal Windows driver?</p></td>
<td><p>Indicates whether or not your driver meets the Universal Windows Platform requirements. For more information, see <a href="/windows-hardware/drivers/develop/getting-started-with-universal-drivers" data-raw-source="[Getting Started with Universal Windows drivers](../develop/getting-started-with-windows-drivers.md)">Getting Started with Universal Windows drivers</a>.</p></td>
</tr>
<tr class="even">
<td><p>What type of device?</p></td>
<td><p>Indicates that your device is:</p>
<ul>
<li><p>An internal component, if your device is part of a system and connects inside the PC.</p></li>
<li><p>An external component, if your device is an external device (peripheral) that connects to a PC.</p></li>
<li><p>Both, if your device can be connected internally (inside a PC) and externally (peripheral).</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p>Select metadata category</p></td>
<td><p>The device metadata category you selected.</p>
<p>If needed, you can generate a Sysdev reference ID that allows you to link up Dev Center hardware submissions with Sysdev Device Metadata submissions.</p></td>
</tr>
<tr class="even">
<td><p>Announcement date</p></td>
<td><p>The date when you want your product included on the Windows Server Catalog, the Windows Certified Product List, and the Universal Driver List. The default setting is <strong>Today</strong>.</p></td>
</tr>
<tr class="odd">
<td><p>Marketing names</p></td>
<td><p>Your marketing name(s). Marketing names allow you to provide aliases for your product. You can provide as many names as you want.</p></td>
</tr>
</tbody>
</table>

Submissions are automatically assigned Declarative and Universal attributes based off the entire submission contents.  If you want a submission to be marked as `Declarative=True` and/or `Universal=True`, all files and INFs within the submission must be compliant with the appropriate attribute(s).  For example, a merged HLK package can contain two driver sets for different OS certifiations. If one set is Declarative and another set is not, the entire submission would be marked as `Declarative=False`. INF only packages will have Universal greyed out as there are no binaries to validate.  Each set should be separated into two submissions to ensure they are marked appropriately. 

If you want to add or update your announcement date, use the **Announcement date (UTC)** field and select **Submit**.

You can also add or remove marketing names. To add a name, enter it in the **Marketing name** text box and select **Add**. To remove a name, select the red X button next to the marketing name you want to remove. You can also add multiple names at once by selecting **Add multiple names**. When you are finished, select **Submit**.

### Distribution

This section displays shipping label information for this submission. For information about how to use shipping labels, see the [Manage driver distribution with shipping labels](manage-driver-distribution-by-submission.md) section.

Select **New shipping label** to create a new shipping label.

Select **Publish all pending** to publish all shipping labels that are not yet published.

The shipping label list displays the shipping labels for this submission. This list includes shipping labels you created, and partner shipping labels for your shared driver. Select the shipping label name to see details for that shipping label. The shipping label list displays the following information about each label:

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
<td><p>Name</p></td>
<td><p>The shipping label name. Select this name to see details for the shipping label.</p></td>
</tr>
<tr class="even">
<td><p>Creator</p></td>
<td><p>The <strong>Publisher display name</strong> of the shipping label creator. This allows you to easily keep track of which business partners sent you drivers.</p></td>
</tr>
<tr class="odd">
<td><p>Destination</p></td>
<td><p>For a Windows Update shipping label, the destination is "Windows Update".</p>
<p>For a shared driver, the destination is the <strong>Publisher display name</strong> of the company you selected for <strong>Who is publishing?</strong> when you created the shipping label. This allows you to easily see all companies that you have shared your driver with.</p></td>
</tr>
<tr class="even">
<td><p>Created date</p></td>
<td><p>The creation date of the shipping label.</p></td>
</tr>
<tr class="odd">
<td><p>Release date</p></td>
<td><p>The release date of the shipping label.</p></td>
</tr>
<tr class="even">
<td><p>User created</p></td>
<td><p>If the shipping label was created by your company, you will see the details of the user who created the shipping label. This allows you to follow up if you have any questions about the creation. This field is not applicable if another company created the label.</p></td>
</tr>
<tr class="odd">
<td><p>User changed</p></td>
<td><p>If the shipping label was created by your company, you will see the details of the user who last modified the shipping label. This allows you to follow up if you have any questions about the changes. This field is not applicable if another company created the label.</p></td>
</tr>
</tbody>
</table>

The status graphic displays the publish status for each shipping label. A green check means the label has been published. A yellow circle means the label is not published yet.

## In this section

- [Create a new hardware submission](create-a-new-hardware-submission.md)

- [Manage hardware submissions](manage-your-hardware-submissions.md)
