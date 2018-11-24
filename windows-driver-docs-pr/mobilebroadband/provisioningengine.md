---
title: ProvisioningEngine
description: ProvisioningEngine
ms.assetid: b6b10145-d554-43be-8682-1355145b3241
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# ProvisioningEngine

[!include[MBAE deprecation warning](mbae-deprecation-warning.md)]

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
<td><p><a href="trustedcertificates.md" data-raw-source="[TrustedCertificates](trustedcertificates.md)">TrustedCertificates</a></p></td>
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
<td><p><a href="mobilebroadbandinfo.md" data-raw-source="[MobileBroadbandInfo](mobilebroadbandinfo.md)">MobileBroadbandInfo</a></p></td>
<td><p>The <a href="mobilebroadbandinfo.md" data-raw-source="[MobileBroadbandInfo](mobilebroadbandinfo.md)">MobileBroadbandInfo</a> element is the parent element of the <a href="mobilebroadbandinfo-xml-schema.md" data-raw-source="[MobileBroadbandInfo XML schema](mobilebroadbandinfo-xml-schema.md)">MobileBroadbandInfo XML schema</a>.</p></td>
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

 

 





