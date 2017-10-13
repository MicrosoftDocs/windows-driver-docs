---
title: AutoplayHandler
description: AutoplayHandler
ms.assetid: 0ee7ac9b-7c1a-4267-b718-ba110ef5b12d
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# AutoplayHandler


The AutoplayHandler element specifies a UWP device app that should appear as the recommended AutoPlay action when a user plugs in a device.

## <span id="Usage"></span><span id="usage"></span><span id="USAGE"></span>Usage


``` syntax
<AutoplayHandler>
  child elements
</AutoplayHandler>
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
<td><p>[PackageIdentity](packageidentity.md)</p></td>
<td><p>Specifies the package identity (name and publisher) for the app.</p></td>
</tr>
<tr class="even">
<td><p>[Application](application-windowsinfo-v2.md)</p></td>
<td><p>Specifies the application ID for the app.</p></td>
</tr>
<tr class="odd">
<td><p>[Verb](verb.md)</p></td>
<td><p>Specifies the verb that the app registers.</p></td>
</tr>
<tr class="even">
<td><p>[AutoplayType](autoplaytype.md)</p></td>
<td><p>Specifies whether the AutoPlay event is a device event or a content event. AutoPlay determines the type of device and raises either a Device event for non-volume devices, or a Content event for volume devices.</p></td>
</tr>
<tr class="odd">
<td><p>[EnableAutoPlayForRegisteredApps](enableautoplayforregisteredapps.md)</p></td>
<td><p>Specifies whether AutoPlay is enabled for registered apps.</p></td>
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
<td><p>[LaunchApplicationOnDeviceConnect](launchapplicationondeviceconnect.md)</p></td>
<td><p>Specifies an app that should appear as the recommended AutoPlay action when a user plugs in the device.</p></td>
</tr>
</tbody>
</table>

 

## <span id="XSD"></span><span id="xsd"></span>XSD


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

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


-   The structure for the [PackageIdentity](packageidentity.md) and [Application](application-windowsinfo-v2.md) elements are identical with the Application Manifest structure, so copy the elements from the application's manifest.

-   In addition to including the AutoplayHandler element in the device metadata, the specified UWP device app must also register for the AutoPlay event by adding a Declaration in its application manifest for the event. AutoPlay recognizes the declaration for the app and then includes it in the list of possible actions that a user can take to respond to that event.

-   Only the package listed in the [DeviceCompanionApplications](devicecompanionapplications.md) value in the SoftwareInfo.xml file will be downloaded as part of the device installation. If the [LaunchApplicationOnDeviceConnect](launchapplicationondeviceconnect.md) element value is from a different package, Windows does not know whether it will actually be on the user’s device. If the recommended application is not on the user’s device, users will not be presented with the choice.

-   Even if the application is the same as the [DeviceCompanionApplications](devicecompanionapplications.md) entry, it may not always appear in the AutoPlay list. If the user is not connected to the Internet or otherwise fails to download the companion application, it will not appear in the list. However, when the user gets the application, they will be presented with a “New Option Available” AutoPlay dialog box the next time they connect their device.

The AutoplayHandler element is optional.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20AutoplayHandler%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




