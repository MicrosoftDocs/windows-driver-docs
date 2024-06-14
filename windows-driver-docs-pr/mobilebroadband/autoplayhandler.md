---
title: AutoplayHandler
description: AutoplayHandler
ms.date: 04/20/2017
---

# AutoplayHandler

[!include[MBAE deprecation warning](../includes/mbae-deprecation-warning.md)]

The AutoplayHandler element specifies a UWP device app that should appear as the recommended AutoPlay action when a user plugs in a device.

## Usage


``` syntax
<AutoplayHandler>
  child elements
</AutoplayHandler>
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
<td><p><a href="packageidentity.md" data-raw-source="[PackageIdentity](packageidentity.md)">PackageIdentity</a></p></td>
<td><p>Specifies the package identity (name and publisher) for the app.</p></td>
</tr>
<tr class="even">
<td><p><a href="application-windowsinfo-v2.md" data-raw-source="[Application](application-windowsinfo-v2.md)">Application</a></p></td>
<td><p>Specifies the application ID for the app.</p></td>
</tr>
<tr class="odd">
<td><p><a href="verb.md" data-raw-source="[Verb](verb.md)">Verb</a></p></td>
<td><p>Specifies the verb that the app registers.</p></td>
</tr>
<tr class="even">
<td><p><a href="autoplaytype.md" data-raw-source="[AutoplayType](autoplaytype.md)">AutoplayType</a></p></td>
<td><p>Specifies whether the AutoPlay event is a device event or a content event. AutoPlay determines the type of device and raises either a Device event for non-volume devices, or a Content event for volume devices.</p></td>
</tr>
<tr class="odd">
<td><p><a href="enableautoplayforregisteredapps.md" data-raw-source="[EnableAutoPlayForRegisteredApps](enableautoplayforregisteredapps.md)">EnableAutoPlayForRegisteredApps</a></p></td>
<td><p>Specifies whether AutoPlay is enabled for registered apps.</p></td>
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
<td><p><a href="launchapplicationondeviceconnect.md" data-raw-source="[LaunchApplicationOnDeviceConnect](launchapplicationondeviceconnect.md)">LaunchApplicationOnDeviceConnect</a></p></td>
<td><p>Specifies an app that should appear as the recommended AutoPlay action when a user plugs in the device.</p></td>
</tr>
</tbody>
</table>

 

## XSD


``` syntax
      <xs:element name="AutoplayHandler" type="tns:AutoplayHandlerType" />

  <xs:complexType name="AutoplayHandlerType">
    <xs:sequence>
      <xs:element name="PackageIdentity" type="tns:PackageIdentityType" />
      <xs:element name="Application" type="tns:ApplicationType" />
      <xs:element name="Verb" type="tns:VerbType" />
      <xs:element name="AutoplayType" type="tns:AutoplayTypeType" />
      <xs:element name="EnableAutoPlayForRegisteredApps" type ="xs:boolean" default="false" minOccurs="0" />
      <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
    </xs:sequence>
  </xs:complexType>
```

## Remarks


-   The structure for the [PackageIdentity](packageidentity.md) and [Application](application-windowsinfo-v2.md) elements are identical with the Application Manifest structure, so copy the elements from the application's manifest.

-   In addition to including the AutoplayHandler element in the device metadata, the specified UWP device app must also register for the AutoPlay event by adding a Declaration in its application manifest for the event. AutoPlay recognizes the declaration for the app and then includes it in the list of possible actions that a user can take to respond to that event.

-   Only the package listed in the [DeviceCompanionApplications](devicecompanionapplications.md) value in the SoftwareInfo.xml file will be downloaded as part of the device installation. If the [LaunchApplicationOnDeviceConnect](launchapplicationondeviceconnect.md) element value is from a different package, Windows does not know whether it will actually be on the user’s device. If the recommended application is not on the user’s device, users will not be presented with the choice.

-   Even if the application is the same as the [DeviceCompanionApplications](devicecompanionapplications.md) entry, it may not always appear in the AutoPlay list. If the user is not connected to the Internet or otherwise fails to download the companion application, it will not appear in the list. However, when the user gets the application, they will be presented with a “New Option Available” AutoPlay dialog box the next time they connect their device.

The AutoplayHandler element is optional.

 

 





