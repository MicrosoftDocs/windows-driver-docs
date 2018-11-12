---
title: ServiceCategory
description: ServiceCategory
ms.assetid: 770cb127-808f-4d77-905e-66064553d3d7
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# ServiceCategory

[!include[MBAE deprecation warning](mbae-deprecation-warning.md)]

The ServiceCategory element specifies the functional category that applies to the service.

## <span id="Usage"></span><span id="usage"></span><span id="USAGE"></span>Usage


``` syntax
<ServiceCategory>
  text
</ServiceCategory>
```

## <span id="Attributes"></span><span id="attributes"></span><span id="ATTRIBUTES"></span>Attributes


There are no attributes.

## <span id="Text_value"></span><span id="text_value"></span><span id="TEXT_VALUE"></span>Text value


Must contain one ServiceCategory element.

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
<td><p><a href="servicecategorylist.md" data-raw-source="[ServiceCategoryList](servicecategorylist.md)">ServiceCategoryList</a></p></td>
<td><p>The <a href="servicecategorylist.md" data-raw-source="[ServiceCategoryList](servicecategorylist.md)">ServiceCategoryList</a> element specifies the functional categories that apply to the service.</p></td>
</tr>
</tbody>
</table>

 

## <span id="XSD"></span><span id="xsd"></span>XSD


``` syntax
<xs:element name="ServiceCategory" type="tns:ServiceCategoryType" maxOccurs="unbounded" />

<xs:simpleType name="ServiceCategoryType">
    <xs:union memberTypes="tns:ServiceCategoryTypeEnumeration xs:string"/>
</xs:simpleType>

<xs:simpleType name="ServiceCategoryTypeEnumeration">
  <xs:restriction base="xs:string">
    <xs:enumeration value="Network"/>
    <xs:enumeration value="Network.MobileBroadband"/>
    <xs:enumeration value="Other"/>
  </xs:restriction>
</xs:simpleType>
```

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


The following discusses the use of the [ServiceCategoryList](servicecategorylist.md) elements in a service metadata package:

-   The first ServiceCategory element in the [ServiceCategoryList](servicecategorylist.md) element specifies the service’s primary functional category. The primary functional category should match how the service is advertised, packaged, sold, and ultimately identified by users.

-   Because a service is defined only by its primary functional category, you should specify only one instance of the ServiceCategory element in the [ServiceCategoryList](servicecategorylist.md) element.

-   The ServiceCategory for service metadata packages must be one of the following:

    -   Network.MobileBroadband

    -   Network.MobileBroadband.CDMA

    -   Network.MobileBroadband.GSM

The ServiceCategory element is required.

 

 





