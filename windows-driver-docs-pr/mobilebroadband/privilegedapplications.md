---
title: PrivilegedApplications
description: PrivilegedApplications
ms.assetid: fb0c4a7e-173e-4768-b1ba-a6c5149d61aa
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# PrivilegedApplications


The PrivilegedApplications element specifies the app that will be allowed to access privileged Mobile Broadband interfaces.

## <span id="Usage"></span><span id="usage"></span><span id="USAGE"></span>Usage


``` syntax
<PrivilegedApplications>
  Child elements
</PrivilegedApplications>
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
<td><p>[Package](package-privapps.md)</p></td>
<td><p>The app that should have access to the privileged Mobile Broadband interfaces.</p></td>
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
<td><p>[SoftwareInfo](softwareinfo.md)</p></td>
<td><p>The parent element of the [SoftwareInfo XML schema](softwareinfo-xml-schema.md).</p></td>
</tr>
</tbody>
</table>

 

## <span id="XSD"></span><span id="xsd"></span>XSD


``` syntax
<xs:element name="PrivilegedApplications" type="tns:PrivilegedApplicationsType" minOccurs="0" />

<xs:complexType name="PrivilegedApplicationsType">
  <xs:choice>
    <xs:element name="AnyApplication" type="tns:AnyApplicationType" />
    <xs:element name="Package" type="tns:PackageForPrivilegedApplications" maxOccurs="unbounded" />
    <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
  </xs:choice>
</xs:complexType>
```

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


-   The PrivilegedApplications element allows a specified app to access the Mobile Broadband and SMS APIs with privileged access rights.

-   The structure for the package [Identity](identity-privapps.md) is identical with the &lt;Identity&gt; element in the application manifest structure. You should copy the elements from the application manifest.

-   To specify multiple packages, list multiple [Package](package-privapps.md) elements in the PrivilegedApplications element.

-   The Package Name, Publisher, and Application ID must match the information in package.appxmanifest for the Microsoft Store app. The publisher also must match the publisher certificate that is installed on the PC.

-   For the Microsoft Store app that is listed under the [DeviceCompanionApplications](devicecompanionapplications.md) element to have access to privileged Mobile Broadband interfaces including SMS, that app also must be specified under the PrivilegedApplications element.

-   When you are submitting your service metadata package to the Windows Dev Center Dashboard, you cannot declare more than 2 privileged apps. One of apps must be the app ID for the Microsoft Store device app that will be automatically downloaded. The second privileged app is not automatically downloaded, but will access to the privileged Mobile Broadband APIs if the app is installed.

The PrivilegedApplications element is optional.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20PrivilegedApplications%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




