---
title: ProvisioningEngine
description: ProvisioningEngine
ms.date: 04/20/2017
---

# ProvisioningEngine

[!include[MBAE deprecation warning](../includes/mbae-deprecation-warning.md)]

The ProvisioningEngine element specifies the trusted certificates. This allows operators to provision the PC with packages that are signed with a trusted certificate.

For more information about provisioning, see [Account provisioning](account-provisioning.md).

## Usage


``` syntax
<ProvisioningEngine>
  child element
</ProvisioningEngine>
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
<td><p><a href="trustedcertificates.md" data-raw-source="[TrustedCertificates](trustedcertificates.md)">TrustedCertificates</a></p></td>
<td><p>Specifies the trusted certificates.</p></td>
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
<td><p><a href="mobilebroadbandinfo.md" data-raw-source="[MobileBroadbandInfo](mobilebroadbandinfo.md)">MobileBroadbandInfo</a></p></td>
<td><p>The <a href="mobilebroadbandinfo.md" data-raw-source="[MobileBroadbandInfo](mobilebroadbandinfo.md)">MobileBroadbandInfo</a> element is the parent element of the <a href="mobilebroadbandinfo-xml-schema.md" data-raw-source="[MobileBroadbandInfo XML schema](mobilebroadbandinfo-xml-schema.md)">MobileBroadbandInfo XML schema</a>.</p></td>
</tr>
</tbody>
</table>

 

## XSD


``` syntax
<xs:element name="ProvisioningEngine" type="tns:ProvisioningEngineType" minOccurs="0" />

<xs:complexType name="ProvisioningEngineType">
  <xs:sequence>
    <xs:element name="TrustedCertificates" type="tns:TrustedCertificateListType" minOccurs="0" />
    <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
  </xs:sequence>
</xs:complexType>
```

## Remarks


-   Windows 8, Windows 8.1, and Windows 10 allow mobile network operators to provide packages to make updates to the user’s mobile broadband network settings called provisioning packages.

-   To ensure those provisioning packages come from the mobile network operator, Windows verifies that the Issuer Name and Subject Name from the certificate that is used to sign the provisioning package match what is described in the service metadata package.

The ProvisioningEngine element is optional.

 

 





