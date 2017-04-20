---
title: PrintTicket document example
author: windows-driver-content
description: The keywords in this example are for illustration only, although they reflect the Print Schema keywords for 3D manufacturing.
ms.assetid: 139CF759-0A94-44A5-97BD-4EFD072220EF
---

# PrintTicket document example


The keywords in this example are for illustration only, although they reflect the Print Schema keywords for 3D manufacturing. This PrintTicket is constructed specifically for a hypothetical device represented by the [PrintCapabilities document example](example-printcapabilities-document.md).

```
<?xml version="1.0" encoding="UTF-8" ?>
<psf:PrintTicket
    xmlns:psf="http://schemas.microsoft.com/windows/2003/08/printing/printschemaframework"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema" version="1"
    xmlns:ns0000="http://schemas.microsoft.com/windows/printing/oemdriverpt/3dprinter"
    xmlns:psk="http://schemas.microsoft.com/windows/2003/08/printing/printschemakeywords"
    xmlns:psk3d="http://schemas.microsoft.com/3dmanufacturing/2013/01/pskeywords3d"
    xmlns:vnd="http://foo">

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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20PrintTicket%20document%20example%20%20RELEASE:%20%289/2/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


