---
title: Application
description: Application
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: e76ede51-e494-47b4-b30a-e354799f66e7
---

# Application


The Application element specifies the application ID for the app.

## <span id="Usage"></span><span id="usage"></span><span id="USAGE"></span>Usage


``` syntax
<Application Id=”tns:ApplicationIdType” />
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
<td><p>Id</p></td>
<td><p>tns:ApplicationIdType</p></td>
<td><p>Yes</p></td>
<td><p>The application ID. Copy this value from the app manifest, as described in Remarks..</p></td>
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
<td><p>[AutoplayHandler](autoplayhandler.md)</p></td>
<td><p>Specifies a Windows Store device app that should appear as the recommended AutoPlay action when a user plugs in a device.</p></td>
</tr>
</tbody>
</table>

 

## <span id="XSD"></span><span id="xsd"></span>XSD


``` syntax
<xs:element name="Application" type="tns:ApplicationType" />

<xs:complexType name="ApplicationType">
  <xs:attribute name="Id" type="tns:ApplicationIdType" use="required"/>
</xs:complexType>

<xs:simpleType name="ApplicationIdType">
  <xs:restriction base="tns:AsciiWindowsIdType">
    <xs:maxLength value="64"/>
  </xs:restriction>
</xs:simpleType>
```

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


The structure for the Application element correspond to the structure of the &lt;Application&gt; element in an app manifest. Copy the value of the Id value from the Id attribute in the app manifest.

Here is an example of how the &lt;Applications&gt; element may be structured inside an app manifest:

``` syntax
<Applications>
  <Application Id="DeviceAppForPrinters" Executable="$targetnametoken$.exe" EntryPoint="DeviceAppForPrinters.App">
</Application>
</Applications>
```

The Application element is optional.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Application%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




