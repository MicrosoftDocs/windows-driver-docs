---
title: Errors and Solutions When Submitting Device Metadata Experiences
description: Errors and Solutions When Submitting Device Metadata Experiences
ms.assetid: 793b4c92-96e8-4b3e-a7de-d00e953c983a
ms.topic: article
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Errors and Solutions When Submitting Device Metadata Experiences


When you submit device metadata experiences for validation and publication, you may see errors that can affect the release of your experience.

## <span id="Common_errors"></span><span id="common_errors"></span><span id="COMMON_ERRORS"></span>Common errors


Here are some of the most common errors, listed in alphabetical order, and including solutions if available.

### <span id="To_solve_common_errors"></span><span id="to_solve_common_errors"></span><span id="TO_SOLVE_COMMON_ERRORS"></span>To solve common errors

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Error</th>
<th>Suggested solution</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[CategoryName] Category id is incorrect in Behavior.xml. Correct Category id is [CategoryId]</p></td>
<td><p>For more information, see the <a href="http://go.microsoft.com/fwlink/p/?LinkId=241658" data-raw-source="[Microsoft Device Experience Development Kit](http://go.microsoft.com/fwlink/p/?LinkId=241658)">Microsoft Device Experience Development Kit</a>.</p></td>
</tr>
<tr class="even">
<td><p>[CategoryName] Guid [CategoryId] is required for your device in Behavior.xml.</p></td>
<td><p>For more information, see the <a href="http://go.microsoft.com/fwlink/p/?LinkId=241658" data-raw-source="[Microsoft Device Experience Development Kit](http://go.microsoft.com/fwlink/p/?LinkId=241658)">Microsoft Device Experience Development Kit</a>.</p></td>
</tr>
<tr class="odd">
<td><p>[FolderName] folder is missing.</p></td>
<td><p>One of your folders is missing.</p>
<p>For more information, see the <a href="http://go.microsoft.com/fwlink/p/?LinkId=241658" data-raw-source="[Microsoft Device Experience Development Kit](http://go.microsoft.com/fwlink/p/?LinkId=241658)">Microsoft Device Experience Development Kit</a>.</p></td>
</tr>
<tr class="even">
<td><p>[FolderName] folder name is required in &lt;PackageStructure&gt; element in PackageInfo.xml.</p></td>
<td><p>You must include the correct folder name reference in PackageInfo.xml.</p>
<p>For more information, see the <a href="http://go.microsoft.com/fwlink/p/?LinkId=241658" data-raw-source="[Microsoft Device Experience Development Kit](http://go.microsoft.com/fwlink/p/?LinkId=241658)">Microsoft Device Experience Development Kit</a>.</p></td>
</tr>
<tr class="odd">
<td><p>[ImageType] Image – [FileName] size for [SplitType] split is invalid. Valid size(s) are: [ListOfAllowedSizes]</p></td>
<td><p>For more information, see the <a href="http://go.microsoft.com/fwlink/p/?LinkId=241658" data-raw-source="[Microsoft Device Experience Development Kit](http://go.microsoft.com/fwlink/p/?LinkId=241658)">Microsoft Device Experience Development Kit</a>.</p></td>
</tr>
<tr class="even">
<td><p>[ImageType] Image – [FileName] size is invalid. Valid size(s) are: [ListOfAllowedSizes]</p></td>
<td><p>For more information, see the <a href="http://go.microsoft.com/fwlink/p/?LinkId=241658" data-raw-source="[Microsoft Device Experience Development Kit](http://go.microsoft.com/fwlink/p/?LinkId=241658)">Microsoft Device Experience Development Kit</a>.</p></td>
</tr>
<tr class="odd">
<td><p>[TaskGroupName] Guid [TaskGroupGuid] is not referenced for the task [TaskId] in Behavior.xml</p></td>
<td><p>For more information, see the <a href="http://go.microsoft.com/fwlink/p/?LinkId=241658" data-raw-source="[Microsoft Device Experience Development Kit](http://go.microsoft.com/fwlink/p/?LinkId=241658)">Microsoft Device Experience Development Kit</a>.</p></td>
</tr>
<tr class="even">
<td><p>[TaskName] Task – [TaskId] is required for your device within the System Settings category in Behavior.xml.</p></td>
<td><p>The Action Center task and System Settings task must appear under the System Settings category in Device Stage for your device.</p>
<p>For more information, see the <a href="http://go.microsoft.com/fwlink/p/?LinkId=241658" data-raw-source="[Microsoft Device Experience Development Kit](http://go.microsoft.com/fwlink/p/?LinkId=241658)">Microsoft Device Experience Development Kit</a>.</p></td>
</tr>
<tr class="odd">
<td><p>[TaskName] Task – [TaskId] should reference taskGroupGuid [TaskGroupGuid] for your device in Behavior.xml.</p></td>
<td><p>For more information, see the <a href="http://go.microsoft.com/fwlink/p/?LinkId=241658" data-raw-source="[Microsoft Device Experience Development Kit](http://go.microsoft.com/fwlink/p/?LinkId=241658)">Microsoft Device Experience Development Kit</a>.</p></td>
</tr>
<tr class="even">
<td><p>[TaskName] task [TaskId] is required to exist at root for your device in Behavior.xml.</p></td>
<td><p>For more information, see the <a href="http://go.microsoft.com/fwlink/p/?LinkId=241658" data-raw-source="[Microsoft Device Experience Development Kit](http://go.microsoft.com/fwlink/p/?LinkId=241658)">Microsoft Device Experience Development Kit</a>.</p></td>
</tr>
<tr class="odd">
<td><p>\DeviceStage\Device[Locale]\ and \DeviceStage\Device\ folders should have same files.</p></td>
<td><p>If this package is set to be the default locale, the locale directory and the language-neutral directory must have the same files.</p>
<p>For more information, see the <a href="http://go.microsoft.com/fwlink/p/?LinkId=241658" data-raw-source="[Microsoft Device Experience Development Kit](http://go.microsoft.com/fwlink/p/?LinkId=241658)">Microsoft Device Experience Development Kit</a>.</p></td>
</tr>
<tr class="even">
<td><p>A .cab submission needs to contain either Hardware and/or Model information. Please correct the .cab or modify the existing .cabs.</p></td>
<td><p>Your package must contain at least one hardware ID or model ID.</p>
<p>For more information, see the <a href="http://go.microsoft.com/fwlink/p/?LinkId=241658" data-raw-source="[Microsoft Device Experience Development Kit](http://go.microsoft.com/fwlink/p/?LinkId=241658)">Microsoft Device Experience Development Kit</a>.</p></td>
</tr>
<tr class="odd">
<td><p>A Hardware ID in this .cab is in conflict and the .cab cannot be uploaded. Please ensure no other experience you have created uses this Hardware ID.</p></td>
<td><p>Your hardware ID has been used in another one of your experiences. On the dashboard, under <strong>Device metadata</strong>, open the <strong>Manage experiences</strong> page. In the filter, enter the hardware ID to find the other experience. You can then resolve any conflicts.</p>
<p>For more information, see <a href="https://docs.microsoft.com/windows-hardware/drivers/dashboard/device-metadata-business-rules" data-raw-source="[Device Metadata Business Rules](https://docs.microsoft.com/windows-hardware/drivers/dashboard/device-metadata-business-rules)">Device Metadata Business Rules</a>.</p></td>
</tr>
<tr class="even">
<td><p>A Hardware ID in this. cab is in use by another company and the .cab cannot be uploaded. Please verify this Hardware ID.</p></td>
<td><p>The hardware ID you have included in your package is in use by another company. You can&#39;t submit a hardware ID for another company. Make sure that your hardware IDs are not misspelled. If you still receive an error message, email Dashboard Support at sysdev@microsoft.com for a resolution.</p></td>
</tr>
<tr class="odd">
<td><p>A live submission already exists for this locale in this experience.</p></td>
<td><p>Delete the existing live package for the locale before you upload a new package for the same locale.</p></td>
</tr>
<tr class="even">
<td><p>A live submission already exists with default locale set to true in this experience.</p></td>
<td><p>Only one live package in an experience can be set as the default package.</p>
<p>For more information, see <a href="https://docs.microsoft.com/windows-hardware/drivers/dashboard/device-metadata-business-rules" data-raw-source="[Device Metadata Business Rules](https://docs.microsoft.com/windows-hardware/drivers/dashboard/device-metadata-business-rules)">Device Metadata Business Rules</a>.</p></td>
</tr>
<tr class="odd">
<td><p>A logo submission for a MultiPurpose device does not match the submission category.</p></td>
<td><p>The device category listed in your logo submission doesn&#39;t match the primary device category of your device metadata package. To resolve this problem, follow these steps:</p>
<ul>
<li><p>Correct the device category for your logo submission.</p></li>
<li><p>Create a new experience and only bind the correct logo submissions.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>A Model ID in this cab is in conflict and the cab cannot be uploaded. Please ensure no other experience you have created uses this Model ID.</p></td>
<td><p>Your model ID has been used in another one of your experiences. On the dashboard, under <strong>Device metadata</strong>, open the <strong>Manage experiences</strong> page. In the filter, enter the model ID to find the other experience. You can then resolve any conflicts.</p>
<p>For more information, see <a href="https://docs.microsoft.com/windows-hardware/drivers/dashboard/device-metadata-business-rules" data-raw-source="[Device Metadata Business Rules](https://docs.microsoft.com/windows-hardware/drivers/dashboard/device-metadata-business-rules)">Device Metadata Business Rules</a>.</p></td>
</tr>
<tr class="odd">
<td><p>A Model ID in this cab is in use by another company and the cab cannot be uploaded. Please verify this Model ID.</p></td>
<td><p>The model ID you have included in your package is in use by another company. You can&#39;t submit a model ID for another company. Make sure that your model IDs are not misspelled. If you still receive an error message, email Dashboard Support at sysdev@microsoft.com for a resolution.</p></td>
</tr>
<tr class="even">
<td><p>A non-preview live package cannot be promoted to live.</p></td>
<td><p>You can&#39;t promote a live package to Live status.</p></td>
</tr>
<tr class="odd">
<td><p>A package with a status of error cannot be promoted to live.</p></td>
<td><p>You can&#39;t promote a package that contains errors to Live status.</p></td>
</tr>
<tr class="even">
<td><p>A preview submission already exists for this locale in this experience.</p></td>
<td><p>To resolve this problem, try the following:</p>
<ul>
<li><p>Delete the existing preview package for the locale, and then upload a new preview package for the same locale.</p></li>
<li><p>Promote the current preview package for the locale to Release status, and then upload a new preview package for the same locale.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p>A preview submission already exists with default locale set to true in this experience.</p></td>
<td><p>Only one preview package in an experience can be set as the default package.</p>
<p>For more information, see <a href="https://docs.microsoft.com/windows-hardware/drivers/dashboard/device-metadata-business-rules" data-raw-source="[Device Metadata Business Rules](https://docs.microsoft.com/windows-hardware/drivers/dashboard/device-metadata-business-rules)">Device Metadata Business Rules</a>.</p></td>
</tr>
<tr class="even">
<td><p>All device metadata .cab files in an experience must support the same Hardware IDs. Please correct the .cab.</p></td>
<td><p>This package does not have the same list of model IDs that the other packages in the experience have. Correct the model ID list in the package and upload the package again.</p>
<p>For more information, see <a href="https://docs.microsoft.com/windows-hardware/drivers/dashboard/device-metadata-business-rules" data-raw-source="[Device Metadata Business Rules](https://docs.microsoft.com/windows-hardware/drivers/dashboard/device-metadata-business-rules)">Device Metadata Business Rules</a>.</p></td>
</tr>
<tr class="odd">
<td><p>Allowed Domain should not be empty for task [TaskID] in Tasks.xml.</p></td>
<td><p>For more information, see the <a href="http://go.microsoft.com/fwlink/p/?LinkId=241658" data-raw-source="[Microsoft Device Experience Development Kit](http://go.microsoft.com/fwlink/p/?LinkId=241658)">Microsoft Device Experience Development Kit</a>.</p></td>
</tr>
<tr class="even">
<td><p>An unexpected file was found:&#39;[ExtraFile]&#39;. Please ensure you follow the architecture or reference all root files in PackageInfo.xml.</p></td>
<td><p>There are extra files at the root of your package.</p>
<p>For more information, see the <a href="http://go.microsoft.com/fwlink/p/?LinkId=241658" data-raw-source="[Microsoft Device Experience Development Kit](http://go.microsoft.com/fwlink/p/?LinkId=241658)">Microsoft Device Experience Development Kit</a>.</p></td>
</tr>
<tr class="odd">
<td><p>An unexpected folder was found: ‘[ExtraFolder]&#39;. Please ensure you follow the architecture or reference all root folders in PackageInfo.xml.</p></td>
<td><p>For more information, see the <a href="http://go.microsoft.com/fwlink/p/?LinkId=241658" data-raw-source="[Microsoft Device Experience Development Kit](http://go.microsoft.com/fwlink/p/?LinkId=241658)">Microsoft Device Experience Development Kit</a>.</p></td>
</tr>
<tr class="even">
<td><p>CommandLine URL should not be null for task [TaskID] in Tasks.xml.</p></td>
<td><p>For more information, see the <a href="http://go.microsoft.com/fwlink/p/?LinkId=241658" data-raw-source="[Microsoft Device Experience Development Kit](http://go.microsoft.com/fwlink/p/?LinkId=241658)">Microsoft Device Experience Development Kit</a>.</p></td>
</tr>
<tr class="odd">
<td><p>Device Category not found in DeviceInfo.xml .</p></td>
<td><p>You must set a primary device category that is one of the pre-defined options.</p>
<p>For more information, see the <a href="http://go.microsoft.com/fwlink/p/?LinkId=241658" data-raw-source="[Microsoft Device Experience Development Kit](http://go.microsoft.com/fwlink/p/?LinkId=241658)">Microsoft Device Experience Development Kit</a>.</p></td>
</tr>
<tr class="even">
<td><p>Device folder not found in \DeviceStage\ folder</p></td>
<td><p>For more information, see the <a href="http://go.microsoft.com/fwlink/p/?LinkId=241658" data-raw-source="[Microsoft Device Experience Development Kit](http://go.microsoft.com/fwlink/p/?LinkId=241658)">Microsoft Device Experience Development Kit</a>.</p></td>
</tr>
<tr class="odd">
<td><p>Device icon information not found in DeviceInfo.xml</p></td>
<td><p>If you include a device icon in the DeviceInfo.xml file, you must also include the device icon information. Device icons are required for Device Stage packages.</p>
<p>For more information, see the <a href="http://go.microsoft.com/fwlink/p/?LinkId=241658" data-raw-source="[Microsoft Device Experience Development Kit](http://go.microsoft.com/fwlink/p/?LinkId=241658)">Microsoft Device Experience Development Kit</a>.</p></td>
</tr>
<tr class="even">
<td><p>Device Metadata Category for this submission needs to match the existing experience category.</p></td>
<td><p>The category for the device in this package doesn&#39;t match the category in the other packages in this experience. Revise your device category and resubmit the package.</p></td>
</tr>
<tr class="odd">
<td><p>Device Metadata Submission Type for this submission needs to match the existing experience category.</p></td>
<td><p>The device metadata submission type is defined as either Device Stage or Devices and Printers. Only Device Stage packages can be included in a Device Stage experience. Similarly, only Devices and Printers packages can be included in a Devices and Printers experience.</p></td>
</tr>
<tr class="even">
<td><p>Device Stage inbox submissions are not allowed for the computer device class.</p></td>
<td><p>If your package and experience are for Device Stage and a computer device, you must have already certified them for a logo, or you must certify them for a logo within 90 days.</p></td>
</tr>
<tr class="odd">
<td><p>Device Stage is not supported for this device.</p></td>
<td><p>The device category you have chosen is not supported in Device Stage.</p></td>
</tr>
<tr class="even">
<td><p>Device Stage metadata cannot be submitted for your device [DeviceCategory]</p></td>
<td><p>Device Stage submissions are allowed only for the following devices:</p>
<ul>
<li><p>Portable media players</p></li>
<li><p>Digital still cameras</p></li>
<li><p>Cellular phones</p></li>
<li><p>Printers or fax machines</p></li>
<li><p>Scanners</p></li>
<li><p>Computer systems</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p>Device Stage requires either Marketing Bullets or Status Items to be present in Behavior.xml.</p></td>
<td><p>For more information, see the <a href="http://go.microsoft.com/fwlink/p/?LinkId=241658" data-raw-source="[Microsoft Device Experience Development Kit](http://go.microsoft.com/fwlink/p/?LinkId=241658)">Microsoft Device Experience Development Kit</a>.</p></td>
</tr>
<tr class="even">
<td><p>Device Stage requires LaunchDeviceStageFromExplorer to be set to true for your device in WindowsInfo.xml.</p></td>
<td><p>For more information, see the <a href="http://go.microsoft.com/fwlink/p/?LinkId=241658" data-raw-source="[Microsoft Device Experience Development Kit](http://go.microsoft.com/fwlink/p/?LinkId=241658)">Microsoft Device Experience Development Kit</a>.</p></td>
</tr>
<tr class="odd">
<td><p>Device Stage requires LaunchDeviceStageOnDeviceConnect to be set to True for your device in WindowsInfo.xml</p></td>
<td><p>For more information, see the <a href="http://go.microsoft.com/fwlink/p/?LinkId=241658" data-raw-source="[Microsoft Device Experience Development Kit](http://go.microsoft.com/fwlink/p/?LinkId=241658)">Microsoft Device Experience Development Kit</a>.</p></td>
</tr>
<tr class="even">
<td><p>Device Stage requires ShowDeviceInDisconnectedState to be set to True for your device in WindowsInfo.xml.</p></td>
<td><p>For more information, see the <a href="http://go.microsoft.com/fwlink/p/?LinkId=241658" data-raw-source="[Microsoft Device Experience Development Kit](http://go.microsoft.com/fwlink/p/?LinkId=241658)">Microsoft Device Experience Development Kit</a>.</p></td>
</tr>
<tr class="odd">
<td><p>Devices and Printers requires LaunchDeviceStageFromExplorer to be set to False for your device in WindowsInfo.xml.</p></td>
<td><p>For more information, see the <a href="http://go.microsoft.com/fwlink/p/?LinkId=241658" data-raw-source="[Microsoft Device Experience Development Kit](http://go.microsoft.com/fwlink/p/?LinkId=241658)">Microsoft Device Experience Development Kit</a>.</p></td>
</tr>
<tr class="even">
<td><p>Devices and Printers requires LaunchDeviceStageOnDeviceConnect to be set to False for your device in WindowsInfo.xml.</p></td>
<td><p>For more information, see the <a href="http://go.microsoft.com/fwlink/p/?LinkId=241658" data-raw-source="[Microsoft Device Experience Development Kit](http://go.microsoft.com/fwlink/p/?LinkId=241658)">Microsoft Device Experience Development Kit</a>.</p></td>
</tr>
<tr class="odd">
<td><p>Error in xml file [FileName] : [Error]</p></td>
<td><p>The specified .xml file has failed because it contains one or more errors. Verify that the file is compliant with its corresponding schema and that the namespace is correct.</p>
<p>For more information, see the <a href="http://go.microsoft.com/fwlink/p/?LinkId=241658" data-raw-source="[Microsoft Device Experience Development Kit](http://go.microsoft.com/fwlink/p/?LinkId=241658)">Microsoft Device Experience Development Kit</a>.</p></td>
</tr>
<tr class="even">
<td><p>File [FileName] is different in \DeviceStage\Device[Locale]\ and \DeviceStage\Device\ folders.</p></td>
<td><p>If you have set this package as the default locale, the locale directory and the language-neutral directory must contain the same files.</p>
<p>One of the following errors has occurred:</p>
<ul>
<li><p>Files that have the same specified name exist in both directories but the files are different.</p></li>
<li><p>The specified file exists in only one directory.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p>File Name PackageInfo.xml is expected in &lt;PackageStructure&gt; element in PackageInfo.xml.</p></td>
<td><p>Your PackageInfo.xml file isn&#39;t correctly authored for your package. Each root object in the package must be referenced in the PackageInfo.xml file by using a &lt;PackageStructure&gt; node.</p>
<p>For more information, see the <a href="http://go.microsoft.com/fwlink/p/?LinkId=241658" data-raw-source="[Microsoft Device Experience Development Kit](http://go.microsoft.com/fwlink/p/?LinkId=241658)">Microsoft Device Experience Development Kit</a>.</p></td>
</tr>
<tr class="even">
<td><p>Filename [FileReference] is incorrect in &lt;PackageStructure&gt; element in PackageInfo.xml. Correct filename: PackageInfo.xml</p></td>
<td><p>The file name that you referenced by using the &lt;PackageStructure&gt; node in the PackageInfo.xml file is misspelled. Correct the error and resubmit your package.</p>
<p>For more information, see the <a href="http://go.microsoft.com/fwlink/p/?LinkId=241658" data-raw-source="[Microsoft Device Experience Development Kit](http://go.microsoft.com/fwlink/p/?LinkId=241658)">Microsoft Device Experience Development Kit</a>.</p></td>
</tr>
<tr class="odd">
<td><p>For Printing and Scanning Devices, LaunchDeviceStageOnDeviceConnect needs to be set to False in WindowsInfo.xml.</p></td>
<td><p>For more information, see the <a href="http://go.microsoft.com/fwlink/p/?LinkId=241658" data-raw-source="[Microsoft Device Experience Development Kit](http://go.microsoft.com/fwlink/p/?LinkId=241658)">Microsoft Device Experience Development Kit</a>.</p></td>
</tr>
<tr class="even">
<td><p>HardwareIDs in this submission: [list of Hardware ID(s)] are not owned by your company.</p></td>
<td><p>The hardware IDs listed use VIDs that your company does not own according to the respective SIGs. If this is incorrect, email Dashboard Support at sysdev@microsoft.com.</p></td>
</tr>
<tr class="odd">
<td><p>Hardware IDs in this submission: [list of Hardware ID(s)] do not match the expected list of Hardware IDs from SMBIOS.</p></td>
<td><p>The hardware IDs you have submitted are not generated from the SMBIOS information that you submitted together with the SMBIOSFields.xml file.</p>
<p>Try one of the following solutions:</p>
<ul>
<li><p>Regenerate the hardware IDs and include the correct hardware IDs in your package.</p></li>
<li><p>Update the SMBIOSFields.xml file to include the fields that are used to generate the correct hardware IDs.</p></li>
</ul>
<p>For more information, see the <a href="http://go.microsoft.com/fwlink/p/?LinkId=241658" data-raw-source="[Microsoft Device Experience Development Kit](http://go.microsoft.com/fwlink/p/?LinkId=241658)">Microsoft Device Experience Development Kit</a>.</p></td>
</tr>
<tr class="even">
<td><p>Hardware IDs in this submission: [list of Hardware ID(s)] fail the Inbox Driver Distribution Agreement (IDDA) list validation.</p></td>
<td><p>The hardware IDs you have included in your package are not listed in the Inbox Driver Distribution Agreement (IDDA) with Microsoft. Remove these hardware IDs and resubmit.</p></td>
</tr>
<tr class="odd">
<td><p>Invalid scheme [Scheme] in Allowed Domain for task [TaskID] in Tasks.xml</p></td>
<td><p>URLs must begin with HTTP or HTTPs.</p>
<p>For more information, see the <a href="http://go.microsoft.com/fwlink/p/?LinkId=241658" data-raw-source="[Microsoft Device Experience Development Kit](http://go.microsoft.com/fwlink/p/?LinkId=241658)">Microsoft Device Experience Development Kit</a>.</p></td>
</tr>
<tr class="even">
<td><p>Locale not found or is incorrect in PackageInfo.xml</p></td>
<td><p>The locale tag in the PackageInfo.xml file must exist, be formatted correctly, and comply with RFC 4646.</p>
<p>Correct the locale, and then resubmit your package.</p></td>
</tr>
<tr class="odd">
<td><p>Missing resource reference for [Id] in Resource.xml file in \DeviceStage\Task[TaskID][Locale] folder</p></td>
<td><p>For more information, see the <a href="http://go.microsoft.com/fwlink/p/?LinkId=241658" data-raw-source="[Microsoft Device Experience Development Kit](http://go.microsoft.com/fwlink/p/?LinkId=241658)">Microsoft Device Experience Development Kit</a>.</p></td>
</tr>
<tr class="even">
<td><p>Model IDs are not allowed for [Device Class] submissions.</p></td>
<td><p>You can&#39;t use model IDs when you submit device metadata for this type of device class. Instead, use only the hardware IDs for your device. To find the hardware IDs for a computer device, see the <a href="http://go.microsoft.com/fwlink/p/?LinkId=241658" data-raw-source="[Microsoft Device Experience Development Kit](http://go.microsoft.com/fwlink/p/?LinkId=241658)">Microsoft Device Experience Development Kit</a>.</p></td>
</tr>
<tr class="odd">
<td><p>Model Name not found in DeviceInfo.xml</p></td>
<td><p>Your DeviceInfo.xml file isn&#39;t correctly authored.</p>
<p>For more information, see the <a href="http://go.microsoft.com/fwlink/p/?LinkId=241658" data-raw-source="[Microsoft Device Experience Development Kit](http://go.microsoft.com/fwlink/p/?LinkId=241658)">Microsoft Device Experience Development Kit</a>.</p></td>
</tr>
<tr class="even">
<td><p>No preview key can be found for this organization.</p></td>
<td><p>You must set your PreviewKey before you upload a preview package.</p>
<p>For more information, see <a href="https://docs.microsoft.com/windows-hardware/drivers/dashboard/device-metadata-business-rules" data-raw-source="[Device Metadata Business Rules](https://docs.microsoft.com/windows-hardware/drivers/dashboard/device-metadata-business-rules)">Device Metadata Business Rules</a>.</p></td>
</tr>
<tr class="odd">
<td><p>PackageStructure node in PackageInfo.xml is invalid.</p></td>
<td><p>Make sure that your PackageInfo.xml file is correct.</p>
<p>For more information, see the <a href="http://go.microsoft.com/fwlink/p/?LinkId=241658" data-raw-source="[Microsoft Device Experience Development Kit](http://go.microsoft.com/fwlink/p/?LinkId=241658)">Microsoft Device Experience Development Kit</a>.</p></td>
</tr>
<tr class="even">
<td><p>Task [TaskGUID] is required for your device in Behavior.xml.</p></td>
<td><p>For more information, see the <a href="http://go.microsoft.com/fwlink/p/?LinkId=241658" data-raw-source="[Microsoft Device Experience Development Kit](http://go.microsoft.com/fwlink/p/?LinkId=241658)">Microsoft Device Experience Development Kit</a>.</p></td>
</tr>
<tr class="odd">
<td><p>Task [TaskID] should not use taskGroupGuid [TaskGroupGuid]</p></td>
<td><p>For more information, see the <a href="http://go.microsoft.com/fwlink/p/?LinkId=241658" data-raw-source="[Microsoft Device Experience Development Kit](http://go.microsoft.com/fwlink/p/?LinkId=241658)">Microsoft Device Experience Development Kit</a>.</p></td>
</tr>
<tr class="even">
<td><p>TaskGroupGuid [TaskGroupGuid] should not be used by your device for task [TaskId]</p></td>
<td><p>You are trying to use a reserved GUID that doesn&#39;t apply to your device.</p>
<p>Try one of the following solutions:</p>
<ul>
<li><p>Do not use GUIDs for tasks that your device can&#39;t support.</p></li>
<li><p>If you are trying to create a task, generate a new GUID for the task.</p></li>
</ul>
<p>For more information, see the <a href="http://go.microsoft.com/fwlink/p/?LinkId=241658" data-raw-source="[Microsoft Device Experience Development Kit](http://go.microsoft.com/fwlink/p/?LinkId=241658)">Microsoft Device Experience Development Kit</a>.</p></td>
</tr>
<tr class="odd">
<td><p>TaskGroupGuid incorrect for taskId [TaskId] in Behavior.xml</p></td>
<td><p>Correct the task GUID, and then resubmit the package.</p>
<p>For more information, see the <a href="http://go.microsoft.com/fwlink/p/?LinkId=241658" data-raw-source="[Microsoft Device Experience Development Kit](http://go.microsoft.com/fwlink/p/?LinkId=241658)">Microsoft Device Experience Development Kit</a>.</p></td>
</tr>
<tr class="even">
<td><p>The [FileName] icon file in [FolderName] folder is missing image <a href="http://go.microsoft.com/fwlink/p/?LinkId=241658" data-raw-source="[Microsoft Device Experience Development Kit](http://go.microsoft.com/fwlink/p/?LinkId=241658)">MissingImageSize</a>.</p></td>
<td><p>Verify that the image size is present. If not, add the image size to the icon, and then resubmit the package.</p>
<div class="alert">
<strong>Note</strong><br/><p>256x256 image layers must be in the PNG compressed format. BMP format for this size is not allowed. If this size is present but in the BMP format, create the image in a PNG format for the size, add this image to the icon, and then resubmit the package.</p>
</div>
<div>

</div>
<p>For more information, see the <a href="http://go.microsoft.com/fwlink/p/?LinkId=241658" data-raw-source="[Microsoft Device Experience Development Kit](http://go.microsoft.com/fwlink/p/?LinkId=241658)">Microsoft Device Experience Development Kit</a>.</p></td>
</tr>
<tr class="odd">
<td><p>The [FileName] icon file in [FolderName] folder is missing image [MissingImageSize].</p></td>
<td><p>For more information, see the <a href="http://go.microsoft.com/fwlink/p/?LinkId=241658" data-raw-source="[Microsoft Device Experience Development Kit](http://go.microsoft.com/fwlink/p/?LinkId=241658)">Microsoft Device Experience Development Kit</a>.</p></td>
</tr>
<tr class="even">
<td><p>The cab Friendly Name is not unique to the Experience. Please choose another name.</p></td>
<td><p>Create a new friendly name for the experience, and then resubmit it.</p></td>
</tr>
<tr class="odd">
<td><p>The CommandLine argument should point to a valid URL beginning with HTTP or HTTPS for task [TaskID] in Tasks.xml.</p></td>
<td><p>For more information, see the <a href="http://go.microsoft.com/fwlink/p/?LinkId=241658" data-raw-source="[Microsoft Device Experience Development Kit](http://go.microsoft.com/fwlink/p/?LinkId=241658)">Microsoft Device Experience Development Kit</a>.</p></td>
</tr>
<tr class="even">
<td><p>The device category reported in your Device Metadata package and Logo Submission don&#39;t match. If the device category in the package is incorrect, please fix and upload again. If the device category in Logo Submission is incorrect, please fix in Submission Manager and try uploading your package again: [list of links per offending logo submission to SubmissionManager]</p></td>
<td><p>Device categories between bound logo submissions and device metadata must be identical for a submission to pass. Verify that your logo submissions all have the same device category, and that the device category is the same as the device category for your package.</p>
<p>The links provided point to the Submission Manager, which will allow you to change the device category in the logo submission, if the category is incorrect.</p>
<p>After all issues are resolved, resubmit your package.</p></td>
</tr>
<tr class="odd">
<td><p>The Device Metadata Category for this submission does not exist.</p></td>
<td><p>The device metadata category that you have used isn&#39;t valid. You must choose from the pre-defined device metadata categories outlined in the Windows Hardware Certification Kit (HCK).</p></td>
</tr>
<tr class="even">
<td><p>The Experience name already exists for this organization.</p></td>
<td><p>Create a new experience that has a different name.</p></td>
</tr>
<tr class="odd">
<td><p>The provided Logo submissions do not share Hardware IDs or Model IDs with the Device Metadata submission.</p></td>
<td><p>The bound logo submissions must contain the hardware IDs in the device metadata packages in the experience.</p></td>
</tr>
<tr class="even">
<td><p>The reference in PackageInfo.xml, DeviceInformation, was not found in the package.</p></td>
<td><p>The DeviceInformation folder reference is missing from the PackageInfo.xml file.</p>
<p>For more information, see the <a href="http://go.microsoft.com/fwlink/p/?LinkId=241658" data-raw-source="[Microsoft Device Experience Development Kit](http://go.microsoft.com/fwlink/p/?LinkId=241658)">Microsoft Device Experience Development Kit</a>.</p></td>
</tr>
<tr class="odd">
<td><p>The reference in PackageInfo.xml, DeviceStage, was not found in the package.</p></td>
<td><p>The reference in the &lt;PackageStructure&gt; element in the PackageInfo.xml file is either misspelled or isn&#39;t located in the root in the package. Remove the reference, or add the correct file or directory.</p>
<p>For more information, see the <a href="http://go.microsoft.com/fwlink/p/?LinkId=241658" data-raw-source="[Microsoft Device Experience Development Kit](http://go.microsoft.com/fwlink/p/?LinkId=241658)">Microsoft Device Experience Development Kit</a>.</p></td>
</tr>
<tr class="even">
<td><p>The reference in PackageInfo.xml, WindowsInformation, was not found in the package.</p></td>
<td><p>The WindowsInformation folder reference is missing from the PackageInfo.xml file.</p>
<p>For more information, see the <a href="http://go.microsoft.com/fwlink/p/?LinkId=241658" data-raw-source="[Microsoft Device Experience Development Kit](http://go.microsoft.com/fwlink/p/?LinkId=241658)">Microsoft Device Experience Development Kit</a>.</p></td>
</tr>
<tr class="odd">
<td><p>The submission contains [list of Hardware ID(s) and/or Model ID(s)] that are not covered via a logo submission.</p></td>
<td><p>Your package contains hardware IDs or model IDs that your logo submissions don&#39;t cover.</p>
<p>Try one of the following solutions:</p>
<ul>
<li><p>Correct the hardware IDs or model IDs in your device metadata package.</p></li>
<li><p>Create a new experience and bind only the associated logo submissions.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>The system manufacturer for this computer submission does not match the organization of the submitting user.</p></td>
<td><p>The system manufacturer in the SMBIOSFields.xml file you submitted doesn&#39;t match the manufacturer in our records.</p>
<p>Try one of the following solutions:</p>
<ul>
<li><p>Correct the name of the system manufacturer, and then resubmit the package.</p></li>
<li><p>If the system manufacturer field is correct and your file doesn&#39;t pass, email board Support at sysdev@microsoft.com.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p>The TaskID [TaskID] cannot be used with multiple TaskGroups.</p></td>
<td><p>Your Device Stage package contains a TaskID that is used with different TaskGroups. TaskIDs must be unique per TaskGroup and per task.</p>
<p>For more information, see the <a href="http://go.microsoft.com/fwlink/p/?LinkId=241658" data-raw-source="[Microsoft Device Experience Development Kit](http://go.microsoft.com/fwlink/p/?LinkId=241658)">Microsoft Device Experience Development Kit</a>.</p></td>
</tr>
<tr class="even">
<td><p>This preview key has been rejected. Please choose another value.</p></td>
<td><p>The PreviewKey you set by using the Dashboard isn&#39;t accepted. Submit a new PreviewKey.</p></td>
</tr>
<tr class="odd">
<td><p>Unexpected file found in [FolderName] folder- [ExtraFile]</p></td>
<td><p>There is an issue with your package structure.</p>
<p>For more information, see the <a href="http://go.microsoft.com/fwlink/p/?LinkId=241658" data-raw-source="[Microsoft Device Experience Development Kit](http://go.microsoft.com/fwlink/p/?LinkId=241658)">Microsoft Device Experience Development Kit</a>.</p></td>
</tr>
<tr class="even">
<td><p>Unexpected file found in [Path] folder – [ExtraFile]</p></td>
<td><p>There is an issue with your package structure.</p>
<p>For more information, see the <a href="http://go.microsoft.com/fwlink/p/?LinkId=241658" data-raw-source="[Microsoft Device Experience Development Kit](http://go.microsoft.com/fwlink/p/?LinkId=241658)">Microsoft Device Experience Development Kit</a>.</p></td>
</tr>
<tr class="odd">
<td><p>Unexpected file found in the [locale] subfolder of task [TaskGroupGuid] folder – [FileName]</p></td>
<td><p>Remove the specified file, and then resubmit the package.</p>
<p>For more information, see the <a href="http://go.microsoft.com/fwlink/p/?LinkId=241658" data-raw-source="[Microsoft Device Experience Development Kit](http://go.microsoft.com/fwlink/p/?LinkId=241658)">Microsoft Device Experience Development Kit</a>.</p></td>
</tr>
<tr class="even">
<td><p>Unexpected folder found in [FolderName] folder- [ExtraFolder]</p></td>
<td><p>There is an issue with your package structure.</p>
<div class="alert">
<strong>Note</strong><br/><p>This error may occur if the device category in the DeviceInfo.xml file isn&#39;t set correctly.</p>
</div>
<div>

</div>
<p>For more information, see the <a href="http://go.microsoft.com/fwlink/p/?LinkId=241658" data-raw-source="[Microsoft Device Experience Development Kit](http://go.microsoft.com/fwlink/p/?LinkId=241658)">Microsoft Device Experience Development Kit</a>.</p></td>
</tr>
<tr class="odd">
<td><p>Unexpected folder found in [Path] folder – [ExtraFolder]</p></td>
<td><p>There is an issue with your package structure.</p>
<p>For more information, see the <a href="http://go.microsoft.com/fwlink/p/?LinkId=241658" data-raw-source="[Microsoft Device Experience Development Kit](http://go.microsoft.com/fwlink/p/?LinkId=241658)">Microsoft Device Experience Development Kit</a>.</p></td>
</tr>
<tr class="even">
<td><p>URL should not be a localhost for task [TaskID] in Tasks.xml.</p></td>
<td><p>For more information, see the <a href="http://go.microsoft.com/fwlink/p/?LinkId=241658" data-raw-source="[Microsoft Device Experience Development Kit](http://go.microsoft.com/fwlink/p/?LinkId=241658)">Microsoft Device Experience Development Kit</a>.</p></td>
</tr>
<tr class="odd">
<td><p>URL specified in the commandLine is not valid for task [TaskID] in Tasks.xml.</p></td>
<td><p>For more information, see the <a href="http://go.microsoft.com/fwlink/p/?LinkId=241658" data-raw-source="[Microsoft Device Experience Development Kit](http://go.microsoft.com/fwlink/p/?LinkId=241658)">Microsoft Device Experience Development Kit</a>.</p></td>
</tr>
<tr class="even">
<td><p>Valid logo submission(s) are needed for [SubmissionType] metadata for [DeviceClass]</p></td>
<td><p>Digital still cameras and portable media players must have one or more Windows 7 or Windows Vista® logo submissions.</p>
<p>Cellular phones must have one or more Windows 7 logo submissions.</p></td>
</tr>
<tr class="odd">
<td><p>You already have a preview submission for this Operating System Version. Remove the current Live submission.</p></td>
<td><p>You are trying to promote a preview package for a locale, but there is already a released package for that locale.</p>
<p>If you want to promote this preview package, delete the released package first, and then try again.</p></td>
</tr>
<tr class="even">
<td><p>You do not have access to this experience.</p></td>
<td><p>You are trying to gain access to an experience that doesn&#39;t belong to your company.</p></td>
</tr>
<tr class="odd">
<td><p>Your device cannot have the command value set to HostedSiteWithDevice for task [TaskID] in Tasks.xml.</p></td>
<td><p>For more information, see the <a href="http://go.microsoft.com/fwlink/p/?LinkId=241658" data-raw-source="[Microsoft Device Experience Development Kit](http://go.microsoft.com/fwlink/p/?LinkId=241658)">Microsoft Device Experience Development Kit</a>.</p></td>
</tr>
<tr class="even">
<td><p>Your submission is blocked due to a Dashboard error. Please email Dashboard Support at sysdev@microsoft.com for a resolution.</p></td>
<td><p>Email Dashboard Support at sysdev@microsoft.com.</p></td>
</tr>
</tbody>
</table>



## <span id="related_topics"></span>Related topics


[Create a Device Metadata Experience](https://docs.microsoft.com/windows-hardware/drivers/dashboard/create-a-device-metadata-experience)

[Submit a Device Metadata Package (Dashboard help)](https://docs.microsoft.com/windows-hardware/drivers/dashboard/submit-a-device-metadata-package--dashboard-help-)

[Device Metadata Business Rules](https://docs.microsoft.com/windows-hardware/drivers/dashboard/device-metadata-business-rules)










