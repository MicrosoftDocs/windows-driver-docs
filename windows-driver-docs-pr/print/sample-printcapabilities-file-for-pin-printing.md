---
title: Sample PrintCapabilities File for PIN Printing
description: Here is a sample PrintCapabilities file to show how to specify personal ID number (PIN) protected printing.
ms.date: 01/25/2023
---

# Sample PrintCapabilities File for PIN Printing

Driver support For Protected Printing

Here is a sample PrintCapabilities file to show how to specify personal ID number (PIN) protected printing.

```xml
<?xml version="1.0"?>
<psf:PrintCapabilities
   xmlns:psf="https://schemas.microsoft.com/windows/2003/08/printing/printschemaframework" 
   xmlns:xsi="https://www.w3.org/2001/XMLSchema-instance" 
   xmlns:xsd="https://www.w3.org/2001/XMLSchema" version="1"
   xmlns:psk="https://schemas.microsoft.com/windows/2003/08/printing/printschemakeywords"
   xmlns:pskv11=" https://schemas.microsoft.com/windows/2013/05/printing/printschemakeywordsv11">
   <psf:ParameterDef name="pskv11:JobPasscodeString">
      <psf:Property name="psf:DataType">
           <psf:Value xsi:type="xsd:QName">xsd:string</psf:Value>
      </psf:Property>
      <psf:Property name="psf:DefaultValue">
           <psf:Value xsi:type="xsd:string"/>
      </psf:Property>
      <psf:Property name="psf:MaxLength">
           <psf:Value xsi:type="xsd:integer">9</psf:Value>
      </psf:Property>
      <psf:Property name="psf:MinLength">
           <psf:Value xsi:type="xsd:integer">4</psf:Value>
      </psf:Property>
      <psf:Property name="psf:Mandatory">
              <psf:Value xsi:type="xsd:QName">psk:Optional</psf:Value>
      </psf:Property>
      <psf:Property name="psf:UnitType">
              <psf:Value xsi:type="xsd:string">numeric</psf:Value>
      </psf:Property>
      <psf:Property name="psk:DisplayName">
           <psf:Value xsi:type="xsd:string">Job PassCode</psf:Value>
      </psf:Property>
   </psf:ParameterDef>
   <psf:Feature name="pskv11:JobPasscode">
      <psf:Property name="psf:SelectionType">
           <psf:Value xsi:type="xsd:string">psk:PickOne</psf:Value>
      </psf:Property>
      <psf:Property name="psk:DisplayName">
           <psf:Value xsi:type="xsd:string">Enable Job PassCode</psf:Value>
      </psf:Property>
      <psf:Option name="psk:On" />
      <psf:Option name="psk:Off" />
   </psf:Feature>
</psf:PrintCapabilities>
```

For more information about protected printing, see [Driver Support For Protected Printing](driver-support-for-protected-printing.md).
