---
title: Output keywords
description: These keywords are used to describe the actual output processes for a given 3D manufacturing job.
ms.assetid: FBCE5E9C-8411-46C1-899E-A6C8FE27D947
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Output keywords


These keywords are used to describe the actual output processes for a given 3D manufacturing job.

## 4.1. Job3DQuality


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Characteristic</th>
<th>Details</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Name</td>
<td>psk3d:Job3DQuality</td>
</tr>
<tr class="even">
<td>Valid for</td>
<td><p>PrintCapabilities documents</p>
<p>PrintTicket documents</p></td>
</tr>
<tr class="odd">
<td>Element type</td>
<td>Feature</td>
</tr>
<tr class="even">
<td>SelectionType</td>
<td>psk:PickOne</td>
</tr>
<tr class="odd">
<td>Contents</td>
<td><p>Options defined by the Print Schema keywords for 3D manufacturing are as follows:</p>
<p><strong>Child:</strong> Option psk3d:Draft</p>
<p><strong>Description:</strong> This Option specifies that the device SHOULD have the fastest output with the lowest resolution possible for the device.</p>
<p><strong>Child:</strong> Option psk3d:Medium</p>
<p><strong>Description:</strong> This Option specifies that the device SHOULD give equal priority to speed of output and output resolution.</p>
<p><strong>Child:</strong> Option psk3d:High</p>
<p><strong>Description:</strong> This Option specifies that the device SHOULD give highest priority to output resolution, regardless of speed.</p></td>
</tr>
</tbody>
</table>

 

Job3DQuality keyword usage

```xml
<psf:Feature name="psk3d:Job3DQuality">
    <psf:Property name="SelectionType">
        <psf:Value xsi:type="xsd:QName">psk:PickOne</psf:Value>
    </psf:Property>
    <psf:Option name="psk3d:Draft" />
    <psf:Option name="psk3d:Medium" />
    <psf:Option name="psk3d:High" />
</psf:Feature>
```

## 4.2. Job3DDensity


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Characteristic</th>
<th>Details</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Name</td>
<td>psk3d:Job3DDensity</td>
</tr>
<tr class="even">
<td>Valid for</td>
<td><p>PrintCapabilities documents</p>
<p>PrintTicket documents</p></td>
</tr>
<tr class="odd">
<td>Element type</td>
<td>Feature</td>
</tr>
<tr class="even">
<td>SelectionType</td>
<td>psk:PickOne</td>
</tr>
<tr class="odd">
<td>Contents</td>
<td><p>Options defined by the Print Schema keywords for 3D manufacturing are as follows:</p>
<p><strong>Child:</strong> Option psk3d:Hollow</p>
<p><strong>Description:</strong> This Option specifies that the device SHOULD output jobs with no internal supports (hollow).</p>
<p><strong>Child:</strong> Option psk3d:Low</p>
<p><strong>Description:</strong> This Option specifies that the device SHOULD output jobs with approximately 10% infill supports.</p>
<p><strong>Child:</strong> Option psk3d:Medium</p>
<p><strong>Description:</strong> This Option specifies that the device SHOULD output jobs with approximately 25% infill supports.</p>
<p><strong>Child:</strong> Option psk3d:High</p>
<p><strong>Description:</strong> This Option specifies that the device SHOULD output jobs with approximately 50% infill supports.</p>
<p><strong>Child:</strong> Option psk3d:Solid</p>
<p><strong>Description:</strong> This Option specifies that the device SHOULD output jobs 100% filled.</p></td>
</tr>
</tbody>
</table>

 

Job3DDensity keyword usage

```xml
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
```

## 4.3. Job3DSliceHeight


This Parameter SHOULD be used to communicate the desired thickness of each slice, if the psk3d:Job3DQuality parameter is deemed insufficient.

Job3DSliceHeight keyword profile

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Characteristic</th>
<th>Details</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Name</td>
<td>psk3d:Job3DSliceHeight</td>
</tr>
<tr class="even">
<td>Valid for</td>
<td>PrintCapabilities documents</td>
</tr>
<tr class="odd">
<td>Element type</td>
<td>ParameterDef</td>
</tr>
<tr class="even">
<td>Contents</td>
<td><p>psk3d:Job3DSliceHeight is an IntegerParamType, as described in §2.1.3.1, &quot;&lt;psf:ParameterDef&gt;&quot; in the Print Schema Specification.</p>
<p><strong>Child:</strong> IntegerParamType</p>
<p><strong>Description:</strong></p>
<p>The psf:MinValue Property Value MUST be greater than 0.</p>
<p>The psf:MaxValue Property Value MAY be defined by vendors, and MUST be greater than or equal to the psf:MinValue Property Value.</p>
<p>The psf:Multiple Property Value MUST be 1.</p>
<p>The psf:Multiple Property Value MUST be 1.</p>
<p>The psf:UnitType Property Value MUST be microns.</p></td>
</tr>
</tbody>
</table>

 

Job3DSliceHeight initialization profile

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Characteristic</th>
<th>Details</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Name</td>
<td>psk3d:Job3DSliceHeight</td>
</tr>
<tr class="even">
<td>Valid for</td>
<td>PrintTicket documents</td>
</tr>
<tr class="odd">
<td>Element type</td>
<td>ParameterInit</td>
</tr>
<tr class="even">
<td>Contents</td>
<td><p>Contains exactly 1 &lt;Value&gt; child element as follows:</p>
<p><strong>Child:</strong> Value</p>
<p><strong>xsi:type:</strong> xsd:integer</p>
<p><strong>Value:</strong> SliceHeight</p>
<p><strong>Description:</strong> SliceHeight MUST contain a positive integer equal to desired slice height, in microns.</p></td>
</tr>
</tbody>
</table>

 

Job3DSliceHeight keyword usage

The Parameter definition is as follows:

```xml
<psf:ParameterDef name="psk3d:Job3DSliceHeight">
    <psf:Property name="psf:DataType">
        <psf:Value xsi:type="xsd:QName">xsd:integer</psf:Value>
    </psf:Property>
    <psf:Property name="psf:DefaultValue">
        <psf:Value xsi:type="xsd:integer">100</psf:Value>
    </psf:Property>
    <psf:Property name="psf:MaxValue">
        <psf:Value xsi:type="xsd:integer">3000</psf:Value>
    </psf:Property>
    <psf:Property name="psf:MinValue">
        <psf:Value xsi:type="xsd:integer">50</psf:Value>
    </psf:Property>
    <psf:Property name="psf:Multiple">
        <psf:Value xsi:type="xsd:integer">1</psf:Value>
    </psf:Property>
    <psf:Property name="psf:Mandatory">
        <psf:Value xsi:type="xsd:QName">psk:Optional</psf:Value>
    </psf:Property>
    <psf:Property name="psf:UnitType">
        <psf:Value xsi:type="xsd:string">microns</psf:Value>
    </psf:Property>
</psf:ParameterDef>
```

This Parameter is initialized as follows:

```xml
<psf:ParameterInit name="psk3d:Job3DSliceHeight">
    <psf:Value xsi:type="xsd:integer">150</psf:Value>
</psf:ParameterInit>
```

## 4.4. Job3DOutputColor


The psk3d:Job3DOutputColor keyword specifies whether the model is to be reproduced in full color or with a single monochromatic material (the color of the base material).

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Characteristic</th>
<th>Details</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Name</td>
<td>psk3d:Job3DOutputColor</td>
</tr>
<tr class="even">
<td>Valid for</td>
<td><p>PrintCapabilities documents</p>
<p>PrintTicket documents</p></td>
</tr>
<tr class="odd">
<td>Element type</td>
<td>Feature</td>
</tr>
<tr class="even">
<td>SelectionType</td>
<td>psk:PickOne</td>
</tr>
<tr class="odd">
<td>Contents</td>
<td><p>Options defined by the Print Schema keywords for 3D manufacturing are as follows:</p>
<p><strong>Child:</strong> Option psk3d:Color</p>
<p><strong>Description:</strong> This Option specifies that the device SHOULD output a job in full color.</p>
<p><strong>Child:</strong> Option psk3d:Monochrome</p>
<p><strong>Description:</strong> This Option specifies that the device SHOULD output a job in a single color.</p></td>
</tr>
</tbody>
</table>

 

Job3DOutputColor keyword usage

```xml
<psf:Feature name="psk3d:Job3DOutputColor">
    <psf:Property name="SelectionType">
        <psf:Value xsi:type="xsd:QName">psk:PickOne</psf:Value>
    </psf:Property>
    <psf:Option name="psk3d:Color" />
    <psf:Option name="psk3d:Monochrome" />
</psf:Feature>
```

 

 




