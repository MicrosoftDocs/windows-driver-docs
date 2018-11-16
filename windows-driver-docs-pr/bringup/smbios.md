---
title: SMBIOS
description: The SMBIOS specification defines data structures and information that will go into the data structures pertinent to a system.
ms.date: 05/07/2018
ms.localizationpriority: medium
---


# SMBIOS

The SMBIOS specification defines data structures and information that will go into the data structures pertinent to a system. By using the latest SMBIOS specification, we keep up with the latest changes defined in the specification. The tables below describe recommended SMBIOS settings along with guidance on what type of information should be in these fields. Having these fields populated with data pertaining to each individual system allows system administrators the ability to remotely identify and manage these systems. Computer Hardware IDs (CHIDs) are generated using the values from these tables, and care and thought should be given to setting these.

To add uniformity to SMBIOS to better identify device information, we recommend the following as guidance when populating SMBIOS fields. The SMBIOS data below is also collected and used in various capacities. The data going into these fields should be planned in detail before populating using tools provided by BIOS/Firmware vendors. The hash generated for CHID targeting is based on the data populating these fields.

Although this information is similar to that listed in the [Windows 10 Driver Publishing Workflow](http://download.microsoft.com/download/B/A/8/BA89DCE0-DB25-4425-9EFF-1037E0BA06F9/windows10_driver_publishing_workflow.docx), the following tables prescribe additional levels of detail for some fields, increasing the level of specificity.

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
            <td>Manufacturer</td>
            <td>System Information (Type 1)</td>
            <td>String</td>
            <td>04h</td>
            <td>32</td>
            <td rowspan="8">Contoso, Inc. manufactures 2 product lines: 1) &quot;A&quot; series, and 2) &quot;B&quot; series. The &quot;A&quot; series of devices include the Contoso &quot;A11&quot; and &quot;A13&quot; device sub-brands, each of which have different screen sizes and both support physically detachable keyboards (though the keyboards are sold as an option). The &quot;A11&quot; has three models: 1) the base model (the a110001) 2) a midsize model with a premium audio package (the a110002) and 3) a high-end model with a higher resolution touch panel (the a110003). Each model has gone through several generations of baseboard revisions, which are identified internally with codes bb01 through bb04. Each of the &quot;A11&quot; models can be further customized with different storage and memory configurations. To separate different production runs on their manufacturing floor, Contoso uses an internal identification system that combines the Family, Product Name, market region, and production run number.</td>
            <td>&quot;Contoso&quot;</td>
        </tr>
        <tr>
            <td>Family</td>
            <td>System Information (Type 1)</td>
            <td>String</td>
            <td>1Ah</td>
            <td>64</td>
            <td>&quot;A11&quot;</td>
        </tr>
        <tr>
            <td>Product Name</td>
            <td>System Information (Type 1)</td>
            <td>String</td>
            <td>05h</td>
            <td>64</td>
            <td>&quot;A11 a110001&quot;</td>
        </tr>
        <tr>
            <td>Baseboard Product</td>
            <td>Baseboard Information (Type 2)</td>
            <td>String</td>
            <td>05h</td>
            <td>32</td>
            <td>&quot;bb03&quot;</td>
        </tr>
        <tr>
            <td>KU Number</td>
            <td>System Information (Type 1)</td>
            <td>String</td>
            <td>19h</td>
            <td>32</td>
            <td>&quot;A11a11001-EU-04&quot;</td>
        </tr>
        <tr>
            <td>Serial Number</td>
            <td>System Information (Type 1)</td>
            <td>String</td>
            <td>07h</td>
            <td></td>
            <td>&quot;A1B2C3456789ABC&quot;</td>
        </tr>
        <tr>
            <td>UUID</td>
            <td>System Information (Type 1)</td>
            <td>Varies</td>
            <td>08h</td>
            <td>16</td>
            <td>Universal unique ID number<br>See section 7.2.1. in <a href="http://www.dmtf.org/standards/smbios">DMTF SMBIOS Specification 3.1</a> or later.</td>
        </tr>
        <tr>
            <td>Enclosure Type</td>
            <td>System Enclosure (Type 3) </td>
            <td>Byte</td>
            <td>05h</td>
            <td>N/A</td>
            <td>&quot;detachable&quot;</td>
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

**Note**  SMBIOS fields starting with **BIOS** may be considered optional or recommended. These are used to build the **Computer Hardware ID (CHID)** and ensure additional levels of uniqueness in the resulting CHID.

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
			<td>The value in the <b>manufacturer</b> field identifies the company brand name under which the device is marketed to the end user. (for example, a brand name or logo imprinted on the device)</td>
			<td>The format of the <b>manufacturer</b> field string is to match what end users identify as the company brand.</td>
			<td>The <b>manufacturer</b> field is the first-level indicator to end users, representing the grouping of all devices sold by the company. This field should rarely, if ever, change.</td>
		</tr>
		<tr>
			<td>Family</td>
            <td>Number of null-terminated string.</td>&gt;
			<td>The value in the familyf field identifies the company sub-brand name, specific to a grouping of similar devices know as a product line, under which the device is marketed to end users. The <b>family</b> value excludes variance by components, device generation, manufactured year, SKU, or other factors. The <b>family</b> value is generally not specific enough to indicate an actual device, but rather product line marketed to end users.</td>
			<td>The format of the <b>family</b> field string is to match what End Users identify as Company’s sub-brand name, specific to a product line. The <b>family</b> field string should not contain the <b>manufacturer</b> name.</td>
			<td>The <b>family</b> field is the second-level indicator to End Users, representing a grouping of similar devices know as a product line. This field should remain consistent for the life of the product line.</td>
		</tr>
		<tr>
			<td>Product Name</td>
			<td>Number of null-terminated string.</td>
			<td>The value in the <b>product name</b> field identifies Company’s specific model of device, without enumerating configuration variance. (for example, processor, memory, and storage variance) There are often several <b>product names</b> that are specific to model in a specific <b>family</b>, although generally no more than a dozen or so.</td>
			<td>The format of the <b>product name</b> field string is to match what End Users see as the device model name or identifier value. The recommendation is to include the full value of the Family field followed by a single space and then the model name/identifier value.</td>
			<td>The <b>product name</b> field is the third-level indicator to End Users, representing the specific model of device. A <b>product name</b> may last for the lifetime of the <b>family</b>, through multiple revisions or generations of the hardware where hardware revisions are not marketed as a new product to End Users.</td>
		</tr>
		<tr>
			<td>Baseboard Product</td>
			<td>Number of null-terminated string.</td>
			<td>The value in the <b>baseboard product</b> field identifies the baseboard and should accurately reflect variances in baseboards across different devices in the same <b>family</b> and <b>product name</b>. This value must change when the baseboard in the device model changes and it may be used as an asset identifier for servicing.</td>
			<td>The format of the <b>baseboard product</b> field string can be set by Company, and it does not need to align to end user marketing information.</td>
			<td>The <b>baseboard product</b> field is the fourth-level indicator of devices to the company and is not marketed to end users. </td>
		</tr>
		<tr>
			<td>Serial Number</td>
			<td>Number of null-terminated string.</td>
			<td>The information in this structure defines attributes of the overall system and is intended to be associated with the Component ID group of the system’s MIF. An SMBIOS implementation is associated with a single system instance and contains one and only one System Information (Type 1) structure.</td>
			<td>The format of the <b>Serial Number</b> field string is to match the Serial Number on the exterior of the device.</td>
			<td>The <b>Serial Number</b> field is indicator of the Serial Number assigned from Company and is accessible on exterior of device. The <b>Serial Number</b> field is the sixth-level indicator of devices.</td>
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
			<td>Number of null-terminated string. This text string identifies a particular computer configuration for sale. It is sometimes also called a product ID or purchase order number. This number is frequently found in existing fields, but there is no standard format. Typically for a given system board from a given OEM, there are tens of unique processor, memory, hard drive, and optical drive configurations.</td>
			<td>The value in the <b>SKU number</b> field identifies the device in a format that can be determined by Company. This field may include variations of the device determined by production run, shipment region, retailer, configuration variances. (for example, processor, memory, and storage variance) This value can be used as an asset identifier for servicing and if it is not used by Company, it may be left blank.</td>
			<td>The format of the <b>SKU number</b> field string can be set by Company, and it does not need to align to end user marketing information.</td>
			<td>The <b>SKU number</b> field is the fifth-level indicator of devices to Company and is not marketed to end users.</td>
		</tr>
		<tr>
			<td>Enclosure Type</td>
			<td>N/A</td>
			<td>Defined in the <b>Enclosure Type</b> table below</td>
			<td>N/A</td>
			<td>N/A</td>
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
			<td>String number of the BIOS Version. This value is a free-form string that may contain Core and OEM version information.</td>
			<td>Defined in the DMTF SMBIOS specification 3.1 or later</td>
			<td></td>
			<td></td>
		</tr>
		<tr>
			<td>BIOS Major Release</td>
			<td>Identifies the major release of the System BIOS, for example, the value is 0Ah for revision 10.22 and 02h for revision 2.1. This field or the System BIOS Minor Release field or both are updated each time a System BIOS update for a given system is released. If the system does not support the use of this field, the value is FFh for both this field and the System BIOS Minor Release field.</td>
			<td>Defined in the DMTF SMBIOS specification 3.1 or later</td>
			<td></td>
			<td></td>
		</tr>
		<tr>
			<td>BIOS Minor Release</td>
			<td>Identifies the minor release of the System BIOS, for example, the value is 16h for revision 10.22 and 01h for revision 2.1.</td>
			<td>Defined in the DMTF SMBIOS specification 3.1 or later</td>
			<td></td>
			<td></td>
		</tr>
	</tbody>
</table>


The following table describes settings for the **Enclosure Type** field.

<table>
	<tbody>
		<tr>
			<td><b>Enclosure Type</b></td>
			<td><b>Byte Value</b></td>
			<td><b>OHR FFC/FFSC</b></td>
			<td><b>Microsoft description</b></td>
		</tr>
		<tr>
			<td>Desktop</td>
			<td>03h</td>
			<td>Desktop/Standard</td>
			<td><b>Desktop</b> means a Customer System in a tower case and is not a portable Customer System. It does not include an integrated display and inputs.</td>
		</tr>
		<tr>
			<td>Notebook</td>
			<td>0Ah</td>
			<td>Notebook/Standard</td>
			<td><b>Notebook</b> means a Customer System with a clamshell form factor and has a non-detachable keyboard. Portable (08h) or Laptop (09h) are not to be used when identifying a <b>Notebook</b>. </td>
		</tr>
		<tr>
			<td>All-in-One</td>
			<td>0Dh</td>
			<td>Desktop/AiO</td>
			<td><b>All-in-One</b> means a Customer System that integrates a touch screen with other hardware components in a single chassis.</td>
		</tr>
		<tr>
			<td>Tablet</td>
			<td>1Eh</td>
			<td>Tablet/Standard</td>
			<td><b>Tablet</b> means a Customer System that combines a display, rechargeable power source, and other components into a single chassis, and utilizes touch as its primary means of input. It does not include a physically attached keyboard. In the case where the Customer System’s form factor does not allow for a keyboard to be physically connected to the chassis, but a Bluetooth or other wireless keyboard is sold as an optional accessory to the End User, the <b>enclosure type</b> field is to be identified as a <b>Tablet</b>.</td>
		</tr>
		<tr>
			<td>Convertible</td>
			<td>1Fh</td>
			<td>Notebook/Convertible</td>
			<td><b>Convertible</b> means a Customer System that combines a display, rechargeable power source, and point device into a single chassis with an adjustable (any motion:  flips, swivels, turns) display to be facing forward or facing away from the attached keyboard.</td>
		</tr>
		<tr>
			<td>Detachable</td>
			<td>20h</td>
			<td>Tablet/Standard</td>
			<td><b>Detachable</b> means a Customer System that combines a display, rechargeable power source, and pointing device into a single chassis together with a detachable keyboard. In the case where the Customer System’s form factor allows for a keyboard, not including Bluetooth or other wireless keyboards, to be physically connected to the chassis but the physical keyboard is sold as an optional accessory to the End User, the <b>enclosure type</b> field is to be identified as a <b>Detachable</b>.</td>
		</tr>
	</tbody>
</table>


## Related resources

[Windows 10 Driver Publishing Workflow](http://download.microsoft.com/download/B/A/8/BA89DCE0-DB25-4425-9EFF-1037E0BA06F9/windows10_driver_publishing_workflow.docx) 

[SMBIOS DMTF Specifications](http://www.dmtf.org/standards/smbios)                                                 



