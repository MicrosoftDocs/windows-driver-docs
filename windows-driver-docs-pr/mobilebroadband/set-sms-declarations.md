---
title: Set SMS declarations
description: Set SMS declarations
ms.assetid: fad7fb60-eb08-43e9-bc58-afb8d6b5633c
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Set SMS declarations


## <span id="SMS_device_capability_declaration_in_package_manifest"></span><span id="sms_device_capability_declaration_in_package_manifest"></span><span id="SMS_DEVICE_CAPABILITY_DECLARATION_IN_PACKAGE_MANIFEST"></span>SMS device capability declaration in package manifest


A UWP app that uses SMS must declare SMS capability in its package manifest in Visual Studio.

Example **package.appxmanifest**:

``` syntax
  <Capabilities>
    <DeviceCapability Name="sms" />
  </Capabilities>
```

For more information, see [App capability declarations (UWP apps)](http://go.microsoft.com/fwlink/p/?linkid=317125).

## <span id="SMS_app_declaration_in_device_metadata"></span><span id="sms_app_declaration_in_device_metadata"></span><span id="SMS_APP_DECLARATION_IN_DEVICE_METADATA"></span>SMS app declaration in device metadata


The mobile broadband device can determine which apps it trusts to send and receive SMS messages. To do so, it adds the package name that it trusts in the [Service metadata](service-metadata.md), as shown in the following entry:

**\\Package\\SoftwareInformation\\SoftwareInfo.xml**

``` syntax
<PrivilegedApplications>
  <Package>
    <Identity Name="Microsoft.SDKSamples.SMSSendReceive.JS" Version="1.0.0.0" Publisher="CN=Contoso Corporation, O=Contoso Corporation, L=Redmond, S=Washington, C=US" />
  </Package>
```

## <span id="related_topics"></span>Related topics


[Developing SMS apps](developing-sms-apps.md)

 

 






