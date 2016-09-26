---
title: Supporting Usages in Multi-touch Digitizers
description: Supporting Usages in Multi-touch Digitizers
ms.assetid: C139C81E-78D2-4CB6-A532-748613B1F068
---

# Supporting Usages in Multi-touch Digitizers


In the context of a Windows Pointer Device, multi-touch refers to support for two or more contact points. The required and optional usages for a multi-touch digitizer device are described below.

### <span id="required_hid_usages"></span><span id="REQUIRED_HID_USAGES"></span>Required HID Usages for Multi-touch Digitizers

The report descriptor for a multi-touch digitizer must specify that the device is a HID touch screen (page = 0x0D and usage = 0x04).

In addition to the existing HID touch usages, multi-touch digitizers must implement the following [usages](supporting-usages-in-digitizer-report-descriptors.md#required-hid-usages).

-   Contact identifier
-   Contact count maximum
-   Scan Time

### <span id="optional_hid_usages"></span><span id="OPTIONAL_HID_USAGES"></span>Optional HID Usages

The following [usages](supporting-usages-in-digitizer-report-descriptors.md#optional-hid-usages) are optional, but multi-touch digitizers should repoirt them if the digitizer hardware supports them.

-   Confidence
-   Pressure
-   Azimuth
-   In-range (optional for touch, required for pen)
-   Width and Height

### <span id="HID_Usages_for_Multi-touch_Digitizers"></span><span id="hid_usages_for_multi-touch_digitizers"></span><span id="HID_USAGES_FOR_MULTI-TOUCH_DIGITIZERS"></span>HID Usages for Multi-touch Digitizers

The HID standard defines the following usages for multi-touch input from digitizers.

| Name                  | Description                          | CA Usage | Page      | Type               | ID   |
|-----------------------|--------------------------------------|----------|-----------|--------------------|------|
| Contact Identifier    | Contact identifier                   | Touch    | Digitizer | Dynamic Value (DV) | 0x51 |
| Contact Count         | Actual contact count                 | Touch    | Digitizer | Dynamic Value (DV) | 0x54 |
| Contact count maximum | Maximum number of contacts supported | Touch    | Digitizer | Dynamic Value (DV) | 0x55 |

 

<span id="_Contact_identifier"></span><span id="_contact_identifier"></span><span id="_CONTACT_IDENTIFIER"></span> **Contact identifier**  
Specifies the identifier of the current contact. An identifier must remain constant while the contact is detected by the device. Each separate concurrent contact must have a unique identifier. Identifiers can be reused if a contact is no longer detected. If the device supports "in-air" packets (the contact is hovering above the surface), the identifier must persist from the time that the contact is detected until the time that it goes out of range.

<span id="_Contact_count"></span><span id="_contact_count"></span><span id="_CONTACT_COUNT"></span> **Contact count**  
Specifies the number of valid contacts in the current packet. Drivers that use parallel or Hybrid mode should include this usage. A device that cannot provide this value must use **NULL** for all values in the first position that do not contain valid contact information. However, **NULL** is an option only for Parallel mode devices. Devices should not use a combination of Contact count and **NULL** for reporting the actual count. Either one or the other should be used.

<span id="_Contact_count_maximum"></span><span id="_contact_count_maximum"></span><span id="_CONTACT_COUNT_MAXIMUM"></span> **Contact count maximum**  
Specifies the total number of contacts that a multi-touch device supports. This usage must be included in the multi-touch top-level collection and not in any child collection. This usage must be present in a feature report in the touch top-level collection. While reporting data, a device must not report more contacts than the contact count maximum. Any new contact information reported after the contact count maximum has been reached will be ignored by the host. A device without the Contact count maximum in the descriptor will be considered to be a single-touch device.

 

 




