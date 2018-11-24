---
title: Device control keywords
description: These keywords are used to provide control over the 3D manufacturing device.
ms.assetid: 1F0CBFC4-F641-4D82-9173-C89218E822B5
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Device control keywords


These keywords are used to provide control over the 3D manufacturing device.

## 2.1. Job3DOutputArea


The psk3d:Job3DOutputArea Property SHOULD be used to define the size of the area where the device can actually print: the lower left bottom corner of the Job3DOutputArea is defined as (0,0,0). Job3DOutputAreaWidth, Job3DOutputAreaDepth, and Job3DOutputAreaHeight Properties define the bounding box of the print volume, while Job3DOutputAreaMesh optionally defines the exact print volume within that bounding box if the print volume is not a cuboid.

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
<td>psk3d:Job3DOutputArea</td>
</tr>
<tr class="even">
<td>Valid for</td>
<td>PrintCapabilities documents</td>
</tr>
<tr class="odd">
<td>Element type</td>
<td>Property</td>
</tr>
<tr class="even">
<td>Contents</td>
<td><p>Contains exactly 1 &lt;Value&gt; child element, which MUST contain Job3DOutputAreaWidth, Job3DOutputAreaDepth, and Job3DOutputAreaHeight Properties, and MAY contain Job3DOutputAreaMesh.</p>
<p><strong>Child:</strong> Value</p>
<p><strong>xsi:type:</strong> N/A</p>
<p><strong>Value:</strong> OutputDimensions</p>
<p><strong>Description:</strong> OutputDimensions contains the set of 3 properties that make up each of the output area dimensions.</p></td>
</tr>
</tbody>
</table>

 

Job3DOutputArea keyword usage

```xml
<psf:Property name="psk3d:Job3DOutputArea">
    <psf:Property name="psk3d:Job3DOutputAreaWidth">
        <psf:Value xsi:type="xsd:integer">285000</psf:Value>
    </psf:Property>
    <psf:Property name="psk3d:Job3DOutputAreaDepth">
        <psf:Value xsi:type="xsd:integer">153000</psf:Value>
    </psf:Property>
    <psf:Property name="psk3d:Job3DOutputAreaHeight">
        <psf:Value xsi:type="xsd:integer">155000</psf:Value>
    </psf:Property>
     <psf:Property name="psk3d:Job3DOutputAreaMesh">
         <psf:Value xsi:type="xsd:string">
          <![CDATA[
            <mesh xmlns="http://schemas.microsoft.com/3dmanufacturing/mesh/2014/11" unit="millimeter">
             <vertices>
                <vertex x="0" y="0" z="0" />
                <vertex x="0" y="153000" z="0" />
                <vertex x="285000" y="0" z="0" />
                <vertex x="0" y="0" z="155000" />
             </vertices>
             <triangles>
                <triangle v1="0" v2="1" v3="2" />
                <triangle v1="0" v2="2" v3="3" />
                <triangle v1="0" v2="3" v3="1" />
                <triangle v1="2" v2="1" v3="3" />
             </triangles>
          </mesh>
          ]]></psf:Value>
    </psf:Property>
</psf:Property>
```

### 2.1.1. Job3DOutputAreaWidth

Describes the width of the output area along the X axis, in microns.

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
<td>psk3d:Job3DOutputAreaWidth</td>
</tr>
<tr class="even">
<td>Valid for</td>
<td>PrintCapabilities documents</td>
</tr>
<tr class="odd">
<td>Element type</td>
<td>Property</td>
</tr>
<tr class="even">
<td>Contents</td>
<td><p>Contains exactly 1 &lt;Value&gt; child element, as follows:</p>
<p><strong>Child:</strong> Value</p>
<p><strong>xsi:type:</strong> xsd:integer</p>
<p><strong>Value:</strong> OutputWidth</p>
<p><strong>Description:</strong> OutputWidth MUST contain an integer greater than 0 that is equal to the width of the output area along the X axis, in microns.</p></td>
</tr>
</tbody>
</table>

 

### 2.1.2. Job3DOutputAreaDepth

Describes the depth of the output area along the Y axis, in microns.

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
<td>psk3d:Job3DOutputAreaDepth</td>
</tr>
<tr class="even">
<td>Valid for</td>
<td>PrintCapabilities documents</td>
</tr>
<tr class="odd">
<td>Element type</td>
<td>Property</td>
</tr>
<tr class="even">
<td>Contents</td>
<td><p>Contains exactly 1 &lt;Value&gt; child element, as follows:</p>
<p><strong>Child:</strong> Value</p>
<p><strong>xsi:type:</strong> xsd:integer</p>
<p><strong>Value:</strong> OutputDepth</p>
<p><strong>Description:</strong> OutputDepth MUST contain an integer greater than 0 that is equal to the depth of the output area along the Y axis, in microns.</p></td>
</tr>
</tbody>
</table>

 

### 2.1.3. Job3DOutputAreaHeight

Describes the height of the output area along the Z axis, in microns.

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
<td>psk3d:Job3DOutputAreaHeight</td>
</tr>
<tr class="even">
<td>Valid for</td>
<td>PrintCapabilities documents</td>
</tr>
<tr class="odd">
<td>Element type</td>
<td>Property</td>
</tr>
<tr class="even">
<td>Contents</td>
<td><p>Contains exactly 1 &lt;Value&gt; child element, as follows:</p>
<p><strong>Child:</strong> Value</p>
<p><strong>xsi:type:</strong> xsd:integer</p>
<p><strong>Value:</strong> OutputHeight</p>
<p><strong>Description:</strong> OutputHeight MUST contain an integer greater than 0 that is equal to the depth of the output area along the Z axis, in microns.</p></td>
</tr>
</tbody>
</table>

 

### 2.1.4. Job3DOutputAreaMesh

Describes the shape of the output volume if not a rectangular prism. The string value is an XML blob following the 3MF spec for a &lt;mesh&gt; element (containing vertices and triangles, and conforming to the manifoldness standards for 3MF meshes). This polyhedron MUST be entirely contained within the bounding box described by the previous OutputArea Properties.

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
<td>psk3d:Job3DOutputAreaMesh</td>
</tr>
<tr class="even">
<td>Valid for</td>
<td>PrintCapabilities documents</td>
</tr>
<tr class="odd">
<td>Element type</td>
<td>Property</td>
</tr>
<tr class="even">
<td>Contents</td>
<td><p>Contains exactly 1 &lt;Value&gt; child element, as follows:</p>
<p><strong>Child:</strong> Value</p>
<p><strong>xsi:type:</strong> xsd:string</p>
<p><strong>Value:</strong> OutputMesh</p>
<p><strong>Description:</strong> OutputMesh MUST contain an xml string of vertices and triangles, as defined in the mesh section of the 3MF spec, which represents the boundary of the output volume.</p></td>
</tr>
</tbody>
</table>

 

## 2.2. Job3DAppName


The device MAY identify a workflow app other than the default (the example contains the default workflow) that the print dialog will invoke when this printer is selected. This workflow app allows for any custom UI that may be necessary or desired to best set up a 3D print job for this device.

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
<td>psk3d:Job3DAppName</td>
</tr>
<tr class="even">
<td>Valid for</td>
<td>PrintCapabilities documents</td>
</tr>
<tr class="odd">
<td>Element type</td>
<td>Property</td>
</tr>
<tr class="even">
<td>Contents</td>
<td><p>Contains exactly 1 &lt;Value&gt; child element, as follows:</p>
<p><strong>Child:</strong> Value</p>
<p><strong>xsi:type:</strong> xsd:string</p>
<p><strong>Value:</strong></p>
<p><strong>Description:</strong> The package name of the workflow app to be used for this printer in the Modern Print Dialog</p></td>
</tr>
</tbody>
</table>

 

Job3DAppName keyword usage

```xml
<psf:Property name="psk3d:Job3DAppName">
    <psf:Value xsi:type="xsd:string">Microsoft.3DBuilder_8wekyb3d8bbwe</psf:Value>
</psf:Property>
```

## 2.3. Job3DWSDAPackageFamilyName


The device MAY identify a UWP device app, which the print dialog will launch when the **Advanced settings** button is clicked by a user. This app presents UI for operations such as printer maintenance, material setup, calibration, etc. No default is supplied, so if this keyword is omitted, no **Advanced settings** button will be displayed.

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
<td>psk3d:Job3DWSDAPackageFamilyName</td>
</tr>
<tr class="even">
<td>Valid for</td>
<td>PrintCapabilities documents</td>
</tr>
<tr class="odd">
<td>Element type</td>
<td>Property</td>
</tr>
<tr class="even">
<td>Contents</td>
<td><p>Contains exactly 1 &lt;Value&gt; child element, as follows:</p>
<p><strong>Child:</strong> Value</p>
<p><strong>xsi:type:</strong> xsd:string</p>
<p><strong>Value:</strong></p>
<p><strong>Description:</strong> The package name of the UWP device app to be used for this printer’s advanced settings.</p></td>
</tr>
</tbody>
</table>

 

Job3DWSDAPackageFamilyName keyword usage

```xml
<psf:Property name="psk3d:Job3DWSDAPackageFamilyName">
    <psf:Value xsi:type="xsd:string"> </psf:Value>
</psf:Property>
```

## 2.4. Job3D3MFVersion


The device MUST identify the version of 3MF file that it expects to receive from the Windows print system. The version is specified by the URI namespace from the appropriate version of the core specification. For backwards compatibility, if this keyword is omitted, it will be assumed to take a default value of “<http://schemas.microsoft.com/3dmanufacturing/2013/01”>, indicating the legacy 0.93 version of 3MF, which is NOT RECOMMENDED.

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
<td>psk3d:Job3D3MFVersion</td>
</tr>
<tr class="even">
<td>Valid for</td>
<td>PrintCapabilities documents</td>
</tr>
<tr class="odd">
<td>Element type</td>
<td>Property</td>
</tr>
<tr class="even">
<td>Contents</td>
<td><p>Contains exactly 1 &lt;Value&gt; child element, as follows:</p>
<p><strong>Child:</strong> Value</p>
<p><strong>xsi:type:</strong> xsd:string</p>
<p><strong>Value:</strong></p>
<p><strong>Description:</strong> A URI namespace defining the 3MF core version supported by the device as input.</p></td>
</tr>
</tbody>
</table>

 

Job3D3MFVersion keyword usage

```xml
<psf:Property name="psk3d:Job3D3MFVersion">
    <psf:Value xsi:type="xsd:string"> http://schemas.microsoft.com/3dmanufacturing/core/2015/02</psf:Value>
</psf:Property>
```

## 2.5. Job3D3MFExtensions


The device MAY specify 3MF extensions (by namespace, forming a space-delimited list) that it understands, for instance allowing the print system to send slice data if available.

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
<td>psk3d:Job3D3MFExtensions</td>
</tr>
<tr class="even">
<td>Valid for</td>
<td>PrintCapabilities documents</td>
</tr>
<tr class="odd">
<td>Element type</td>
<td>Property</td>
</tr>
<tr class="even">
<td>Contents</td>
<td><p>Contains exactly 1 &lt;Value&gt; child element, as follows:</p>
<p><strong>Child:</strong> Value</p>
<p><strong>xsi:type:</strong> xsd:string</p>
<p><strong>Value:</strong></p>
<p><strong>Description:</strong> A space-delimited list of URI namespaces defining the 3MF extensions supported by the device as input.</p></td>
</tr>
</tbody>
</table>

 

Job3D3MFExtensions keyword usage

```xml
<psf:Property name="psk3d:Job3D3MFExtensions">
    <psf:Value xsi:type="xsd:string"> http://schemas.microsoft.com/3dmanufacturing/material/2015/02</psf:Value>
</psf:Property>
```

 

 




