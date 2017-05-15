---
title: SMBIOS
description: The SMBIOS specification defines data structures and information that will go into the data structures pertinent to a system.
author: windows-driver-content
ms.author: windowsdriverdev
ms.date: 05/15/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---


# SMBIOS

SMBIOS specification defines data structures and information that will go into the data structures pertinent to a system. By using the latest SMBIOS specification, we keep up with the latest changes defined in the specification. The table below describe the recommended SMBIOS settings along with guidance on what type of information should be in these fields. Having these fields populated with data pertaining to each individual system allows system administrators the ability to remotely identify and manage these systems. Computer Hardware IDs (CHIDs) are generated using the values from this table, and care and thought should be given to setting these.

To add uniformity to SMBIOS to better identify device information, we recommend the following as guidance when populating SMBIOS fields. The SMBIOS data below is also collected and used in various capacities. The data going into these fields should be planned in detail before populating using tools provided by BIOS/Firmware vendors. The hash generated for CHID targeting is based off of data populating these fields.

Although this information is similar to that listed in the [Windows 10 Driver Publishing Workflow](http://download.microsoft.com/download/B/A/8/BA89DCE0-DB25-4425-9EFF-1037E0BA06F9/windows10_driver_publishing_workflow.docx), the following tables prescribe additional levels of detail for some fields, helping to increase the level of specificity.

## Recommended settings when moving to SMBIOS 3.0

<table>
    <tbody>
        <tr>
            <td>Field Name</b></td>
            <td><b>Structure Name and Type</b></td>
            <td><b>Value</b></td>
            <td><b>Offset</b></td>
            <td><b>Length</b></td>
            <td><b>Example Scenario</b></td>
            <td><b>Example</b></td>
        </tr>
        <tr>
            <td>"Manufacturer"</td>
            <td>System Information (Type 1)</td>
            <td>String</td>
            <td>04h</td>
            <td>32</td>
            <td rowspan="8">Contoso, Inc. manufactures 2 product lines: 1) "A" series, and 2) "B" series. The "A" series of devices include the Contoso "A11" and "A13" device sub-brands, each of which have different screen sizes and both support physically detachable keyboards (though the keyboards are sold as an option). The "A11" has three models: 1) the base model (the a110001) 2) a midsize model with a premium audio package (the a110002) and 3) a high-end model with a higher resolution touch panel (the a110003). Each model has gone through several generations of baseboard revisions, which are identified internally with codes bb01 through bb04. Each of the "A11" models can be further customized with different storage and memory configurations. To separate different production runs on their manufacturing floor, Contoso uses an internal identification system that combines the Family, Product Name, market region, and production run number.</td>
            <td>"Contoso"</td>
        </tr>
        <tr>
            <td>"Family"</td>
            <td>System Information (Type 1)</td>
            <td>String</td>
            <td>1Ah</td>
            <td>64</td>
            <td>"A11"</td>
        </tr>
        <tr>
            <td>"Product Name"</td>
            <td>System Information (Type 1)</td>
            <td>String</td>
            <td>05h</td>
            <td>64</td>
            <td>"A11 a110001"</td>
        </tr>
        <tr>
            <td>"Baseboard Product"</td>
            <td>Baseboard Information (Type 2)</td>
            <td>String</td>
            <td>05h</td>
            <td>32</td>
            <td>"bb03"</td>
        </tr>
        <tr>
            <td>"SKU Number"</td>
            <td>System Information (Type 1)</td>
            <td>String</td>
            <td>19h</td>
            <td>32</td>
            <td>"A11a11001-EU-04"</td>
        </tr>
        <tr>
            <td>"Serial Number"</td>
            <td>System Information (Type 1)</td>
            <td>String</td>
            <td>07h</td>
            <td></td>
            <td>"A1B2C3456789ABC"</td>
        </tr>
        <tr>
            <td>"UUID"</td>
            <td>System Information (Type 1)</td>
            <td>Varies</td>
            <td>08h</td>
            <td>16</td>
            <td>Universal unique ID number<br>See section 7.2.1. in <a href="http://www.dmtf.org/standards/smbios">DMTF SMBIOS Specification 3.1</a> or later.</td>
        </tr>
        <tr>
            <td>"Enclosure Type"</td>
            <td>System Enclosure (Type 3) </td>
            <td>Byte</td>
            <td>05h</td>
            <td>N/A</td>
            <td>"detachable"</td>
        </tr>
        <tr>
            <td>BIOS Vendor</td>
            <td>BIOS Information (Type 0)</td>
            <td>Byte</td>
            <td>04h</td>
            <td>String</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>BIOS Version </td>
            <td>BIOS Information (Type 0)</td>
            <td>Byte</td>
            <td>05h</td>
            <td>String</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>BIOS Major Release</td>
            <td>BIOS Information (Type 0)</td>
            <td>Byte</td>
            <td>14h</td>
            <td>Varies</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>BIOS Minor Release</td>
            <td>BIOS Information (Type 0)</td>
            <td>Byte</td>
            <td>15h</td>
            <td>Varies</td>
            <td></td>
            <td></td>
        </tr>
    </tbody>
</table>



**Note** SMBIOS fields starting with BIOS \* may be considered optional or recommended.<br>These are used to build the **Computer Hardware ID (CHID)** and ensure additional levels of uniqueness in resulting CHID.


## TBD A

<table>
	<tbody>
		<tr>
			<td><b>Field name</b></td>
			<td><b>DTMF.org description</b></td>
			<td><b>Microsoft description</b></td>
			<td><b>Field format</b></td>
			<td><b>Hierarchy</b></td>
		</tr>
		<tr>
			<td>Manufacturer</td>
			<td>Number of null-terminated string.</td>
			<td>The value in the "manufacturer" field identifies the company brand name under which the device is marketed to the end user. (for example, a brand name or logo imprinted on the device)</td>
			<td>The format of the "manufacturer" field string is to match what end users identify as the company brand.</td>
			<td>The “manufacturer” field is the first-level indicator to end users, representing the grouping of all devices sold by the company. This field should rarely, if ever, change.</td>
		</tr>
		<tr>
			<td>Family</td>
			<td>Number of null-terminated string.</td>>
			<td>The value in the familyf field identifies the company sub-brand name, specific to a grouping of similar devices know as a product line, under which the device is marketed to end users. The "family" value excludes variance by components, device generation, manufactured year, SKU, or other factors. The "family" value is generally not specific enough to indicate an actual device, but rather product line marketed to end users.</td>
			<td>The format of the “family” field string is to match what End Users identify as Company’s sub-brand name, specific to a product line. The “family” field string should not contain the “manufacturer” name.</td>
			<td>The “family” field is the second-level indicator to End Users, representing a grouping of similar devices know as a product line. This field should remain consistent for the life of the product line.</td>
		</tr>
		<tr>
			<td>Product Name</td>
			<td>Number of null-terminated string.</td>
			<td>The value in the “product name” field identifies Company’s specific model of device, without enumerating configuration variance. (for example, processor, memory, and storage variance) There are often several “product names” that are specific to model in a specific “family”, although generally no more than a dozen or so.</td>
			<td>The format of the “product name” field string is to match what End Users see as the device model name or identifier value. The recommendation is to include the full value of the Family field followed by a single space and then the model name/identifier value.</td>
			<td>The “product name” field is the third-level indicator to End Users, representing the specific model of device. A “product name” may last for the lifetime of the “family”, through multiple revisions or generations of the hardware where hardware revisions are not marketed as a new product to End Users.</td>
		</tr>
		<tr>
			<td>Baseboard Product</td>
			<td>Number of null-terminated string.</td>
			<td>The value in the “baseboard product” field identifies the baseboard and should accurately reflect variances in baseboards across different devices in the same “family” and “product name”. This value must change when the baseboard in the device model changes and it may be used as an asset identifier for servicing.</td>
			<td>The format of the “baseboard product” field string can be set by Company, and it does not need to align to end user marketing information.</td>
			<td>The “baseboard product” field is the fourth-level indicator of devices to the company and is not marketed to end users. </td>
		</tr>
		<tr>
			<td>Serial Number</td>
			<td>Number of null-terminated string.</td>
			<td>The information in this structure defines attributes of the overall system and is intended to be associated with the Component ID group of the system’s MIF. An SMBIOS implementation is associated with a single system instance and contains one and only one System Information (Type 1) structure.</td>
			<td>TBD</td>
			<td>TBD</td>
		</tr>
		<tr>
			<td>UUID</td>
			<td>A UUID is an identifier that is designed be unique across to both time and space. It requires no central registration process. The UUID is 128 bits in length. The format is described in RFC4122.</td>
			<td>The value in this structure is a universally unique value as defined in the specification documents. This value is intended to be associated with this specific machine.</td>
			<td>The field format follows the latest DTMF.org SMBIOS specification document to meet universal uniqueness.</td>
			<td>The UUID field is not marketed to end users and is considered the seventh-level indicator of this device.</td>
		</tr>
		<tr>
			<td>SKU Number</td>
			<td>TBD</td>
			<td>TBD</td>
			<td>TBD</td>
			<td>TBD</td>
		</tr>
		<tr>
			<td>Enclosure Type</td>
			<td>TBD</td>
			<td>TBD</td>
			<td>N/A</td>
			<td>N/a</td>
		</tr>
		<tr>
			<td>BIOS Vendor</td>
			<td>String number of the BIOS vendor’s name</td>
			<td>Defined in the DMTF SMBIOS specification 3.1 or later</td>
			<td></td>
			<td></td>
		</tr>
        <tr>
			<td>BIOS Version</td>
			<td>TBD</td>
			<td>Defined in the DMTF SMBIOS specification 3.1 or later</td>
			<td>TBD</td>
			<td>TBD</td>
		</tr>
		<tr>
			<td>BIOS Major Release</td>
			<td>TBD</td>
			<td>Defined in the DMTF SMBIOS specification 3.1 or later</td>
			<td>TBD</td>
			<td>TBD</td>
		</tr>
		<tr>
			<td>BIOS Minor Release</td>
			<td>Identifies the minor release of the System BIOS; for example, the value is 16h for revision 10.22 and 01h for revision 2.1.</td>
			<td>Defined in the DMTF SMBIOS specification 3.1 or later</td>
			<td></td>
			<td></td>
		</tr>
	</tbody>
</table>




### TBD B

<table>
	<tbody>
		<tr>
			<td>TBD</td>
			<td>TBD</td>
			<td>TBD</td>
			<td>TBD</td>
		</tr>
		<tr>
			<td>TBD</td>
			<td>TBD</td>
			<td>TBD</td>
			<td>TBD</td>
		</tr>
		<tr>
			<td>TBD</td>
			<td>TBD</td>
			<td>TBD</td>
			<td>TBD</td>
		</tr>
		<tr>
			<td>TBD</td>
			<td>TBD</td>
			<td>TBD</td>
			<td>TBD</td>
		</tr>
		<tr>
			<td>TBD</td>
			<td>TBD</td>
			<td>TBD</td>
			<td>TBD</td>
		</tr>
		<tr>
			<td>TBD</td>
			<td>TBD</td>
			<td>TBD</td>
			<td>TBD</td>
		</tr>
		<tr>
			<td>TBD</td>
			<td>TBD</td>
			<td>TBD</td>
			<td>TBD</td>
		</tr>
	</tbody>
</table>
<p>TBD</p>



## Related resources

[Windows 10 Driver Publishing Workflow](http://download.microsoft.com/download/B/A/8/BA89DCE0-DB25-4425-9EFF-1037E0BA06F9/windows10_driver_publishing_workflow.docx) 

[SMBIOS DMTF Specifications](http://www.dmtf.org/standards/smbios)                                                 




--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Slicer%20settings%20%20RELEASE:%20%289/2/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


