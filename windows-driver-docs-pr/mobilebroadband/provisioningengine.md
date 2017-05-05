---
title: ProvisioningEngine
description: ProvisioningEngine
ms.assetid: b6b10145-d554-43be-8682-1355145b3241
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# ProvisioningEngine


The ProvisioningEngine element specifies the trusted certificates. This allows operators to provision the PC with packages that are signed with a trusted certificate.

For more information about provisioning, see [Account provisioning](account-provisioning.md).

## <span id="Usage"></span><span id="usage"></span><span id="USAGE"></span>Usage


``` syntax
<ProvisioningEngine>
  child element
</ProvisioningEngine>
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
<td><p>[TrustedCertificates](trustedcertificates.md)</p></td>
<td><p>Specifies the trusted certificates.</p></td>
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
<td><p>[MobileBroadbandInfo](mobilebroadbandinfo.md)</p></td>
<td><p>The [MobileBroadbandInfo](mobilebroadbandinfo.md) element is the parent element of the [MobileBroadbandInfo XML schema](mobilebroadbandinfo-xml-schema.md).</p></td>
</tr>
</tbody>
</table>

 

## <span id="XSD"></span><span id="xsd"></span>XSD


``` syntax
<xs:element name="ProvisioningEngine" type="tns:ProvisioningEngineType" minOccurs="0" />

<xs:complexType name="ProvisioningEngineType">
  <xs:sequence>
    <xs:element name="TrustedCertificates" type="tns:TrustedCertificateListType" minOccurs="0" />
    <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
  </xs:sequence>
</xs:complexType>
```

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


-   Windows 8, Windows 8.1, and Windows 10 allow mobile network operators to provide packages to make updates to the user’s mobile broadband network settings called provisioning packages.

-   To ensure those provisioning packages come from the mobile network operator, Windows verifies that the Issuer Name and Subject Name from the certificate that is used to sign the provisioning package match what is described in the service metadata package.

The ProvisioningEngine element is optional.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20ProvisioningEngine%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




