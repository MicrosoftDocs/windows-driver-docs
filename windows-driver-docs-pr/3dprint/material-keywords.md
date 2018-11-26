---
title: Material keywords
description: These keywords describe the raw material in the device used to create 3D objects.
ms.assetid: B2264CA8-64F9-4A20-AC55-46A0C48EDF3C
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Material keywords


These keywords describe the raw material in the device used to create 3D objects.

## 3.1. Job3DMaterialCount


This parameter MUST define the number of materials currently loaded in the device that can be used in a single job. If the device does not know when materials are loaded, this parameter MUST be the possible number of materials used in a single job. If the printer has only a single, unknown material, this parameter MAY be omitted, along with all the other material keywords.

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
<td>psk3d:Job3DMaterialCount</td>
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
<p><strong>Value:</strong> JobMaterialCountText</p>
<p><strong>Description:</strong> JobMaterialCountText, if this Property is specified, MUST contain a positive integer that identifies the number of materials that are available on this device.</p></td>
</tr>
</tbody>
</table>



Job3DMaterialCount keyword usage

```cpp
<psf:Property name="psk3d:Job3DMaterialCount">
    <psf:Value xsi:type="xsd:integer">2</psf:Value>
</psf:Property>
```

## 3.2. Job3DMaterials


This property MUST contain descriptions of the Materials loaded in the device, or if this is unknown, MUST contain enumerations of the possible locations materials can be loaded.

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
<td>psk3d:Job3DMaterials</td>
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
<td><p>Contains 1 or more child Property elements as follows:</p>
<p><strong>Child:</strong> Property List</p>
<p><strong>xsi:type:</strong> N/A</p>
<p><strong>Value:</strong> MaterialsList</p>
<p><strong>Description:</strong> MaterialsList contains a set of child Properties.</p></td>
</tr>
</tbody>
</table>



### 3.2.1. MaterialsList Properties

Vendors MUST create their own materials, enumerating the print materials loaded in their device. The names of these materials are vendor-defined, and SHOULD represent a stock description if the device is capable of reading such information from a loaded material cartridge. If the device does not possess this information, the vendor SHOULD define the material name as descriptive of where this material is loaded (for example, "Left Extruder").

Each Material SHOULD specify the following child Properties.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Material name</th>
<th>xsi:type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>psk:DisplayName</td>
<td>xsd:string</td>
<td>This property SHOULD contain a psf:Value element containing the localized display name.</td>
</tr>
<tr class="even">
<td>psk3d:MaterialColor</td>
<td>xsd:string</td>
<td><p>Devices MAY define this Property to specify the color of the material. If specified, the Value MUST be an sRGB color conforming to the description below:</p>
<div class="code">
<code>cpp
sRGBColorText = &quot;#&quot; hR hG hB hA
hR = hG = hB = hA = hexpair
hexpair = hexdigit hexdigit
hexdigit = &quot;0&quot; / &quot;1&quot; / &quot;2&quot; / &quot;3&quot; /
           &quot;4&quot; / &quot;5&quot; / &quot;6&quot; / &quot;7&quot; /
           &quot;8&quot; / &quot;9&quot; / &quot;A&quot; / &quot;B&quot; /
           &quot;C&quot; / &quot;D&quot; / &quot;E&quot; / &quot;F&quot; /
           &quot;a&quot; / &quot;b&quot; / &quot;c&quot; / &quot;d&quot; /
           &quot;e&quot; / &quot;f&quot;</code>
</div>
<p>hR, hG, hB, and hA specify the hexadecimal single-byte values of the red, green, blue, and alpha components respectively, ranging from 00 to FF. Devices MAY omit alpha (i.e. #hRhGhB), in which case alpha takes on the default value of FF (completely opaque).</p></td>
</tr>
</tbody>
</table>



Job3DMaterials keyword usage

```cpp
<psf:Property name="psk3d:Job3DMaterials">
    <psf:Property name="vnd:ABS_RED">
        <psf:Property name="psk:DisplayName">
            <psf:Value xsi:type="xsd:string">Red ABS Plastic</psf:Value>
        </psf:Property>
        <psf:Property name="psk3d:MaterialColor">
            <psf:Value xsi:type="xsd:string">#FF0000</psf:Value>
        </psf:Property>
    </psf:Property>
    <psf:Property name="vnd:PLA_TEAL">
        <psf:Property name="psk:DisplayName">
            <psf:Value xsi:type="xsd:string">Teal PLA Plastic</psf:Value>
        </psf:Property>
        <psf:Property name="psk3d:MaterialColor">
            <psf:Value xsi:type="xsd:string">#00FFFF</psf:Value>
        </psf:Property>
    </psf:Property>
</psf:Property>
```

## 3.3. Job3DSupports


The psk3d:Job3DSupports keyword specifies whether this job should include *supports* generated by the device or driver.

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
<td>psk3d:Job3DSupports</td>
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
<p><strong>Child:</strong> Option psk3d:SupportsIncluded</p>
<p><strong>Description:</strong> This Option specifies that the device SHOULD generate external supports for the model.</p>
<p><strong>Child:</strong> Option psk3d:SupportsExcluded</p>
<p><strong>Description:</strong> This Option specifies that the device SHOULD NOT generate external supports for the model.</p></td>
</tr>
</tbody>
</table>



Job3DSupports keyword usage

```cpp
<psf:Feature name="psk3d:Job3DSupports">
    <psf:Property name="SelectionType">
        <psf:Value xsi:type="xsd:QName">psk:PickOne</psf:Value>
    </psf:Property>
    <psf:Option name="psk3d:SupportsIncluded" />
    <psf:Option name="psk3d:SupportsExcluded" />
</psf:Feature>
```

### 3.3.1. Job3DSupportsMaterial

If the option psk3d:SupportsIncluded is chosen and the device supports more than one material, this parameter SHOULD indicate the primary material to be used for the support structures. This parameter SHOULD be interpreted as a reference to a named child Property of the psk3d:Job3DMaterials Property.

Job3DSupportsMaterial keyword profile

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
<td>psk3d:Job3DSupportsMaterial</td>
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
<td><p>psk3d:Job3DSupportsMaterial is a QNameParamType, as described in §2.1.3.1, &quot;&lt;psf:ParameterDef&gt;&quot; in the Print Schema Specification:</p>
<p><strong>Child:</strong> QNameParamType</p>
<p><strong>Description:</strong></p>
<p>The psf:MinLength Property Value MUST be an integer greater than or equal to 1.</p>
<p>The psf:MaxLength Property Value MAY be defined by vendors, and MUST be greater than or equal to the psf:MinLength Property Value. It SHOULD be 1024.</p>
<p>The psf:Mandatory Property Value MUST be psk:Optional.</p>
<p>The psf:UnitType Property Value MUST be characters.</p></td>
</tr>
</tbody>
</table>



Job3DSupportsMaterial initialization profile

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
<td>psk3d:Job3DSupportsMaterial</td>
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
<td><p>Contains exactly 1 &lt;Value&gt; child element, as follows:</p>
<p><strong>Child:</strong> Value</p>
<p><strong>xsi:type:</strong> xsd:QName</p>
<p><strong>Value:</strong> MaterialName</p>
<p><strong>Description:</strong> MaterialName MUST reference a material identified as a psk3D:Job3DMaterials Property child.</p></td>
</tr>
</tbody>
</table>



Job3DSupportsMaterial keyword usage

The Parameter definition is as follows:

```cpp
<psf:ParameterDef name="psk3d:Job3DSupportsMaterial">
    <psf:Property name="psf:DataType">
        <psf:Value xsi:type="xsd:QName">xsd:QName</psf:Value>
    </psf:Property>
    <psf:Property name="psf:DefaultValue">
        <psf:Value xsi:type="xsd:QName">vnd:ABS_RED</psf:Value>
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
```

This Parameter is initialized as follows:

```cpp
<psf:ParameterInit name="psk3d:Job3DSupportsMaterial">
    <psf:Value xsi:type="xsd:QName">vnd:PLA_TEAL</psf:Value>
</psf:ParameterInit>
```

## 3.4. Job3DRaft


The psk3d:Job3DRaft keyword specifies whether this job should include a *raft* generated by the device or driver.

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
<td>psk3d:Job3DRaft</td>
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
<p><strong>Child:</strong> Option psk3d:RaftIncluded</p>
<p><strong>Description:</strong> This Option specifies that the device SHOULD generate a raft for the model.</p>
<p><strong>Child:</strong> Option psk3d:RaftExcluded</p>
<p><strong>Description:</strong> This Option specifies that the device SHOULD NOT generate a raft for the model.</p></td>
</tr>
</tbody>
</table>



Job3DRaft keyword usage

```cpp
<psf:Feature name="psk3d:Job3DRaft">
    <psf:Property name="SelectionType">
        <psf:Value xsi:type="xsd:QName">psk:PickOne</psf:Value>
    </psf:Property>
    <psf:Option name="psk3d:RaftIncluded" />
    <psf:Option name="psk3d:RaftExcluded" />
</psf:Feature>
```

### 3.4.1. Job3DRaftMaterial

If the option psk3d:RaftIncluded is chosen and the device supports more than one material, this parameter SHOULD indicate the primary material to be used for the raft. This parameter SHOULD be interpreted as a reference to a named child Property of the psk3d:Job3DMaterials Property.

Job3DRaftMaterial keyword profile

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
<td>psk3d:Job3DRaftMaterial</td>
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
<td><p>psk3d:Job3DRaftMaterial is a QNameParamType, as described in §2.1.3.1, &quot;&lt;psf:ParameterDef&gt;&quot; in the Print Schema Specification:</p>
<p><strong>Child:</strong> QNameParamType</p>
<p><strong>Description:</strong></p>
<p>The psf:MinLength Property Value MUST be an integer greater than or equal to 1.</p>
<p>The psf:MaxLength Property Value MAY be defined by vendors, and MUST be greater than or equal to the psf:MinLength Property Value. It SHOULD be 1024.</p>
<p>The psf:Mandatory Property Value MUST be psk:Optional.</p>
<p>The psf:UnitType Property Value MUST be characters.</p></td>
</tr>
</tbody>
</table>



Job3DRaftMaterial initialization profile

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
<td>psk3d:Job3DRaftMaterial</td>
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
<td><p>Contains exactly 1 &lt;Value&gt; child element, as follows:</p>
<p><strong>Child:</strong> Value</p>
<p><strong>xsi:type:</strong> xsd:QName</p>
<p><strong>Value:</strong> MaterialName</p>
<p><strong>Description:</strong> MaterialName MUST reference a material identified as a psk3D:Job3DMaterials Property child.</p></td>
</tr>
</tbody>
</table>



Job3DRaftMaterial keyword usage

The Parameter definition is as follows:

```cpp
<psf:ParameterDef name="psk3d:Job3DRaftMaterial">
    <psf:Property name="psf:DataType">
        <psf:Value xsi:type="xsd:QName">xsd:QName</psf:Value>
    </psf:Property>
    <psf:Property name="psf:DefaultValue">
        <psf:Value xsi:type="xsd:QName">vnd:ABS_RED</psf:Value>
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
```

This Parameter is initialized as follows:

```cpp
<psf:ParameterInit name="psk3d:Job3DRaftMaterial">
    <psf:Value xsi:type="xsd:QName">vnd:PLA_TEAL</psf:Value>
</psf:ParameterInit>
```

## 3.5. Material Mapping Parameter


If the device supports more than one material, this parameter SHOULD indicate the list of basematerials (ID:index) from the payload file to map to a particular output material. The IDs MUST reference a basematerials element in the payload file, as mapping other types of materials is not allowed. The output material (specified by Job3DMaterialSelected) MUST be a child of the psk3d:Job3DMaterials property. The name of the Material Mapping Parameter MUST begin with "Job3D" and have appended the value of the psk3d:Job3DMaterialSelected property, with "Map" appended to the end. In this way, the Print Ticket can be parsed for the whole material map without need for the Print Capabilities, allowing the job to be portable to other printers which could have the same materials, but loaded in a different order.

Material Mapping Parameter keyword profile

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
<td><em>Vendor specified</em></td>
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
<td><p>Material Mapping Parameters are a MaterialMapParamType, as described in section 1.8.1 of this document.:</p>
<p><strong>Child:</strong> MaterialMapParamType</p>
<p><strong>Description:</strong></p>
<p>The psf:MinLength Property Value MUST be an integer greater than or equal to 1.</p>
<p>The psf:MaxLength Property Value MAY be defined by vendors, and MUST be greater than or equal to the psf:MinLength Property Value. It SHOULD be 1024.</p>
<p>The psf:Mandatory Property Value MUST be psk:Optional.</p>
<p>The psf:UnitType Property Value MUST be materialMapUnitType.</p>
<p>The psk3d:Job3DMaterialSelected Property Value MUST reference the name of a child of the Job3DMaterials Property.</p></td>
</tr>
</tbody>
</table>



Job3DRaftMaterial initialization profile

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
<td><em>Vendor specified</em></td>
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
<p><strong>xsi:type:</strong> Psk3d:MaterialMapUnitType</p>
<p><strong>Value:</strong> Materials List</p>
<p><strong>Description:</strong> Materials List MUST be a semi-colon delimited list of material ID:index values, referencing basematerials in the model payload.</p></td>
</tr>
</tbody>
</table>



Material Mapping Parameter keyword usage

The Parameter definition is as follows:

```cpp
   <psf:ParameterDef name="vnd:Job3DABS_REDMap">
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
          <psf:Value xsi:type="xsd:QName">vnd:ABS_RED</psf:Value>
       </psf:Property>
   </psf:ParameterDef>
   <psf:ParameterDef name="vnd:Job3DPLA_TEALMap">
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
          <psf:Value xsi:type="xsd:QName">vnd:PLA_TEAL</psf:Value>
       </psf:Property>
   </psf:ParameterDef>
```

This Parameter is initialized as follows:

```cpp
   psf:ParameterInit name="vnd:Job3DABS_REDMap">
      <psf:Value xsi:type="xsd:string">1:0;1:2</psf:Value>
   </psf:ParameterInit>
   <psf:ParameterInit name="vnd:Job3DPLA_TEALMap">
      <psf:Value xsi:type="xsd:string">1:1</psf:Value>
   </psf:ParameterInit>
```








