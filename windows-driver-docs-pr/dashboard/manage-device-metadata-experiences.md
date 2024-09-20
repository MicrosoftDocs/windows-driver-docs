---
title: Manage Device Metadata Experiences
description: After you create and submit your device metadata experiences, you can review or edit them through the dashboard.
ms.topic: article
ms.date: 09/17/2024
---

# Manage Device Metadata Experiences

After you create and submit your device metadata experiences, you can review or edit them through the dashboard.

## Managing your device metadata experiences

On the **Manage experiences** page, you can add, remove, or promote (from preview to release) a device metadata package in a selected experience. You can also add packages for the same hardware IDs or model IDs into the same experience if the IDs are for different locales.

## To filter your device metadata experiences

1. Sign in to the **Dashboard** from either the Hardware Dev Center or the Windows Dev Center by using a Microsoft account.

1. On the left side of the window, select **Device metadata**, and then select **Manage experiences**.

1. All the experiences that you or your company created appear. Select the column headings to change the order of the list.

1. To display only the experiences that you want to see, use the filter at the top of the list. Enter one or more of the following parameters:

   | Parameter | Description |
   |--|--|
   | Experience name | From the list, select the name of the experience that you want to review or update. |
   | Hardware ID | Enter one or more hardware IDs that you want to review, inserting a semicolon after each entry. |
   | Device category | From the list, select the device category that you want to review. |
   | Model ID | Enter one or more model IDs that you want to review, inserting a semicolon after each entry. |

## To open and view your device metadata experience

1. To view the details, select an experience.

1. Under **Experience information**, review the information, which includes:

   | Element | Description |
   |--|--|
   | Experience type | The type of packages in an experience, including metadata for:<ul><li>Devices and printers<li>Device stage |
   | Device category | The device category of the packages in the experience. |
   | Model IDs | The model IDs defined in the packages in the experience. |
   | Hardware IDs | The hardware IDs defined in the packages in the experience. |
   | Logo submission IDs | The submission IDs bound to the experience. |

1. Under **Metadata packages**, expand an individual package to view more details. You can also download a package that is live or ready to be published.

   If a metadata package has an error, the error message is displayed here.

1. You can sort the list by clicking one of the following column headers:

   | Column header | Description |
   |--|--|
   | Name | The packages in the experience are listed according to their friendly name, if they have one, or by their file name. |
   | Submission date | This shows the date when you submitted each individual package. |
   | Preview | This check box is selected if the package is in preview and not released. |
   | Locale | This lists the country and region for which the package is designed. |
   | Default | **Yes** indicates the package that you designated as the default package. |
   | Status | This value indicates the current state of the selected package, and can be one of these values: <ul><li>**Pending**: The package is uploaded and is being validated.<li>**To Be Published**: The package is validated and is waiting to be sent to the metadata servers. You can download a validated copy of your package, and it becomes live and available to your users within 24 hours.<li>**Live**: The package is now available for your users to download.<li>**Error**: One or more errors were discovered during validation. Expand the section for more details. |

## To modify your device metadata experience

1. To release a preview package, select the package, and then select **Release**.

   It can take up to 48 hours for a released file to be available for users to download.

1. To remove a package from the experience, select the package, and then select **Delete**.

   You can only remove a package that is in the **Live** or **Error** state.

1. To update an existing package, select the package, select **Delete**, and then create and upload a new package.

   For more information about creating a new package, see the [Device Metadata Authoring Wizard](../devtest/device-metadata-authoring-wizard-portal.md), available in the [Windows Driver Kit](../download-the-wdk.md).

1. To add a new package, under **Add more metadata**, browse for the file or files that you want to add, create a friendly name if you want, and then select **Submit**.

   You can add a total of 50 packages to an experience.

## Related topics

- [Create a Device Metadata Experience](create-a-device-metadata-experience.md)
- [Submit a Bulk Metadata Package](submit-a-bulk-metadata-package.md)
- [Creating a Preview Package](creating-a-preview-package.md)
- [Errors and Solutions When Submitting Device Metadata Experiences](errors-and-solutions-when-submitting-device-metadata-experiences.md)
- [Device Metadata Business Rules](device-metadata-business-rules.md)
