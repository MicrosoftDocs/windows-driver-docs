---
title: Manage hardware submissions
description: Learn how to manage your hardware submissions by searching with text or by selecting driver attributes in a keyword search, or updating them using DUA and extension IDs.
ms.topic: article
ms.date: 04/24/2022
---

# Manage hardware submissions

After you submit your hardware drivers to the Partner Center Hardware dashboard for certification, you can manage them through the dashboard.

This article shows you how to search for, view, update, and manage your driver submissions.

## View hardware submission details

The hardware submission page contains information about a specific hardware submission, including status, packages, certification info, and shipping labels. For information about how to create a hardware submission, see [Create a new hardware submission](hardware-submission-create.md).

You can monitor the progress of your submission with the progress tracker at the top of the page. Once all steps show a green check, the submission is complete and your company will receive a notification.

To view your hardware submission:

1. Go to [Partner Center Hardware dashboard](https://partner.microsoft.com/dashboard/hardware/Search) and sign in using your credentials.

2. If you don't see your hardware, you can then [search for it](hardware-submission-manage.md#search-for-hardware-submissions).

3. In the **Private Product ID** column, select your driver's ID.

    :::image type="content" source="./images/hardware-submission-manage/hardware-select.png" alt-text="Screenshot that shows a selected hardware driver submission":::

4. You can now see your hardware submission details:

    :::image type="content" source="./images/hardware-submission-manage/hardware-details.png" alt-text="Screenshot that shows a hardware submission page":::

## Edit hardware submission details

### Upload driver packages

 DUA submissions can only be created off of an initial submission. DUA submissions shared with another company won't see the download DUA Shell button as you cannot do a DUA on a DUA submission.

To upload your driver packages:

1. Go to your [hardware submission details page](#view-your-hardware-submission).

2. Follow the directions in [Create a new hardware submission](hardware-submission-create.md#submit-your-new-hardware).

The uploaded package list displays your uploaded packages for this submission.

To download your signed files, the initial package, or the certification report:

1. Select **More**. The text will turn to **Less**.

2. Choose which files you want to download.

    :::image type="content" source="./images/hardware-submission-manage/hardware-download-packages.png" alt-text="Screenshot that shows file download options for a driver submission":::

### Download DUA shell

1. Go to your [hardware submission details page](#view-your-hardware-submission).

2. Move through the page, and then select **Download DUA shell** to download the DUA shell package.

    :::image type="content" source="./images/hardware-submission-manage/hardware-download-dua.png" alt-text="Screenshot that shows the DUA download button for a driver submission":::

### View certification information

1. Go to your [hardware submission details page](#view-your-hardware-submission).

2. Move through the page to the **Certification** section.

3. Select **See more info**.

    :::image type="content" source="./images/hardware-submission-manage/hardware-certification-view.png" alt-text="Screenshot that shows the certification section for a driver submission":::

4. You can now review the certification information that you provided, which includes the following information:

|Field|Description|
|----|----|
| DCHU Compliance |Indicates whether or not your driver meets the Universal Windows Platform requirements. For more information, see [Getting Started with Universal Windows drivers](https://techcommunity.microsoft.com/t5/Hardware-Dev-Center/Upcoming-Hardware-Dev-Center-changes-that-enable-support-for/ba-p/504574). |
|What type of device?|Indicates that your device is an *internal component* (part of a system and connects inside the PC), *external component* (an external device (peripheral) that connects to a PC), or *both*.|
| firmware version | The firmware version of your driver. |
|Announcement date| The date when you want your product included on the Windows Server Catalog, the Windows Certified Product List, and the Universal Driver List. The default setting is **Today**.|
|Marketing names|Your marketing name(s). Marketing names allow you to provide aliases for your product. You can provide as many names as you want.|

>[!IMPORTANT]
>Submissions are automatically assigned Declarative and Universal attributes based off the entire submission contents.  If you want a submission to be marked as `Declarative=True` and/or `Universal=True`, all files and INFs within the submission must be compliant with the appropriate attribute(s).  For example, a merged HLK package can contain two driver sets for different OS certifications. If one set is Declarative and another set is not, the entire submission would be marked as `Declarative=False`. INF only packages will have Universal greyed out as there are no binaries to validate.  Each set should be separated into two submissions to ensure they are marked appropriately.

### Update certification information

You can update the announcement date, and the marketing names for your driver.

**To add or update the announcement date:**

1. For **Announcement date (UTC)**, enter the desired date.

2. Select **Update**.

**To add a marketing name:**

1. For **Marketing name**, enter the name.

2. Select **Add**.

3. Select **Update**.

**To add multiple marketing names:**

1. Select **Add multiple**.

2. Enter each marketing name; one per line; no commas.

3. Select **Add marketing name(s)**.

4. Select **Update**.

**To remove a marketing name:**

1. Select **Remove** to the right of the marketing name you wish to remove.

2. Select **Update**.

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

## Update a hardware submission

After you submit your product for the Windows Hardware Compatibility Program for Windows 10 (or the certification program for previous Windows versions), you can then update it through the dashboard. There are two different options for updating your drivers:

- Driver Update Acceptable (DUA) process (not available for drivers signed with attestation)
- Register an Extension Id

### Use the Driver Update Acceptable (DUA) process

DUA submissions can only be created off of an initial submission. DUA submissions shared with another company won't see the download DUA Shell button as you cannot do a DUA on a DUA submission.

For instructions on how to create a DUA submission from a DUA Shell, see [Create a driver only update package](/windows-hardware/test/hlk/user/create-a-driver-only-update-package).

### Register an ExtensionId

Prior to Windows 10, Windows selected a single driver package to install for a given device. This resulted in large, complex driver packages that included code for all scenarios and configurations, and each minor update required an update to the entire driver package. Starting in Windows 10, you can split INF functionality into multiple components, each of which can be serviced independently. The core driver package installed on a device is now called the base driver package and is handled by the system in the same way driver packages have been handled prior to Windows 10. To extend a base driver package's functionality, provide an extension INF in a separate driver package. For more information about using **ExtensionId**, see [Using an extension INF file](../install/using-an-extension-inf-file.md).

>[!NOTE]
>In your submissions, you may only use ExtensionIDs that are registered to your account.

## Search for hardware submissions

All hardware submissions that have been submitted by your organization are displayed on the **Drivers** page of the hardware dashboard. To find a specific hardware submission, you can search using either:

- plain text search

- driver attributes for a keyword search

### Plain-text search

You can enter any search phrase in the text box. The dashboard returns entries with a word matching the phrase in any of these fields:

- product ID (private & shared)

- submission ID

- product name

- submission name

- hardware ID

- INF name

- operating System code

For example, the search phrase **mydriver** returns submissions with the product names *mydriver 1*, *new mydriver* and *old mydriver 2*, *mydriver1* and *mydriver_new*.

### Keyword Search

You can search for drivers by driver attributes using the keyword search. When you type an at symbol (**\@**) in the search box, the dashboard displays a list of the usable attributes. 

:::image type="content" source="./images/hardware-submission-manage/ampersand-search.png" alt-text="Screenshot of the Drivers page in the hardware dashboard, with @ symbol entered into the text box. A list of available attributes shows under @ symbol.":::

As you enter text after @ symbol, the list narrows to match the criteria. When you click one of the prepopulated values, it appears in the search box in the form **(@*ParameterName*: "")**. Do not modify the parameter name or the format, other than to enter a string between the quotation marks (**""**). Search phrase can be a complete search value or partial one. For example, to search for drivers  by operating system codes you could use either:

**@OperatingSystemCode:"Windows 10 RS4 Client x64"** 

or

**@OperatingSystemCode:"Windows 10 RS4"**

You can also search by using multiple attributes. Multiple attributes behave as if they are in an AND operator combination. For example, if you search for both product name and submission status (**@ProductName:"test" @SubmissionStatus:"Failed"**) the dashboard returns only those records that match **both** product name and submission status.

:::image type="content" source="./images/hardware-submission-manage/two-attribute-search.png" alt-text="Screenshot of the Drivers page in the hardware dashboard, in which two attributes, @ProductName:'test' and @SubmissionStatus:'Failed', are entered. Results all have 'test' in the product name as well as 'Failed' in the submission status.":::

You can use the following driver attributes for keyword searches:

|Parameter|Type|Possible values|
|----|----|----|
|ProductID |Numeric|17 digit private product ID|
|SharedProductID |Numeric|19 digit shared product ID|
|ProductName |Text|
|CertificationType |Text|Attestation, HCK, HLK, WLK|
|Permission |Text|Author, Publisher|
|SubmissionID |Numeric|19 digit Submission ID|
|SubmissionName |Text|
|SubmissionType |Text|Initial, Derived|
|SubmissionStatus |Text|Complete, Failed, Processing, Ready|
|IsExtensionDriver |Boolean|False, True|
|IsUniversalDriver |Boolean|False, True|
|IsDeclarativeDriver |Boolean|False, True|
|INFName |Text|
|HardwareID |Text|
|OperatingSystemCode |Text|[list of OS codes](./get-product-data.md#list-of-operating-system-codes)|

### Search results

Search results displayed on the dashboard list the driver submissions that match the search phrase.

> [!NOTE]
> The hardware dashboard creates entities only after the package acceptance is complete. Driver submissions therefore will not appear in search results until after the package acceptance is complete.

In the results, click the **Private Product ID** to navigate to that driver's overview page. There, you can view information about the driver's submission; updating the submission through the [DUA process](/windows-hardware/test/hlk/user/create-a-driver-only-update-package); and viewing, creating, and editing shipping labels or download signed files.

### Important Points

1. You can use a given parameter only once in a keyword search. For example, searching for (**@ProductName:"test" @ProductName:"system"**) causes an error.

2. Currently, you cannot search by using the parameters **Submission Created Date** or **Source**. They are not available at this time.

3. By default, search results are sorted by descending order of **Submission Created Date**. You can click any of the column title fields to change the sorting.

4. To search for product names or hardware ID, use the full search string. If you need to use a wildcard operator for these fields, avoid special characters (characters that are not letters or numbers).

