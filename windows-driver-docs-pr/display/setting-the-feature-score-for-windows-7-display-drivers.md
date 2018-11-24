---
title: Setting the Feature Score for Windows 7 Display Drivers
description: Setting the Feature Score for Windows 7 Display Drivers
ms.assetid: 7b2cf25d-a88d-48e1-8d62-8c245c289566
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Setting the Feature Score for Windows 7 Display Drivers


This section applies only to Windows 7 and later, and Windows Server 2008 R2 and later versions of Windows operating system.

The **FeatureScore** directive is required for all drivers that install and run on Windows Vista and later operating systems. The feature score settings that apply for Windows Vista are described in [Setting the Driver Feature Score](setting-the-driver-feature-score.md). The following table shows the feature score settings that apply for Windows 7 and later.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Feature
<div>
 
</div>
score</th>
<th align="left">Driver Model and Distribution Method</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>E6</p></td>
<td align="left"><p>Vendor-supplied drivers that are written to the Windows Display Driver Model (WDDM) are optimized for the model&#39;s Windows 7 features, are packaged in a Windows 7 driver package that is qualified by the Windows Hardware Quality Labs (WHQL), and are included in the Windows <a href="http://go.microsoft.com/fwlink/p/?linkid=138031" data-raw-source="[Compatibility Center](http://go.microsoft.com/fwlink/p/?linkid=138031)">Compatibility Center</a> tested products list</p></td>
</tr>
<tr class="even">
<td align="left"><p>E6</p></td>
<td align="left"><p>Vendor-supplied drivers that are written to the WDDM are optimized for the model&#39;s Windows 7 features, and are packaged with a unified Windows 7 and Windows Vista driver package that is certified by using the Windows Hardware Certification Kit</p></td>
</tr>
<tr class="odd">
<td align="left"><p>EC</p></td>
<td align="left"><p>In-box drivers that are written to WDDM are optimized for the model&#39;s Windows 7 features, and are packaged with a Windows 7 driver package</p></td>
</tr>
<tr class="even">
<td align="left"><p>F4</p></td>
<td align="left"><p>Vendor-supplied drivers that are written to WDDM with a unified Windows 7 and Windows Vista driver package, with certification of the package by using the Windows Hardware Certification Kit</p></td>
</tr>
<tr class="odd">
<td align="left"><p>F4</p></td>
<td align="left"><p>In-box drivers that are written to WDDM with a Windows 7 driver package</p></td>
</tr>
<tr class="even">
<td align="left"><p>F6</p></td>
<td align="left"><p>Vendor-supplied drivers that are written to WDDM with a Windows Vista driver package that is qualified by WHQL and included in the Windows <a href="http://go.microsoft.com/fwlink/p/?linkid=138031" data-raw-source="[Vista Compatibility Center](http://go.microsoft.com/fwlink/p/?linkid=138031)">Vista Compatibility Center</a> tested products list</p></td>
</tr>
<tr class="odd">
<td align="left"><p>F8</p></td>
<td align="left"><p>In-box drivers that are written to WDDM with a Windows Vista driver package</p></td>
</tr>
<tr class="even">
<td align="left"><p>FC</p></td>
<td align="left"><p>Vendor-supplied drivers that are written to the <a href="windows-2000-display-driver-model-design-guide.md" data-raw-source="[Windows 2000 display driver model](windows-2000-display-driver-model-design-guide.md)">Windows 2000 display driver model</a></p></td>
</tr>
<tr class="odd">
<td align="left"><p>FD</p></td>
<td align="left"><p>In-box drivers in Windows Vista that are written to the <a href="windows-2000-display-driver-model-design-guide.md" data-raw-source="[Windows 2000 display driver model](windows-2000-display-driver-model-design-guide.md)">Windows 2000 display driver model</a></p></td>
</tr>
<tr class="even">
<td align="left"><p>FE</p></td>
<td align="left"><p>Video graphics array (VGA) drivers</p></td>
</tr>
</tbody>
</table>

 

For drivers written to WDDM, graphics hardware vendors must place the **FeatureScore** directive under the [**DDInstall section**](https://msdn.microsoft.com/library/windows/hardware/ff547344) of their INF file and use **FeatureScore** to apply the feature score to the drivers.

For [Windows 2000 Display Driver Model](windows-2000-display-driver-model-design-guide.md) drivers, Microsoft applies the appropriate feature score through the class installer at the time of driver installation, or in the INF for in-box Windows 2000 Display Driver Model drivers. Vendors must not use the **FeatureScore** directive to insert a feature score for drivers written to the Windows 2000 Display Driver Model.

An unsigned driver receives a feature score that is equal to FF. This value is the default and indicates no score.

 

 





