---
title: Create a device metadata experience
description: Create a Device Metadata Experience
ms.topic: article
ms.date: 04/20/2017
---

# Create a Device Metadata Experience

After you've created your device metadata files (.devicemetadata-ms or .devicemanifest-ms) that provide the images and other features that make your device easily recognizable, you must submit them as an experience.

The devicemanifest-ms file is a .cab file that contains a devicemetadata-ms file and additional information for multi-locale packages, computer packages, and Mobile Broadband Account experience packages. For all devicemanifest-ms packages, additional information must be included in a LocaleInfo.xml file. For more information, see the PcMetadataSubmission.xml MobileBroadbandMetadataSubmission.xml creation pages.

## Creating a device metadata experience package

Before you can submit the files for logo certification, you must package the files into an experience. This experience is also a way to group together device metadata packages for devices that have the exact same set of Hardware IDs and Model IDs, but different locales.

### To create a device metadata experience package

1. Sign in to the Dashboard from the Partner Center using the Microsoft account associated with this service.

2. On the left side of the window, click **Device metadata**, and then click **Create experience**.

3. On the **Create experience** page, enter the following information:

   |Field|Description|
   |----|----|
   |Experience name|Create a name for the experience that is different from all other experience names that your company has produced.|
   |Package friendly name|If necessary, create a name that is easier to use and remember.|
   |Files|Browse to find and upload up to 50 files that you want to include in your experience.|
   |Preview package|Select this if you want to submit all your selected packages as preview packages. For more information, see [Creating a Preview Package](creating-a-preview-package.md).|
   |Bind to logo submissions|Choose the first option if you are submitting a device that only uses in-box drivers and does not have a logo certification. Choose the second option if your device has associated logo submissions; your device is a PC, printer, fax or scanner; or if your metadata is for a collection of mobile broadband account identifiers.|
   |Bind to logo submissions: select submissions|If you choose the second option and you are submitting metadata for a computer, Mobile Broadband Account experience, or a printer or fax on the IDDA list, you do not have to bind any logo submissions.</br>If you chose the second option and you are submitting metadata for any other type of device, you must select and bind the logo submissions that apply to your device.|

4. Click **Submit**.

## Related topics

[Manage Device Metadata Experiences](manage-device-metadata-experiences.md)

[Submit a Bulk Metadata Package](submit-a-bulk-metadata-package.md)

[Errors and Solutions When Submitting Device Metadata Experiences](errors-and-solutions-when-submitting-device-metadata-experiences.md)

[Device Metadata Business Rules](device-metadata-business-rules.md)
