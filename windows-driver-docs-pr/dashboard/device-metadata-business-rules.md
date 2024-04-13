---
title: Device Metadata Business Rules
description: Device Metadata Business Rules
ms.topic: article
ms.date: 04/20/2017
---

# Device Metadata Business Rules

When you submit device metadata packages through the Dashboard, you should ensure that:

- Packages are downloaded for the correct device.

- The right package is clearly identified by the associated hardware IDs and model IDs and no conflict exists.

- Preview packages are not downloaded as released packages.

## General rules for submitting device metadata

The following general rules apply when you submit a package through the Dashboard.

- All packages must be free from malicious software.
- Each of your device metadata packages must be signed with your company's Microsoft Authenticode certificate.
- The name of each experience that your company has created must be unique in your company.
- The friendly name of a package must be unique in the experience that contains the package.
- The original file name for a package must be unique.
- All hardware IDs in all packages must be unique. A hardware ID can't match a hardware ID in another experience created by your company or by another company.
- All model IDs in all packages must be unique. A model ID can't match a model ID in another experience created by your company or by another company.
- A link to any valid logo submission for a device must be included in the device metadata submission. Each of those valid logo submissions must include the primary device category that is listed in the device metadata submission.
- To update a package in an existing experience, you must first delete the existing package, create a new package, and then upload the new package to the existing experience.
- A package can contain no more than 1,000 IDs. This includes hardware IDs and model IDs.

### Device metadata types

Different types of device metadata packages must follow different rules. Additionally, different device categories within Device Stage metadata must follow specific rules.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Metadata type</th>
<th>Applies to</th>
<th>Requirements</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Devices and Printers Folder</p></td>
<td><ul>
<li><p>All devices</p></li>
<li><p>Devices that have a UWP device app</p></li>
<li><p>Devices that have a privileged app</p></li>
</ul></td>
<td><p>The device must either use only in-box drivers that do not have an associated Windows® logo submission, or custom drivers that have Windows logo submissions that are bound to the device experience.</p></td>
</tr>
<tr class="even">
<td><p>Device Stage</p></td>
<td><ul>
<li><p>Digital still cameras</p>
<ul>
<li><p>Imaging.Camera</p></li>
</ul></li>
<li><p>Portable media players</p>
<p>Multimedia.PMP</p></li>
<li><p>Cellular phones</p>
<ul>
<li><p>Communication.Phone.Cell</p></li>
</ul></li>
<li><p>Printers, fax machines, and scanners</p>
<ul>
<li><p>PrintFax</p></li>
<li><p>PrintFax.Fax</p></li>
<li><p>PrintFax.MFP</p></li>
<li><p>PrintFax.Printer</p></li>
<li><p>PrintFax.Printer.Inkjet</p></li>
<li><p>PrintFax.Printer.Laser</p></li>
<li><p>PrintFax.Printer.3D</p></li>
<li><p>Imaging.Scanner</p></li>
</ul></li>
<li><p>Computer</p>
<ul>
<li><p>Computer.AllInOne</p></li>
<li><p>Computer.Desktop</p></li>
<li><p>Computer.Desktop.LowProfile</p></li>
<li><p>Computer.Desktop.Pizzabox</p></li>
<li><p>Computer.Laptop</p></li>
<li><p>Computer.Lunchbox</p></li>
<li><p>Computer.Netbook</p></li>
<li><p>Computer.Notebook</p></li>
<li><p>Computer.Notebook.Sub</p></li>
<li><p>Computer.Portable</p></li>
<li><p>Computer.Rackmount</p></li>
<li><p>Computer.Sealed</p></li>
<li><p>Computer.Server</p></li>
<li><p>Computer.SpaceSaving</p></li>
<li><p>Computer.Tablet</p></li>
<li><p>Computer.ThinClient</p></li>
<li><p>Computer.Tower</p></li>
<li><p>Computer.Tower.Mini</p></li>
</ul></li>
<li><p>Keyboards and mice</p>
<ul>
<li><p>Input.Keyboard</p></li>
<li><p>Input.Mouse</p></li>
<li><p>Input.Trackball</p></li>
</ul></li>
<li><p>Smartcards</p>
<ul>
<li><p>PersonalIdentity.Smartcard</p></li>
<li><p>Media.Smartcard</p></li>
</ul></li>
<li><p>Mobile broadband devices</p>
<ul>
<li><p>Network.MobileBroadband</p></li>
</ul></li>
<li><p>Webcams</p>
<ul>
<li><p>Imaging.Webcam</p></li>
</ul></li>
<li><p>Generic portables</p>
<ul>
<li><p>Other.Portable</p></li>
</ul></li>
</ul></td>
<td><p>Each device must have a Windows logo submission.</p></td>
</tr>
</tbody>
</table>

### Experience rules

- All the device metadata packages in a single experience must support the same hardware IDs and model IDs.

- In an experience, when you combine a specific locale, preview status, and Windows operating system in a package, the combination must be unique in every package in the experience. For example, in your experience, for Locale A, you can include one released package and preview package for each Windows operating system. That same experience may not include any other release or preview packages for Locale A and for that Windows operating system.

- In an experience, you can only have one default preview locale package and one default released package for each Windows operating system version.

### Unique Device Stage Metadata Submissions

To submit a PC metadata package, see, [Submit a PC device manifest package](./index.yml).

To submit a mobile broadband metadata package, see [Submit a mobile broadband device manifest package](submit-a-mobile-broadband-device-manifest-package.md).

To submit a multiple-locale metadata package, see [Submit a Multiple-locale device manifest package](submit-a-multiple-locale-device-manifest-package.md).

### UWP device app limits

Device manufacturers are limited in the number of UWP apps that may be specified in device metadata for automatic installation and app privilege. For example, peripheral device manufacturers (IHVs) can submit up to one app that is configured for automatic installation and up to one app that is specified as a privileged app. An IHV can submit one app that meets both limitations or two apps, with each meeting just one of the limitations.

>[!IMPORTANT]
>There is no limit to the total number of UWP device apps that a device manufacturer can submit to the Microsoft Store; these limits apply only to a single device metadata package.

Mobile operators and OEMs have different limits on the number of apps that they can specify in device metadata. For more info, OEMs should contact their Microsoft OEM representative.

In each device metadata package, the following limits apply:

|Developer|Automatic installation app limit|Privileged app limit|
|----|----|----|
|IHV|1|1|
|Mobile operator|1|8|
|OEM|contact Microsoft|contact Microsoft|

## Related topics

- [Create a Device Metadata Experience](create-a-device-metadata-experience.md)

- [Manage Device Metadata Experiences](manage-device-metadata-experiences.md)

- [Submit a Device Metadata Package (Dashboard help)](submit-a-device-metadata-package--dashboard-help-.md)
