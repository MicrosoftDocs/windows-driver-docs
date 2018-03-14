---
title: Fileshare Filter Instructions Schema
description: Fileshare Filter Instructions Schema
ms.assetid: 7168765a-9f2e-47ab-983c-9711f70cd4e5
keywords: ["Fileshare Filter Instructions Schema"]
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 





