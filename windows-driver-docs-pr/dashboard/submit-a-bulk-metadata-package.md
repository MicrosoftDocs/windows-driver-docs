---
title: Submit a Bulk Metadata Package
description: Submit a Bulk Metadata Package
ms.assetid: c8e248d4-a419-48e1-839d-1bbb9adda382
ms.topic: article
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Submit a Bulk Metadata Package


## <span id="Submitting_a_bulk_metadata_package"></span><span id="submitting_a_bulk_metadata_package"></span><span id="SUBMITTING_A_BULK_METADATA_PACKAGE"></span>Submitting a bulk metadata package


**To submit a bulk metadata package**

1.  Sign the bulk metadata package with the [SignTool](http://go.microsoft.com/fwlink/p/?LinkId=238330) tool.

2.  Sign in to the **Dashboard** from either the Hardware Dev Center or the Windows Dev Center by using a Microsoft account.

3.  Under **Device metadata**, click **Create bulk submission**.

4.  Browse for and select your new bulk metadata package, and then click **Submit**.

## <span id="Creating_a_Bulk_Submission_Package"></span><span id="creating_a_bulk_submission_package"></span><span id="CREATING_A_BULK_SUBMISSION_PACKAGE"></span>Creating a Bulk Submission Package


A bulk metadata submission package is the package format in which multiple device metadata packages can be submitted to the Dashboard.

Bulk metadata submission packages should be uploaded to the Dashboard by using the bulk submission feature. This feature removes the user interface for creating experiences to ease the uploading of multiple metadata packages simultaneously. The information to create experiences and modify package attributes is contained in the BulkMetadataSubmission XML document.

A maximum of 50 devicemetadata-ms or devicemanifest-ms files can be included in a bulk package.

For info about using the Device Metadata Submission Wizard to create a bulk metadata package, see [Creating a device metadata submission package in Visual Studio](http://go.microsoft.com/fwlink/p/?LinkId=251705).

### <span id="Bulk_Metadata_Submission_Package_Contents"></span><span id="bulk_metadata_submission_package_contents"></span><span id="BULK_METADATA_SUBMISSION_PACKAGE_CONTENTS"></span>Bulk Metadata Submission Package Contents

Each bulk metadata submission package consists of the following components:

-   Device metadata package(s)

    Device metadata packages contain information and graphics to display device icons, set actions, and utilize device experience features.

-   Device manifest package(s)

    Device manifest packages contain information to validate device metadata packages.

-   BulkMetadataSubmission XML document

    This document contains data used to properly submit packages without a user interface. The Dashboard uses information in this document to create experiences with friendly names, organize packages into experiences, update experiences, and mark individual packages as preview.

**Note**  
The XML documents must be saved by using UTF-8 encoding.

You must include at least one device metadata or device manifest package in your bulk metadata submission package.

 

### <span id="Structure_of_a_Bulk_Metadata_Submission_Package"></span><span id="structure_of_a_bulk_metadata_submission_package"></span><span id="STRUCTURE_OF_A_BULK_METADATA_SUBMISSION_PACKAGE"></span>Structure of a Bulk Metadata Submission Package

The components of a bulk metadata submission package are stored in a compressed cabinet file. The file name must have a suffix of “.bulkmetadata-ms.”

Each bulk metadata submission package must have the following structure:

``` syntax
DDMMYYYY.bulkmetadata-ms
\Filename1.devicemetadata-ms
\Filename2.devicemetadata-ms
\...
\Filename3.devicemanifest-ms
\Filename4.devicemanifest-ms
\...
\BulkMetadataSubmission.xml
```

Filename1, Filename2, Filename3, Filename4, and so on, must be GUIDs.

To create the BulkMetadataSubmission.xml, see below.

To develop the device metadata package, \*.devicemetadata-ms, see [Device Metadata Package Schema Reference for Windows 8](http://go.microsoft.com/fwlink/p/?LinkId=226753).

To develop the device manifest package, \*.devicemanifest-ms, see [Submit a PC device manifest package](https://msdn.microsoft.com/library/windows/hardware/hh801890.aspx).

You can use the Cabarc tool to create these CAB packages. To learn more about this tool, see [Cabarc Overview](http://go.microsoft.com/fwlink/p/?LinkId=248843).

When you create a \*.bulkmetadata-ms file by using the Cabarc tool, you must create a local directory in which the device metadata packages (\*.devicemetadata-ms), the device manifest packages (\*.devicemanifest-ms), and the BulkMetadataSubmission XML document are at the root of the directory.

**Remarks**

-   The .devicemetadata-ms and .devicemanifest-ms filenames must specify the GUID without the curly brace ({}) delimiters.

-   The GUID for each device metadata package and device manifest package must be unique. When you create a new or revised package, you must create a new GUID.

-   For more details about how to create cabinet files, see [Microsoft Cabinet SDK](http://go.microsoft.com/fwlink/p/?LinkId=248844).

**Example**

The following is an example of how to use the Cabarc tool to create a .bulkmetadata-ms file. In this example, the components of the bulk metadata file are located in a local directory that is named BulkPackages:

``` syntax
.\BulkPackages\
.\BulkPackages\BulkMetadataSubmission.xml
.\BulkPackages\GUID1.devicemetadata-ms
.\BulkPackages\GUID2.devicemetadata-ms
.\BulkPackages\GUID3.devicemanifest-ms
.\BulkPackages\GUID4.devicemanifest-ms
```

The GUID.pcmetadata-ms file was created in a local directory that is named PCFiles:

``` syntax
Cabarc.exe -r -p -P  .\BulkPackages\ 
N .\BulkFiles\ DDMMYYYY.bulkmetadata-ms 
.\BulkPackages\BulkMetadataSubmission.xml
.\BulkPackages\GUID1.devicemetadata-ms
.\BulkPackages\GUID2.devicemetadata-ms
.\BulkPackages\GUID3.devicemanifest-ms
.\BulkPackages\GUID4.devicemanifest-ms
```

**Note**  
You can find more information about this tool in [Cabarc Overview](http://go.microsoft.com/fwlink/p/?LinkId=248843).

 

## <span id="creating_bulkmetadatasubmission.xml"></span><span id="CREATING_BULKMETADATASUBMISSION.XML"></span>Creating BulkMetadataSubmission.xml


### <span id="BulkMetadataSubmission_XML_Schema"></span><span id="bulkmetadatasubmission_xml_schema"></span><span id="BULKMETADATASUBMISSION_XML_SCHEMA"></span>BulkMetadataSubmission XML Schema

A bulk metadata submission package contains one BulkMetadataSubmission.xml document, which has information that the Dashboard uses to create experiences with friendly names, organize packages into experiences, update experiences, and mark individual packages as preview.

The data in the BulkMetadataSubmission.xml document is formatted based on the BulkMetadataSubmission XML schema, which is described below.

**Note**  
The XML document must be saved by using UTF-8 encoding.

 

**BulkMetadataSubmission XML Schema NameSpace**

The following is the namespace of the PcMetadataSubmission XML schema: http://schemas.microsoft.com/Windows/2010/08/MetadataSubmission/BulkMetadataSubmission

**Overview of BulkMetadataSubmission XML Elements/Attributes**

The following table describes the metadata elements and attributes of the BulkMetadataSubmission XML schema.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Element/Attributes</th>
<th>Element/Attribute type</th>
<th>Required/ optional</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Experience</p></td>
<td><p>ExperienceType</p></td>
<td><p>Required</p></td>
</tr>
<tr class="even">
<td><p>ExperienceName</p></td>
<td><p>xs:string</p></td>
<td><p>Required</p></td>
</tr>
<tr class="odd">
<td><p>ExperienceId</p></td>
<td><p>tns:GUIDType</p></td>
<td><p>Optional</p></td>
</tr>
<tr class="even">
<td><p>PackageList</p></td>
<td><p>tns:PackageListType</p></td>
<td><p>Required</p></td>
</tr>
<tr class="odd">
<td><p>PackageFileName</p></td>
<td><p>PackageFileNameType</p></td>
<td><p>Required</p></td>
</tr>
<tr class="even">
<td><p>preview</p></td>
<td><p>xs:Boolean</p></td>
<td><p>Required</p></td>
</tr>
<tr class="odd">
<td><p>locale</p></td>
<td><p>xs:string</p></td>
<td><p>Required</p></td>
</tr>
<tr class="even">
<td><p>Qualification</p></td>
<td><p>tns:QualificationType</p></td>
<td><p>Required</p></td>
</tr>
<tr class="odd">
<td><p>LogoSubmissionIDList</p></td>
<td><p>tns:LogoSubmissionIDListType</p></td>
<td><p>Optional</p></td>
</tr>
<tr class="even">
<td><p>LogoSubmissionID</p></td>
<td><p>xs:integer</p></td>
<td><p>Required</p></td>
</tr>
<tr class="odd">
<td><p>update</p></td>
<td><p>xs:Boolean</p></td>
<td><p>Required</p></td>
</tr>
</tbody>
</table>

 

**BulkMetadataSubmission XML Schema Metadata**

The following is the BulkMetadataSubmission XML schema metadata:

``` syntax
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema targetNamespace="http://schemas.microsoft.com/Windows/2010/08/MetadataSubmission/BulkMetadataSubmission" xmlns:tns="http://schemas.microsoft.com/Windows/2010/08/MetadataSubmission/BulkMetadataSubmission" xmlns:xs="http://www.w3.org/2001/XMLSchema" elementFormDefault="qualified" blockDefault="#all">

 <xs:element name="BulkMetadataSubmission" type="tns:BulkMetadataSubmissionType" />

 <xs:complexType name="BulkMetadataSubmissionType">
  <xs:sequence>
   <xs:element name="Experience" type="tns:ExperienceType"  maxOccurs="unbounded" />
   <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
  </xs:sequence>
 </xs:complexType>

  <xs:complexType name="ExperienceType">
    <xs:complexContent>
      <xs:extension base ="tns:BaseExperienceType">
        <xs:attribute name="update" type="xs:boolean" use="required"/>        
      </xs:extension>      
    </xs:complexContent>
  </xs:complexType>
    
  <xs:complexType name="BaseExperienceType">  
    <xs:sequence>
      <xs:element name="ExperienceName" type="xs:string" />
      <xs:element name="ExperienceId" type="tns:GUIDType" minOccurs="0" />
      <xs:element name="PackageList" type="tns:PackageListType" />
      <xs:element name="Qualification" type="tns:QualificationType" />
      <xs:element name="LogoSubmissionIDList" type="tns:LogoSubmissionIDListType" minOccurs="0" maxOccurs="unbounded" />
      <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
    </xs:sequence>
  </xs:complexType>

  <xs:simpleType name="GUIDType">
    <xs:restriction base="xs:string">
      <xs:pattern value="[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}" />
    </xs:restriction>
  </xs:simpleType>

 <xs:complexType name="PackageListType">
  <xs:sequence>
   <xs:element name="PackageFileName" type="tns:PackageFileNameType"  maxOccurs="unbounded" />
   <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
  </xs:sequence>
 </xs:complexType>

  <xs:complexType name="PackageFileNameType">
    <xs:simpleContent>
      <xs:extension base="xs:string">
        <xs:attribute name="preview" type="xs:boolean" use="required" />
        <xs:attribute name="locale" type="xs:string" use="required" />
      </xs:extension>
    </xs:simpleContent>
  </xs:complexType>

 <xs:simpleType name="QualificationType">
<xs:union memberTypes="tns:QualificationTypeEnumeration xs:string" />
 </xs:simpleType>

 <xs:simpleType name="QualificationTypeEnumeration">
   <xs:restriction base="xs:string">
     <xs:enumeration value="Logo/IDDA" />
     <xs:enumeration value="MicrosoftInboxDriver" />
   </xs:restriction>
 </xs:simpleType>

 <xs:complexType name="LogoSubmissionIDListType">
  <xs:sequence>
   <xs:element name="LogoSubmissionID" type="xs:integer"  maxOccurs="unbounded" />
   <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
  </xs:sequence>
 </xs:complexType>

</xs:schema>
```

### <span id="BulkMetadataSubmission_XML_Schema_Reference"></span><span id="bulkmetadatasubmission_xml_schema_reference"></span><span id="BULKMETADATASUBMISSION_XML_SCHEMA_REFERENCE"></span>BulkMetadataSubmission XML Schema Reference

The BulkMetadataSubmission XML schema defines the following elements and attributes:

-   BulkMetadataSubmission

    -   Experience

        -   ExperienceName

        -   ExperienceID

        -   PackageList

            -   PackageFileName

                -   preview

                -   locale

        -   Qualification

        -   LogoSubmissionIDList

            -   LogoSubmissionID

        -   update

**Experience Element**

The Experience element specifies information for a single experience. For more information about experiences, see [Device Metadata Package Schema Reference for Windows 8](http://go.microsoft.com/fwlink/p/?LinkId=226753).

Based on this information, the Dashboard either creates an experience with the correct information and submits packages to this experience, or updates an existing experience with new packages.

``` syntax
<xs:element name="Experience" type="tns:ExperienceType"  maxOccurs="unbounded" />

<xs:complexType name="ExperienceType">
  <xs:complexContent>
    <xs:extension base ="tns:BaseExperienceType">
      <xs:attribute name="update" type="xs:boolean" use="required"/>        
    </xs:extension>      
  </xs:complexContent>
</xs:complexType>
    
<xs:complexType name="BaseExperienceType">  
  <xs:sequence>
    <xs:element name="ExperienceName" type="xs:string" />
    <xs:element name="ExperienceId" type="tns:GUIDType" minOccurs="0" />
    <xs:element name="PackageList" type="tns:PackageListType" />
    <xs:element name="Qualification" type="tns:QualificationType" />
    <xs:element name="LogoSubmissionIDList" type="tns:LogoSubmissionIDListType" minOccurs="0" maxOccurs="unbounded" />
    <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
  </xs:sequence>
</xs:complexType>
```

Remarks

More than one Experience element can be used to specify multiple experiences. This allows for a single submission of many packages for different devices.

For example, see the following.

``` syntax
<Experience update="false">
  <ExperienceName>Test1</ExperienceName>
  <PackageList>
    <PackageFileName locale="en-us" preview ="false">
      XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX.devicemanifest-ms
    </PackageFileName>
  </PackageList>
  <Qualification>Logo/IDDA</Qualification>
  <LogoSubmissionIDList>
    <LogoSubmissionID>XXXXXXX</LogoSubmissionID>
  </LogoSubmissionIDList>
</Experience>

<Experience update="false">
  <ExperienceName>Test2</ExperienceName>
  <PackageList>
    <PackageFileName locale="en-us" preview ="false">
      XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX.devicemetadata-ms
    </PackageFileName>
  </PackageList>
  <Qualification>Logo/IDDA</Qualification>
  <LogoSubmissionIDList>
    <LogoSubmissionID>XXXXXXX</LogoSubmissionID>
  </LogoSubmissionIDList>
</Experience>
```

**ExperienceName Element**

The ExperienceName element specifies the name of an experience. The Dashboard will create an experience with this name if this is a new experience. Or, it ignores this value when this is an update to an existing experience.

``` syntax
<xs:element name="ExperienceName" type="xs:string" />
```

**ExperienceId Element**

The ExperienceId element specifies the GUID that is the Experience ID. This value is required when updating an existing experience. The Dashboard uses this value to identify the experience to update.

``` syntax
<xs:element name="ExperienceId" type="tns:GUIDType" minOccurs="0" />

<xs:simpleType name="GUIDType">
  <xs:restriction base="xs:string">
    <xs:pattern value="[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}" />
  </xs:restriction>
</xs:simpleType>
```

**PackageList Element**

The PackageList element specifies the list of device metadata or device manifest packages to be included in an experience. The Dashboard uses this information to add packages to a new or existing experience.

``` syntax
<xs:element name="PackageList" type="tns:PackageListType" />

<xs:complexType name="PackageListType">
  <xs:sequence>
    <xs:element name="PackageFileName" type="tns:PackageFileNameType"  maxOccurs="unbounded" />
    <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
  </xs:sequence>
</xs:complexType>
```

**PackageFileName Element**

The PackageFileName element specifies the filename and information of a single device metadata or device manifest package. The Dashboard uses this information to add a package to a new or existing experience, and correctly mark the package as preview if indicated. Based on the preview and locale values, the Dashboard also deletes existing packages if required

``` syntax
<xs:element name="PackageFileName" type="tns:PackageFileNameType"  maxOccurs="unbounded" />

<xs:complexType name="PackageFileNameType">
  <xs:simpleContent>
    <xs:extension base="xs:string">
      <xs:attribute name="preview" type="xs:boolean" use="required" />
      <xs:attribute name="locale" type="xs:string" use="required" />
    </xs:extension>
  </xs:simpleContent>
</xs:complexType>
```

Remarks

The preview and locale attributes of the PackageFileName element allow the Dashboard to update your existing live package with a newly submitted package.

For example, if an en-US preview package already exists in the experience, and an en-US preview package was submitted in a bulk metadata submission package for the same experience, the existing package would be automatically deleted and the new package would be submitted.

For this reason, it is also important to be careful when updating packages to avoid accidental deletions.

**preview Attribute**

The preview attribute specifies whether a device metadata or device manifest package should be marked preview. See PackageFileName Element for more information about how the Dashboard uses this value.

``` syntax
<xs:attribute name="preview" type="xs:boolean" use="required" />
```

**locale Attribute**

The locale attribute specifies the declared locale (from PackageInfo.xml) of a device metadata or device manifest package should be marked preview. See PackageFileName Element for more information about how the Dashboard uses this value.

``` syntax
<xs:attribute name="locale" type="xs:string" use="required" />
```

**Qualification Element**

The Qualification element specifies whether the device has a Logo certification, is included in the Inbox Driver Distribution Agreement (IDDA) list, or uses a Microsoft inbox driver. The Dashboard uses this information to ensure correct device certification for the type of device metadata you are submitting.

``` syntax
<xs:element name="Qualification" type="tns:QualificationType" />

<xs:simpleType name="QualificationType">
<xs:union memberTypes="tns:QualificationTypeEnumeration xs:string" />
 </xs:simpleType>

 <xs:simpleType name="QualificationTypeEnumeration">
   <xs:restriction base="xs:string">
     <xs:enumeration value="Logo/IDDA" />
     <xs:enumeration value="MicrosoftInboxDriver" />
   </xs:restriction>
 </xs:simpleType>
```

**Remarks**

Features such as Device Stage are not available for devices that have not passed Logo certification and are not on the IDDA list.

You can select one of two options for each experience. These options and their definitions are indicated in the table below:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Enumeration value</th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Logo/IDDA</p></td>
<td><p>Your device has a Logo certification or is on the IDDA list. If you have a Logo certification, you will need to specify the specific Logo Submission IDs in the LogoSubmissionIDList element.</p></td>
</tr>
<tr class="even">
<td><p>MicrosoftInboxDrive</p></td>
<td><p>Your device uses a Microsoft inbox driver. Some features of device metadata might not be available when using this qualification level (such as Device Stage)</p></td>
</tr>
</tbody>
</table>

 

**LogoSubmissionIDList Element**

The LogoSubmissionIDList element specifies the list of logo certification(s) for a device. See Qualification Element for more information about how the Dashboard uses this value.

``` syntax
<xs:element name="LogoSubmissionIDList" type="tns:LogoSubmissionIDListType" minOccurs="0" maxOccurs="unbounded" />

<xs:complexType name="LogoSubmissionIDListType">
  <xs:sequence>
    <xs:element name="LogoSubmissionID" type="xs:integer"  maxOccurs="unbounded" />
    <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
  </xs:sequence>
</xs:complexType>
```

**LogoSubmissionID Element**

The LogoSubmissionID element specifies an individual logo certification for a device. See Qualification Element for more information about how the Dashboard uses this value.

``` syntax
<xs:element name="LogoSubmissionID" type="xs:integer"  maxOccurs="unbounded" />
```

Remarks

Multiple LogoSubmissionID elements can be used to indicate multiple Logo certifications for a single device. Users should list all logo certifications for their device in the list. The following is an example where multiple logo certifications are listed:

``` syntax
<LogoSubmissionIDList>
  <LogoSubmissionID>0000001</LogoSubmissionID>
  <LogoSubmissionID>0000002</LogoSubmissionID>
  <LogoSubmissionID>0000003</LogoSubmissionID>
</LogoSubmissionIDList>
```

**update Attribute**

The update attribute designates whether or not an experience is being updated. The Dashboard uses this value to update an experience by deleting conflicting packages and uploading new packages when the update attribute is set to true. When the update attribute is set to false, the Dashboard will create a new experience and upload new packages to it.

``` syntax
<xs:attribute name="update" type="xs:boolean" use="required"/>
```

### <span id="BulkMetadataSubmission_XML_Example"></span><span id="bulkmetadatasubmission_xml_example"></span><span id="BULKMETADATASUBMISSION_XML_EXAMPLE"></span>BulkMetadataSubmission XML Example

The following XML document uses the BulkMetadataSubmission XML schema to specify the components of the BulkMetadataSubmission XML document.

``` syntax
<BulkMetadataSubmission xmlns="http://schemas.microsoft.com/Windows/2010/08/MetadataSubmission/BulkMetadataSubmission">

  <Experience update="false">
    <ExperienceName>Test1</ExperienceName>
    <PackageList>
      <PackageFileName locale="en-us" preview ="false">
        XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX.devicemanifest-ms
      </PackageFileName>
    </PackageList>
    <Qualification>Logo/IDDA</Qualification>
    <LogoSubmissionIDList>
      <LogoSubmissionID>XXXXXXX</LogoSubmissionID>
    </LogoSubmissionIDList>
  </Experience>

  <Experience update="false">
    <ExperienceName>Test2</ExperienceName>
    <PackageList>
      <PackageFileName locale="en-us" preview ="false">
        XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX.devicemetadata-ms
      </PackageFileName>
    </PackageList>
    <Qualification>Logo/IDDA</Qualification>
    <LogoSubmissionIDList>
      <LogoSubmissionID>XXXXXXX</LogoSubmissionID>
    </LogoSubmissionIDList>
  </Experience>

  <Experience update="false">
    <ExperienceName>Test3</ExperienceName>
    <PackageList>
      <PackageFileName locale="en-us" preview="false">
        XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX.devicemanifest-ms
      </PackageFileName>
    </PackageList>
    <Qualification>Logo/IDDA</Qualification>
    <LogoSubmissionIDList>
      <LogoSubmissionID>XXXXXXX</LogoSubmissionID>
    </LogoSubmissionIDList>
  </Experience>

  <Experience update="false">
    <ExperienceName>Test4</ExperienceName>
    <PackageList>
      <PackageFileName locale="en-us" preview="false">
        XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX.devicemetadata-ms
      </PackageFileName>
    </PackageList>
    <Qualification>Logo/IDDA</Qualification>
    <LogoSubmissionIDList>
      <LogoSubmissionID>XXXXXXX</LogoSubmissionID>
    </LogoSubmissionIDList>
  </Experience>

  <Experience update="false">
    <ExperienceName>Test5</ExperienceName>
    <PackageList>
      <PackageFileName locale="en-us" preview="false">
        XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX.devicemetadata-ms
      </PackageFileName>
    </PackageList>
    <Qualification>Logo/IDDA</Qualification>
    <LogoSubmissionIDList>
      <LogoSubmissionID>XXXXXXX</LogoSubmissionID>
    </LogoSubmissionIDList>
  </Experience>

</BulkMetadataSubmission>
```

 

 





