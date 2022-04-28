---
title: Creating a Preview Package
description: Creating a Preview Package
ms.topic: article
ms.date: 04/20/2017
---

# Creating a Preview Package

When you create a package, you can submit it for preview only. This allows you to test an experience on client devices, and then change or modify the experience before you release it as a live experience.

## Submitting a preview package

Before you submit preview packages, you must first create a PreviewKey that is unique to your company. Only people who know the PreviewKey can download your preview packages.

The process for releasing a preview package is the same as the process for releasing any other package, except that you identify the package as a preview so that your selected users know to use the PreviewKey.

Any preview package submitted by the partner of a company will require the company’s PreviewKey to be set in a registry key with the following settings:

- Key: HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Device Metadata

- Value Name: DeviceMetadataPreviewKey

- Value Type: REG\_SZ

- Value: &lt;Your PreviewKey&gt;

### To create a PreviewKey

1. From the Partner Center, sign in to the dashboard with the Microsoft account.

2. On the left side of the window, click **Device metadata**.

3. On the **Device metadata** page, under **Manage preview key**, enter a PreviewKey that conforms to the following guidelines:

    - The PreviewKey must contain between 1 and 15 characters.

    - The characters must be alphanumeric. In other words, the PreviewKey can include only uppercase letters, lowercase letters, or numbers. The PreviewKey cannot contain special characters.

    - The PreviewKey must be unlike any other existing PreviewKey.

    - Only one PreviewKey is allowed for each company.

## Related topics


[Create a Device Metadata Experience](create-a-device-metadata-experience.md)

[Submit a Device Metadata Package (Dashboard help)](submit-a-device-metadata-package--dashboard-help-.md)

[Device Metadata Business Rules](device-metadata-business-rules.md)
