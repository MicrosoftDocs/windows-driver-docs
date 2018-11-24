---
title: WMI Class Qualifiers
description: WMI Class Qualifiers
ms.assetid: 62a00184-59b7-496d-b523-f4adb879d402
keywords: ["class qualifiers WDK WMI", "MOF class qualifiers WDK WMI", "embedded classes WDK WMI", "dynamic MOF qualifiers WDK WMI", "static MOF qualifiers WDK WMI", "classes WDK WMI", "WMI WDK kernel , classes"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# WMI Class Qualifiers





The following table lists the required and optional MOF class qualifiers that can be used to describe a driver's WMI data blocks and event blocks.

An *embedded class*, which is a class used solely as a data item in another class and not exposed as a WMI data block, requires only the **WMI** and **Guid** qualifiers. The other qualifiers are irrelevant to embedded classes and are ignored. For more information about embedded classes, see [Driver-defined WMI Data Items](driver-defined-wmi-data-items.md).

**Dynamic** and **Static** are standard MOF qualifiers. For information about other standard MOF qualifiers, see the Microsoft Windows SDK.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Qualifier</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>Dynamic</strong></p></td>
<td><p>Indicates that the data provider supplies instances of the data block at run time, rather than providing instances of static data in the MOF file. All data and event blocks that a driver registers with WMI must be defined with the <strong>Dynamic</strong> qualifier.</p></td>
</tr>
<tr class="even">
<td><p><strong>Static</strong></p></td>
<td><p>Indicates that the data provider supplies instances of static data in the MOF file, rather than supplying instances of the data block at run time. A driver does not register static data blocks with WMI, because the static data resides in the WMI database. Classes marked as <strong>Static</strong> in the MOF file should not be registered by the driver&#39;s <a href="https://msdn.microsoft.com/library/windows/hardware/ff551731" data-raw-source="[&lt;strong&gt;IRP_MN_REGINFO&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551731)"><strong>IRP_MN_REGINFO</strong></a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff551734" data-raw-source="[&lt;strong&gt;IRP_MN_REGINFO_EX&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551734)"><strong>IRP_MN_REGINFO_EX</strong></a> handlers.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Provider(&quot;WMIProv&quot;)</strong></p></td>
<td><p>(Required) Indicates that the provider of the class is a WMI provider.</p></td>
</tr>
<tr class="even">
<td><p><strong>WMI</strong></p></td>
<td><p>(Required) Indicates that the class is a WMI class.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Description(&quot;</strong><em>description-string</em><strong>&quot;)</strong></p></td>
<td><p>(Optional) Specifies a description of the block for the locale specified by the <strong>Locale</strong> qualifier. If defined, WMI clients can display the description string to users. A driver writer can use <strong>Description</strong> to document a class.</p></td>
</tr>
<tr class="even">
<td><p><strong>Guid(&quot;</strong><em>guid-string</em><strong>&quot;)</strong></p></td>
<td><p>(Required) Specifies the GUID, in string format, that uniquely identifies the block to WMI. A driver writer should generate a GUID for each data block in the driver&#39;s MOF file, using either guidgen.exe or uuidgen.exe (which are included in the Windows SDK). A driver passes this value in GUID format to WMI when the driver registers its blocks. WMI then uses the GUID to look up the block&#39;s definition in the driver&#39;s MOF resource.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Locale(&quot;MS&lt;/strong&gt;<em>locale-identifier</em><strong>&quot;)</strong></p></td>
<td><p>(Optional) Specifies the language identifier and locale for the string specified by <strong>Description</strong>. For example, a <em>locale-identifier</em> of 0x409 specifies American English. A single MOF file can contain blocks with different locales, but typically all of the blocks in a MOF file have the same locale.</p></td>
</tr>
<tr class="even">
<td><p><strong>WmiExpense(</strong><em>expense-value</em><strong>)</strong></p></td>
<td><p>(Optional) Specifies the average number of CPU cycles needed to collect data for the data block. For example, a WMI client might check a data block&#39;s <strong>WmiExpense</strong> value to determine how often to query for its data. If <strong>WmiExpense</strong> is omitted, <em>expense-value</em> is assumed to be 0. <strong>WmiExpense</strong> is unrelated to registering a data block as expensive to collect.</p></td>
</tr>
</tbody>
</table>

 

 

 




