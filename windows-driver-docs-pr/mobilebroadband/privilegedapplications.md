---
title: PrivilegedApplications
description: PrivilegedApplications
ms.date: 04/20/2017
---

# PrivilegedApplications

[!include[MBAE deprecation warning](../includes/mbae-deprecation-warning.md)]

The PrivilegedApplications element specifies the app that will be allowed to access privileged Mobile Broadband interfaces.

## Usage


``` syntax
<PrivilegedApplications>
  Child elements
</PrivilegedApplications>
```

## Attributes


There are no attributes.

## Child elements


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
<td><p><a href="package-privapps.md" data-raw-source="[Package](package-privapps.md)">Package</a></p></td>
<td><p>The app that should have access to the privileged Mobile Broadband interfaces.</p></td>
</tr>
</tbody>
</table>

 

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
<td><p><a href="softwareinfo.md" data-raw-source="[SoftwareInfo](softwareinfo.md)">SoftwareInfo</a></p></td>
<td><p>The parent element of the <a href="softwareinfo-xml-schema.md" data-raw-source="[SoftwareInfo XML schema](softwareinfo-xml-schema.md)">SoftwareInfo XML schema</a>.</p></td>
</tr>
</tbody>
</table>

 

## XSD


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

## Remarks


-   The PrivilegedApplications element allows a specified app to access the Mobile Broadband and SMS APIs with privileged access rights.

-   The structure for the package [Identity](identity-privapps.md) is identical with the &lt;Identity&gt; element in the application manifest structure. You should copy the elements from the application manifest.

-   To specify multiple packages, list multiple [Package](package-privapps.md) elements in the PrivilegedApplications element.

-   The Package Name, Publisher, and Application ID must match the information in package.appxmanifest for the Microsoft Store app. The publisher also must match the publisher certificate that is installed on the PC.

-   For the Microsoft Store app that is listed under the [DeviceCompanionApplications](devicecompanionapplications.md) element to have access to privileged Mobile Broadband interfaces including SMS, that app also must be specified under the PrivilegedApplications element.

-   When you are submitting your service metadata package to the Windows Dev Center Dashboard, you cannot declare more than 2 privileged apps. One of apps must be the app ID for the Microsoft Store device app that will be automatically downloaded. The second privileged app is not automatically downloaded, but will access to the privileged Mobile Broadband APIs if the app is installed.

The PrivilegedApplications element is optional.

 

 





