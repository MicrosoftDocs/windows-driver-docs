---
title: Getting started with the Microsoft Partner Center Hardware dashboard
description: Getting started with the Microsoft Partner Center Hardware dashboard
ms.topic: article
ms.date: 04/13/2022
---

# Getting started with Partner Center Hardware dashboard

This article shows you how to get started using the Partner Center Hardware dashboard.

## Step 1: Get an EV code signing certificate

Your Hardware Dev Center dashboard account must have at least one extended validation (EV) certificate associated with it to submit binaries for attestation signing or to submit binaries for HLK certification. To learn how to get an EV certificate, see [EV certificate signed drivers](code-signing-reqs.md#ev-certificate-signed-drivers)

## Step 2: Register for the Hardware Developer Program

Now that you have your EV certificate ready, you can now register for the Hardware Developer Program. To register, follow the steps in [How to register for the Microsoft Windows Hardware Developer Program](register-for-the-hardware-program.md).

## Step 3: Test your hardware and drivers

Now that your company is registered in the Hardware Developer program, you'll need to design, create, and test your hardware and drivers. To ensure that your drivers and hardware run on Windows systems as your customers expect, you'll need to participate in either one of the following programs:

 * [Windows Hardware Compatibility Program](/windows-hardware/design/compatibility/) (for Windows 10 and above)
 * [Windows Hardware Certification Program](/previous-versions/windows/hardware/hck/jj125187(v=vs.85)) (for Windows 8/8.1 and older operating systems).

## Step 4: Submit for certification and compatibility

Once you've properly tested your drivers, you can now [create a new hardware submission](create-a-new-hardware-submission.md) in the [Partner Hardware dashboard](https://go.microsoft.com/fwlink/?LinkID=828002).

## Step 5: Manage driver distribution

If you have drivers that you want to distribute with Windows Update or share with another company, see [Manage driver distribution with shipping labels](manage-driver-distribution-by-submission.md), which covers common driver distribution tasks such as:

  * [Publish a driver to Windows Update](publish-a-driver-to-windows-update.md)
  * [Share a driver with a partner (Resell)](sharing-drivers-with-your-partners.md)
  * [Expire a driver from Windows Update](expire-a-driver-from-windows-update.md)
  * [View partner shipping labels for a shared driver](viewing-shipping-labels-for-your-shared-driver.md)

## Step 6: Publish your driver

Now that your driver has passed the review process in the Partner Hardware dashboard, it then becomes eligible for the hardware compatibility or certification program. In addition, you can publish it to the [Windows Server Catalog](https://www.windowsservercatalog.com/ ) and the [Windows Certified Products List](windows-certified-products-list.md) by providing an announcement date in your submission.

You can continue to use the Partner Center Hardware dashboard to:

* Customize your driver after initial certification (DUA).

* Manage your users and legal agreements.

* Use the dashboard API to programmatically work with submissions.

## Next Steps

> [!div class="nextstepaction"]
> [Manage your hardware driver submissions](manage-your-hardware-submissions.md).

> [!div class="nextstepaction"]
> [Find your hardware driver submissions](find-hardware-submission.md).

To learn more about attestation signing your drivers on the Sysdev dashboard, see

> [!div class="nextstepaction"]
> [Attestation signing a kernel driver for public release](code-signing-attestation.md).
