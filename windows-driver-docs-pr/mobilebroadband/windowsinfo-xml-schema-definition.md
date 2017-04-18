---
title: WindowsInfo XML Schema Definition
description: WindowsInfo XML Schema Definition
ms.assetid: d14e0537-0b95-4986-a11c-67645bd88b26
---

# WindowsInfo XML Schema Definition


The following are the namespaces of the WindowsInfo XML schema:

``` syntax
http://schemas.microsoft.com/windows/DeviceMetadata/WindowsInfo/2007/11/
http://schemas.microsoft.com/windows/2010/08/DeviceMetadata/WindowsInfov2
```

The following is a definition of the WindowsInfo XML schema:

``` syntax
<?xml version="1.0" encoding="UTF-8"?>

<xs:schema targetNamespace="http://schemas.microsoft.com/windows/DeviceMetadata/WindowsInfo/2007/11/"
           xmlns:tns="http://schemas.microsoft.com/windows/DeviceMetadata/WindowsInfo/2007/11/"
           xmlns:v2="http://schemas.microsoft.com/windows/2010/08/DeviceMetadata/WindowsInfov2"
           xmlns:xs="http://www.w3.org/2001/XMLSchema" elementFormDefault="qualified" blockDefault="#all">

  <xs:element name="WindowsInfo" type="tns:WindowsInfoType" />

  <xs:complexType name="WindowsInfoType">
    <xs:sequence>
      <xs:element name="ShowDeviceInDisconnectedState" type="xs:boolean" default="false" />
      <xs:element name="LaunchDeviceStageOnDeviceConnect" type="xs:boolean" default="false" minOccurs="0" />
      <xs:element name="LaunchDeviceStageFromExplorer" type="xs:boolean" default="false" minOccurs="0" />
    </xs:sequence>
  </xs:complexType>

</xs:schema> 
```

The following is a definition of the WindowsInfov2 XML schema:

``` syntax
<?xml version="1.0" encoding="UTF-8"?>

<xs:schema targetNamespace="http://schemas.microsoft.com/windows/2010/08/DeviceMetadata/WindowsInfov2"
           xmlns:tns="http://schemas.microsoft.com/windows/2010/08/DeviceMetadata/WindowsInfov2"
           xmlns:xs="http://www.w3.org/2001/XMLSchema" elementFormDefault="qualified" blockDefault="#all">

  <xs:element name="LaunchApplicationOnDeviceConnect" type ="tns:LaunchApplicationOnDeviceConnectType" />
  <xs:element name="WindowsHardwareLogoCertified" type="tns:WindowsHardwareLogoCertifiedType" />
  <xs:element name="EnableAutoPlayForRegisteredApps" type="xs:boolean" default="false" />


  <!-- LaunchApplicationOnDeviceConnectType Definition-->
  <xs:complexType name="LaunchApplicationOnDeviceConnectType">
    <xs:choice>
      <xs:element name="AutoplayHandler" type="tns:AutoplayHandlerType" />
      <xs:element name="DesktopAutoplayHandler" type="xs:string" />
      <xs:any namespace="##other" processContents="lax" />
    </xs:choice>
  </xs:complexType>

  <!-- Autoplay Handler Type Definition-->
  <xs:complexType name="AutoplayHandlerType">
    <xs:sequence>
      <xs:element name="PackageIdentity" type="tns:PackageIdentityType" />
      <xs:element name="Application" type="tns:ApplicationType" />
      <xs:element name="Verb" type="tns:VerbType" />
      <xs:element name="AutoplayType" type="tns:AutoplayTypeType" />
      <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
    </xs:sequence>
  </xs:complexType>


<!-- Package Identity Type Definition -->
  <xs:complexType name="PackageIdentityType">
    <xs:attribute name="Name" type="tns:PackageNameType" use="required" />
    <xs:attribute name="Publisher" type="tns:PublisherType" use="required" />
  </xs:complexType>

  <xs:simpleType name="PackageNameType">
    <xs:restriction base="tns:AsciiIdentifierType">
      <xs:minLength value="3"/>
      <xs:maxLength value="50"/>
    </xs:restriction>
  </xs:simpleType>

  <xs:simpleType name="AsciiIdentifierType">
    <xs:restriction base="tns:AllowedAsciiCharSetType">
      <xs:pattern value="[^_ ]+"/>
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
  
  <xs:simpleType name="AutoplayTypeType">
    <xs:restriction base="xs:string">
       <xs:enumeration value="Device" />
       <xs:enumeration value="Content" />
    </xs:restriction>
  </xs:simpleType>

<!-- Applications Type Definition -->
  <xs:complexType name="ApplicationType">
    <xs:attribute name="Id" type="tns:ApplicationIdType" use="required"/>
  </xs:complexType>

  <xs:simpleType name="ApplicationIdType">
    <xs:restriction base="tns:AsciiWindowsIdType">
      <xs:maxLength value="64"/>
    </xs:restriction>
  </xs:simpleType>


  <!--AUTO-PLAY EXTENSION SCHEMA Types-->
  <xs:simpleType name="VerbType">
    <xs:restriction base="tns:AllowedAsciiCharSetType">
      <xs:pattern value="[^ ]+"/>
      <xs:maxLength value="64"/>
    </xs:restriction>
  </xs:simpleType>

  <!-- WindowsHardwareLogoCertifiedType Definition-->
  <xs:complexType name="WindowsHardwareLogoCertifiedType">
  </xs:complexType>
  
  <!-- String Restriction Types definition -->
  <xs:simpleType name="AllowedAsciiCharSetType">
    <xs:restriction base="tns:NonEmptyStringType">
      <xs:pattern value="[-_. A-Za-z0-9]+"/>
    </xs:restriction>
  </xs:simpleType>

  <xs:simpleType name="AsciiWindowsIdType">
    <xs:restriction base="tns:NonEmptyStringType">
      <xs:pattern value="([A-Za-z][A-Za-z0-9]*)(\.[A-Za-z][A-Za-z0-9]*)*"/>
      <xs:maxLength value="255"/>
    </xs:restriction>
  </xs:simpleType>
  
  <xs:simpleType name="NonEmptyStringType">
    <xs:restriction base="xs:string">
      <xs:minLength value="1"/>
      <xs:maxLength value="32767"/>
      <xs:pattern value="[^\s]|([^\s].*[^\s])"/>
    </xs:restriction>
  </xs:simpleType>
  
</xs:schema>
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20WindowsInfo%20XML%20Schema%20Definition%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




