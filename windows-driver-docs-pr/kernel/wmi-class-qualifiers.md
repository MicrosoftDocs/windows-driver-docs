---
title: WMI Class Qualifiers
author: windows-driver-content
description: WMI Class Qualifiers
MS-HAID:
- 'WMI\_3dcc0f82-29e3-4479-9fae-cf56c025f7ab.xml'
- 'kernel.wmi\_class\_qualifiers'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 62a00184-59b7-496d-b523-f4adb879d402
keywords: ["class qualifiers WDK WMI", "MOF class qualifiers WDK WMI", "embedded classes WDK WMI", "dynamic MOF qualifiers WDK WMI", "static MOF qualifiers WDK WMI", "classes WDK WMI", "WMI WDK kernel , classes"]
---

# WMI Class Qualifiers


## <a href="" id="ddk-wmi-class-qualifiers-kg"></a>


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
<td><p>Indicates that the data provider supplies instances of static data in the MOF file, rather than supplying instances of the data block at run time. A driver does not register static data blocks with WMI, because the static data resides in the WMI database. Classes marked as <strong>Static</strong> in the MOF file should not be registered by the driver's [<strong>IRP_MN_REGINFO</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551731) or [<strong>IRP_MN_REGINFO_EX</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551734) handlers.</p></td>
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
<td><p>(Required) Specifies the GUID, in string format, that uniquely identifies the block to WMI. A driver writer should generate a GUID for each data block in the driver's MOF file, using either guidgen.exe or uuidgen.exe (which are included in the Windows SDK). A driver passes this value in GUID format to WMI when the driver registers its blocks. WMI then uses the GUID to look up the block's definition in the driver's MOF resource.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Locale(&quot;MS\\</strong><em>locale-identifier</em><strong>&quot;)</strong></p></td>
<td><p>(Optional) Specifies the language identifier and locale for the string specified by <strong>Description</strong>. For example, a <em>locale-identifier</em> of 0x409 specifies American English. A single MOF file can contain blocks with different locales, but typically all of the blocks in a MOF file have the same locale.</p></td>
</tr>
<tr class="even">
<td><p><strong>WmiExpense(</strong><em>expense-value</em><strong>)</strong></p></td>
<td><p>(Optional) Specifies the average number of CPU cycles needed to collect data for the data block. For example, a WMI client might check a data block's <strong>WmiExpense</strong> value to determine how often to query for its data. If <strong>WmiExpense</strong> is omitted, <em>expense-value</em> is assumed to be 0. <strong>WmiExpense</strong> is unrelated to registering a data block as expensive to collect.</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20WMI%20Class%20Qualifiers%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


