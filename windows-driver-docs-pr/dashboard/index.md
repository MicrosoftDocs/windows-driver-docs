---
title: Partner Center for Windows Hardware
description: This article describes how to get started with the hardware submission process by using the Partner Center for Windows Hardware.
ms.topic: article
ms.date: 09/05/2024
---

# Partner Center for Windows Hardware

This article describes how to get started with the hardware submission process by using the Partner Center for Windows Hardware. We take you through each step of the process, from getting an extended validation (EV), to registration, and finally, to driver publication and certification.

With the Windows Hardware Compatibility Program you can design, create, and test your hardware and drivers before you submit the final version through the Partner Center hardware dashboard for certification. By certifying your hardware device, system, and drivers for Windows, you gain the support of Microsoft marketing resources in the form of compatibility and reliability listings, logo artwork, and promotional partnerships.

## Step 1: Get an EV code signing certificate

Your Hardware Dev Center dashboard account must have at least one extended validation (EV) certificate associated with it to submit binaries for attestation signing or to submit binaries for Windows Hardware Lab Kit (HLK) certification. To learn how to get an EV certificate, see [EV certificate signed drivers](code-signing-reqs.md#ev-certificate-signed-drivers).

## Step 2: Register for the Hardware Developer Program

Now that you have your EV certificate ready, you can now register for the Hardware Developer Program. To register, follow the steps in [How to register for the Microsoft Windows Hardware Developer Program](hardware-program-register.md).

## Step 3: Test your hardware and drivers

Now that your company is registered in the Hardware Developer program, you need to design, create, and test your hardware and drivers. To ensure that your drivers and hardware run on Windows systems as your customers expect, you need to participate in the [Windows Hardware Compatibility Program](/windows-hardware/design/compatibility/).

## Step 4: Submit for certification and compatibility

Once your drivers are properly tested, [create a new hardware submission](hardware-submission-create.md).

## Step 5: Manage driver distribution

If you have drivers that you want to distribute with Windows Update or share with another company, see [Manage driver distribution with shipping labels](manage-driver-distribution-by-submission.md) to learn about common driver distribution tasks such as:

- [Publish a driver to Windows Update](publish-a-driver-to-windows-update.md)
- [Share a driver with a partner (Resell)](sharing-drivers-with-your-partners.md)
- [Expire a driver from Windows Update](expire-a-driver-from-windows-update.md)
- [View partner shipping labels for a shared driver](viewing-shipping-labels-for-your-shared-driver.md)

## Step 6: Publish your driver

When your driver has passes the review process in the Partner hardware dashboard, it becomes eligible for the hardware compatibility or certification program. In addition, you can publish it to the [Windows Server Catalog](https://www.windowsservercatalog.com/ ) and the [Windows Certified Products List](windows-certified-products-list.md) by providing an announcement date in your submission.

You can continue to use the Partner Center hardware dashboard to:

- Customize your driver after initial certification using the Driver Update Acceptable (DUA) process.
- Manage your users and legal agreements.
- Use the dashboard API to programmatically work with submissions.

## Step 7: Share a link to a Windows Certification Verification Report

Once your driver is certified, you can share the verification report with a sharable URL. This URL allows the report to be accessed and downloaded without prior authorization or access to the Partner Center. The sharable URL contains three identification numbers separated by slashes:

`https://developer.microsoft.com/dashboard/hardware/driver/DownloadCertificationReport/<SellerID>/<PrivateProductID>/<SubmissionID>`

To create a sharable link, replace **SellerID**, **PrivateProductID**, and **SubmissionID** in the example URL with the appropriate identification numbers.

The identification numbers used in the URL and their locations are:

| Component | Description |
|--|--|
| **SellerID** | The identification number of your partner account found on the account management page, under **Account settings**. |
| **PrivateProductID** | The identification number generated with each product creation. Located on the driver details page for your product. For more information, see [Dashboard ID definitions](./hardware-submission-ids.md). |
| **SubmissionID** | The identification number given to each submission and submission update. Located on the driver details page for your product. For more information, see [Dashboard ID definitions](./hardware-submission-ids.md). |

## Next Steps

> [!div class="nextstepaction"]
> [Create a hardware submission](hardware-submission-create.md)

> [!div class="nextstepaction"]
> [View hardware submissions](hardware-submissions-view.md)

> [!div class="nextstepaction"]
> [Update a hardware submission](hardware-submission-update.md)

> [!div class="nextstepaction"]
> [Validate a hardware submission signature](code-signing-validate.md)

> [!div class="nextstepaction"]
> [Windows HLK Getting Started Guide](/windows-hardware/test/hlk/getstarted/windows-hlk-getting-started)

> [!div class="nextstepaction"]
> [Attestation sign Windows 10+ drivers](code-signing-attestation.md).
