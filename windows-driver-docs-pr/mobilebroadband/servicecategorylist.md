---
title: ServiceCategoryList
description: ServiceCategoryList
ms.assetid: 69ea35aa-c658-49ed-86bd-815392d157f6
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# ServiceCategoryList


The ServiceCategoryList element specifies one or more functional categories that apply to the service. Each functional category is specified through a [ServiceCategory](servicecategory.md) element.

## <span id="Usage"></span><span id="usage"></span><span id="USAGE"></span>Usage


``` syntax
<ServiceCategorylist>
  child element
</ServiceCategorylist>
```

## <span id="Attributes"></span><span id="attributes"></span><span id="ATTRIBUTES"></span>Attributes


There are no attributes.

## <span id="Text_value"></span><span id="text_value"></span><span id="TEXT_VALUE"></span>Text value


Must contain one [ServiceCategory](servicecategory.md) element.

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
<td><p>[ServiceCategory](servicecategory.md)</p></td>
<td><p>Specifies one or more functional categories that apply to the service.</p></td>
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
<td><p>[ServiceInfo](serviceinfo.md)</p></td>
<td><p>The [ServiceInfo](serviceinfo.md) element is the parent element of the [ServiceInfo XML schema](serviceinfo-xml-schema.md).</p></td>
</tr>
</tbody>
</table>

 

## <span id="XSD"></span><span id="xsd"></span>XSD


``` syntax
<xs:element name="ServiceCategoryList" type="tns:ServiceCategoryListType" />

<xs:complexType name="ServiceCategoryListType">
  <xs:sequence>
    <xs:element name="ServiceCategory" type="tns:ServiceCategoryType" maxOccurs="unbounded" />
    <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
  </xs:sequence>
</xs:complexType>
```

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


The following discusses the use of the ServiceCategoryList elements in a service metadata package:

-   The first [ServiceCategory](servicecategory.md) element in the ServiceCategoryList element specifies the service’s primary functional category. The primary functional category should match how the service is advertised, packaged, sold, and ultimately identified by users.

-   Because a service is defined only by its primary functional category, you should specify only one instance of the [ServiceCategory](servicecategory.md) element in the ServiceCategoryList element.

-   The [ServiceCategory](servicecategory.md) for service metadata packages must be one of the following:

    -   Network.MobileBroadband

    -   Network.MobileBroadband.CDMA

    -   Network.MobileBroadband.GSM

The ServiceCategoryList element is required.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20ServiceCategoryList%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




