---
title: Manage hardware submissions
description: Learn how to manage your hardware submissions by searching with text or by selecting driver attributes in a keyword search, or updating them using DUA and extension IDs.
ms.topic: article
ms.date: 04/24/2022
---

# Manage hardware submissions

After you submit your hardware drivers to the Partner Center Hardware dashboard for certification, you can manage them through the dashboard.

This article shows you how to perform the following tasks:

- Search for hardware submissions using plain-text or keyword search.
- Update your certified drivers with the Driver Update Acceptable (DUA) process.
- Extend a Windows 10+ base driver package's functionality by registering an ExtensionId.


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

## Update a hardware submission

After you submit your product for the Windows Hardware Compatibility Program for Windows 10 (or the certification program for previous Windows versions), you can then update it through the dashboard. This article describes the different options for updating your drivers.

### Use the Driver Update Acceptable (DUA) process

 DUA submissions can only be created off of an initial submission. DUA submissions shared with another company won't see the download DUA Shell button as you cannot do a DUA on a DUA submission.

For instructions on how to create a DUA submission from a DUA Shell, see [Create a driver only update package](/windows-hardware/test/hlk/user/create-a-driver-only-update-package).

### Register an ExtensionId

Prior to Windows 10, Windows selected a single driver package to install for a given device. This resulted in large, complex driver packages that included code for all scenarios and configurations, and each minor update required an update to the entire driver package. Starting in Windows 10, you can split INF functionality into multiple components, each of which can be serviced independently. The core driver package installed on a device is now called the base driver package and is handled by the system in the same way driver packages have been handled prior to Windows 10. To extend a base driver package's functionality, provide an extension INF in a separate driver package. For more information about using **ExtensionId**, see [Using an extension INF file](../install/using-an-extension-inf-file.md).

>[!NOTE]
>In your submissions, you may only use ExtensionIDs that are registered to your account.
