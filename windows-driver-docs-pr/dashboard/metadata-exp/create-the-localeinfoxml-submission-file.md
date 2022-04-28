---
title: Create the LocaleInfo.xml Submission File
description: Create the LocaleInfo.xml Submission File
ms.topic: article
ms.date: 04/20/2017
---

# Create the LocaleInfo.xml Submission File

## LocaleInfo XML Schema

A device manifest submission package must contain one LocaleInfo.xml document, which has information that the Partner Center uses to validate the locale information in the device metadata package.

The data in the LocaleInfo.xml document is formatted based on the LocaleInfo XML schema, which is described below.

> [!NOTE]
> The XML document must be saved by using UTF-8 encoding.

For more information about address ranges, see [How to Create a Device Metadata Package for Devices and Printers](/previous-versions/windows/hardware/metadata/dn465877(v=vs.85)).

### LocaleInfo XML Schema NameSpace

The following is the namespace of the LocaleInfo XML schema: `http://schemas.microsoft.com/Windows/2010/08/MetadataSubmission/LocaleInfo`

### Overview of LocaleInfo XML Elements/Attributes

The following table describes the metadata elements and attributes of the LocaleInfo XML schema.

|Element/Attributes|Element/Attribute type|Required/ optional|
|----|----|----|
|MultipleLocale|xs:boolean|Optional|
|LocaleDeclaredInPackageInfo|tns:LocaleDeclaredInPackageInfoType|Optional|
|default|xs:boolean|Required|
|SupportedLocaleList|tns:SupportedLocaleListType|Optional|
|Locale|xs:string|Optional|

### LocaleInfo XML Schema Definition

The following is the LocaleInfo XML schema definition:

``` syntax
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema targetNamespace="http://schemas.microsoft.com/Windows/2010/08/MetadataSubmission/LocaleInfo" xmlns:tns="http://schemas.microsoft.com/Windows/2010/08/MetadataSubmission/LocaleInfo" xmlns:xs="http://www.w3.org/2001/XMLSchema" elementFormDefault="qualified" blockDefault="#all">

 <xs:element name="LocaleInfo" type="tns:LocaleInfoType" />

 <xs:complexType name="LocaleInfoType">
  <xs:sequence>
   <xs:element name="MultipleLocale" type="xs:boolean" />
   <xs:element name="LocaleDeclaredInPackageInfo" type="tns:LocaleDeclaredInPackageInfoType" />
   <xs:element name="SupportedLocaleList" type="tns:SupportedLocaleListType" minOccurs="0" />
   <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
  </xs:sequence>
 </xs:complexType>

  <xs:complexType name="LocaleDeclaredInPackageInfoType">
    <xs:simpleContent>
      <xs:extension base="xs:string">
        <xs:attribute name="default" type="xs:boolean" use="required" />
      </xs:extension>
    </xs:simpleContent>
  </xs:complexType>

  <xs:complexType name="SupportedLocaleListType">
    <xs:sequence>
      <xs:element name="Locale" type="xs:string" maxOccurs="unbounded" />
      <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
    </xs:sequence>
  </xs:complexType>

</xs:schema>
```

## LocaleInfo XML Schema Reference

The LocaleInfo XML schema defines the following elements and attributes:

- LocaleInfo
  - MultipleLocale
  - LocaleDeclaredInPackageInfo
    - default
  - SupportedLocaleList
    - Locale

### MultipleLocale Element

The MultipleLocale element specifies if the device metadata package supports multiple locales. The Partner Center uses this value to properly validate the package.

``` syntax
<xs:element name="MultipleLocale" type="xs:boolean" />
```

#### Remarks (MultipleLocale element)

The MultipleLocale element must be “true” if more than one locale is supported in the device metadata package. The element can be “true” or “false” if the device metadata package only supports one locale. The value of MultipleLocale must match the value specified in PackageInfo.xml.

### LocaleDeclaredInPackageInfo Element

The LocaleDeclaredInPackageInfo element specifies information about the locale and package attributes declared in the device metadata package. The Partner Center uses this information to properly validate the declared locale metadata in the device metadata package.

``` syntax
<xs:element name="LocaleDeclaredInPackageInfo" type="tns:LocaleDeclaredInPackageInfoType" />

<xs:complexType name="LocaleDeclaredInPackageInfoType">
  <xs:simpleContent>
    <xs:extension base="xs:string">
      <xs:attribute name="default" type="xs:boolean" use="required" />
    </xs:extension>
  </xs:simpleContent>
</xs:complexType>
```

#### Remarks (LocaleDeclaredInPackageInfo element)

The LocaleDeclaredInPackageInfo element must match the locale value specified in PackageInfo.xml.

### default Attribute

The default attribute specifies if the device metadata package is a default package, as indicated in PackageInfo.xml.

``` syntax
<xs:attribute name="default" type="xs:boolean" use="required" />
```

#### Remarks (default element)

The default element must match the default value specified in PackageInfo.xml.

### SupportedLocaleList Element

The SupportedLocaleList element specifies which other locales are supported in the device metadata package. The Partner Center uses this information to properly validate the additional locale metadata in the device metadata package.

``` syntax
<xs:element name="SupportedLocaleList" type="tns:SupportedLocaleListType" minOccurs="0" />

<xs:complexType name="SupportedLocaleListType">
  <xs:sequence>
    <xs:element name="Locale" type="xs:string" maxOccurs="unbounded" />
    <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
  </xs:sequence>
</xs:complexType>
```

### Locale Element

The Locale element specifies an extra locale that is supported in the device metadata package. See SupportedLocaleList Element for more information about how the Partner Center uses this value.

## LocaleInfo XML Example

The following XML document uses the LocaleInfo XML schema to specify the components of LocaleInfo information.

This example applies to a device metadata package that supports the en-US, ja-JP, and fr-FR locales. It lists the en-US locale in PackageInfo.xml and is a default locale package, as indicated in PackageInfo.xml.

``` syntax
<?xml version="1.0" encoding="utf-8"?>
<LocaleInfo xmlns="http://schemas.microsoft.com/Windows/2010/08/MetadataSubmission/LocaleInfo">
  
  <MultipleLocale>
    true
  </MultipleLocale>
  
  <LocaleDeclaredInPackageInfo default="true">
    en-US
  </LocaleDeclaredInPackageInfo>
  
  <SupportedLocaleList>
    <Locale>en-US</Locale>
    <Locale>ja-JP</Locale>
    <Locale>fr-FR</Locale>
  </SupportedLocaleList>
  
</LocaleInfo>
```
