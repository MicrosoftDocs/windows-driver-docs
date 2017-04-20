---
title: ExperienceID
description: ExperienceID
ms.assetid: 550527ae-fef9-46c6-816b-d842fe472b68
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# ExperienceID


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
<td><p>[Relationships](relationships.md)</p></td>
<td><p>The [Relationships](relationships.md) element specifies data that is used to track a device metadata package within the device metadata cache.</p></td>
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20ExperienceID%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




