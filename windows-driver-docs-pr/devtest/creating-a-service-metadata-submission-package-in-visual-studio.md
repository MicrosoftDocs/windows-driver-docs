---
title: Creating a Service Metadata Submission Package in Visual Studio
description: Creating a service metadata submission package in Visual Studio
keywords:
- Creating a service metadata submission package in Visual Studio
ms.date: 06/25/2025
ms.topic: how-to
---

# Creating a service metadata submission package in Visual Studio

> [!IMPORTANT]
> Device metadata is deprecated and will be removed in a future release of Windows. For information about the replacement for this functionality, see **[Driver Package Container Metadata](../install/driver-package-container-metadata.md)**.

Use the Submission tool in Microsoft Visual Studio to create a submission package.

## To create a submission package

1. Click the **Driver** menu, select **Device Metadata**, and then select **Submission**.
1. Click **Add Metadata Package**, find and select the metadata package, and then click **Open**.
1. Confirm the **Package Name** and **Model Name**, and then select **Preview** if you want to preview the package. The **Model Name** field is the **Service Provider** name that is specified as part of the service metadata package.
1. Click **Next**.
1. Review the **Model Name**, **Hardware IDs**, and **Experience ID**.
1. Next to **Experience Name**, type a name for the experience. This step is required for all package submissions.
1. Next to **Qualification**, select **This device has an associated logo or unclassified submission** from the list.
1. If the package has been submitted before, select **Update Experience**.
1. Click **Next**.
1. Confirm the mobile broadband provider's information by re-entering the Hardware ID information (for example, IMSI or ICCID). The plain text Hardware ID information is used by the Hardware Dashboard in the Windows Dev Center to verify the hashed Hardware IDs that are specified in the metadata package.

1. If you haven't signed your package, follow these steps to sign it:    1. Find your certificate file and double-click it to install it.

    1. Make sure that you install the certificate file in the user store and not the machine store.
    1. Click **Launch Signature Wizard**.
    1. Click **Select store**.
    1. Select the certificate from the dialog box. The file name in the Signature Wizard is what you receive after you complete the submission metadata wizard. Therefore, unless you have a specific reason, do not change the file name or path.
    1. Complete the signing process.

1. When you're ready to submit your package, click **Launch Windows Dev Center - Hardware Dashboard**.

For more information about how to submit your package, see [Submit a Device Metadata Package](../dashboard/submit-a-device-metadata-package--dashboard-help-.md).

For more information about the device manifest file, see [Submit a mobile broadband device manifest package](../dashboard/submit-a-mobile-broadband-device-manifest-package.md).

For more information about the bulk metadata file, see [Submit a Bulk Metadata Package](../dashboard/submit-a-bulk-metadata-package.md).
