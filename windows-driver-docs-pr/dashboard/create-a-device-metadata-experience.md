---
title: Create a Device Metadata Experience
description: Create a Device Metadata Experience
ms.assetid: 964ad06e-0f29-441d-b184-61f80a614914
ms.topic: article
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Create a Device Metadata Experience


After you've created your device metadata files (.devicemetadata-ms or .devicemanifest-ms) that provide the images and other features that make your device easily recognizable, you must submit them as an experience.

The devicemanifest-ms file is a .cab file that contains a devicemetadata-ms file and additional information for multi-locale packages, computer packages, and Mobile Broadband Account experience packages. For all devicemanifest-ms packages, additional information must be included in a LocaleInfo.xml file. For more information, see the PcMetadataSubmission.xml MobileBroadbandMetadataSubmission.xml creation pages.

## <span id="Creating_a_device_metadata_experience_package"></span><span id="creating_a_device_metadata_experience_package"></span><span id="CREATING_A_DEVICE_METADATA_EXPERIENCE_PACKAGE"></span>Creating a device metadata experience package


Before you can submit the files for logo certification, you must package the files into an experience. This experience is also a way to group together device metadata packages for devices that have the exact same set of Hardware IDs and Model IDs, but different locales.

**To create a device metadata experience package**

1. Sign in to the Dashboard from either the Windows Dev Center or the Hardware Dev Center using the Microsoft account associated with this service.

2. On the left side of the window, click **Device metadata**, and then click **Create experience**.

3. On the **Create experience** page, enter the following information:

   <table>
   <colgroup>
   <col width="50%" />
   <col width="50%" />
   </colgroup>
   <thead>
   <tr class="header">
   <th>Field</th>
   <th>Description</th>
   </tr>
   </thead>
   <tbody>
   <tr class="odd">
   <td><p>Experience name</p></td>
   <td><p>Create a name for the experience that is different from all other experience names that your company has produced.</p></td>
   </tr>
   <tr class="even">
   <td><p>Package friendly name</p></td>
   <td><p>If necessary, create a name that is easier to use and remember.</p></td>
   </tr>
   <tr class="odd">
   <td><p>Files</p></td>
   <td><p>Browse to find and upload up to 50 files that you want to include in your experience.</p></td>
   </tr>
   <tr class="even">
   <td><p>Preview package</p></td>
   <td><p>Select this if you want to submit all your selected packages as preview packages. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/br230780.aspx" data-raw-source="[Creating a Preview Package](https://msdn.microsoft.com/library/windows/hardware/br230780.aspx)">Creating a Preview Package</a>.</p></td>
   </tr>
   <tr class="odd">
   <td><p>Bind to logo submissions</p></td>
   <td><p>Choose the first option if you are submitting a device that only uses in-box drivers and does not have a logo certification. Choose the second option if your device has associated logo submissions; your device is a PC, printer, fax or scanner; or if your metadata is for a collection of mobile broadband account identifiers.</p></td>
   </tr>
   <tr class="even">
   <td><p>Bind to logo submissions: select submissions</p></td>
   <td><p>If you choose the second option and you are submitting metadata for a computer, Mobile Broadband Account experience, or a printer or fax on the IDDA list, you do not have to bind any logo submissions.</p>
   <p>If you chose the second option and you are submitting metadata for any other type of device, you must select and bind the logo submissions that apply to your device.</p></td>
   </tr>
   </tbody>
   </table>

     

4. Click **Submit**.

## <span id="related_topics"></span>Related topics


[Manage Device Metadata Experiences](https://msdn.microsoft.com/library/windows/hardware/br230797.aspx)

[Submit a Bulk Metadata Package](https://msdn.microsoft.com/library/windows/hardware/hh801895.aspx)

[Errors and Solutions When Submitting Device Metadata Experiences](https://msdn.microsoft.com/library/windows/hardware/br230786.aspx)

[Device Metadata Business Rules](https://msdn.microsoft.com/library/windows/hardware/br230767.aspx)

 

 






