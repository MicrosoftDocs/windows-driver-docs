---
title: MobileBroadbandInfo XML example
description: MobileBroadbandInfo XML example
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# MobileBroadbandInfo XML example

[!include[MBAE deprecation warning](../includes/mbae-deprecation-warning.md)]

The following XML document uses the [MobileBroadbandInfo XML schema](mobilebroadbandinfo-xml-schema.md) to specify the mobile broadband specific information for the service:

``` syntax
<?xml version="1.0" encoding="UTF-8"?>
<MobileBroadbandInfo xmlns="http://schemas.microsoft.com/windows/2010/12/DeviceMetadata/MobileBroadbandInfo">
  <NetworkConfiguration>
    <MobileBroadbandProfiles>
      <Purchase>PurchaseProfile.xml</Purchase>
      <Internet>OperatingProfile.xml</Internet>
    </MobileBroadbandProfiles>
    <AllowStandardUserPinUnlock>true</AllowStandardUserPinUnlock>
  </NetworkConfiguration>
  <ProvisioningEngine>
    <TrustedCertificates>
      <TrustedCertificate>
        <SubjectName>CN=Contoso, OU=Contosodev, O=Contoso, C=US</SubjectName>
        <IssuerName>CN= Contoso SA Root CA, OU=Contosodev, O=Contoso, C=US</IssuerName>
      </TrustedCertificate>
    </TrustedCertificates>
  </ProvisioningEngine>
</MobileBroadbandInfo>
```
