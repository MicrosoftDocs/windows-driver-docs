---
title: Creating a Preview Package
description: Creating a Preview Package
MS-HAID:
- 'p\_dashboard.creating\_a\_preview\_package'
- 'hw\_dashboard.creating\_a\_preview\_package'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 49880681-480d-4f2d-bf8f-d621ac275244
---

# Creating a Preview Package


When you create a package, you can submit it for preview only. This allows you to test an experience on client devices, and then change or modify the experience before you release it as a live experience.

## <span id="Submitting_a_preview_package"></span><span id="submitting_a_preview_package"></span><span id="SUBMITTING_A_PREVIEW_PACKAGE"></span>Submitting a preview package


Before you submit preview packages, you must first create a PreviewKey that is unique to your company. Only people who know the PreviewKey can download your preview packages.

The process for releasing a preview package is the same as the process for releasing any other package, except that you identify the package as a preview so that your selected users know to use the PreviewKey.

Any preview package submitted by the partner of a company will require the company’s PreviewKey to be set in a registry key with the following settings:

-   Key: HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Device Metadata

-   Value Name: DeviceMetadataPreviewKey

-   Value Type: REG\_SZ

-   Value: &lt;Your PreviewKey&gt;

**To create a PreviewKey**

1.  From either the Windows Dev Center or the Hardware Dev Center, sign in to the dashboard with the Microsoft account.

2.  On the left side of the window, click **Device metadata**.

3.  On the **Device metadata** page, under **Manage preview key**, enter a PreviewKey that conforms to the following guidelines:

    -   The PreviewKey must contain between 1 and 15 characters.

    -   The characters must be alphanumeric. In other words, the PreviewKey can include only uppercase letters, lowercase letters, or numbers. The PreviewKey cannot contain special characters.

    -   The PreviewKey must be unlike any other existing PreviewKey.

    -   Only one PreviewKey is allowed for each company.

## <span id="related_topics"></span>Related topics


[Create a Device Metadata Experience](https://msdn.microsoft.com/library/windows/hardware/br230794.aspx)

[Submit a Device Metadata Package (Dashboard help)](https://msdn.microsoft.com/library/windows/hardware/br230807.aspx)

[Device Metadata Business Rules](https://msdn.microsoft.com/library/windows/hardware/br230767.aspx)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhw_dashboard\hw_dashboard%5D:%20Creating%20a%20Preview%20Package%20%20RELEASE:%20%281/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





