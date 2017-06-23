---
title: ServiceProvider
description: ServiceProvider
ms.assetid: 6fa22f4d-9be9-4d02-b610-e20bed4958e9
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# ServiceProvider

> [!IMPORTANT]
> In Windows 10, version 1709 and later, this field has been replaced by branding through COSA. Fields in COSA for branding are described on [Planning your COSA/APN database submission](planning-your-cosa-apn-database-submission.md). If you are targeting versions of Windows before Windows 10, version 1709, you will still create a metadata package as described in this section. For more information about COSA, see [COSA overview](cosa-overview.md). 

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
<td><p>[ServiceInfo](serviceinfo.md)</p></td>
<td><p>The [ServiceInfo](serviceinfo.md) element is the parent element of the [ServiceInfo XML schema](serviceinfo-xml-schema.md).</p></td>
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20ServiceProvider%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




