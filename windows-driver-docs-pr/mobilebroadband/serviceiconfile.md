---
title: ServiceIconFile
description: ServiceIconFile
ms.date: 04/20/2017
---

# ServiceIconFile

[!include[MBAE deprecation warning](../includes/mbae-deprecation-warning.md)]

> [!IMPORTANT]
> In Windows 10, version 1709 and later, this field has been replaced by branding through COSA. Fields in COSA for branding are described on [Planning your desktop COSA database submission](planning-your-desktop-cosa-database-submission.md). If you are targeting versions of Windows before Windows 10, Version 1709, you will still create a metadata package as described in this section. For more information about COSA, see [COSA overview](cosa-overview.md). 

The ServiceIconFile element specifies the name of the service icon file in the service metadata package. The service icon file is used to display the logo of the mobile network operator (MNO) or mobile virtual network operator (MVNO) in Windows Connection Manager.

## Usage


``` syntax
<ServiceProvider>
  text
</ServiceProvider>
```

## Attributes


There are no attributes.

## Text value


The name of an icon file with an .ICO extension.

## Child elements


There are no child elements.

## Parent elements


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Element</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="serviceinfo.md" data-raw-source="[ServiceInfo](serviceinfo.md)">ServiceInfo</a></p></td>
<td><p>The <a href="serviceinfo.md" data-raw-source="[ServiceInfo](serviceinfo.md)">ServiceInfo</a> element is the parent element of the <a href="serviceinfo-xml-schema.md" data-raw-source="[ServiceInfo XML schema](serviceinfo-xml-schema.md)">ServiceInfo XML schema</a>.</p></td>
</tr>
</tbody>
</table>

 

## XSD


``` syntax
<xs:element name="ServiceIconFile" type="tns:ServiceIconFileType" minOccurs="0"/>

<xs:simpleType name="ServiceIconFileType">
  <xs:restriction base="xs:string">
    <xs:pattern value=".+\.ico"/>
  </xs:restriction>
</xs:simpleType>
```

## Remarks


The required icon file sizes are as follows:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>256x256:32bit+Alpha(compressed)</p></td>
<td><p>24x24:32bit+Alpha</p></td>
</tr>
<tr class="even">
<td><p>48x48:32bit+Alpha</p></td>
<td><p>24x24:8bit256</p></td>
</tr>
<tr class="odd">
<td><p>48x48:8bit256</p></td>
<td><p>24x24:4bit16</p></td>
</tr>
<tr class="even">
<td><p>48x48:4bit16</p></td>
<td><p>16x16:32bit+Alpha</p></td>
</tr>
<tr class="odd">
<td><p>32x32:32bit+Alpha</p></td>
<td><p>16x16:8bit256</p></td>
</tr>
<tr class="even">
<td><p>32x32:8bit256</p></td>
<td><p>16x16:4bit16</p></td>
</tr>
<tr class="odd">
<td><p>32x32:4bit16</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

 

The ServiceIconFile element is marked as optional in the schema. However, service metadata packages that are submitted to the Windows Dev Center Dashboard without the ServiceIconFile element will be rejected.

 

 





