---
title: How to limit or expand a driver’s distribution based on Windows version
description: Creating a floor or ceiling for a driver submission in order to change its distribution.
ms.topic: article 
ms.date: 10/02/2018
ms.localizationpriority: medium
---

# How to limit or expand a driver’s distribution based on Windows version

Partners may sometimes need to expand or limit the OS distribution of a driver submission.  This topic describes each of the associated shipping label features for this and how to use them.

Before you begin working with these features, you should be familiar with a few key terms and definitions.

**Windows Update**: When you publish a driver to RS1 (Windows 10, version 1607), Windows Update will also offered the driver to devices running RS1, RS2, RS3, [Windows 10, versions 1607, 1703, 1709] and so on.  But it would not be offered to TH1 or TH2 (Windows 10, version 1507 or 1511). In other words, drivers are always *offered forward*.
This is especially important to remember when dealing with the OS and Hardware ID combinations within the PNP Grid. In practice, the offering drivers forward means that for the previous example, you need not publish the same Hardware ID to both RS4 and RS5. Windows Update will offer your RS4 posting to RS5 and later versions. You only need to publish the RS4 items in the PNP grid.

**Windows Dynamic Updates and OS Floors**:  You use Windows Upgrade and Dynamic Update to deploy to a new version of Windows, so it overrides the OS version information reported by the client and sets it to the target feature update version. For instance, if the client is on 10.0.17763 (Windows 10, version 1809) and upgrading to 10.0.18362 (Windows 10, version 1903), Dynamic Update will offer drivers from within the 18362 OS boundary. This is especially important to understand when dealing with the Floor feature. For more info see [Understanding Windows Update Automatic and Optional Rules for Driver Distribution](understanding-windows-update-automatic-and-optional-rules-for-driver-distribution.md).

**Submission Owner**:  The original submitter of the HLKx or .CAB driver package is granted the capability to use the Driver Expansion feature.  Customers with a Shared submission must work with their submission owner.

**Required Permissions**:  Only users designated as Administrators, Shipping Label Owners, and Shipping Label Promoters can set floors and ceilings for driver submissions.  Only Co-Engineering partners have access to the Ceiling and Build Number based features.

**Floor and Ceiling types**: There are two types of floors and ceilings supported by the Driver Dashboard:

<table>
  <thead>
    <tr>
      <th>Floor/ceiling type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>OS release-based</td>
        <td>
        <ul>
            <li>The choices are limited to TH, RS1, RS2, etc.</li>
            <li>Meant for drivers released to the public.</li></ul>
        </td>
    </tr>
    <tr>
      <td>Build number-based</td>
      <td>
        <ul>
            <li><em>Available for Microsoft co-engineering partners only.</em></li>
            <li>The choices are limited to a five-digit build number that is higher than the latest released Windows version.</li>
            <li>Used when developing drivers for unreleased versions of Windows.</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

## Setting an OS Floor

* *A floor is implicitly and automatically set when you select a Hardware ID and OS combination from the PnP grid.* This means, the lowest OS you select from the PnP grid will be the implied floor.  
* The minimum allowable OS Floor is initially determined by the submissions lowest Certified OS level, or the Attested OS level.  If you need to set an OS Floor that is below these automatically determined levels then you must perform a Driver Expansion prior to setting the OS Floor.

The OS Floor describes the earliest Windows version that the driver could be distributed to.  Use this feature when you want to move the implied floor **UP** so that the driver will only be offered at and above the selected operating system.
The most common use case is described in the Driver Expansion section, Use Case 2.  
### To set the OS Floor:

1. Create a shipping label and enter your details.  For more information, see [Publish a driver to Windows Update](publish-a-driver-to-windows-update.md).
2. In the **Select PNPs** grid area, select *at least one* Hardware ID and operating system combination, and then click **Publish**.
3. Scroll down to the **Restrict operating systems for driver distribution** section, and check **I want to restrict OS for driver distribution**.
4. From the **Select Min OS Version (Floor)** drop down, pick the earliest OS version to distribute the driver to.
 
![Dropdown menu listing OS versions](images/Restrict_Floor.PNG)

