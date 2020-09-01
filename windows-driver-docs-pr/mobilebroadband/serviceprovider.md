---
title: ServiceProvider
description: ServiceProvider
ms.assetid: 6fa22f4d-9be9-4d02-b610-e20bed4958e9
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# ServiceProvider

[!include[MBAE deprecation warning](mbae-deprecation-warning.md)]

> [!IMPORTANT]
> In Windows 10, version 1709 and later, this field has been replaced by branding through COSA. Fields in COSA for branding are described on [Planning your desktop COSA/APN database submission](planning-your-desktop-cosa-apn-database-submission.md). If you are targeting versions of Windows before Windows 10, version 1709, you will still create a metadata package as described in this section. For more information about COSA, see [COSA overview](cosa-overview.md). 

The ServiceProvider element specifies the name of the service provider. It is shown in Windows Connection Manger to display the home provider network name. If the user is on a roaming network the roaming network name is displayed instead.

## <span id="Usage"></span><span id="usage"></span><span id="USAGE"></span>Usage


``` syntax
<ServiceProvider>
  text
</ServiceProvider>
```

## <span id="Attributes"></span><span id="attributes"></span><span id="ATTRIBUTES"></span>Attributes


There are no attributes.

## <span id="Text_value"></span><span id="text_value"></span><span id="TEXT_VALUE"></span>Text value


A string of up to 20 printable characters.

## <span id="Child_elements"></span><span id="child_elements"></span><span id="CHILD_ELEMENTS"></span>Child elements


There are no child elements.

## <span id="Parent_elements"></span><span id="parent_elements"></span><span id="PARENT_ELEMENTS"></span>Parent elements


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

 

## <span id="XSD"></span><span id="xsd"></span>XSD


``` syntax
<xs:element name="ServiceProvider" type="tns:ProviderNameType"/>

<xs:simpleType name="ProviderNameType">
  <xs:restriction base="xs:string">
    <xs:minLength value="1" />
    <xs:maxLength value="20" />
  </xs:restriction>
</xs:simpleType>
```

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


The ServiceProvider element is not shown in Windows Connection Manager when the user is roaming.

The ServiceProvider element is required.

 

 





