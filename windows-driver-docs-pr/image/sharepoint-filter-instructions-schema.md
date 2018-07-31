---
title: Sharepoint Filter Instructions Schema
description: Sharepoint Filter Instructions Schema
ms.assetid: 084da70e-6e3a-4ac1-8e35-c48745a6d564
keywords: ["Sharepoint Filter Instructions Schema"]
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# Sharepoint Filter Instructions Schema


You can use the following schema for post-scan filtering for Microsoft Sharepoint destinations.

```
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:spf="http://schemas.microsoft.com/windows/2007/10/imaging/postscan/filter/sharepoint"
        xmlns:xs="http://www.w3.org/2001/XMLSchema"
        targetNamespace="http://schemas.microsoft.com/windows/2007/10/imaging/postscan/filter/sharepoint"
        elementFormDefault="qualified">
    <xs:annotation>
        <xs:documentation>
            WSD Enterprise Scanning - SharePoint filter Instructions schema
            Copyright 2007 Microsoft Corp. All rights reserved
        </xs:documentation>
    </xs:annotation>

    <xs:annotation>
        <xs:documentation>
            Define the XML Elements that represent the Filter configuration for SharePoint integration.
        </xs:documentation>
    </xs:annotation>
    <xs:element name="SharePointConfig" type="spf:SharePointConfigType" />
    <xs:complexType name="SharePointConfigType">
        <xs:sequence>
            <xs:element name="SaveToMySite" type="spf:BoolExtType" minOccurs="0" />
            <xs:element name="SaveToSharePointSites" type="spf:SharePointSitesType" minOccurs="0" />
            <xs:any namespace="##other" minOccurs="0" maxOccurs="unbounded"/>
        </xs:sequence>
        <xs:anyAttribute namespace="##other" processContents="lax"/>
    </xs:complexType>
    <xs:complexType name="SharePointSitesType">
        <xs:sequence>
            <xs:element name="SaveToSharePointSiteURL" type="spf:String2048ExtType" maxOccurs="unbounded"/>
            <xs:any namespace="##other" minOccurs="0" maxOccurs="unbounded"/>
        </xs:sequence>
        <xs:anyAttribute namespace="##other" processContents="lax"/>
    </xs:complexType>
    <xs:annotation>
        <xs:documentation>Extensions to basic element types to allow IHV extensibility</xs:documentation>
    </xs:annotation>
    <xs:complexType name="BoolExtType">
        <xs:simpleContent>
            <xs:extension base="xs:boolean">
                <xs:anyAttribute namespace="##other" processContents="lax"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
    <xs:complexType name="String2048ExtType">
        <xs:simpleContent>
            <xs:extension base="spf:String2048BaseType">
                <xs:anyAttribute namespace="##other" processContents="lax"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
    <xs:simpleType name="String2048BaseType">
        <xs:restriction base="xs:string">
            <xs:maxLength value="2048"/>
            <xs:whiteSpace value="preserve"/>
        </xs:restriction>
    </xs:simpleType>

</xs:schema>
```

The DSM Sharepoint Filter Instruction Schema supports the following element:

[SharePointConfig](sharepointconfig.md)

 

 





