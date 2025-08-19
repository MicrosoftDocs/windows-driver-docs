---
title: Creating a Device Metadata Submission Package in Visual Studio
description: Creating a device metadata submission package in Visual Studio
keywords:
- Creating a device metadata submission package in Visual Studio
ms.date: 06/25/2025
ms.topic: how-to
---

# Creating a device metadata submission package in Visual Studio

> [!IMPORTANT]
> Device metadata is deprecated and will be removed in a future release of Windows. For information about the replacement for this functionality, see **[Driver Package Container Metadata](../install/driver-package-container-metadata.md)**.

To create a device metadata submission package, use the Submission tool in Microsoft Visual Studio.

1. In Visual Studio, click the **Driver** menu, select **Device Metadata**, and then select **Submission**.
1. Click **Add Metadata Package**, select the package, and then click **Open**.
1. Confirm the **Package Name** and **Model Name**, select **Preview** if you want to preview the package, and then click **Next** .
1. Review the **Model Name**, **Hardware IDs**, and **Experience ID**.
1. Next to **Experience Name**, type a name for the experience. This step is required for all package submissions.
1. Next to **Qualification**, select one of the following options from the list:
    - **This device has an associated logo or unclassified submission**
        - Enter **Logo Submission IDs**.
    - **This device uses only inbox drivers and has no associated logo submissions**

1. If the package has been submitted before, select **Update Experience**.
1. Click **Next**.
1. If you haven't signed your package, complete the following steps in the Signature Wizard to sign it:    1. Find your certificate file and double-click it to install it.
    1. Make sure that you install the certificate file in the user store and not in the machine store.
    1. Click **Launch Signature Wizard**.
    1. Click **Select store**.
    1. Select the certificate from the dialog box.
        **Note**   The file name in the Signature Wizard is what you receive after you complete the submission metadata wizard. Therefore, unless you have a specific reason, do not change the file name or path.

    1. Complete the signing process.

1. When you're ready to submit your package, click **Launch Windows Dev Center - Hardware Dashboard**.

For more information about how to submit your package, see [Submit a Device Metadata Package](../dashboard/submit-a-device-metadata-package--dashboard-help-.md).

For more information about the bulk metadata file, see [Submit a Bulk Metadata Package](../dashboard/submit-a-bulk-metadata-package.md).
