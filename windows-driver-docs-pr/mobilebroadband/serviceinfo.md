---
title: ServiceInfo
description: ServiceInfo
ms.assetid: 0dab9e5b-122c-4fe4-9314-97a0531af4aa
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# ServiceInfo

[!include[MBAE deprecation warning](mbae-deprecation-warning.md)]

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
<td><p><a href="servicecategorylist.md" data-raw-source="[ServiceCategoryList](servicecategorylist.md)">ServiceCategoryList</a></p></td>
<td><p>Specifies one or more functional categories that apply to the service.</p></td>
</tr>
<tr class="even">
<td><p><a href="servicename.md" data-raw-source="[ServiceName](servicename.md)">ServiceName</a></p></td>
<td><p>Not used.</p></td>
</tr>
<tr class="odd">
<td><p><a href="servicedescription1.md" data-raw-source="[ServiceDescription1](servicedescription1.md)">ServiceDescription1</a></p></td>
<td><p>Specifies descriptive information about the service. This is applied to the description field of the wireless wide area network (WWAN) connection profile. It is not displayed in the user interface to the end user.</p></td>
</tr>
<tr class="even">
<td><p><a href="servicedescription2.md" data-raw-source="[ServiceDescription2](servicedescription2.md)">ServiceDescription2</a></p></td>
<td><p>Not used.</p></td>
</tr>
<tr class="odd">
<td><p><a href="servicenumber.md" data-raw-source="[ServiceNumber](servicenumber.md)">ServiceNumber</a></p></td>
<td><p>This is a self-generated GUID that identifies the operator that is submitting this package.</p></td>
</tr>
<tr class="even">
<td><p><a href="serviceprovider.md" data-raw-source="[ServiceProvider](serviceprovider.md)">ServiceProvider</a></p></td>
<td><p>This appears in Windows Connection Manager as the home network display name.</p></td>
</tr>
<tr class="odd">
<td><p><a href="serviceiconfile.md" data-raw-source="[ServiceIconFile](serviceiconfile.md)">ServiceIconFile</a></p></td>
<td><p>Specifies the name of the service icon file in the service metadata package.</p>
<div class="alert">
<strong>Note</strong><br/><p>This is listed as optional in the schema. However, it is required in order to pass validation when the package is submitted to the Windows Dev Center Dashboard.</p>
</div>
<div>

</div></td>
</tr>
<tr class="even">
<td><p><a href="servicespecificextension.md" data-raw-source="[ServiceSpecificExtension](servicespecificextension.md)">ServiceSpecificExtension</a></p></td>
<td><p>References the location of the file that is specific to this ServiceCategory. For Windows 8, Windows 8.1, or Windows 10 for desktop editions (Home, Pro, Enterprise, and Education) service metadata packages, this is the location of MobileBroadbandInfo.xml.</p></td>
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









