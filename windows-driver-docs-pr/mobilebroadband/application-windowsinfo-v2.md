---
title: Application (WindowsInfo)
description: Application (WindowsInfo)
ms.date: 04/20/2017
---

# Application (WindowsInfo)

[!include[MBAE deprecation warning](../includes/mbae-deprecation-warning.md)]

The Application element specifies the application ID for the app.

## Usage

``` syntax
<Application Id=”tns:ApplicationIdType” />
```

## Attributes

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
<td><p><a href="autoplayhandler.md" data-raw-source="[AutoplayHandler](autoplayhandler.md)">AutoplayHandler</a></p></td>
<td><p>Specifies a UWP device app that should appear as the recommended AutoPlay action when a user plugs in a device.</p></td>
</tr>
</tbody>
</table>

## XSD

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

## Remarks

The structure for the Application element correspond to the structure of the &lt;Application&gt; element in an app manifest. Copy the value of the Id value from the Id attribute in the app manifest.

Here is an example of how the &lt;Applications&gt; element may be structured inside an app manifest:

``` syntax
<Applications>
  <Application Id="DeviceAppForPrinters" Executable="$targetnametoken$.exe" EntryPoint="DeviceAppForPrinters.App">
</Application>
</Applications>
```

The Application element is optional.
