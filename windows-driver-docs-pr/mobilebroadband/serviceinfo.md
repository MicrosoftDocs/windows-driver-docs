---
title: ServiceInfo
description: ServiceInfo
ms.assetid: 0dab9e5b-122c-4fe4-9314-97a0531af4aa
---

# ServiceInfo


The ServiceInfo element is the parent element of the [ServiceInfo XML schema](serviceinfo-xml-schema.md).

## <span id="Usage"></span><span id="usage"></span><span id="USAGE"></span>Usage


``` syntax
<ServiceInfo>
  child elements
</ServiceInfo>
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
<td><p>[ServiceCategoryList](servicecategorylist.md)</p></td>
<td><p>Specifies one or more functional categories that apply to the service.</p></td>
</tr>
<tr class="even">
<td><p>[ServiceName](servicename.md)</p></td>
<td><p>Not used.</p></td>
</tr>
<tr class="odd">
<td><p>[ServiceDescription1](servicedescription1.md)</p></td>
<td><p>Specifies descriptive information about the service. This is applied to the description field of the wireless wide area network (WWAN) connection profile. It is not displayed in the user interface to the end user.</p></td>
</tr>
<tr class="even">
<td><p>[ServiceDescription2](servicedescription2.md)</p></td>
<td><p>Not used.</p></td>
</tr>
<tr class="odd">
<td><p>[ServiceNumber](servicenumber.md)</p></td>
<td><p>This is a self-generated GUID that identifies the operator that is submitting this package.</p></td>
</tr>
<tr class="even">
<td><p>[ServiceProvider](serviceprovider.md)</p></td>
<td><p>This appears in Windows Connection Manager as the home network display name.</p></td>
</tr>
<tr class="odd">
<td><p>[ServiceIconFile](serviceiconfile.md)</p></td>
<td><p>Specifies the name of the service icon file in the service metadata package.</p>
<div class="alert">
<strong>Note</strong>  
<p>This is listed as optional in the schema. However, it is required in order to pass validation when the package is submitted to the Windows Dev Center Dashboard.</p>
</div>
<div>
 
</div></td>
</tr>
<tr class="even">
<td><p>[ServiceSpecificExtension](servicespecificextension.md)</p></td>
<td><p>References the location of the file that is specific to this ServiceCategory. For Windows 8, Windows 8.1, or Windows 10 for desktop editions (Home, Pro, Enterprise, and Education) service metadata packages, this is the location of MobileBroadbandInfo.xml.</p></td>
</tr>
</tbody>
</table>

 

## <span id="Parent_elements"></span><span id="parent_elements"></span><span id="PARENT_ELEMENTS"></span>Parent elements


There are no parent elements.

## <span id="XSD"></span><span id="xsd"></span>XSD


``` syntax
<xs:element name="ServiceInfo" type="tns:ServiceInfoType" />

<xs:complexType name="ServiceInfoType">
  <xs:sequence>
    <xs:element name="ServiceCategoryList" type="tns:ServiceCategoryListType" />
    <xs:element name="ServiceName" type="tns:ServiceNameType" minOccurs="0" />
    <xs:element name="ServiceDescription1" type="tns:ServiceDescriptionType" minOccurs="0" />
    <xs:element name="ServiceDescription2" type="tns:ServiceDescriptionType" minOccurs="0" />
    <xs:element name="ServiceNumber" type ="tns:ServiceNumberType" />
    <xs:element name="ServiceProvider" type="tns:ProviderNameType" />
    <xs:element name="ServiceIconFile" type="tns:ServiceIconFileType" minOccurs="0" />
    <xs:element name="ServiceSpecificExtension" type="tns:ServiceSpecificExtensionType" minOccurs="0" />
    <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
  </xs:sequence>
</xs:complexType>
```

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


The ServiceInfo element must contain one instance of the [ServiceCategoryList](servicecategorylist.md), [ServiceNumber](servicenumber.md), [ServiceProvider](serviceprovider.md), and [ServiceSpecificExtension](servicespecificextension.md) elements.

The ServiceInfo element is required.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20ServiceInfo%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




