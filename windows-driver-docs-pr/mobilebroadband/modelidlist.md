---
title: ModelIDList
description: ModelIDList
ms.date: 04/20/2017
---

# ModelIDList

[!include[MBAE deprecation warning](../includes/mbae-deprecation-warning.md)]

The ModelIDList element specifies one or more GUIDs. Each GUID is specified through a [ModelID](modelid.md) element, and identifies a physical device specified within the device metadata package.

**Caution**  
The ModelIDList and [ModelID](modelid.md) elements are not supported for service metadata packages. You must use the [HardwareIDList](hardwareidlist.md) and [HardwareID](hardwareid.md) elements instead.

 

## Usage


``` syntax
<ModelIDList>
  child elements
</ModelIDList>
```

## Attributes


There are no attributes.

## Child elements


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
<td><p><a href="modelid.md" data-raw-source="[ModelID](modelid.md)">ModelID</a></p></td>
<td><p>The <a href="modelid.md" data-raw-source="[ModelID](modelid.md)">ModelID</a> element specifies the GUID of a physical device.</p></td>
</tr>
</tbody>
</table>

 

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
<td><p><a href="metadatakey.md" data-raw-source="[MetadataKey](metadatakey.md)">MetadataKey</a></p></td>
<td><p>The <a href="metadatakey.md" data-raw-source="[MetadataKey](metadatakey.md)">MetadataKey</a> element specifies the attributes of the device metadata package. These include the following:</p>
<ul>
<li><p>The identifier for each hardware function supported by the device.</p></li>
<li><p>The language-specific locale for the text strings within the package.</p></li>
</ul></td>
</tr>
</tbody>
</table>

 

## XSD


``` syntax
<xs:element name="ModelIDList" type="tns:ModelIDListType" minOccurs="0" />

<xs:complexType name="ModelIDListType">
  <xs:sequence>
    <xs:element name="ModelID" type="tns:GUIDType" maxOccurs="unbounded" />
  </xs:sequence>
</xs:complexType>
```

## Remarks


The ModelIDList element is required only if the [HardwareIDList](hardwareidlist.md) element is not specified in the [MetadataKey](metadatakey.md) element. If it is specified, the ModelIDList element must contain one or more [ModelID](modelid.md) elements. If your device metadata package supports multiple device models or model IDs, you can specify a ModelID element for each device model.

**Caution**  
The ModelIDList and [ModelID](modelid.md) elements are not supported for service metadata packages. You must use the [HardwareIDList](hardwareidlist.md) and [HardwareID](hardwareid.md) elements instead.

 

If the PackageInfo XML data contains both of the [HardwareIDList](hardwareidlist.md) and ModelIDList elements, the operating system uses the following rules when it determines whether a device is specified by a device metadata package:

-   If the device has a model ID, the operating system does not search for a match in the [HardwareIDList](hardwareidlist.md) element. For more information about model IDs, see [ModelID](modelid.md).

-   Otherwise, the operating searches the [HardwareIDList](hardwareidlist.md) element for a match of the device's hardware ID.

 

 





