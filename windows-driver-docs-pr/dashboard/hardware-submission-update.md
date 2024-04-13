---
title: Update a hardware submission
description: Learn how to update hardware submission details, including status, packages, certification info, and shipping labels.
ms.topic: article
ms.date: 04/24/2022
---

# Update a hardware submission

Using the hardware dashboard, can view and update hardware submission details, including status, packages, certification info, and shipping labels.

## Prerequisites

[Create a new hardware submission](hardware-submission-create.md).

## View hardware submission details

To view your hardware submission details:

1. Go to [Partner Center hardware dashboard](https://partner.microsoft.com/dashboard/hardware/Search) and sign in using your credentials.

2. If you don't see your hardware, you can then [search for it](hardware-submissions-view.md).

3. In the **Private Product ID** column, select your driver's ID.

    :::image type="content" source="./images/hardware-submission-update/hardware-select.png" alt-text="Screenshot that shows a selected hardware driver submission":::

4. You can monitor the progress of your submission with the progress tracker. Once all steps show a green check, the submission is complete and your company will receive a notification.

    :::image type="content" source="./images/hardware-submission-update/hardware-details.png" alt-text="Screenshot that shows a hardware submission page":::

## Update your hardware submission

There are two different options for updating your hardware submission:

- **Driver Update Acceptable (DUA) process (not available for drivers signed with attestation).**
After you submit your product for the Windows Hardware Compatibility Program for Windows 10 (or the certification program for previous Windows versions), you can then update it through the dashboard. 
DUA submissions can only be created off of an initial submission. DUA submissions shared with another company won't see the download DUA Shell button as you cannot do a DUA on a DUA submission. For instructions on how to create a DUA submission from a DUA Shell, see [Create a driver only update package](/windows-hardware/test/hlk/user/create-a-driver-only-update-package).

- **Register an Extension Id.** Prior to Windows 10, Windows selected a single driver package to install for a given device. This resulted in large, complex driver packages that included code for all scenarios and configurations, and each minor update required an update to the entire driver package. Starting in Windows 10, you can split INF functionality into multiple components, each of which can be serviced independently. The core driver package installed on a device is now called the base driver package and is handled by the system in the same way driver packages have been handled prior to Windows 10. To extend a base driver package's functionality, provide an extension INF in a separate driver package. For more information about using **ExtensionId**, see [Using an extension INF file](../install/using-an-extension-inf-file.md).


>[!NOTE]
>In your submissions, you may only use ExtensionIDs that are registered to your account.

### Upload your driver update files

**To update your submissions:**

1. Go to your [hardware submission details page](#view-hardware-submission-details).

1. Move down through the page, and then select **Download DUA shell** to download the DUA shell package.

    :::image type="content" source="./images/hardware-submission-update/hardware-download-dua.png" alt-text="Screenshot that shows the DUA download button for a driver submission":::

1. Create a DUA submission from a DUA Shell. For information on how to create a DUA submission, see see [Create a driver only update package](/windows-hardware/test/hlk/user/create-a-driver-only-update-package).

1. On the driver details page, in the **Packages and signing properties** section, select **Upload new**.

1. Either drag or browse to the DUA package file that you want to submit.

### Download your submission files

In the submission details page, you can download signed files, the initial package, or the certification report:

1. Go to your [hardware submission details page](#view-hardware-submission-details).

1. Move down through the page, to the **Packages and signing properties** section.

1. Select **More**. The text will turn to **Less**.

1. Choose which files you want to download.

    :::image type="content" source="./images/hardware-submission-update/hardware-download-packages.png" alt-text="Screenshot that shows file download options for a driver submission":::

## View certification information

1. Go to your [hardware submission details page](#view-hardware-submission-details).

1. Move through the page to the **Certification** section.

1. Select **See more info**.

    :::image type="content" source="./images/hardware-submission-update/hardware-certification-view.png" alt-text="Screenshot that shows the certification section for a driver submission":::

1. You can now review the certification information that you provided, which includes the following information:

    |Field|Description|
    |----|----|
    | DCHU Compliance |Indicates whether or not your driver meets the Universal Windows Platform requirements. For more information, see [Getting Started with Universal Windows drivers](https://techcommunity.microsoft.com/t5/Hardware-Dev-Center/Upcoming-Hardware-Dev-Center-changes-that-enable-support-for/ba-p/504574). |
    |What type of device?|Indicates that your device is an *internal component* (part of a system and connects inside the PC), *external component* (an external device (peripheral) that connects to a PC), or *both*.|
    | firmware version | The firmware version of your driver. |
    |Announcement date| The date when you want your product included on the Windows Server Catalog, the Windows Certified Product List, and the Universal Driver List. The default setting is **Today**.|
    |Marketing names|Your marketing name(s). Marketing names allow you to provide aliases for your product. You can provide as many names as you want.|

    >[!IMPORTANT]
    >Submissions are automatically assigned Declarative and Universal attributes based off the entire submission contents.  If you want a submission to be marked as `Declarative=True` and/or `Universal=True`, all files and INFs within the submission must be compliant with the appropriate attribute(s).  For example, a merged HLK package can contain two driver sets for different OS certifications. If one set is Declarative and another set is not, the entire submission would be marked as `Declarative=False`. INF only packages will have Universal greyed out as there are no binaries to validate.  Each set should be separated into two submissions to ensure they are marked appropriately.

## Update certification information

In the submission details page, you can update certification information, such as the announcement date and marketing names for your driver.

>[!NOTE]
>Make sure to check the announcement date that's been set. Once the announcement date has passed, you won't be able to add a new name.

To update certification details:

1. Go to your [hardware submission details page](#view-hardware-submission-details).

1. Move through the page to the **Certification** section.

1. Select **See more info**.

**To add or update the announcement date:**

1. For **Announcement date (UTC)**, enter the desired date.

1. Select **Update**.

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

## Create and publish shipping labels

This section displays shipping label information for this submission. For information about how to use shipping labels, see the [Manage driver distribution with shipping labels](manage-driver-distribution-by-submission.md) section.

To create a new shipping label, select **New shipping label**.

To publish all shipping labels that are not yet published, select **Publish all pending**.

The shipping label list displays the shipping labels for this submission. This list includes shipping labels you created, and partner shipping labels for your shared driver. Select the shipping label name to see details for that shipping label. The shipping label list displays the following information about each label:

|Field|Description|
|--|--|
|Name|The shipping label name. Select this name to see details for the shipping label.|
|Creator|The **Publisher display name** of the shipping label creator. This allows you to easily keep track of which business partners sent you drivers.|
|Destination|For a Windows Update shipping label, the destination is "Windows Update".For a shared driver, the destination is the **Publisher display name** of the company you selected for **Who is publishing?** when you created the shipping label. This allows you to easily see all companies that you have shared your driver with.|
|Created date|The creation date of the shipping label.|
|Release date|The release date of the shipping label.|
|User created|If the shipping label was created by your company, you will see the details of the user who created the shipping label. This allows you to follow up if you have any questions about the creation. This field is not applicable if another company created the label.|
|User changed|If the shipping label was created by your company, you will see the details of the user who last modified the shipping label. This allows you to follow up if you have any questions about the changes. This field is not applicable if another company created the label.|

The status graphic displays the publish status for each shipping label. A green check means the label has been published. A yellow circle means the label is not published yet.

## Next Steps

> [!div class="nextstepaction"]
> [Validate a hardware submission signature](code-signing-validate.md)