---
title: SoftwareInfo XML Schema Definition
description: SoftwareInfo XML Schema Definition
ms.assetid: 7b09ffc6-0f69-4710-988b-4952823da72e
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# SoftwareInfo XML Schema Definition

[!include[MBAE deprecation warning](mbae-deprecation-warning.md)]

The following is the namespace of the SoftwareInfo XML schema:

``` syntax
http://schemas.microsoft.com/windows/2010/08/DeviceMetadata/SoftwareInfo
```

The following is a definition of the SoftwareInfo schema.

``` syntax
<?xml version="1.0" encoding ="UTF-8" ?>
  <xs:schema targetNamespace="http://schemas.microsoft.com/windows/2010/08/DeviceMetadata/SoftwareInfo"
             xmlns:tns="http://schemas.microsoft.com/windows/2010/08/DeviceMetadata/SoftwareInfo"
             xmlns:xs="http://www.w3.org/2001/XMLSchema" elementFormDefault="qualified" blockDefault="#all">

  <xs:element name="SoftwareInfo" type="tns:SoftwareInfoType" />

  <!-- Software Information Type Definition -->
  <xs:complexType name="SoftwareInfoType">
    <xs:choice>
      <xs:sequence>
        <xs:element name="DeviceCompanionApplications" type="tns:DeviceCompanionApplicationsType" />
        <xs:element name="PrivilegedApplications" type="tns:PrivilegedApplicationsType" minOccurs="0" />
        <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
      </xs:sequence>
      <xs:element name="PrivilegedApplications" type="tns:PrivilegedApplicationsType" />
    </xs:choice>
  </xs:complexType>

<!-- Device Companion Applications Definition -->
  <xs:complexType name="DeviceCompanionApplicationsType">
    <xs:sequence>
      <xs:element name="Package" type="tns:PackageType" maxOccurs="unbounded" />
      <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
    </xs:sequence>
  </xs:complexType>

<!-- PrivilegedApplications Definition -->
  <xs:complexType name="PrivilegedApplicationsType">
    <xs:choice>
      <xs:element name="AnyApplication" type="tns:AnyApplicationType" />
      <xs:element name="Package" type="tns:PackageForPrivilegedApplications" maxOccurs="unbounded" />
      <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
    </xs:choice>
  </xs:complexType>

<!-- Package Type Definition -->
  <xs:complexType name="PackageType">
    <xs:sequence>
        <xs:element name="Identity" type="tns:IdentityType" />
        <xs:element name="Applications" type="tns:ApplicationsType" />
      <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
    </xs:sequence>
  </xs:complexType>

<!-- Package Identity Type Definition -->
  <xs:complexType name="IdentityType">
    <xs:attribute name="Name" type="tns:PackageNameType" use="required"/>
    <xs:attribute name="Publisher" type="tns:PublisherType" use="required"/>
  </xs:complexType>

  <xs:simpleType name="PackageNameType">
    <xs:restriction base="tns:AsciiIdentifierType">
      <xs:minLength value="3"/>
      <xs:maxLength value="50"/>
    </xs:restriction>
  </xs:simpleType>

  <xs:simpleType name="PublisherType">
    <xs:restriction base="tns:DistinguishedNameType">
      <xs:maxLength value="8192"/>
    </xs:restriction>
  </xs:simpleType>

  <xs:simpleType name="DistinguishedNameType">
    <xs:restriction base="tns:NonEmptyStringType">
      <xs:pattern value="(CN|L|O|OU|E|C|S|STREET|T|G|I|SN|DC|SERIALNUMBER|(OID\.(0|[1-9][0-9]*)(\.(0|[1-9][0-9]*))+))=(([^,+=&quot;&lt;&gt;#;])+|&quot;.*&quot;)(, ((CN|L|O|OU|E|C|S|STREET|T|G|I|SN|DC|SERIALNUMBER|(OID\.(0|[1-9][0-9]*)(\.(0|[1-9][0-9]*))+))=(([^,+=&quot;&lt;&gt;#;])+|&quot;.*&quot;)))*"/>
    </xs:restriction>
  </xs:simpleType>

<!-- Applications Type Definition -->
  <xs:complexType name="ApplicationsType">
    <xs:sequence>
      <xs:element name="Application" type="tns:ApplicationType" />
      <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="ApplicationType">
    <xs:sequence>
      <xs:element name="DeviceNotificationHandlers" type="tns:DeviceNotificationHandlersType" minOccurs="0" />
      <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
    </xs:sequence>
    <xs:attribute name="Id" type="tns:ApplicationIdType" use="required"/>
  </xs:complexType>

  <xs:simpleType name="ApplicationIdType">
    <xs:restriction base="tns:AsciiWindowsIdType">
      <xs:maxLength value="64"/>
    </xs:restriction>
  </xs:simpleType>

  <!-- Device Notification Handlers Type Definition -->
  <xs:complexType name="DeviceNotificationHandlersType">
    <xs:sequence>
      <xs:element name="DeviceNotificationHandler" type="tns:DeviceNotificationHandlerType" maxOccurs="unbounded" />
      <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
    </xs:sequence>
  </xs:complexType>

  <!-- Device Notification Handler Type Definition -->
  <xs:complexType name="DeviceNotificationHandlerType">
    <xs:attribute name="EventID" type="xs:string" use="required"/>
    <xs:attribute name="EventAsset" type="xs:string" use="required"/>
  </xs:complexType>

<!-- Privileged Applications Definition -->
  <xs:complexType name ="AnyApplicationType"/>

  <xs:complexType name="PackageForPrivilegedApplications">
    <xs:sequence>
      <xs:element name="Identity" type="tns:IdentityForPrivilegedApplicationsType" />
      <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="IdentityForPrivilegedApplicationsType">
    <xs:attribute name="Name" type="tns:PackageNameType" use="required"/>
    <xs:attribute name="Publisher" type="tns:PublisherType" use="required"/>
    <xs:attribute name="AccessCustomDriver" type="xs:boolean" />
  </xs:complexType>

  <xs:simpleType name="AsciiIdentifierType">
    <xs:restriction base="tns:AllowedAsciiCharSetType">
      <xs:pattern value="[^_ ]+"/>
    </xs:restriction>
  </xs:simpleType>

  <!-- String Restriction Types definition -->
  <xs:simpleType name="AllowedAsciiCharSetType">
    <xs:restriction base="tns:NonEmptyStringType">
      <xs:pattern value="[-_. A-Za-z0-9]+"/>
    </xs:restriction>
  </xs:simpleType>

  <xs:simpleType name="NonEmptyStringType">
    <xs:restriction base="xs:string">
      <xs:minLength value="1"/>
      <xs:maxLength value="32767"/>
      <xs:pattern value="[^\s]|([^\s].*[^\s])"/>
    </xs:restriction>
  </xs:simpleType>

  <xs:simpleType name="AsciiWindowsIdType">
    <xs:restriction base="tns:NonEmptyStringType">
      <xs:pattern value="([A-Za-z][A-Za-z0-9]*)(\.[A-Za-z][A-Za-z0-9]*)*"/>
      <xs:maxLength value="255"/>
    </xs:restriction>
  </xs:simpleType>

  <xs:simpleType name="UnicodeIdentifierType">
    <xs:restriction base="tns:UnicodeIdentifierCharSetType" /> 
  </xs:simpleType>

  <xs:simpleType name="UnicodeIdentifierCharSetType">
  <xs:restriction base="tns:AllowedUnicodeCharSetType">
    <xs:pattern value="[^!#$%'()\*\+,/:;=\?@\[\\\]^_`\|]+" /> 
  </xs:restriction>
  </xs:simpleType>

  <xs:simpleType name="AllowedUnicodeCharSetType">
    <xs:restriction base="tns:UnicodeNoPrivateUseOrNonCharacterCodePointsType">
      <xs:pattern value="[^&quot;&&lt;&gt;\u0000-\u0020\u007F\u0080-\u009F\u00A0\u00AD\u0340-\u0341\u034F\u06DD\u070F\u1680\u1806\u180B-\u180E\u2000-\u200F\u2028-\u202F\u205F\u2060-\u2063\u206A-\u206F\u2FF0-\u2FFB\u3000\uD800-\uDFFF\uFEFF\p{IsVariationSelectors}]+"/>
    </xs:restriction>
  </xs:simpleType>

  <xs:simpleType name="UnicodeNoPrivateUseOrNonCharacterCodePointsType">
    <xs:restriction base="tns:NonEmptyStringType">
      <xs:pattern value="[^\uE000-\uF8FF\uFDD0-\uFDEF\uFFF9-\uFFFF\p{IsPrivateUse}]+"/>
    </xs:restriction>
  </xs:simpleType>

</xs:schema>

<?xml version="1.0" encoding ="UTF-8" ?>
  <xs:schema targetNamespace="http://schemas.microsoft.com/windows/2010/05/DeviceMetadata/ServiceInfo"
             xmlns:tns="http://schemas.microsoft.com/windows/2010/05/DeviceMetadata/ServiceInfo"
             xmlns:xs="http://www.w3.org/2001/XMLSchema"
             elementFormDefault="qualified"
             blockDefault="#all">

    <xs:element name="ServiceInfo" type="tns:ServiceInfoType" />

    <xs:complexType name="ServiceInfoType">
      <xs:sequence>
        <xs:element name="ServiceCategoryList" type="tns:ServiceCategoryListType" />
        <xs:element name="ServiceName" type="tns:ServiceNameType" minOccurs="0" />
        <xs:element name="ServiceDescription1" type="tns:ServiceDescriptionType" minOccurs="0" />
        <xs:element name="ServiceDescription2" type="tns:ServiceDescriptionType" minOccurs="0" />
        <xs:element name="ServiceNumber" type ="tns:ServiceNumberType" />
        <xs:element name="ServiceProvider" type="tns:ProviderNameType" />
        <xs:element name="ServiceIconFile" type="tns:ServiceIconFileType" minOccurs="0" />
        <xs:element name="ServiceSpecificExtension" type="tns:ServiceSpecificExtensionType" minOccurs="0" />
        <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
      </xs:sequence>
    </xs:complexType>

    <xs:complexType name="ServiceCategoryListType">
      <xs:sequence>
        <xs:element name="ServiceCategory" type="tns:ServiceCategoryType" maxOccurs="unbounded" />
        <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
      </xs:sequence>
    </xs:complexType>

    <xs:simpleType name="ServiceCategoryType">
      <xs:union memberTypes="tns:ServiceCategoryTypeEnumeration xs:string" />
    </xs:simpleType>

    <xs:simpleType name="ServiceCategoryTypeEnumeration">
      <xs:restriction base="xs:string" >
        <xs:enumeration value="Network" />
        <xs:enumeration value="Network.MobileBroadband" />
        <xs:enumeration value="Other" />
      </xs:restriction>
    </xs:simpleType>

    <xs:simpleType name="ServiceNameType">
      <xs:restriction base="xs:string">
        <xs:minLength value="0" />
        <xs:maxLength value="200" />
      </xs:restriction>
    </xs:simpleType>

    <xs:simpleType name="ServiceNumberType">
      <xs:union memberTypes="tns:GUIDType xs:string" />
    </xs:simpleType>

    <xs:simpleType name="ProviderNameType">
      <xs:restriction base="xs:string">
        <xs:minLength value="1" />
        <xs:maxLength value="20" />
      </xs:restriction>
    </xs:simpleType>

    <xs:simpleType name="ServiceDescriptionType">
      <xs:restriction base="xs:string">
        <xs:minLength value="1" />
        <xs:maxLength value="1024" />
      </xs:restriction>
    </xs:simpleType>

    <xs:simpleType name="ServiceIconFileType">
      <xs:restriction base="xs:string">
        <xs:pattern value=".+\.ico" />
      </xs:restriction>
    </xs:simpleType>

    <xs:simpleType name="GUIDType">
      <xs:restriction base="xs:string">
        <xs:pattern value="[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}" />
      </xs:restriction>
    </xs:simpleType>

    <xs:complexType name="ServiceSpecificExtensionType">
      <xs:simpleContent>
        <xs:extension base="xs:string">
          <xs:attribute name="namespace" type="xs:anyURI" use="required" />
        </xs:extension>
      </xs:simpleContent>
    </xs:complexType>

</xs:schema>
```

 

 





