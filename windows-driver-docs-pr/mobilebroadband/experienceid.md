---
title: ExperienceID
description: ExperienceID
ms.assetid: 550527ae-fef9-46c6-816b-d842fe472b68
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# ExperienceID

[!include[MBAE deprecation warning](mbae-deprecation-warning.md)]

The ExperienceID element specifies a GUID representing the device experience. This GUID is used to group one or more metadata packages for the same device identifiers independent of the packages’ locale.

In Windows 8, Windows 8.1, and Windows 10 it is also used to link the device metadata to a device app that can be automatically acquired when the device is first connected. A device app specifies one or more ExperienceID elements in a StoreManifest.XML file in the app submission package. Each of these ExperienceID GUIDs corresponds to the ExperienceID element of a device metadata package. After the StoreManifest.xml file has been submitted, the device app can then be distributed to one or more device models, if the ExperienceID in a device’s metadata is also specified in the device apps StoreManifest file.

## <span id="Usage"></span><span id="usage"></span><span id="USAGE"></span>Usage


``` syntax
<ExperienceID>
  text
</ExperienceID>
```

## <span id="Attributes"></span><span id="attributes"></span><span id="ATTRIBUTES"></span>Attributes


There are no attributes.

## <span id="Text_value"></span><span id="text_value"></span><span id="TEXT_VALUE"></span>Text value


A value formatted as a [GUIDType](guidtype-packageinfo.md) XML simple type.

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
<td><p><a href="relationships.md" data-raw-source="[Relationships](relationships.md)">Relationships</a></p></td>
<td><p>The <a href="relationships.md" data-raw-source="[Relationships](relationships.md)">Relationships</a> element specifies data that is used to track a device metadata package within the device metadata cache.</p></td>
</tr>
</tbody>
</table>

 

## <span id="XSD"></span><span id="xsd"></span>XSD


``` syntax
<xs:element name="ExperienceID" type="tns:GUIDType" minOccurs="0" />
```

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


In Windows 8.1 and Windows 10, the ExperienceID is created by the Service Metadata Wizard on the Windows Dev Center Dashboard.

In Windows 8 the ExperienceID can be specified by the service metadata developer, or automatically generated and added to the service metadata using the [Device Metadata Authoring Wizard](https://go.microsoft.com/fwlink/?linkid=620032). If the ExperienceID is not specified in the service metadata package, the Windows Dev Center Dashboard creates a GUID and updates the ExperienceID element within the metadata package when the mobile network operator or mobile virtual network operator submits the service metadata package.

 

 





