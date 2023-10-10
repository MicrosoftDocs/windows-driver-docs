---
title: ServiceProvider
description: ServiceProvider
ms.date: 04/20/2017
---

# ServiceProvider

[!include[MBAE deprecation warning](../includes/mbae-deprecation-warning.md)]

> [!IMPORTANT]
> In Windows 10, version 1709 and later, this field has been replaced by branding through COSA. Fields in COSA for branding are described on [Planning your desktop COSA database submission](planning-your-desktop-cosa-database-submission.md). If you are targeting versions of Windows before Windows 10, version 1709, you will still create a metadata package as described in this section. For more information about COSA, see [COSA overview](cosa-overview.md). 

The ServiceProvider element specifies the name of the service provider. It is shown in Windows Connection Manager to display the home provider network name. If the user is on a roaming network the roaming network name is displayed instead.

## Usage


``` syntax
<ServiceProvider>
  text
</ServiceProvider>
```

## Attributes


There are no attributes.

## Text value


A string of up to 20 printable characters.

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
<xs:element name="ServiceProvider" type="tns:ProviderNameType"/>

<xs:simpleType name="ProviderNameType">
  <xs:restriction base="xs:string">
    <xs:minLength value="1" />
    <xs:maxLength value="20" />
  </xs:restriction>
</xs:simpleType>
```

## Remarks


The ServiceProvider element is not shown in Windows Connection Manager when the user is roaming.

The ServiceProvider element is required.

 

 





