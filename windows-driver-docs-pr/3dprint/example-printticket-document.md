---
title: PrintTicket document example
description: The keywords in this example are for illustration only, although they reflect the Print Schema keywords for 3D manufacturing.
ms.date: 03/17/2023
---

# PrintTicket document example

The keywords in this example are for illustration only, although they reflect the Print Schema keywords for 3D manufacturing. This PrintTicket is constructed specifically for a hypothetical device represented by the [PrintCapabilities document example](example-printcapabilities-document.md).

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<psf:PrintTicket
    xmlns:psf="https://schemas.microsoft.com/windows/2003/08/printing/printschemaframework"
    xmlns:xsi="https://www.w3.org/2001/XMLSchema-instance"
    xmlns:xsd="https://www.w3.org/2001/XMLSchema" version="1"
    xmlns:ns0000="https://schemas.microsoft.com/windows/printing/oemdriverpt/3dprinter"
    xmlns:psk="https://schemas.microsoft.com/windows/2003/08/printing/printschemakeywords"
    xmlns:psk3d="https://schemas.microsoft.com/3dmanufacturing/2013/01/pskeywords3d"
    xmlns:vnd="https://foo">

    <psf:ParameterInit name="vnd:Job3DAMap">
        <psf:Value xsi:type="xsd:string">1:0</psf:Value>
    </psf:ParameterInit>
    <psf:ParameterInit name="vnd:Job3DBMap">
        <psf:Value xsi:type="xsd:string">1:1</psf:Value>
    </psf:ParameterInit>

    <psf:Feature name="psk3d:Job3DSupports">
        <psf:Option name="psk3d:SupportsIncluded" />
    </psf:Feature>
    <psf:ParameterInit name="psk3d:Job3DSupportsMaterial">
        <psf:Value xsi:type="xsd:QName">vnd:B</psf:Value>
    </psf:ParameterInit>

    <psf:Feature name="psk3d:Job3DRaft">
        <psf:Option name="psk3d:RaftIncluded" />
    </psf:Feature>
    <psf:ParameterInit name="psk3d:Job3DRaftMaterial">
        <psf:Value xsi:type="xsd:QName">vnd:B</psf:Value>
    </psf:ParameterInit>

    <psf:Feature name="psk3d:Job3DQuality">
        <psf:Option name="psk3d:Medium" />
    </psf:Feature>
    <psf:Feature name="psk3d:Job3DDensity">
        <psf:Option name="psk3d:Low"/>
    </psf:Feature>
    
</psf:PrintTicket>
```
