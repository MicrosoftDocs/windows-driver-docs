---
title: Windows Driver Model (WDM)
description: This section describes the Windows Driver Model (WDM), and discusses types of WDM drivers, device configuration, driver layering, and WDM versioning.
ms.assetid: 9e76c5a8-a19a-44cf-867a-b2246ea8eaf1
keywords: ["kernel-mode drivers WDK , WDM drivers"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Windows Driver Model (WDM)


This section describes the *Windows Driver Model* (WDM), and discusses types of WDM drivers, device configuration, driver layering, and WDM versioning. WDM simplifies the design of kernel-mode drivers that are written to run on multiple versions of the Windows operating system.




## In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Topic</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="introduction-to-wdm.md" data-raw-source="[Introduction to WDM](introduction-to-wdm.md)">Introduction to WDM</a></p></td>
<td><p>To allow driver developers to write device drivers that are source-code compatible across all Microsoft Windows operating systems, the <em>Windows Driver Model</em> (WDM) was introduced. Kernel-mode drivers that follow WDM rules are called <em>WDM drivers</em>.</p></td>
</tr>
<tr class="even">
<td><p><a href="types-of-wdm-drivers.md" data-raw-source="[Types of WDM Drivers](types-of-wdm-drivers.md)">Types of WDM Drivers</a></p></td>
<td><p>There are three kinds of WDM drivers: bus drivers, function drivers, and filter drivers.</p></td>
</tr>
<tr class="odd">
<td><p><a href="device-configurations-and-layered-drivers.md" data-raw-source="[Device Configurations and Layered Drivers](device-configurations-and-layered-drivers.md)">Device Configurations and Layered Drivers</a></p></td>
<td><p>For the most common kinds of devices, the Windows Driver Kit (WDK) supplies a sample set of fully functional system drivers. Individual sample drivers can be used as models when developing new drivers for similar kinds of devices. However, the system&#39;s drivers had an additional design requirement: to make it easy to develop new device drivers. Consequently, many of the system&#39;s drivers have a layered architecture so that certain drivers can be reused to support new drivers for similar devices.</p></td>
</tr>
<tr class="even">
<td><p><a href="wdm-versions.md" data-raw-source="[WDM Versions](wdm-versions.md)">WDM Versions</a></p></td>
<td><p>Later versions of WDM generally support all the features available in earlier versions of WDM; that is, each new version of WDM is a superset of the previous WDM version. When possible, a cross-system driver should conform to the lowest WDM version on any operating system.</p></td>
</tr>
</tbody>
</table>

 

 

 




