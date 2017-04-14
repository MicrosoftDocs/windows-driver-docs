---
title: Locale
description: Locale
ms.assetid: 1cf8d075-a1b3-4554-83d5-71fd5059c1c4
---

# Locale


The Locale element specifies the locale of the service metadata package. A service metadata package can specify single or multiple locales. To use multiple locales, you must set the [MultipleLocale](multiplelocale.md) element to **true**.

## <span id="Usage"></span><span id="usage"></span><span id="USAGE"></span>Usage


``` syntax
<Locale
  default = "xs:boolean">
  text
</Locale>
```

## <span id="Attributes"></span><span id="attributes"></span><span id="ATTRIBUTES"></span>Attributes


<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Type</th>
<th>Required</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>default</strong></p></td>
<td><p>xs:boolean</p></td>
<td><p>Yes</p></td>
<td><p>Must be true (1) or false (0). If the default attribute is set to true, the operating system uses this device metadata package as the default for the current locale of the computer.</p></td>
</tr>
</tbody>
</table>

 

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
<td><p>[MetadataKey](metadatakey.md)</p></td>
<td><p>The [MetadataKey](metadatakey.md) element specifies the attributes of the device metadata package. These include the following:</p>
<ul>
<li><p>The identifier for each hardware function supported by the device.</p></li>
<li><p>The language-specific locale for the text strings within the package.</p></li>
</ul></td>
</tr>
</tbody>
</table>

 

## <span id="XSD"></span><span id="xsd"></span>XSD


``` syntax
<xs:element name="Locale" type="tns:LocaleType" />

<xs:complexType name="LocaleType">
  <xs:simpleContent>
    <xs:extension base="xs:string">
      <xs:attribute name="default" type="xs:boolean" use="required" />
    </xs:extension>
  </xs:simpleContent>
</xs:complexType>
```

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


-   The Locale element can be *&lt;Language&gt;*-*&lt;Region&gt;* (such as EN-US) or *&lt;Language&gt;* (such as EN). If the *&lt;Language&gt;* is set, the package applies to all *&lt;Language&gt;* locales. For example, EN applies to EN-US and EN-BR.

-   To specify the metadata package as the default for the current locale of the computer, set the **default** attribute to **true** (1).

    **Note**  
    Only one metadata package for a service should set the **default** attribute to **true** (1). Otherwise, the operating system randomly selects a metadata package for the service.

     

-   When the operating system selects a service metadata package to display, it uses the Locale element in the following way:

    1.  The operating system retrieves the system preferred language and region. This is typically configured during Windows Setup.

    2.  If the Locale element of a service metadata package matches the system preferred language and region, the operating system selects the package for the service and uses the icon and **ServiceProvider** value (from ServiceInfo.xml) that matches that language and region.

    3.  If the services metadata package does not have a Locale element that matches the system preferred language, the operating system will apply the language neutral icon and **ServiceProvider** value (from ServiceInfo.xml) that is stored in the root of the service metadata package.

The Locale element is required.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Locale%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




