---
title: Fileshare Filter Instructions Schema
description: Fileshare Filter Instructions Schema
MS-HAID:
- 'dsm\_ref\_psp\_f8445689-1f90-4590-bcf9-71f1bd630ed4.xml'
- 'image.fileshare\_filter\_instructions\_schema'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 7168765a-9f2e-47ab-983c-9711f70cd4e5
keywords: ["Fileshare Filter Instructions Schema"]
---

# Fileshare Filter Instructions Schema


You can use the following schema for post-scan filtering for fileshare destinations.

```
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:fsf="http://schemas.microsoft.com/windows/2007/10/imaging/postscan/filter/fileshare"
        xmlns:xs="http://www.w3.org/2001/XMLSchema"
        targetNamespace="http://schemas.microsoft.com/windows/2007/10/imaging/postscan/filter/fileshare"
        elementFormDefault="qualified">
    <xs:annotation>
        <xs:documentation>
            WSD Enterprise Scanning - File Share filter Instructions schema
            Copyright 2007 Microsoft Corp. All rights reserved
        </xs:documentation>
    </xs:annotation>

    <xs:annotation>
        <xs:documentation>
            Define the XML Elements that represent the Filter configuration for File Shares.
        </xs:documentation>
    </xs:annotation>
    <xs:element name="FileShareConfig" type="fsf:FileShareConfigType" />
    <xs:complexType name="FileShareConfigType">
        <xs:sequence>
            <xs:element name="FileShares" type="fsf:FileShareType" minOccurs="0"/>
            <xs:any namespace="##other" minOccurs="0" maxOccurs="unbounded"/>
        </xs:sequence>
        <xs:anyAttribute namespace="##other" processContents="lax"/>
    </xs:complexType>
    <xs:complexType name="FileShareType">
        <xs:sequence>
            <xs:element name="ShareUNC" type="fsf:String255ExtType" maxOccurs="unbounded"/>
            <xs:any namespace="##other" minOccurs="0" maxOccurs="unbounded"/>
        </xs:sequence>
        <xs:anyAttribute namespace="##other" processContents="lax"/>
    </xs:complexType>

    <xs:annotation>
        <xs:documentation>Extensions to basic element types to allow IHV extensibility</xs:documentation>
    </xs:annotation>
    <xs:complexType name="String255ExtType">
        <xs:simpleContent>
            <xs:extension base="fsf:String255BaseType">
                <xs:anyAttribute namespace="##other" processContents="lax"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
    <xs:simpleType name="String255BaseType">
        <xs:restriction base="xs:string">
            <xs:maxLength value="255"/>
            <xs:whiteSpace value="preserve"/>
        </xs:restriction>
    </xs:simpleType>

</xs:schema>
```

The DSM Fileshare Filter Instruction Schema supports the following element:

[FileShareConfig](fileshareconfig.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Fileshare%20Filter%20Instructions%20Schema%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




