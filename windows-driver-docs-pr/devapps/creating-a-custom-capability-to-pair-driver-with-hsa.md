---
title: Creating a custom capability to pair a driver with a Hardware Support App (HSA)
author: windows-driver-content
description: getting Creating a custom capability to pair a driver with a Hardware Support App (HSA)
keywords:
- Custom , Capabilities
- UWP Apps
- custom capabilities
- UWP
- Hardware
ms.author: windowsdriverdev
ms.date: 08/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Creating a custom capability to pair a driver with a Hardware Support App (HSA)

A Hardware Support App (HSA) is a [Universal Windows Platform (UWP)](https://msdn.microsoft.com/50a5605e-3a91-41db-800a-9180717c1e86) app that is paired with a specific driver or [RPC (Remote Procedure Call)](https://msdn.microsoft.com/en-us/library/windows/desktop/aa378651) using a custom capability.  The owner of the driver or RPC endpoint reserves the custom capability, permits access to UWP apps that advertise it, and then provides the capability to the app developer.  This page describes that process.

The steps for the app developer are described in [Using a custom capability to pair a Hardware Support App (HSA) with a driver](using-a-custom-capability-to-pair-hsa-with-driver.md).

## Reserving a custom capability

To reserve a custom capability:

1.  Email Microsoft Hardware Support Apps Review (<HSAReview@microsoft.com>) with the following information:

    * Contact information
    * Company name
    * Name of the capability (must be unique and reference the owner)
    * What resources does capability need to access?
    * Any security or privacy concerns
    * What data does your capability provide access to?
    * Include the Windows Store App Publisher ID.  To get one, create a skeleton app entry on the Windows Store page. For more info on reserving your App PFN, see [Create your app by reserving a name](https://msdn.microsoft.com/en-us/windows/uwp/publish/create-your-app-by-reserving-a-name).

2.  If the request is approved, Microsoft emails back a unique custom capability string name in the format **CompanyName.capabilityName\_PublisherID**.

Now you can use the custom capability to allow access to either an RPC endpoint or a driver.

## Allowing access to an RPC endpoint to a UWP app using the custom capability

To allow access to an RPC endpoint to a UWP app that has the custom capability, follow these steps:

1.  Call [**DeriveCapabilitySidsFromName**](https://msdn.microsoft.com/library/windows/desktop/mt803273) to convert the custom capability name to a security ID (SID).
2.  Add the SID to your access allowed ACE along with any other SIDs that are needed for the security descriptor of your RPC endpoint.
3.  Create an RPC endpoint using the information from the Security Descriptor.

You can see an implementation of the above in the [RPC server code](https://github.com/Microsoft/Windows-universal-samples/blob/master/Samples/CustomCapability/Service/Server/RpcServer.cpp) in the [Custom Capability sample](https://github.com/Microsoft/Windows-universal-samples/tree/master/Samples/CustomCapability).

## Allowing access to a driver to a UWP app using the custom capability

To allow access to a driver to a UWP app with the custom capability, add a few lines to either the INF file or the driver source.

In the INF file, specify your custom capability as follows:

```
[WDMPNPB003_Device.NT.Interfaces] 
AddInterface= {B0823231-61F1-4685-85CA-8DF9DDDEBF6E},,AddInterfaceSection 
 
[AddInterfaceSection] 
AddProperty= AddInterfaceSection.AddProps 
 
[AddInterfaceSection.AddProps] 
; DEVPKEY_DeviceInterface_UnrestrictedAppCapabilities 
{026e516e-b814-414b-83cd-856d6fef4822}, 8, 0x2012,, “CompanyName.myCustomCapabilityNameTBD_YourStorePubId”
```

Or, do the following in the driver:

```c++
WDF_DEVICE_INTERFACE_PROPERTY_DATA PropertyData = {}; 
WCHAR customCapabilities[] = L”CompanyName.yourCustomCapabilityNameTBD_YourStorePubId\0”; 
 
WDF_DEVICE_INTERFACE_PROPERTY_DATA_INIT( 
   &PropertyData, 
   &m_VendorDefinedSubType, 
   &DEVPKEY_DeviceInterface_UnrestrictedAppCapabilities); 
 
Status = WdfDeviceAssignInterfaceProperty( 
    m_FxDevice, 
    &PropertyData, 
    DEVPROP_TYPE_STRING_LIST, 
    ARRAYSIZE(customCapabilities), 
    reinterpret_cast<PVOID>(customCapabilities)); 

```

For an example of the driver code shown immediately above, see the [Driver package installation toolkit for universal drivers](https://github.com/Microsoft/Windows-driver-samples/tree/master/general/DCHU).

## Preparing the Signed Custom Capability Descriptor (SCCD) file

A Signed Custom Capability Descriptor (SCCD) file is a signed XML file authorizing the use of one or more custom capabilities.  The owner of the driver or RPC endpoint grants the custom capability to the app developer by providing this file.

To prepare the SCCD file, first update the custom capability string.  Use the following example as a starting point:

```xml
<?xml version="1.0" encoding="utf-8"?>
<CustomCapabilityDescriptor xmlns="http://schemas.microsoft.com/appx/2016/sccd" xmlns:s="http://schemas.microsoft.com/appx/2016/sccd">
<CustomCapabilities>
    <CustomCapability Name="microsoft.hsaTestCustomCapability_q536wpkpf5cy2"></CustomCapability>
</CustomCapabilities>
<AuthorizedEntities>
    <AuthorizedEntity AppPackageFamilyName="MicrosoftHSATest.Microsoft.SDKSamples.Hsa.CPP_q536wpkpf5cy2" CertificateSignatureHash="ca9fc964db7e0c2938778f4559946833e7a8cfde0f3eaa07650766d4764e86c4"></AuthorizedEntity>
</AuthorizedEntities>
<Catalog>0000</Catalog>
</CustomCapabilityDescriptor>
```

Next, the custom capability owner obtains the Package Family Name (PFN) and the signature hash from the app developer and updates those strings in the SCCD file.

**Note:**  The app does not have to be signed directly with the certificate, but the specified certificate must be part of the cert chain that signs the app.

After completing the SCCD, the capability owner emails it to Microsoft for signing.  Microsoft returns the signed SCCD to the capability owner.

The capability owner then sends the SCCD to the app developer.  The app developer includes the signed SCCD in the app manifest.  To learn what the app developer needs to do, see [Using a custom capability to pair a Hardware Support App (HSA) with a driver](using-a-custom-capability-to-pair-hsa-with-driver.md).

## Limiting the scope of an SCCD

For testing purposes, a custom capability owner can restrict installation of a hardware support app to computers in developer mode.

To do so, before getting the SCCD signed by Microsoft, add **DeveloperModeOnly**:

```xml
<?xml version="1.0" encoding="utf-8"?>
<CustomCapabilityDescriptor xmlns="http://schemas.microsoft.com/appx/2016/sccd" xmlns:s="http://schemas.microsoft.com/appx/2016/sccd">
<CustomCapabilities>
    <CustomCapability Name="microsoft.hsaTestCustomCapability_q536wpkpf5cy2"></CustomCapability>
</CustomCapabilities>
<AuthorizedEntities>
    <AuthorizedEntity AppPackageFamilyName="MicrosoftHSATest.Microsoft.SDKSamples.Hsa.CPP_q536wpkpf5cy2" CertificateSignatureHash="ca9fc964db7e0c2938778f4559946833e7a8cfde0f3eaa07650766d4764e86c4"></AuthorizedEntity>
</AuthorizedEntities>
<Catalog>0000</Catalog>
<DeveloperModeOnly Value="true" />
</CustomCapabilityDescriptor>
```

The resulting signed SCCD works only on devices in [Developer Mode](https://docs.microsoft.com/en-us/windows/uwp/get-started/enable-your-device-for-development). 

## Summary

The following diagram summarizes the sequence described above:

![Getting an SCCD signed](images/signsccd.png)

## Resources

* [App capability declarations](https://docs.microsoft.com/windows/uwp/packaging/app-capability-declarations)
* [Custom Capability sample](https://github.com/Microsoft/Windows-universal-samples/tree/master/Samples/CustomCapability)
* [Getting Started with Universal Windows drivers](../develop/getting-started-with-universal-drivers.md)
* [Pairing a driver with a Universal Windows Platform (UWP) app](../install/pairing-app-and-driver-versions.md)

### SCCD XML Schema

The following is the formal XML XSD schema for an SCCD file.  Use this schema to validate your SCCD before submitting it for review.  See [Schema Cache](https://docs.microsoft.com/visualstudio/xml-tools/schema-cache) and [XML Document validation](https://docs.microsoft.com/visualstudio/xml-tools/xml-document-validation) for info on importing a schema and validating with IntelliSense.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema attributeFormDefault="unqualified" elementFormDefault="qualified"
  xmlns:xs="http://www.w3.org/2001/XMLSchema"
  targetNamespace="http://schemas.microsoft.com/appx/2016/sccd"
  xmlns:s="http://schemas.microsoft.com/appx/2016/sccd"
  xmlns="http://schemas.microsoft.com/appx/2016/sccd">

  <xs:element name="CustomCapabilityDescriptor" type="CT_CustomCapabilityDescriptor">
    <xs:unique name="Unique_CustomCapability_Name">
      <xs:selector xpath="s:CustomCapabilities/s:CustomCapability"/>
      <xs:field xpath="@Name"/>
    </xs:unique>
  </xs:element>

  <xs:complexType name="CT_CustomCapabilityDescriptor">
    <xs:sequence>
      <xs:element ref="CustomCapabilities" minOccurs="1" maxOccurs="1"/>
      <xs:element ref="AuthorizedEntities" minOccurs="1" maxOccurs="1"/>
      <xs:element ref="DeveloperModeOnly" minOccurs="0" maxOccurs="1"/>
      <xs:element ref="Catalog" minOccurs="1" maxOccurs="1"/>
      <xs:any minOccurs="0"/>
    </xs:sequence>
  </xs:complexType>

  <xs:element name="CustomCapabilities" type="CT_CustomCapabilities" />

  <xs:complexType name="CT_CustomCapabilities">
    <xs:sequence>
      <xs:element ref="CustomCapability" minOccurs="1" maxOccurs="unbounded"/>
    </xs:sequence>
  </xs:complexType>

  <xs:element name="CustomCapability">
    <xs:complexType>
      <xs:attribute name="Name" type="ST_CustomCapability" use="required"/>
    </xs:complexType>
  </xs:element>

  <xs:simpleType name="ST_NonEmptyString">
    <xs:restriction base="xs:string">
      <xs:minLength value="1"/>
      <xs:maxLength value="32767"/>
      <xs:pattern value="[^\s]|([^\s].*[^\s])"/>
    </xs:restriction>
  </xs:simpleType>

  <xs:simpleType name="ST_CustomCapability">
    <xs:annotation>
      <xs:documentation>Custom capabilities should be a string in the form of Company.capabilityName_PublisherId</xs:documentation>
    </xs:annotation>
    <xs:restriction base="ST_NonEmptyString">
      <xs:pattern value="[A-Za-z0-9][-_.A-Za-z0-9]*_[a-hjkmnp-z0-9]{13}"/>
      <xs:minLength value="15"/>
      <xs:maxLength value="255"/>
    </xs:restriction>
  </xs:simpleType>

  <xs:element name="AuthorizedEntities" type="CT_AuthorizedEntities" />

  <xs:complexType name="CT_AuthorizedEntities">
    <xs:sequence>
      <xs:element ref="AuthorizedEntity" minOccurs="1" maxOccurs="unbounded"/>
    </xs:sequence>
  </xs:complexType>

  <xs:element name="AuthorizedEntity" type="CT_AuthorizedEntity" />

  <xs:complexType name="CT_AuthorizedEntity">
    <xs:attribute name="CertificateSignatureHash" type="ST_CertificateSignatureHash" use="required"/>
    <xs:attribute name="AppPackageFamilyName" type="ST_NonEmptyString" use="required"/>
  </xs:complexType>

  <xs:simpleType name="ST_CertificateSignatureHash">
    <xs:restriction base="ST_NonEmptyString">
      <xs:pattern value="[A-Fa-f0-9]+"/>
      <xs:minLength value="64"/>
      <xs:maxLength value="64"/>
    </xs:restriction>
  </xs:simpleType>

  <xs:element name="DeveloperModeOnly">
    <xs:complexType>
      <xs:attribute name="Value" type="xs:boolean" use="required"/>
    </xs:complexType>
  </xs:element>

  <xs:element name="Catalog" type="ST_Catalog" />

  <xs:simpleType name="ST_Catalog">
    <xs:restriction base="xs:string">
      <xs:pattern value="[A-Za-z0-9\+\/\=]+"/>
      <xs:minLength value="4"/>
    </xs:restriction>
  </xs:simpleType>

</xs:schema>
```
