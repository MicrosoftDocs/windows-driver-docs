---
title: Application
description: Application
ms.date: 10/10/2023
---

# Application

[!include[MBAE deprecation warning](../includes/mbae-deprecation-warning.md)]

The Application element specifies the name of the application software that created the device metadata package.

## Usage

``` syntax
<Application>
  text
</Application>
```

## Attributes

There are no attributes.

## Text value

A string that contains between 1 and 256 characters inclusive.

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
<td><p><a href="metadatabuilderinformation.md" data-raw-source="[MetadataBuilderInformation](metadatabuilderinformation.md)">MetadataBuilderInformation</a></p></td>
<td><p>The <a href="metadatabuilderinformation.md" data-raw-source="[MetadataBuilderInformation](metadatabuilderinformation.md)">MetadataBuilderInformation</a> element specifies the application that created the service metadata package.</p></td>
</tr>
</tbody>
</table>

## XSD

``` syntax
<xs:element name="Application" type="tns:ApplicationType" />

<xs:simpleType name="ApplicationType">
  <xs:restriction base="xs:string">
    <xs:minLength value="1" />
    <xs:maxLength value="256" />
  </xs:restriction>
</xs:simpleType>
```

## Remarks

The Application element is not used by the Windows 7 operating system. It is reserved for use by OEMs and developers.
