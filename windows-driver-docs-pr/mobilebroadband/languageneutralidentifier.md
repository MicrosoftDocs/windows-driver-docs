---
title: LanguageNeutralIdentifier
description: LanguageNeutralIdentifier
ms.assetid: 38713565-464c-4b12-9076-331ae43e01e8
---

# LanguageNeutralIdentifier


The LanguageNeutralIdentifier element specifies a GUID, which identifies the service metadata package independent of its locale. The LanguageNeutralIdentifier element lets the same GUID be used to identify one or more localized versions of a service metadata package for the same service.

## <span id="Usage"></span><span id="usage"></span><span id="USAGE"></span>Usage


``` syntax
<LanguageNeutralIdentifier>
  text
</LanguageNeutralIdentifier>
```

## <span id="Attributes"></span><span id="attributes"></span><span id="ATTRIBUTES"></span>Attributes


There are no attributes.

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
<xs:element name="LanguageNeutralIdentifier" type="tns:GUIDType" minOccurs="0" />
```

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


The LanguageNeutralIdentifier element allows the same GUID to be used in one or more localized versions of a device metadata package for the same device.

For example, If you release a device for three locales (such as EN-US, JA-JP, and AR-SA), you can create separate metadata packages for the device for each locale. By using a common GUID for the LanguageNeutralIdentifier elements in these packages, you can easily search for the device's metadata package by browsing its PackageInfo XML document.

**Important**  
The LanguageNeutralIdentifier element is not used by any component of the operating system. It is reserved for use by the OEM, independent hardware vendor (IHV), and independent software vendor (ISV).\]

 

The LanguageNeutralIdentifier element is optional.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20LanguageNeutralIdentifier%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




