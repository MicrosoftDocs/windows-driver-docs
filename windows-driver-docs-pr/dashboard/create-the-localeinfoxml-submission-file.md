---
title: Create the LocaleInfo.xml Submission File
description: Create the LocaleInfo.xml Submission File
ms.assetid: 2b16b045-4d34-418c-8f68-7f688adf8e7e
ms.topic: article
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Create the LocaleInfo.xml Submission File


## <span id="LocaleInfo_XML_Schema"></span><span id="localeinfo_xml_schema"></span><span id="LOCALEINFO_XML_SCHEMA"></span>LocaleInfo XML Schema


A device manifest submission package must contain one LocaleInfo.xml document, which has information that the Hardware Dev Center Dashboard uses to validate the locale information in the device metadata package.

The data in the LocaleInfo.xml document is formatted based on the LocaleInfo XML schema, which is described below.

**Note**  
 The XML document must be saved by using UTF-8 encoding.

 

For more information about address ranges, see [How to Create a Device Metadata Package for Devices and Printers](http://go.microsoft.com/fwlink/?LinkId=253559).

### <span id="LocaleInfo_XML_Schema_NameSpace"></span><span id="localeinfo_xml_schema_namespace"></span><span id="LOCALEINFO_XML_SCHEMA_NAMESPACE"></span>LocaleInfo XML Schema NameSpace

The following is the namespace of the LocaleInfo XML schema: **http://schemas.microsoft.com/Windows/2010/08/MetadataSubmission/LocaleInfo**

### <span id="Overview_of_LocaleInfo_XML_Elements_Attributes"></span><span id="overview_of_localeinfo_xml_elements_attributes"></span><span id="OVERVIEW_OF_LOCALEINFO_XML_ELEMENTS_ATTRIBUTES"></span>Overview of LocaleInfo XML Elements/Attributes

The following table describes the metadata elements and attributes of the LocaleInfo XML schema.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Element/Attributes</th>
<th>Element/Attribute type</th>
<th>Required/ optional</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>MultipleLocale</p></td>
<td><p>xs:boolean</p></td>
<td><p>Optional</p></td>
</tr>
<tr class="even">
<td><p>LocaleDeclaredInPackageInfo</p></td>
<td><p>tns:LocaleDeclaredInPackageInfoType</p></td>
<td><p>Optional</p></td>
</tr>
<tr class="odd">
<td><p>default</p></td>
<td><p>xs:boolean</p></td>
<td><p>Required</p></td>
</tr>
<tr class="even">
<td><p>SupportedLocaleList</p></td>
<td><p>tns:SupportedLocaleListType</p></td>
<td><p>Optional</p></td>
</tr>
<tr class="odd">
<td><p>Locale</p></td>
<td><p>xs:string</p></td>
<td><p>Optional</p></td>
</tr>
</tbody>
</table>

 

### <span id="LocaleInfo_XML_Schema_Definition"></span><span id="localeinfo_xml_schema_definition"></span><span id="LOCALEINFO_XML_SCHEMA_DEFINITION"></span>LocaleInfo XML Schema Definition

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

## <span id="LocaleInfo_XML_Schema_Reference"></span><span id="localeinfo_xml_schema_reference"></span><span id="LOCALEINFO_XML_SCHEMA_REFERENCE"></span>LocaleInfo XML Schema Reference


The LocaleInfo XML schema defines the following elements and attributes:

-   LocaleInfo

    -   MultipleLocale

    -   LocaleDeclaredInPackageInfo

        -   default

    -   SupportedLocaleList

        -   Locale

### <span id="MultipleLocale_Element"></span><span id="multiplelocale_element"></span><span id="MULTIPLELOCALE_ELEMENT"></span>MultipleLocale Element

The MultipleLocale element specifies if the device metadata package supports multiple locales. The Hardware Dev Center Dashboard uses this value to properly validate the package.

``` syntax
<xs:element name="MultipleLocale" type="xs:boolean" />
```

**Remarks**

The MultipleLocale element must be “true” if more than one locale is supported in the device metadata package. The element can be “true” or “false” if the device metadata package only supports one locale. The value of MultipleLocale must match the value specified in PackageInfo.xml.

### <span id="LocaleDeclaredInPackageInfo_Element"></span><span id="localedeclaredinpackageinfo_element"></span><span id="LOCALEDECLAREDINPACKAGEINFO_ELEMENT"></span>LocaleDeclaredInPackageInfo Element

The LocaleDeclaredInPackageInfo element specifies information about the locale and package attributes declared in the device metadata package. The Hardware Dev Center Dashboard uses this information to properly validate the declared locale metadata in the device metadata package.

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

**Remarks**

The LocaleDeclaredInPackageInfo element must match the locale value specified in PackageInfo.xml.

### <span id="default_Attribute"></span><span id="default_attribute"></span><span id="DEFAULT_ATTRIBUTE"></span>default Attribute

The default attribute specifies if the device metadata package is a default package, as indicated in PackageInfo.xml.

``` syntax
<xs:attribute name="default" type="xs:boolean" use="required" />
```

**Remarks**

The default element must match the default value specified in PackageInfo.xml.

### <span id="SupportedLocaleList_Element"></span><span id="supportedlocalelist_element"></span><span id="SUPPORTEDLOCALELIST_ELEMENT"></span>SupportedLocaleList Element

The SupportedLocaleList element specifies which other locales are supported in the device metadata package. The Hardware Dev Center Dashboard uses this information to properly validate the additional locale metadata in the device metadata package.

``` syntax
<xs:element name="SupportedLocaleList" type="tns:SupportedLocaleListType" minOccurs="0" />

<xs:complexType name="SupportedLocaleListType">
  <xs:sequence>
    <xs:element name="Locale" type="xs:string" maxOccurs="unbounded" />
    <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
  </xs:sequence>
</xs:complexType>
```

### <span id="Locale_Element"></span><span id="locale_element"></span><span id="LOCALE_ELEMENT"></span>Locale Element

The Locale element specifies an extra locale that is supported in the device metadata package. See SupportedLocaleList Element for more information about how the Hardware Dev Center Dashboard uses this value.

## <span id="LocaleInfo_XML_Example"></span><span id="localeinfo_xml_example"></span><span id="LOCALEINFO_XML_EXAMPLE"></span>LocaleInfo XML Example


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

 

 





