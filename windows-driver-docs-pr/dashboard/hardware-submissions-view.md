---
title: View hardware submissions
description: This article shows you how to view and search for your organization's hardware submissions.
ms.topic: article
ms.date: 09/12/2024
---

# View hardware submissions

In the hardware dashboard, you can view all your organization's hardware submissions. This article shows you how to view and search for your organization's hardware submissions.

## Prerequisites

[Create a new hardware submission](hardware-submission-create.md).

## View your hardware submissions

In the hardware dashboard, you can view all your submitted driver information.

### View your driver submissions

1. Go to [Partner Center hardware dashboard](https://partner.microsoft.com/dashboard/hardware/Search) and sign in using your credentials.

1. View your drivers, listed with the following attributes for each submission:

   | Column | Description |
   |--|--|
   | Private Product ID | The Private ID of the driver. For more information, see [Hardware submission IDs](hardware-submission-ids.md) |
   | Product Name | The name of the driver specified during the submission creation process. |
   | Submission Status | The current state of the submission. Possible values are: <ul><li>Package acceptance: Your submission package passes initial screening for proper formatting and contents. <li>Preparation: We're preparing your package for further review and signing.<li>Validation: We're validating your package for policy compliance and technical correctness.<li>Manual review: We weren't able to automatically validate the contents of your package, so someone at Microsoft is taking a closer look.<li>Catalog creation: We're creating the security catalog for your driver.<li>Sign: We're applying Microsoft's signature to your security catalog and binaries.Finalize: We're finishing up your driver submission.<li>Completed: Your submission is complete. |
   | Submission Created Date | The date the driver was added to your account, either by you or by someone sharing the driver with you. |
   | Submission Type | The type of the driver submission. |
   | Permission | Your permission for the submission. Possible values are:<ul><li>Author: Author of the driver. You can complete all tasks and share the driver with partners.<li>Publisher: The driver is shared with you. You can download the driver, create Windows Update shipping labels, and create Driver Update Acceptable (DUA) packages. You can't share the driver with other companies.<li>Read-only: The driver was submitted to Windows Update on your behalf. You can see the driver details, download the driver, and view the shipping label that was submitted on your behalf. You can't create shipping labels or create DUA packages. </ul> |
   | Source | The author (shown as the organization name) of the submission. |
   | Shared Product ID | The Shared ID of the driver. For more information, see [Hardware submission IDs](hardware-submission-ids.md) |
   | Submission ID | The unique submission ID of the driver. For more information, see [Hardware submission IDs](hardware-submission-ids.md) |
   | Certification Type | The certification type for your submission. Possible values are: `HLK`, `HCK`, or `Attestation`. |
   | Submission Name | The name of the driver specified during the submission creation process. |

## Search for hardware submissions

After your driver package acceptance is complete, you can then use the search feature of the hardware dashboard. In-process driver submissions don't appear in search results until package acceptance is complete.

### Plain-text search

When you search for your hardware submissions, using plain text, enter search terms that match the value of any one of these fields:

- Private product ID
- Shared product ID
- Submission ID
- Product name
- Submission name
- Hardware ID
- INF name
- Operating system code

For example, the search phrase *mydriver* returns submissions with the product names *mydriver 1*, *new mydriver* and *old mydriver 2*, *mydriver1* and *mydriver_new*.

#### Use plain-text search

1. In the search text box, enter one or more search terms.

    :::image type="content" source="./images/hardware-submissions-view/hardware-search-plain-text.png" alt-text="Screenshot of the Drivers page in the hardware dashboard, with 'Search Service' entered into the search text box.'":::

1. To view the results, select the search icon.

### Keyword search

In this section, we show you how to use keyword search to search over both single and multiple attributes.

With keyword search, you can search for drivers by driver by any number of the following attributes:

| Parameter | Type | Possible values |
|--|--|--|
| ProductID | Numeric | 17 digit private product ID |
| SharedProductID | Numeric | 19 digit shared product ID |
| ProductName | Text | |
| CertificationType | Text | Attestation, HCK, HLK, WLK |
| Permission | Text | Author, Publisher |
| SubmissionID | Numeric | 19 digit Submission ID |
| SubmissionName | Text | |
| SubmissionType | Text | Initial, Derived |
| SubmissionStatus | Text | Complete, Failed, Processing, Ready |
| IsExtensionDriver | Boolean | False, True |
| IsUniversalDriver | Boolean | False, True |
| IsDeclarativeDriver | Boolean | False, True |
| INFName | Text | |
| HardwareID | Text | |
| OperatingSystemCode | Text | [List of OS codes](./get-product-data.md#list-of-operating-system-codes) |

#### Search over a single attribute

1. In the search box, enter an **\@**. The list of attributes should appear as in the following image:

    :::image type="content" source="./images/hardware-submissions-view/hardware-keyword-fields.png" alt-text="Screenshot of the Drivers page in the hardware dashboard, with @ symbol entered into the text box. A list of available attributes shows under @ symbol.":::

1. Select the attribute you wish to search over. For this example, we choose the `ProductName` attribute. The search field should look something like the following image:

   :::image type="content" source="./images/hardware-submissions-view/hardware-keyword-attribute-selected.png" alt-text="Screenshot of the search field with the ProductName attribute selected.'":::

1. Enter your search terms in between the quotation marks (**""**). Be careful not to modify the attribute name. The search phrase can be a complete search value or partial one. For example, to search for drivers by operating system codes you could use either *@OperatingSystemCode:"Windows 10 RS4 Client x64"*  or *@OperatingSystemCode:"Windows 10 RS4"*.

1. To view results, select the search icon.

#### Search over multiple attributes

Multiple attributes behave as if they are in an AND operator combination. For example, if you search for both product name and submission status (*@ProductName:"test" @SubmissionStatus:"Failed"*) the dashboard returns only those records that match *both* product name and submission status.

1. Follow the steps for [single attribute search](#search-over-a-single-attribute), except you separate each attribute with a space. Your search query should look something like the following image:

    :::image type="content" source="./images/hardware-submissions-view/hardware-keyword-attribute-multiple.png" alt-text="Screenshot of the Drivers page in the hardware dashboard, in which two attributes, @ProductName:'test' and @SubmissionStatus:'Failed', are entered. Results all have 'test' in the product name and 'Failed' in the submission status.":::

1. Select the search icon and view results.

### Important points

1. You can use a given parameter only once in a keyword search. For example, searching for (**@ProductName:"test" @ProductName:"system"**) causes an error.
1. Currently, you can't search by using the parameters **Submission Created Date** or **Source**. They aren't available at this time.
1. By default, search results are sorted by descending order of **Submission Created Date**. You can select any of the column title fields to change the sorting.
1. To search for product names or hardware ID, use the full search string. If you need to use a wildcard operator for these fields, avoid special characters (characters that aren't letters or numbers).

## Next steps

> [!div class="nextstepaction"]
> [Update a hardware submission](hardware-submission-update.md)

> [!div class="nextstepaction"]
> [Validate a hardware submission signature](code-signing-validate.md)
