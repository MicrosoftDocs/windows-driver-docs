---
title: ServiceCategory
description: ServiceCategory
ms.date: 04/20/2017
---

# ServiceCategory

[!include[MBAE deprecation warning](../includes/mbae-deprecation-warning.md)]

The ServiceCategory element specifies the functional category that applies to the service.

## Usage


``` syntax
<ServiceCategory>
  text
</ServiceCategory>
```

## Attributes


There are no attributes.

## Text value


Must contain one ServiceCategory element.

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
<td><p><a href="servicecategorylist.md" data-raw-source="[ServiceCategoryList](servicecategorylist.md)">ServiceCategoryList</a></p></td>
<td><p>The <a href="servicecategorylist.md" data-raw-source="[ServiceCategoryList](servicecategorylist.md)">ServiceCategoryList</a> element specifies the functional categories that apply to the service.</p></td>
</tr>
</tbody>
</table>

 

## XSD


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

## Remarks


The following discusses the use of the [ServiceCategoryList](servicecategorylist.md) elements in a service metadata package:

-   The first ServiceCategory element in the [ServiceCategoryList](servicecategorylist.md) element specifies the service’s primary functional category. The primary functional category should match how the service is advertised, packaged, sold, and ultimately identified by users.

-   Because a service is defined only by its primary functional category, you should specify only one instance of the ServiceCategory element in the [ServiceCategoryList](servicecategorylist.md) element.

-   The ServiceCategory for service metadata packages must be one of the following:

    -   Network.MobileBroadband

    -   Network.MobileBroadband.CDMA

    -   Network.MobileBroadband.GSM

The ServiceCategory element is required.

 

 





