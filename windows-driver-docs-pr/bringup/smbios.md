---
title: SMBIOS
description: The SMBIOS specification defines data structures and information that will go into the data structures pertinent to a system.
ms.date: 03/23/2023
---

# SMBIOS

The SMBIOS specification defines data structures and information that will go into the data structures pertinent to a system. By using the latest SMBIOS specification, we keep up with the latest changes defined in the specification. The tables below describe recommended SMBIOS settings along with guidance on what type of information should be in these fields. Having these fields populated with data pertaining to each individual system allows system administrators the ability to remotely identify and manage these systems. Computer Hardware IDs (CHIDs) are generated using the values from these tables, and care and thought should be given to setting these.

To add uniformity to SMBIOS to better identify device information, we recommend the following as guidance when populating SMBIOS fields. The SMBIOS data below is also collected and used in various capacities. The data going into these fields should be planned in detail before populating using tools provided by BIOS/Firmware vendors. The hash generated for CHID targeting is based on the data populating these fields.

Although this information is similar to that listed in the [Windows 10 Driver Publishing Workflow](https://download.microsoft.com/download/B/A/8/BA89DCE0-DB25-4425-9EFF-1037E0BA06F9/windows10_driver_publishing_workflow.docx), the following tables prescribe additional levels of detail for some fields, increasing the level of specificity.

## Recommended settings when moving to SMBIOS 3.0

The following table contains information about the BIOS fields.

| Field name | Structure name and type | Value | Offset | Length | Example scenario | Example |
|--|--|--|--|--|--|--|
| Manufacturer | System Information (Type 1) | String | 04h | 32 | See example scenario below | "Contoso" |
| Family | System Information (Type 1) | String | 1Ah | 64 | See example scenario below | "A11" |
| Product Name | System Information (Type 1) | String | 05h | 64 | See example scenario below | "A11 a110001" |
| Baseboard Product | System Information (Type 2) | String | 05h | 32 | See example scenario below | "bb03" |
| KU Number | System Information (Type 1) | String | 19h | 32 | See example scenario below | "A11a11001-EU-04" |
| Serial Number | System Information (Type 1) | String | 07h | &nbsp; | See example scenario below | "A1B2C3456789ABC" |
| UUID | System Information (Type 1) | Varies | 08h | 16 | See example scenario below | Universal unique ID number (UUID). See section 7.2.1. in [DMTF SMBIOS Specification 3.1](https://www.dmtf.org/standards/smbios) or later. |
| Enclosure Type | System Enclosure (Type 3) | Byte | 05h | N/A | See example scenario below | "detachable" |
| BIOS Vendor | BIOS Information (Type 0) | Byte | 04h | String | &nbsp; | &nbsp; |
| BIOS Version | BIOS Information (Type 0) | Byte | 05h | String | &nbsp; | &nbsp; |
| BIOS Major Release | BIOS Information (Type 0) | Byte | 14h | Varies | &nbsp; | &nbsp; |
| BIOS Minor Release | BIOS Information (Type 0) | Byte | 15h | Varies | &nbsp; | &nbsp; |

**Example scenario:**  Contoso, Inc. manufactures 2 product lines: (1) "A" series, and (2) "B" series. The "A" series of devices include the Contoso "A11" and "A13" device sub-brands, each of which have different screen sizes and both support physically detachable keyboards (though the keyboards are sold as an option). The "A11" has three models: (1) the base model (the a110001) (2) a midsize model with a premium audio package (the a110002) and (3) a high-end model with a higher resolution touch panel (the a110003). Each model has gone through several generations of baseboard revisions, which are identified internally with codes bb01 through bb04. Each of the "A11" models can be further customized with different storage and memory configurations. To separate different production runs on their manufacturing floor, Contoso uses an internal identification system that combines the Family, Product Name, market region, and production run number.

SMBIOS fields starting with **BIOS** may be considered optional or recommended. These are used to build the **Computer Hardware ID (CHID)** and ensure additional levels of uniqueness in the resulting CHID.

The following table describes hierarchy level indicators for end users.

| Field name | DTMF.org description | Microsoft description | Field format | Hierarchy |
|--|--|--|--|--|
| Manufacturer | Number of null-terminated string. | The value in the **manufacturer** field identifies the company brand name under which the device is marketed to the end user (for example, a brand name or logo imprinted on the device). | The format of the **manufacturer** field string is to match what end users identify as the company brand. | The **manufacturer** field is the first-level indicator to end users, representing the grouping of all devices sold by the company. This field should rarely, if ever, change. |
| Family | Number of null-terminated string. | The value in the **family** field identifies the company sub-brand name, specific to a grouping of similar devices know as a product line, under which the device is marketed to end users. The **family** value excludes variance by components, device generation, manufactured year, SKU, or other factors. The **family** value is generally not specific enough to indicate an actual device, but rather product line marketed to end users. | The format of the **family** field string is to match what End Users identify as Company's sub-brand name, specific to a product line. The family field string should not contain the **manufacturer** name. | The **family** field is the second-level indicator to End Users, representing a grouping of similar devices know as a product line. This field should remain consistent for the life of the product line. |
| Product Name | Number of null-terminated string. | The value in the **product name** field identifies Company's specific model of device, without enumerating configuration variance. (for example, processor, memory, and storage variance) There are often several **product names** that are specific to model in a specific **family**, although generally no more than a dozen or so. | The format of the **product name** field string is to match what End Users see as the device model name or identifier value. The recommendation is to include the full value of the Family field followed by a single space and then the model name/identifier value. | The **product name** field is the third-level indicator to End Users, representing the specific model of device. A **product name** may last for the lifetime of the **family**, through multiple revisions or generations of the hardware where hardware revisions are not marketed as a new product to End Users. |
| Baseboard Product | Number of null-terminated string. | The value in the **baseboard product** field identifies the baseboard and should accurately reflect variances in baseboards across different devices in the same **family** and **product name**. This value must change when the baseboard in the device model changes and it may be used as an asset identifier for servicing. | The format of the **baseboard product** field string can be set by Company, and it does not need to align to end user marketing information. | The **baseboard product** field is the fourth-level indicator of devices to the company and is not marketed to end users. |
| Serial Number | Number of null-terminated string. | The information in this structure defines attributes of the overall system and is intended to be associated with the Component ID group of the system's MIF. An SMBIOS implementation is associated with a single system instance and contains one and only one System Information (Type 1) structure. | The format of the **Serial Number** field string is to match the **Serial Number** on the exterior of the device. | The **Serial Number** field is indicator of the **Serial Number** assigned from Company and is accessible on exterior of device. The **Serial Number** field is the sixth-level indicator of devices. |
| UUID | A UUID is an identifier that is designed be unique across to both time and space. It requires no central registration process. The UUID is 128 bits in length. The format is described in RFC4122. | The value in this structure is a universally unique value as defined in the specification documents. This value is intended to be associated with this specific machine. | The field format follows the latest DTMF.org SMBIOS specification document to meet universal uniqueness. | The UUID field is not marketed to end users and is considered the seventh-level indicator of this device. |
| SKU Number | Number of null-terminated string. This text string identifies a particular computer configuration for sale. It is sometimes also called a product ID or purchase order number. This number is frequently found in existing fields, but there is no standard format. Typically for a given system board from a given OEM, there are tens of unique processor, memory, hard drive, and optical drive configurations. | The value in the **SKU number** field identifies the device in a format that can be determined by Company. This field may include variations of the device determined by production run, shipment region, retailer, configuration variances. (for example, processor, memory, and storage variance) This value can be used as an asset identifier for servicing and if it is not used by Company, it may be left blank. | The format of the **SKU number** field string can be set by Company, and it does not need to align to end user marketing information. | The **SKU number** field is the fifth-level indicator of devices to Company and is not marketed to end users. |
| Enclosure Type | N/A | Defined in the **Enclosure Type** table below | N/A | N/A |
| BIOS Vendor | String number of the BIOS vendor's name | Defined in the DMTF SMBIOS specification 3.1 or later | &nbsp; | &nbsp; |
| BIOS Version | String number of the BIOS Version. This value is a free-form string that may contain Core and OEM version information. | Defined in the DMTF SMBIOS specification 3.1 or later | &nbsp; | &nbsp; |
| BIOS Major Release | Identifies the major release of the System BIOS, for example, the value is 0Ah for revision 10.22 and 02h for revision 2.1. This field or the System BIOS Minor Release field or both are updated each time a System BIOS update for a given system is released. If the system does not support the use of this field, the value is FFh for both this field and the System BIOS Minor Release field. | Defined in the DMTF SMBIOS specification 3.1 or later | &nbsp; | &nbsp; |
| BIOS Minor Release | Identifies the minor release of the System BIOS, for example, the value is 16h for revision 10.22 and 01h for revision 2.1. | Defined in the DMTF SMBIOS specification 3.1 or later | &nbsp; | &nbsp; |

The following table describes settings for the **Enclosure Type** field.

| Enclosure type | Byte value | OHR FFC/FFSC | Microsoft description |
|--|--|--|--|
| Desktop | 03h | Desktop/Standard | **Desktop** means a Customer System in a tower case and is not a portable Customer System. It does not include an integrated display and inputs. |
| Notebook | 0Ah | Notebook/Standard | **Notebook** means a Customer System with a clamshell form factor and has a non-detachable keyboard. Portable (08h) or Laptop (09h) are not to be used when identifying a **Notebook**. |
| All-in-One | 0Dh | Desktop/AiO | **All-in-One** means a Customer System that integrates a touch screen with other hardware components in a single chassis. |
| Tablet | 1Eh | Tablet/Standard | **Tablet** means a Customer System that combines a display, rechargeable power source, and other components into a single chassis, and utilizes touch as its primary means of input. It does not include a physically attached keyboard. In the case where the Customer System's form factor does not allow for a keyboard to be physically connected to the chassis, but a Bluetooth or other wireless keyboard is sold as an optional accessory to the End User, the **enclosure type** field is to be identified as a **Tablet**. |
| Convertible | 1Fh | Notebook/Convertible | **Convertible** means a Customer System that combines a display, rechargeable power source, and point device into a single chassis with an adjustable (any motion:  flips, swivels, turns) display to be facing forward or facing away from the attached keyboard. |
| Detachable | 20h | Tablet/Standard | **Detachable** means a Customer System that combines a display, rechargeable power source, and pointing device into a single chassis together with a detachable keyboard. In the case where the Customer System's form factor allows for a keyboard, not including Bluetooth or other wireless keyboards, to be physically connected to the chassis but the physical keyboard is sold as an optional accessory to the End User, the **enclosure type** field is to be identified as a **Detachable**. |

## Related resources

[Windows 10 Driver Publishing Workflow](https://download.microsoft.com/download/B/A/8/BA89DCE0-DB25-4425-9EFF-1037E0BA06F9/windows10_driver_publishing_workflow.docx)

[SMBIOS DMTF Specifications](https://www.dmtf.org/standards/smbios)
