---
title: Working with extension INF files in the Windows Hardware Dashboard
description: You can create shipping labels for your extension INF files on the Windows Hardware Dev Center, enabling you to share and publish them like other submissions.
ms.topic: article 
ms.date: 07/15/2024
---

# Working with extension INF files in the Partner Center

You can create shipping labels for your extension INF files on the Windows Hardware Dev Center, enabling you to share and publish them like other submissions. This article describes the process for packaging, submitting, and publishing these packages. For more information on how extension INFs are created and installed, see [Using an Extension INF file](../install/using-an-extension-inf-file.md).

## Requirements for publishing extension INFs to Windows Update

Publishing extension INFs to Windows update requires you to select automatic driver promotion checkboxes on your shipping label. The reason extension INFs can't be published as optional is because they aren't listed in Device Manager for an end user to initiate an "Update Driver" action. To see these checkboxes, you must first sign up for [driver flighting](./driver-flighting.md).

> [!NOTE]
> For Windows Update to offer extension INFs, all systems must be running at least the RS3 [January 3, 2018—KB4056892](https://support.microsoft.com/topic/january-3-2018-kb4056892-os-build-16299-192-c0ce8445-3adc-7a71-2fbd-9e93ed00b04e) (10.0.16299.192).

## Submitting and publishing extension INFs

This section describes how to submit and publish an INF package. See the highlighted items and FAQ for information on common mistakes and frequently asked questions.

> [!IMPORTANT]
> Microsoft recommends always creating a separate submission for each of your extension INFs, and a separate submission containing only your base driver submission. Publishing your base driver and extension INFs in a single submission will cause the following issues:
>
> - All shipping labels will be classified and evaluated as "Extension Drivers" by the Partner Center. To find items that are Extensions, enter `@IsExtensionDriver:"True"` in the Dev Center search box.
> - After being published to Windows Update, users may be forced to download your driver packages multiple times: Once when the base driver is installed, and again for each applicable extension that PnP detects.

### Creating a submission package

#### Base driver package

1. Start a Hardware Lab Kit (HLK) test run with your base driver and extension INFs as normal. The HLK results are used for all of the package creation steps.

    ![an image showing the files output by an HLK test run.](images/hlk-result-files.png)

1. Remove the extension INF template items from your Drivers folder and add only the base driver files back into your HLK package.

    ![an image showing the base driver files.](images/hlk-result-files2.png)

1. Create and sign this HLKx package to make your base driver package.

    > [!NOTE]
    > Base driver packages must always be backwards compatible with existing extensions.

#### Extension INF package

1. Using the same HLK results from the [base driver package](#base-driver-package) HLK test run, select **Package** > **Replace Driver**

    ![an image showing the 'replace driver' option in the HLK.](images/hlk-replace-driver.png)

1. Add the extension INF to the driver's folder with any referenced binaries. If you have multiple extension INFs, only add one file.

1. Create and sign this new HLK package. This package is your extension INF package.

1. Repeat this process for each of your extension INFs, removing the driver folder contents each time.

### Submitting your packages to the Partner Center

Create a new submission for each of the packages created and upload them to the Hardware Dev Center. Afterwards, create a shipping label for the ones you want share or publish. For more information, see [Create a new hardware submission](./hardware-submission-create.md) and [Manage driver distribution with shipping labels](./manage-driver-distribution-by-submission.md).

#### ExtensionID

The ExtensionID is a GUID that you generate that is used for driver lineage identification and versioning. It describes a hardware device part or part series, and is [automatically registered](https://techcommunity.microsoft.com/t5/Windows-Hardware-Certification/bg-p/WindowsHardwareCertification) to the SellerID that submitted it. The owner of this SellerID is responsible for keeping track of ExtensionID usage and mapping, similar to CHID management.

For example, when you create an ExtensionID for a new system part:

- The ExtensionID ownership is assigned to your SellerID.
- Every system project from your organization that uses the part or part series shares the same ExtensionID.
- The ExtensionID remains unchanged for the life of the part.

> [!NOTE]
>
> - If you use an ExtensionID that is not associated with your SellerID, Partner Center will reject your submission and inform you that the ExtensionID already belongs to another organization:
> - For a given device, only one extension INF is installed for each unique ExtensionID value. Therefore, if a device has multiple extension INFs you will need a new ExtensionID for each one. This also means if two extension INFs target the same device with different ExtensionIDs, both extension INFs will be applied. For more information, see [Using an Extension INF file](../install/using-an-extension-inf-file.md).
>
> If your organization manages projects and submissions for another organization, note the following:
>
> - ExtensionID ownership is assigned to the SellerID who finalizes the submission.
> - Using another organization's SellerID enables you to use their ExtensionID.
> - To use your organization's SellerID, you will need to create your own ExtensionID for the part or part series.

Generate a new ExtensionID for the initial version of an extension INF (that is, the first time you customize and submit an extension INF), including the first time you receive a new shared shipping label for a new device. Visual Studio includes a GUID creation utility in Tools > Create GUID, though any online GUID generation tool should work, if it matches the following registry format.

![An image showing the create GUID screen in Visual Studio.](images/guid-formatting.png)

If you're updating an extension INF that is already published, keep the ExtensionID the same and increment the version and/or date specified by the [DriverVer directive](../install/inf-driverver-directive.md). The driver date and driver version are used (in that order) to differentiate between multiple extension INFs with the same ExtensionID.

### Publishing an extension INF

To publish your extension INF submission, follow the steps in [Publish a driver to Windows Update](./publish-a-driver-to-windows-update.md). Ensure that both automatic driver promotion options are checked, and that your extension INFs have specific targeting.

![An image showing automatic driver promotions.](images/automatic-driver-promotion-options.png)

If you don't see these driver promotion options, you might need to sign up for [driver flighting](./driver-flighting.md).

All extension INFs go through the driver flighting process to be distributed through Windows Update. After a successful flight, the files will be available to retail systems. Joining the Windows Insiders program gives you faster access to drivers in this stage.

## Extension INF targeting and ranking differences

Because extensions are customizations for specific devices, they must always be targeted. Follow these guidelines when working with extension INF targeting:

- Extension INF files must have four-part Hardware IDs (HWIDs), if possible.
- CHIDs can be added to the extension INF's shipping label, in addition to having a four-part HWID.
- CHID targeting is required on the shipping label for parts and part series that don't have a four-part HWID.

This targeting information is vital to accurately evaluate your extension INF during distribution through Windows Update (WU). There are two stages in which WU evaluates drivers:

1. An applicability stage, when WU builds a list of drivers that apply to a given system.
1. A ranking stage where Windows PnP and WU determine which driver from the list to install.

In general, there are a few key principles regarding the ranking and targeting for extension INFs:

- The extension INF's ExtensionID isn't used for applicability – just for lineage and versioning identification.

- WU offers (and PnP installs) the highest-ranked extension driver for each applicable Extension ID.

- Extension drivers are ranked by date and version, which is included in the DriverVer directive. This is used by both WU and PnP. For more information, see [INF Version Section](../install/inf-version-section.md) and [INF DriverVer directive](../install/inf-driverver-directive.md).
- PnP and WU don't consider the Feature or Identifier Score (that is, two-part versus four-part) in regards to extension drivers.

- CHID information isn't used when ranking extension drivers on WU (that is, you can't "block" other extension drivers with CHID targeting).

- For information on driver selection and targeting within the Windows operating system, see [Using an Extension INF file](../install/using-an-extension-inf-file.md)

## FAQ

### Driver development

#### Do we need to change the ExtensionID every time we make an update to our base driver?

No, you should keep the same Extension ID when making updates to your base driver. The ExtensionID is used for version comparison and driver lineage identification. It shouldn't change within a driver's lineage.

### Manufacturing

#### Can we use an IHV-supplied extension INF with their ExtensionID for manufacturing purposes?

No. If you plan on owning the servicing aspect of the extension, then you must use your own extension INF and ExtensionID during manufacturing.

### Driver updates

#### Do we need to publish an updated extension INF to Windows Update every time a base driver package is updated and published?

No, and you must not. The base driver package must always be backwards compatible with existing extensions.

#### What happens when an updated base driver is published and applied to an end user's system?

When a base driver update is applied, the currently installed extension INF is evaluated and applied if necessary. If there are no extension INFs installed, Windows Update downloads the latest applicable version.

#### Do we need to publish an updated extension INF or ExtensionID when we update our OS to the latest version?

No, the existing ExtensionID and extension INF continues to work.

#### Can two systems share the same extension INF if their customizations are the same?

Yes. If multiple systems use the same settings, or if you want to customize settings across a broader set of devices, one extension INF is sufficient. Add the applicable four-part Hardware IDs to the extension INF. For more information, see [Using an Extension INF file](../install/using-an-extension-inf-file.md).

## Related topics

### Hardware Dev Center

- [Hardware submissions](hardware-submission-create.md)
- [Driver flighting](driver-flighting.md)
- [Manage driver distribution with shipping labels](driver-flighting.md)
- [Publishing to Windows Update](publish-a-driver-to-windows-update.md)

### Windows Drivers

- [Using a Universal INF File](../install/using-a-universal-inf-file.md)
- [Getting started with universal drivers](../develop/get-started-developing-windows-drivers.md)
- [Using a component INF file](../install/using-a-component-inf-file.md)
- [How windows ranks drivers](../install/how-setup-ranks-drivers--windows-vista-and-later-.md)
