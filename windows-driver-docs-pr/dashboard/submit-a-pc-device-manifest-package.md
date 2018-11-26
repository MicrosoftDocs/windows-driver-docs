---
title: Submit a PC device manifest package
description: Submit a PC device manifest package
ms.assetid: b96b02b8-8804-403e-9513-7a5d1b730fcd
ms.topic: article
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Submit a PC device manifest package


## <span id="Submitting_a_PC_device_manifest_package"></span><span id="submitting_a_pc_device_manifest_package"></span><span id="SUBMITTING_A_PC_DEVICE_MANIFEST_PACKAGE"></span>Submitting a PC device manifest package


You can use the same method to submit packages for preview or release.

**To submit a device manifest package**

1.  Sign the devicemanifest-ms package with the [SignTool](http://go.microsoft.com/fwlink/p/?LinkId=238330) tool.

2.  Sign in to the **Dashboard** from either the Hardware Dev Center or the Windows Dev Center by using a Microsoft account.

3.  Under **Device metadata**, click **Create experience** if you want to submit a new experience, or click **Manage experience** if you want to modify an existing experience.

4.  Browse for and select your new devicemanifest-ms package, and then click **Submit**.

## <span id="Creating_a_Device_Manifest_Submission_Package"></span><span id="creating_a_device_manifest_submission_package"></span><span id="CREATING_A_DEVICE_MANIFEST_SUBMISSION_PACKAGE"></span>Creating a Device Manifest Submission Package


A device manifest submission package is the package format in which all PC device metadata must be submitted to the Hardware Dev Center.

The device manifest submission package contains files that declare locale support and enable validation of PC HWIDs to belong to submitting companies. The device manifest package also includes a device metadata package.

Device manifest submission packages get uploaded to the Hardware Dev Center in the same way as device metadata packages. Using the same user interface and upload boxes, enter the name of your \*.devicemanifest-ms file for upload.

All file upload boxes other than bulk upload on the Hardware Dev Center user interface will accept device manifest submission packages.

### <span id="Device_Manifest_Submission_Package_Contents"></span><span id="device_manifest_submission_package_contents"></span><span id="DEVICE_MANIFEST_SUBMISSION_PACKAGE_CONTENTS"></span>Device Manifest Submission Package Contents

Each device manifest submission package consists of the following components:

-   **Device metadata package**

    This package contains information and graphics to display device icons, set actions, and utilize device experience features in Windows.

    The device metadata package is always required.

-   **LocaleInfo XML document**

    This document contains data about the locales included in the accompanying device metadata package. The Hardware Dev Center uses this data to properly validate the device metadata package for one or more locales.

    The LocaleInfo XML document is always required, even if the device metadata package only contains a single locale.

-   **PcMetadataSubmission XML document**

    This document contains data used to validate the HWIDs in the accompanying PC device metadata package. The Hardware Dev Center uses this data to verify the HWIDs in the device metadata package belong to the correct companies.

    The PcMetadataSubmission XML document is only required for PC device metadata packages

**Note**  
The XML documents must be saved by using UTF-8 encoding.

 

### <span id="Structure_of_a_PC_Device_Manifest_Submission_Package"></span><span id="structure_of_a_pc_device_manifest_submission_package"></span><span id="STRUCTURE_OF_A_PC_DEVICE_MANIFEST_SUBMISSION_PACKAGE"></span>Structure of a PC Device Manifest Submission Package

The structure of a device manifest package depends on whether the included device metadata is for a PC, for mobile broadband, or contains support for multiple locales.

If the device metadata does not fall into any of the three categories, a device manifest package is not necessary. However, a device manifest package can still be used to indicate the device metadata package is for a single locale.

The components of a PC device manifest submission package are stored in a compressed cabinet file. The file name must have a suffix of .devicemanifest-ms.

Each PC device manifest submission package must have the following structure:

``` syntax
GUID1.devicemanifest-ms
  \GUID1.devicemetadata-ms
  \LocaleInfo.xml
  \PcMetadataSubmission.xml
```

“GUID1” must be a GUID.

To create the LocaleInfo.xml and PcMetadataSubmission.xml, see below.

To learn how to develop the device metadata package, \*.devicemetadata-ms, see [Device Metadata Package Schema Reference for Windows 8](http://go.microsoft.com/fwlink/p/?LinkId=226753)

You can use the Cabarc tool to create these CAB packages. You can find more information about this tool in [Cabarc Overview](http://go.microsoft.com/fwlink/p/?LinkId=248843)

When you create a \*.devicemanifest-ms file by using the Cabarc tool, you must create a local directory in which the device metadata package (\*.devicemetadata-ms), the LocaleInfo XML document, and the PcMetadataSubmission XML document are at the root of the directory.

**Remarks**

-   The .devicemanifest -ms and .devicemetadata-ms filenames must specify the GUID without the curly brace ({}) delimiters.

-   The GUID for each PC device manifest submission and device metadata package must be unique. When you create a new or revised package, you must create a new GUID.

-   For more details about how to create cabinet files, see the [Microsoft Cabinet Software Development Kit](http://go.microsoft.com/fwlink/p/?LinkId=248844).

**Example**

The following shows an example of how to use the Cabarc tool to create a .devicemanifest-ms file. In this example, the components of the PC device manifest file are located in a local directory that is named PcPackages:

``` syntax
.\PcPackages\
.\PcPackages\PcMetadataSubmission.xml
.\PcPackages\LocaleInfo.xml
.\PcPackages\GUID.devicemetadata-ms
```

The GUID.devicemanifest-ms file was created in a local directory that is named PCFiles:

``` syntax
Cabarc.exe -r -p -P  .\PcPackages\ 
N .\PCFiles\ GUID.devicemanifest-ms 
.\PcPackages\PcMetadataSubmission.xml
.\PcPackages\LocaleInfo.xml
```

You can find more information about this tool in the [Cabarc Overview](http://go.microsoft.com/fwlink/p/?LinkId=248843).

## <span id="creating_pcmetadatasubmission.xml"></span><span id="CREATING_PCMETADATASUBMISSION.XML"></span>Creating PcMetadataSubmission.xml


### <span id="PcMetadataSubmission_XML_Schema"></span><span id="pcmetadatasubmission_xml_schema"></span><span id="PCMETADATASUBMISSION_XML_SCHEMA"></span>PcMetadataSubmission XML Schema

A device manifest submission package may contain one PcMetadataSubmission.xml document, which has information that the Hardware Dev Center site uses to validate the Computer HardwareIDs in PackageInfo.xml.

The data in the PcMetadataSubmission.xml document is formatted based on the PcMetadataSubmission XML schema, which is described below.

**Note**  
The XML document must be saved by using UTF-8 encoding.

 

For more information about ComputerHardwareID, see [How to Create a Device Metadata Package for Devices and Printers](http://go.microsoft.com/fwlink/p/?LinkId=253559).

**PcMetadataSubmission XML Schema NameSpace**

The following are the namespaces of the PcMetadataSubmission XML schema:

-   http://schemas.microsoft.com/Windows/2009/05/MetadataSubmission/PcMetadataSubmission

-   http://schemas.microsoft.com/Windows/2011/06/MetadataSubmission/PcMetadataSubmissionv2

**Overview of PcMetadataSubmission XML Elements/Attributes**

The following table describes the metadata elements and attributes of the PcMetadataSubmission XML schema.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>Element/Attributes</th>
<th>Element/Attribute type</th>
<th>Required/ optional</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>SMBIOSEntry</p></td>
<td><p>SMBIOSEntryType</p></td>
<td><p>Required</p></td>
<td><p>Specifies SMBIOS information for the computer.</p></td>
</tr>
<tr class="even">
<td><p>SystemManufacturer</p></td>
<td><p>tns:SMBIOSStringType</p></td>
<td><p>Required</p></td>
<td><p>Specifies the name of the computers.</p></td>
</tr>
<tr class="odd">
<td><p>SystemFamily</p></td>
<td><p>tns:SMBIOSStringType</p></td>
<td><p>Optional</p></td>
<td><p>Specifies the family name of the computer manufacturer.</p></td>
</tr>
<tr class="even">
<td><p>SystemProductName</p></td>
<td><p>tns:SMBIOSStringType</p></td>
<td><p>Optional</p></td>
<td><p>Specifies the name of the product (computer).</p></td>
</tr>
<tr class="odd">
<td><p>BIOSVendor</p></td>
<td><p>tns:SMBIOSStringType</p></td>
<td><p>Optional</p></td>
<td><p>Specifies the name of the BIOS manufacturer.</p></td>
</tr>
<tr class="even">
<td><p>BIOSVersion</p></td>
<td><p>tns:SMBIOSStringType</p></td>
<td><p>Optional</p></td>
<td><p>Specifies the version number of the BIOS.</p></td>
</tr>
<tr class="odd">
<td><p>SystemBIOSMajorRelease</p></td>
<td><p>tns:BIOSReleaseType</p></td>
<td><p>Optional</p></td>
<td><p>Specifies the MajorRelease version of the BIOS.</p></td>
</tr>
<tr class="even">
<td><p>SystemBIOSMinorRelease</p></td>
<td><p>tns:BIOSReleaseType</p></td>
<td><p>Optional</p></td>
<td><p>Specifies the MinorRelease version of the BIOS.</p></td>
</tr>
<tr class="odd">
<td><p>Enclosuretype</p></td>
<td><p>tns:TypeofEnclosureType</p></td>
<td><p>Optional</p></td>
<td><p>Specifies the Enclosure type of the computer.</p></td>
</tr>
<tr class="even">
<td><p>SKUNumber</p></td>
<td><p>v2:SMBIOSStringType</p></td>
<td><p>Optional</p></td>
<td><p>Specifies the SKU Number of the computer.</p></td>
</tr>
</tbody>
</table>

 

**PcMetadataSubmission XML Schema Definition**

The following is the PcMetadataSubmission XML schema definition

``` syntax
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema targetNamespace="http://schemas.microsoft.com/Windows/2009/05/MetadataSubmission/PcMetadataSubmission" xmlns:tns="http://schemas.microsoft.com/Windows/2009/05/MetadataSubmission/PcMetadataSubmission" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:v2="http://schemas.microsoft.com/Windows/2011/06/MetadataSubmission/PcMetadataSubmissionv2" elementFormDefault="qualified" blockDefault="#all">

  <xs:element name="PcMetadataSubmission" type="tns:PcMetadataSubmissionType" />
  <xs:complexType name="PcMetadataSubmissionType">
    <xs:sequence>
      <xs:element name="SMBIOSList" type="tns:SMBIOSListType" />
      <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="SMBIOSListType">
    <xs:sequence>
      <xs:element name="SMBIOSEntry" type="tns:SMBIOSEntryType" maxOccurs="unbounded" />
      <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="SMBIOSEntryType">
    <xs:simpleContent>
      <xs:extension base="xs:string">
        <xs:attribute name="SystemManufacturer" type="tns:SMBIOSStringType" use="required" />
        <xs:attribute name="SystemFamily" type="tns:SMBIOSStringType" use="optional" />
        <xs:attribute name="SystemProductName" type="tns:SMBIOSStringType" use="optional" />
        <xs:attribute name="BIOSVendor" type="tns:SMBIOSStringType" use="optional" />
        <xs:attribute name="BIOSVersion" type="tns:SMBIOSStringType" use="optional" />
        <xs:attribute name="SystemBIOSMajorRelease" type="tns:BIOSReleaseType" use="optional" />
        <xs:attribute name="SystemBIOSMinorRelease" type="tns:BIOSReleaseType" use="optional" />
        <xs:attribute name="EnclosureType" type="tns:TypeofEnclosureType" use="optional" />
        <xs:attribute ref="v2:SKUNumber" use="optional" />
      </xs:extension>
    </xs:simpleContent>
  </xs:complexType>
  <xs:simpleType name="SMBIOSStringType">
    <xs:restriction base="xs:string">
      <xs:minLength value="1" />
      <xs:maxLength value="64" />
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="BIOSReleaseType">
    <xs:restriction base="xs:hexBinary">
      <xs:minLength value="1" />
      <xs:maxLength value="1" />
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="TypeofEnclosureType">
    <xs:restriction base="xs:hexBinary">
      <xs:pattern value="([0-7][0-9A-F]|0[0-9A-F])" />
    </xs:restriction>
  </xs:simpleType>
</xs:schema>
```

The following is the PcMetadataSubmissionv2 XML schema definition:

``` syntax
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema targetNamespace="http://schemas.microsoft.com/Windows/2011/06/MetadataSubmission/PcMetadataSubmissionv2" xmlns:tns="http://schemas.microsoft.com/Windows/2011/06/MetadataSubmission/PcMetadataSubmissionv2" xmlns:xs="http://www.w3.org/2001/XMLSchema" elementFormDefault="qualified" blockDefault="#all">

  <xs:attribute name="SKUNumber" type="tns:SMBIOSStringType" />

  <xs:simpleType name="SMBIOSStringType">
    <xs:restriction base="xs:string">
      <xs:minLength value="1" />
      <xs:maxLength value="64" />
    </xs:restriction>
  </xs:simpleType>

</xs:schema>
```

### <span id="PcMetadataSubmission_XML_Schema_Reference"></span><span id="pcmetadatasubmission_xml_schema_reference"></span><span id="PCMETADATASUBMISSION_XML_SCHEMA_REFERENCE"></span>PcMetadataSubmission XML Schema Reference

The PcMetadataSubmission XML schema defines the following elements and attributes:

-   SMBIOSList

    -   SMBIOSEntry

        -   SystemManufacturer

        -   SystemFamily

        -   SystemProductName

        -   BIOSVendor

        -   BIOSVersion

        -   SystemBIOSMajorRelease

        -   SystemBIOSMinorRelease

        -   Enclosuretype

        -   SKUNumber

**SMBIOSEntry Elements**

The SMBIOSEntry element specifies computer system information. Based on this information, Hardware Dev Center creates computer hardware IDs and compares the value with the computer hardwareID in the packageinfo.xml that you submit along with the PcMetadataSubmission.xml.

``` syntax
<xs:element name="SMBIOSEntry" type="tns:SMBIOSEntryType" maxOccurs="unbounded" />

<xs:complexType name="SMBIOSEntryType">
    <xs:simpleContent>
      <xs:extension base="xs:string">
        <xs:attribute name="SystemManufacturer" type="tns:SMBIOSStringType" use="required" />
        <xs:attribute name="SystemFamily" type="tns:SMBIOSStringType" use="optional" />
        <xs:attribute name="SystemProductName" type="tns:SMBIOSStringType" use="optional" />
        <xs:attribute name="BIOSVendor" type="tns:SMBIOSStringType" use="optional" />
        <xs:attribute name="BIOSVersion" type="tns:SMBIOSStringType" use="optional" />
        <xs:attribute name="SystemBIOSMajorRelease" type="tns:BIOSReleaseType" use="optional" />
        <xs:attribute name="SystemBIOSMinorRelease" type="tns:BIOSReleaseType" use="optional" />
        <xs:attribute name="Enclosuretype" type="tns:TypeofEnclosureType" use="optional" />
        <xs:anyAttribute namespace="##other" processContents="lax" />
      </xs:extension>
    </xs:simpleContent>
  </xs:complexType>
```

**Remarks**

More than one SMBIOSEntry element can be used to specify multiple systems.

For example, consider a metadata package supports multiple PC systems. The following SMBIOSEntry elements can be used to define the PC systems.

``` syntax
<SMBIOSList>
  <SMBIOSEntry
      SystemManufacturer="FABRIKAM" SystemFamily…
  />
  <SMBIOSEntry
      SystemManufacturer="FABRIKAM" SystemFamily…
</SMBIOSList>
```

**SystemManufacturer Attributes**

The SystemManufacturer attributes specifies the family name of the computers.

``` syntax
<xs:attribute name="SystemManufacturer" type="tns:SMBIOSStringType" use="required" />

<xs:simpleType name="SMBIOSStringType">
  <xs:restriction base="xs:string">
    <xs:minLength value="1" />
    <xs:maxLength value="64" />
  </xs:restriction>
</xs:simpleType>
```

**Remarks**

The value specified by the SystemManufacturer attribute must be identical with the value in the Manufacturer field in the SMBIOS table in the target PC. The following table shows the field information in SMBIOS of the Manufacturer field.

<table style="width:100%;">
<colgroup>
<col width="14%" />
<col width="14%" />
<col width="14%" />
<col width="14%" />
<col width="14%" />
<col width="14%" />
<col width="14%" />
</colgroup>
<thead>
<tr class="header">
<th>Field name</th>
<th>Structure name and type</th>
<th>SMBIOS specification version</th>
<th>Offset</th>
<th>Length</th>
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Manufacturer</p></td>
<td><p>System Information (Type 1)</p></td>
<td><p>2.0+</p></td>
<td><p>04h</p></td>
<td><p>BYTE</p></td>
<td><p>STRING</p></td>
<td><p>The index of a null-terminated string within the dmiStrucBuffer array. This string specifies the name of the computer manufacturer.</p></td>
</tr>
</tbody>
</table>

 

For more information about the dmiStrucBuffer array and the SMBIOS fields, see [System Management BIOS (SMBIOS) Specification](http://go.microsoft.com/fwlink/p/?LinkId=145867).

**SystemFamily Attributes**

The SystemFamily attributes specifies the name of the computer manufacturer.

``` syntax
<xs:attribute name="SystemFamily" type="tns:SMBIOSStringType" use="optional" />

<xs:simpleType name="SMBIOSStringType">
  <xs:restriction base="xs:string">
    <xs:minLength value="1" />
    <xs:maxLength value="64" />
  </xs:restriction>
</xs:simpleType>
```

**Remarks**

The value specified by the SystemFamily attribute must be identical with the value in Family field in SMBIOS table in the target PC. The following table shows the field information in SMBIOS of the Family field.

<table style="width:100%;">
<colgroup>
<col width="14%" />
<col width="14%" />
<col width="14%" />
<col width="14%" />
<col width="14%" />
<col width="14%" />
<col width="14%" />
</colgroup>
<thead>
<tr class="header">
<th>Field name</th>
<th>Structure name and type</th>
<th>SMBIOS specification version</th>
<th>Offset</th>
<th>Length</th>
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Family</p></td>
<td><p>System Information (Type 1)</p></td>
<td><p>2.4+</p></td>
<td><p>1Ah</p></td>
<td><p>BYTE</p></td>
<td><p>STRING</p></td>
<td><p>The index of a null-terminated string within the dmiStrucBuffer array. This string specifies the family to which a particular computer belongs.A family refers to a set of computers that are similar but not identical from a hardware or software point of view.Typically a family is composed of different computer models, which have different configurations and pricing points. Computers in the same family often have similar branding and cosmetic features.</p></td>
</tr>
</tbody>
</table>

 

For more information about the dmiStrucBuffer array and the SMBIOS fields, refer to [System Management BIOS (SMBIOS) Specification](http://go.microsoft.com/fwlink/p/?LinkId=145867).

**SystemProductName Attributes**

The SystemProductName attributes specifies the name of the product (computer).

``` syntax
<xs:attribute name="SystemProductName" type="tns:SMBIOSStringType" use="optional" />

<xs:simpleType name="SMBIOSStringType">
  <xs:restriction base="xs:string">
    <xs:minLength value="1" />
    <xs:maxLength value="64" />
  </xs:restriction>
</xs:simpleType>
```

**Remarks**

The value specified by the SystemProductName attribute must be identical with the value in Product Name field in SMBIOS table in the target PC. The following table shows the field information in SMBIOS of the Product Name field.

<table style="width:100%;">
<colgroup>
<col width="14%" />
<col width="14%" />
<col width="14%" />
<col width="14%" />
<col width="14%" />
<col width="14%" />
<col width="14%" />
</colgroup>
<thead>
<tr class="header">
<th>Field name</th>
<th>Structure name and type</th>
<th>SMBIOS specification version</th>
<th>Offset</th>
<th>Length</th>
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Product Name</p></td>
<td><p>System Information (Type 1)</p></td>
<td><p>2.0+</p></td>
<td><p>05h</p></td>
<td><p>BYTE</p></td>
<td><p>STRING</p></td>
<td><p>The index of a null-terminated string within the dmiStrucBuffer array. This string specifies the product name of the computer.</p></td>
</tr>
</tbody>
</table>

 

For more information about the dmiStrucBuffer array and the SMBIOS fields, see [System Management BIOS (SMBIOS) Specification](http://go.microsoft.com/fwlink/p/?LinkId=145867).

**BIOSVendor Attributes**

The BIOSVendor attributes specifies the name of the BIOS manufacturer.

``` syntax
<xs:attribute name="BIOSVendor" type="tns:SMBIOSStringType" use="optional" />

<xs:simpleType name="SMBIOSStringType">
  <xs:restriction base="xs:string">
    <xs:minLength value="1" />
    <xs:maxLength value="64" />
  </xs:restriction>
</xs:simpleType>
```

**Remarks**

The value specified by the BIOSVendor attribute must be identical with the value in the Vendor field in the SMBIOS table in the target PC. The following table shows the field information in the SMBIOS of the Vendor field.

<table style="width:100%;">
<colgroup>
<col width="14%" />
<col width="14%" />
<col width="14%" />
<col width="14%" />
<col width="14%" />
<col width="14%" />
<col width="14%" />
</colgroup>
<thead>
<tr class="header">
<th>Field name</th>
<th>Structure name and type</th>
<th>SMBIOS specification version</th>
<th>Offset</th>
<th>Length</th>
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Vendor</p></td>
<td><p>BIOS Information (Type 0)</p></td>
<td><p>2.0</p></td>
<td><p>04h</p></td>
<td><p>BYTE</p></td>
<td><p>STRING</p></td>
<td><p>The index of a null-terminated string within the dmiStrucBuffer array. This string specifies the name of the BIOS vendor.</p></td>
</tr>
</tbody>
</table>

 

For more information about the dmiStrucBuffer array and the SMBIOS fields, see [System Management BIOS (SMBIOS) Specification](http://go.microsoft.com/fwlink/p/?LinkId=145867).

**BIOSVersion Attributes**

The BIOSVersion attributes specifies the version number of the BIOS.

``` syntax
<xs:attribute name="BIOSVersion" type="tns:SMBIOSStringType" use="optional" />

<xs:simpleType name="SMBIOSStringType">
  <xs:restriction base="xs:string">
    <xs:minLength value="1" />
    <xs:maxLength value="64" />
  </xs:restriction>
</xs:simpleType>
```

**Remarks**

The value specified by the BIOSVersion attribute must be identical with the value in the BIOS Version field in the SMBIOS table in the target PC. The following table shows the field information in the SMBIOS of the BIOS Version field.

<table style="width:100%;">
<colgroup>
<col width="14%" />
<col width="14%" />
<col width="14%" />
<col width="14%" />
<col width="14%" />
<col width="14%" />
<col width="14%" />
</colgroup>
<thead>
<tr class="header">
<th>Field name</th>
<th>Structure name and type</th>
<th>SMBIOS specification version</th>
<th>Offset</th>
<th>Length</th>
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>BIOS Version</p></td>
<td><p>BIOS Information (Type 0)</p></td>
<td><p>2.0</p></td>
<td><p>05h</p></td>
<td><p>BYTE</p></td>
<td><p>STRING</p></td>
<td><p>The index of a null-terminated string within the dmiStrucBuffer array. This string can contain information about the processor core and OEM version.</p></td>
</tr>
</tbody>
</table>

 

For more information about the dmiStrucBuffer array and the SMBIOS fields, see [System Management BIOS (SMBIOS) Specification](http://go.microsoft.com/fwlink/p/?LinkId=145867).

**SystemBIOSMajorRelease Attributes**

The SystemBIOSMajorRelease attributes specifies the Major Release version of the BIOS.

``` syntax
<xs:attribute name="SystemBIOSMajorRelease" type="tns:BIOSReleaseType" use="optional" />

<xs:simpleType name="BIOSReleaseType">
  <xs:restriction base="xs:hexBinary">
    <xs:minLength value="1" />
    <xs:maxLength value="1" />
  </xs:restriction>
</xs:simpleType>
```

**Remarks**

The value specified by the SystemBIOSMajorRelease attribute must be identical with the value in the SystemBIOSMajorRelease field in the SMBIOS table in the target PC. The following table shows the field information in the SMBIOS of the SystemBIOSMajorRelease field.

<table style="width:100%;">
<colgroup>
<col width="14%" />
<col width="14%" />
<col width="14%" />
<col width="14%" />
<col width="14%" />
<col width="14%" />
<col width="14%" />
</colgroup>
<thead>
<tr class="header">
<th>Field name</th>
<th>Structure name and type</th>
<th>SMBIOS specification version</th>
<th>Offset</th>
<th>Length</th>
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>System BIOS Major Release</p></td>
<td><p>BIOS Information (Type 0)</p></td>
<td><p>2.4</p></td>
<td><p>14h</p></td>
<td><p>BYTE</p></td>
<td><p>Varies.</p></td>
<td><p>The major release of the system BIOS.</p></td>
</tr>
</tbody>
</table>

 

For more information about the SMBIOS fields, see [System Management BIOS (SMBIOS) Specification](http://go.microsoft.com/fwlink/p/?LinkId=145867).

**SystemBIOSMinorRelease Attributes**

The SYSTEMBIOSMinorRelease attributes specifies the minor release version of the BIOS.

``` syntax
<xs:attribute name="SystemBIOSMinorRelease" type="tns:BIOSReleaseType" use="optional" />

<xs:simpleType name="BIOSReleaseType">
  <xs:restriction base="xs:hexBinary">
    <xs:minLength value="1" />
    <xs:maxLength value="1" />
  </xs:restriction>
</xs:simpleType>
```

**Remarks**

The value specified by the SystemBIOSMinorRelease attribute must be identical with the value in the SystemBIOSMinorRelease field in the SMBIOS table in the target PC. The following table shows the field information in the SMBIOS of the SystemBIOSMinorRelease field.

<table style="width:100%;">
<colgroup>
<col width="14%" />
<col width="14%" />
<col width="14%" />
<col width="14%" />
<col width="14%" />
<col width="14%" />
<col width="14%" />
</colgroup>
<thead>
<tr class="header">
<th>Field name</th>
<th>Structure name and type</th>
<th>SMBIOS specification version</th>
<th>Offset</th>
<th>Length</th>
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>System BIOS Minor Release</p></td>
<td><p>BIOS Information (Type 0)</p></td>
<td><p>2.4</p></td>
<td><p>15h</p></td>
<td><p>BYTE</p></td>
<td><p>Varies.</p></td>
<td><p>The minor release of the system BIOS.</p></td>
</tr>
</tbody>
</table>

 

For more information about the SMBIOS fields, see [System Management BIOS (SMBIOS) Specification](http://go.microsoft.com/fwlink/p/?LinkId=145867).

**Enclosuretype Attribute**

The Enclosuretype attributes specifies the Enclosure type of the computer.

``` syntax
<xs:attribute name="EnclosureType" type="tns:TypeofEnclosureType" use="optional" />

<xs:simpleType name="TypeofEnclosureType">
  <xs:restriction base="xs:hexBinary">
    <xs:pattern value="([0-7][0-9A-F]|0[0-9A-F])" />
  </xs:restriction>
</xs:simpleType>
```

**Remarks**

The value specified by the Enclosuretype attribute must be identical with the value in the Enclosure field in the SMBIOS table in the target PC. The following table shows the field information in the SMBIOS of the Enclosure field.

<table style="width:100%;">
<colgroup>
<col width="14%" />
<col width="14%" />
<col width="14%" />
<col width="14%" />
<col width="14%" />
<col width="14%" />
<col width="14%" />
</colgroup>
<thead>
<tr class="header">
<th>Field name</th>
<th>Structure name and type</th>
<th>SMBIOS specification version</th>
<th>Offset</th>
<th>Length</th>
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Enclosure type</p></td>
<td><p>System Enclosure (Type 3)</p></td>
<td><p>2.0+</p></td>
<td><p>05h</p></td>
<td><p>BYTE</p></td>
<td><p>Varies.</p></td>
<td><p>The system enclosure or chassis types.</p></td>
</tr>
</tbody>
</table>

 

For more information about the SMBIOS fields, see [System Management BIOS (SMBIOS) Specification](http://go.microsoft.com/fwlink/p/?LinkId=145867).

**SKUNumber Element**

The SKUNumber element specifies the SKU Number of the computer.

``` syntax
<xs:attribute name="SKUNumber" type="tns:SMBIOSStringType" />

<xs:simpleType name="SMBIOSStringType">
  <xs:restriction base="xs:string">
    <xs:minLength value="1" />
    <xs:maxLength value="64" />
  </xs:restriction>
</xs:simpleType>
```

**Remarks**

The value specified by the SKUNumber element must be identical with the value in the SKU Number field in the SMBIOS table in the target PC. The following table shows the field information in the SMBIOS of the SKU Number field.

<table style="width:100%;">
<colgroup>
<col width="14%" />
<col width="14%" />
<col width="14%" />
<col width="14%" />
<col width="14%" />
<col width="14%" />
<col width="14%" />
</colgroup>
<thead>
<tr class="header">
<th>Field name</th>
<th>Structure name and type</th>
<th>SMBIOS specification version</th>
<th>Offset</th>
<th>Length</th>
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>SKU Number</p></td>
<td><p>System Information (Type 1)</p></td>
<td><p>2.4+</p></td>
<td><p>19h</p></td>
<td><p>BYTE</p></td>
<td><p>STRING</p></td>
<td><p>Number of Null terminated string.This text string is used to identify a particular computer configuration for sale. It is sometimes also called a product ID or purchase order number. This number is frequently found in existing fields, but there is no standard format. Typically for a given system board from a given OEM, there are tens of unique processor, memory, hard drive, and optical drive configurations.</p></td>
</tr>
</tbody>
</table>

 

For more information about the SMBIOS fields, see [System Management BIOS (SMBIOS) Specification](http://go.microsoft.com/fwlink/p/?LinkId=145867).

### <span id="PcMetadataSubmission_XML_Example"></span><span id="pcmetadatasubmission_xml_example"></span><span id="PCMETADATASUBMISSION_XML_EXAMPLE"></span>PcMetadataSubmission XML Example

The following XML document uses the PcMetadataSubmission XML schema to specify the components of PcMetadataSubmission information of the target computer.

``` syntax
<?xml version="1.0" encoding="utf-8"?>
<PcMetadataSubmission xmlns="http://schemas.microsoft.com/Windows/2009/05/MetadataSubmission/PcMetadataSubmission">
  <SMBIOSList>
   <SMBIOSEntry
      SystemManufacturer="FABRIKAM"
      SystemFamily="FABRIKAM A SERIES"
      SystemProductName="FABRIKAM LAPTOP"
      BIOSVendor="FABRIKAM"
      BIOSVersion="7BETC7WW (2.08 )"
      SystemBIOSMajorRelease="08"
      SystemBIOSMinorRelease="00"
      EnclosureType="0A"
      v2:SKUNumber="1234567890ABCD"
    />
  </SMBIOSList>
</PcMetadataSubmission>
```

## <span id="creating_localeinfo.xml"></span><span id="CREATING_LOCALEINFO.XML"></span>Creating LocaleInfo.xml


For information about creating the Localeinfo.xml file for submission, see [Create the LocaleInfo.xml Submission File](https://msdn.microsoft.com/library/windows/hardware/hh801885.aspx).

 

 





