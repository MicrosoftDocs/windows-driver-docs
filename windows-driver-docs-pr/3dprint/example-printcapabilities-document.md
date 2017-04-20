---
title: PrintCapabilities document example
author: windows-driver-content
description: The keywords used in the following example are for illustration only, although they generally conform to the Print Schema keywords for 3D manufacturing.
ms.assetid: 0FCEFC25-C22F-44BD-9693-B3DBE6F6D314
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# PrintCapabilities document example


The keywords used in the following example are for illustration only, although they generally conform to the Print Schema keywords for 3D manufacturing.

```
<?xml version="1.0" encoding="UTF-8" ?>
<psf:PrintCapabilities
    xmlns:psf="http://schemas.microsoft.com/windows/2003/08/printing/printschemaframework"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema" version="1"
    xmlns:ns0000="http://schemas.microsoft.com/windows/printing/oemdriverpt/3dprinter"
    xmlns:psk="http://schemas.microsoft.com/windows/2003/08/printing/printschemakeywords"
    xmlns:psk3d="http://schemas.microsoft.com/3dmanufacturing/2013/01/pskeywords3d"
    xmlns:vnd="http://foo">

    <psf:Property name="psk3d:Job3DOutputArea">
        <psf:Property name="psk3d:Job3DOutputAreaWidth">
            <psf:Value xsi:type="xsd:integer">150000</psf:Value>
        </psf:Property>
        <psf:Property name="psk3d:Job3DOutputAreaDepth">
            <psf:Value xsi:type="xsd:integer">150000</psf:Value>
        </psf:Property>
        <psf:Property name="psk3d:Job3DOutputAreaHeight">
            <psf:Value xsi:type="xsd:integer">150000</psf:Value>
        </psf:Property>
    </psf:Property>

    <psf:Property name="psk3d:Job3DKnownObjectTypes">
        <psf:Value xsi:type="xsd:QName">psk3d:MeshOnly</psf:Value>
    </psf:Property>

    <psf:Property name="psk3d:Job3DMaterialCount">
        <psf:Value xsi:type="xsd:integer">5</psf:Value>
    </psf:Property>
    <psf:Property name="psk3d:Job3DMaterials">
        <psf:Property name="vnd:A">
            <psf:Property name="psk:DisplayName">
                <psf:Value xsi:type="xsd:string">Material A</psf:Value>
            </psf:Property>
            <psf:Property name="psk3d:MaterialColor">
                <psf:Value xsi:type="xsd:string">#FFFFFFFF</psf:Value>
            </psf:Property>
        </psf:Property>
        <psf:Property name="vnd:B">
            <psf:Property name="psk:DisplayName">
                <psf:Value xsi:type="xsd:string">Material B</psf:Value>
            </psf:Property>
            <psf:Property name="psk3d:MaterialColor">
                <psf:Value xsi:type="xsd:string">#FF000000</psf:Value>
            </psf:Property>
        </psf:Property>
        <psf:Property name="vnd:C">
            <psf:Property name="psk:DisplayName">
                <psf:Value xsi:type="xsd:string">Material C</psf:Value>
            </psf:Property>
            <psf:Property name="psk3d:MaterialColor">
                <psf:Value xsi:type="xsd:string">#FF000000</psf:Value>
            </psf:Property>
        </psf:Property>
        <psf:Property name="vnd:D">
            <psf:Property name="psk:DisplayName">
                <psf:Value xsi:type="xsd:string">Material D</psf:Value>
            </psf:Property>
            <psf:Property name="psk3d:MaterialColor">
                <psf:Value xsi:type="xsd:string">#FF000000</psf:Value>
            </psf:Property>
        </psf:Property>
        <psf:Property name="vnd:E">
            <psf:Property name="psk:DisplayName">
                <psf:Value xsi:type="xsd:string">Material E</psf:Value>
            </psf:Property>
            <psf:Property name="psk3d:MaterialColor">
                <psf:Value xsi:type="xsd:string">#FF000000</psf:Value>
            </psf:Property>
        </psf:Property>
    </psf:Property>
    
    <psf:ParameterDef name="vnd:Job3DAMap">
        <psf:Property name="psf:DataType">
            <psf:Value xsi:type="xsd:QName">xsd:string</psf:Value>
        </psf:Property>
        <psf:Property name="psf:MinLength">
            <psf:Value xsi:type="xsd:integer">1</psf:Value>
        </psf:Property>
        <psf:Property name="psf:MaxLength">
            <psf:Value xsi:type="xsd:integer">1024</psf:Value>
        </psf:Property>
        <psf:Property name="psf:Mandatory">
            <psf:Value xsi:type="xsd:QName">psk:Optional</psf:Value>
        </psf:Property>
        <psf:Property name="psf:UnitType">
            <psf:Value xsi:type="xsd:string">characters</psf:Value>
        </psf:Property>
        <psf:Property name="psk3d:Job3DMaterialSelected">
            <psf:Value xsi:type="xsd:QName">vnd:A</psf:Value>
        </psf:Property>
    </psf:ParameterDef>
    <psf:ParameterDef name="vnd:Job3DBMap">
        <psf:Property name="psf:DataType">
            <psf:Value xsi:type="xsd:QName">xsd:string</psf:Value>
        </psf:Property>
        <psf:Property name="psf:MinLength">
            <psf:Value xsi:type="xsd:integer">1</psf:Value>
        </psf:Property>
        <psf:Property name="psf:MaxLength">
            <psf:Value xsi:type="xsd:integer">1024</psf:Value>
        </psf:Property>
        <psf:Property name="psf:Mandatory">
            <psf:Value xsi:type="xsd:QName">psk:Optional</psf:Value>
        </psf:Property>
        <psf:Property name="psf:UnitType">
            <psf:Value xsi:type="xsd:string">characters</psf:Value>
        </psf:Property>
        <psf:Property name="psk3d:Job3DMaterialSelected">
            <psf:Value xsi:type="xsd:QName">vnd:B</psf:Value>
        </psf:Property>
    </psf:ParameterDef>
    <psf:ParameterDef name="vnd:Job3DCMap">
        <psf:Property name="psf:DataType">
            <psf:Value xsi:type="xsd:QName">xsd:string</psf:Value>
        </psf:Property>
        <psf:Property name="psf:MinLength">
            <psf:Value xsi:type="xsd:integer">1</psf:Value>
        </psf:Property>
        <psf:Property name="psf:MaxLength">
            <psf:Value xsi:type="xsd:integer">1024</psf:Value>
        </psf:Property>
        <psf:Property name="psf:Mandatory">
            <psf:Value xsi:type="xsd:QName">psk:Optional</psf:Value>
        </psf:Property>
        <psf:Property name="psf:UnitType">
            <psf:Value xsi:type="xsd:string">characters</psf:Value>
        </psf:Property>
        <psf:Property name="psk3d:Job3DMaterialSelected">
            <psf:Value xsi:type="xsd:QName">vnd:C</psf:Value>
        </psf:Property>
    </psf:ParameterDef>
    <psf:ParameterDef name="vnd:Job3DDMap">
        <psf:Property name="psf:DataType">
            <psf:Value xsi:type="xsd:QName">xsd:string</psf:Value>
        </psf:Property>
        <psf:Property name="psf:MinLength">
            <psf:Value xsi:type="xsd:integer">1</psf:Value>
        </psf:Property>
        <psf:Property name="psf:MaxLength">
            <psf:Value xsi:type="xsd:integer">1024</psf:Value>
        </psf:Property>
        <psf:Property name="psf:Mandatory">
            <psf:Value xsi:type="xsd:QName">psk:Optional</psf:Value>
        </psf:Property>
        <psf:Property name="psf:UnitType">
            <psf:Value xsi:type="xsd:string">characters</psf:Value>
        </psf:Property>
        <psf:Property name="psk3d:Job3DMaterialSelected">
            <psf:Value xsi:type="xsd:QName">vnd:D</psf:Value>
        </psf:Property>
    </psf:ParameterDef>
    <psf:ParameterDef name="vnd:Job3DEMap">
        <psf:Property name="psf:DataType">
            <psf:Value xsi:type="xsd:QName">xsd:string</psf:Value>
        </psf:Property>
        <psf:Property name="psf:MinLength">
            <psf:Value xsi:type="xsd:integer">1</psf:Value>
        </psf:Property>
        <psf:Property name="psf:MaxLength">
            <psf:Value xsi:type="xsd:integer">1024</psf:Value>
        </psf:Property>
        <psf:Property name="psf:Mandatory">
            <psf:Value xsi:type="xsd:QName">psk:Optional</psf:Value>
        </psf:Property>
        <psf:Property name="psf:UnitType">
            <psf:Value xsi:type="xsd:string">characters</psf:Value>
        </psf:Property>
        <psf:Property name="psk3d:Job3DMaterialSelected">
            <psf:Value xsi:type="xsd:QName">vnd:E</psf:Value>
        </psf:Property>
    </psf:ParameterDef>

    <psf:Feature name="psk3d:Job3DQuality">
        <psf:Property name="SelectionType">
            <psf:Value xsi:type="xsd:QName">psk:PickOne</psf:Value>
        </psf:Property>
        <psf:Option name="psk3d:Draft" />
        <psf:Option name="psk3d:Medium" />
        <psf:Option name="psk3d:High" />
    </psf:Feature>

    <psf:Feature name="psk3d:Job3DDensity">
        <psf:Property name="SelectionType">
            <psf:Value xsi:type="xsd:QName">psk:PickOne</psf:Value>
        </psf:Property>
        <psf:Option name="psk3d:Hollow"/>
        <psf:Option name="psk3d:Low"/>
        <psf:Option name="psk3d:Medium"/>
        <psf:Option name="psk3d:High"/>
        <psf:Option name="psk3d:Solid"/>
    </psf:Feature>

    <psf:Feature name="psk3d:Job3DSupports">
        <psf:Property name="SelectionType">
            <psf:Value xsi:type="xsd:QName">psk:PickOne</psf:Value>
        </psf:Property>
        <psf:Option name="psk3d:SupportsIncluded" />
        <psf:Option name="psk3d:SupportsExcluded" />
    </psf:Feature>

    <psf:ParameterDef name="psk3d:Job3DSupportsMaterial">
        <psf:Property name="psf:DataType">
            <psf:Value xsi:type="xsd:QName">xsd:QName</psf:Value>
        </psf:Property>
        <psf:Property name="psf:DefaultValue">
            <psf:Value xsi:type="xsd:QName">vnd:B</psf:Value>
        </psf:Property>
        <psf:Property name="psf:MaxLength">
            <psf:Value xsi:type="xsd:integer">1024</psf:Value>
        </psf:Property>
        <psf:Property name="psf:MinLength">
            <psf:Value xsi:type="xsd:integer">1</psf:Value>
        </psf:Property>
        <psf:Property name="psf:Mandatory">
            <psf:Value xsi:type="xsd:QName">psk:Optional</psf:Value>
        </psf:Property>
        <psf:Property name="psf:UnitType">
            <psf:Value xsi:type="xsd:string">characters</psf:Value>
        </psf:Property>
    </psf:ParameterDef>

    <psf:Feature name="psk3d:Job3DRaft">
        <psf:Property name="SelectionType">
            <psf:Value xsi:type="xsd:QName">psk:PickOne</psf:Value>
        </psf:Property>
        <psf:Option name="psk3d:RaftIncluded" />
        <psf:Option name="psk3d:RaftExcluded" />
    </psf:Feature>

    <psf:ParameterDef name="psk3d:Job3DRaftMaterial">
        <psf:Property name="psf:DataType">
            <psf:Value xsi:type="xsd:QName">xsd:QName</psf:Value>
        </psf:Property>
        <psf:Property name="psf:DefaultValue">
            <psf:Value xsi:type="xsd:QName">vnd:B</psf:Value>
        </psf:Property>
        <psf:Property name="psf:MaxLength">
            <psf:Value xsi:type="xsd:integer">1024</psf:Value>
        </psf:Property>
        <psf:Property name="psf:MinLength">
            <psf:Value xsi:type="xsd:integer">1</psf:Value>
        </psf:Property>
        <psf:Property name="psf:Mandatory">
            <psf:Value xsi:type="xsd:QName">psk:Optional</psf:Value>
        </psf:Property>
        <psf:Property name="psf:UnitType">
            <psf:Value xsi:type="xsd:string">characters</psf:Value>
        </psf:Property>
    </psf:ParameterDef>

</psf:PrintCapabilities>
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20PrintCapabilities%20document%20example%20%20RELEASE:%20%289/2/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


