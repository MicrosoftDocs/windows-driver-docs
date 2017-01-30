---
title: MetadataKey
description: MetadataKey
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 1915db47-98bb-40f5-be3b-75e9af80f506
---

# MetadataKey


The MetadataKey element specifies the attributes of the service metadata package. These include the following:

-   The identifier for each hardware function supported by the device.

-   The language-specific locale for the text strings within the package.

## <span id="Usage"></span><span id="usage"></span><span id="USAGE"></span>Usage


``` syntax
<MetadataKey>
  child elements
</MetadataKey>
```

## <span id="Attributes"></span><span id="attributes"></span><span id="ATTRIBUTES"></span>Attributes


There are no attributes.

## <span id="Child_elements"></span><span id="child_elements"></span><span id="CHILD_ELEMENTS"></span>Child elements


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
<td><p>[HardwareIDList](hardwareidlist.md)</p></td>
<td><p>The [HardwareIDList](hardwareidlist.md) element specifies one or more hardware identification strings for the device.</p></td>
</tr>
<tr class="even">
<td><p>[LastModifiedDate](lastmodifieddate.md)</p></td>
<td><p>The [LastModifiedDate](lastmodifieddate.md) element specifies the time stamp on which the service metadata package was last changed.</p></td>
</tr>
<tr class="odd">
<td><p>[Locale](locale.md)</p></td>
<td><p>The [Locale](locale.md) element specifies the localized version of the service metadata package.</p></td>
</tr>
<tr class="even">
<td><p>[ModelIDList](modelidlist.md)</p></td>
<td><p>The [ModelIDList](modelidlist.md) element specifies the GUID of each device type or model that is specified within the service metadata package.</p></td>
</tr>
<tr class="odd">
<td><p>[MultipleLocale](multiplelocale.md)</p></td>
<td><p>The [MultipleLocale](multiplelocale.md) element specifies whether the service metadata package supports multiple locales.</p></td>
</tr>
</tbody>
</table>

 

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
<td><p>[PackageInfo](packageinfo.md)</p></td>
<td><p>The [PackageInfo](packageinfo.md) element is the parent element of the [PackageInfo XML schema](packageinfo-xml-schema.md). The child elements of the PackageInfo element specify the attributes of the device metadata package.</p></td>
</tr>
</tbody>
</table>

 

## <span id="XSD"></span><span id="xsd"></span>XSD


``` syntax
<xs:element name="MetadataKey" type="tns:MetadataKeyType" />

<xs:complexType name="MetadataKeyType">
  <xs:sequence>
    <xs:choice>
      <xs:sequence>
       <xs:element name="HardwareIDList" type="tns:HardwareIDListType" />
       <xs:element name="ModelIDList" type="tns:ModelIDListType" minOccurs="0" />
      </xs:sequence>
      <xs:element name="ModelIDList" type="tns:ModelIDListType" />
    </xs:choice>
    <xs:element name="Locale" type="tns:LocaleType" />
    <xs:element name="LastModifiedDate" type="xs:dateTime" />
    <xs:element ref="v2:MultipleLocale" minOccurs="0" />
    <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
  </xs:sequence>
</xs:complexType>
```

The following is the PackageInfov2 XML schema metadata:

``` syntax
<?xml version="1.0" encoding="UTF-8"?>

<xs:schema targetNamespace="http://schemas.microsoft.com/windows/2010/08/DeviceMetadata/PackageInfov2"
           xmlns:tns="http://schemas.microsoft.com/windows/2010/08/DeviceMetadata/PackageInfov2"
           xmlns:xs="http://www.w3.org/2001/XMLSchema"
           elementFormDefault="qualified"
           blockDefault="#all">

<xs:element name="MultipleLocale" type ="xs:boolean" />

</xs:schema>
```

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


The child elements of the MetadataKey element specify the metadata that the operating system uses to do the following:

-   Search the device metadata store for a service metadata package based on either a device's [ModelID](modelid.md) or [HardwareID](hardwareid.md) value. If more than one metadata packages match the device's Model or Hardware ID, the operating system also compares the [Locale](locale.md) value within the metadata package to the current language setting on the user's computer.

-   Update the device metadata store with the service metadata package if a package has a more recent [LastModifiedDate](lastmodifieddate.md) value than an existing package within the device metadata store.

The MetadataKey element must contain:

-   One instance of the [Locale](locale.md) and [LastModifiedDate](lastmodifieddate.md) elements.

-   One instance of either the [HardwareIDList](hardwareidlist.md) or [ModelIDList](modelidlist.md) elements. The MetadataKey element can contain one instance of both elements.

The MetadataKey element is required.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20MetadataKey%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




