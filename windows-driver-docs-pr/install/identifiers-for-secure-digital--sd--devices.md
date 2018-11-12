---
title: Identifiers for Secure Digital (SD) Devices
description: Identifiers for Secure Digital (SD) Devices
ms.assetid: d5e112b7-29ed-4950-858c-81fe0d19a902
keywords:
- device identification strings WDK , SD devices
- identification strings WDK device , SD devices
- identifiers WDK device , SD devices
- SD device IDs WDK device installations
- Secure Digital device IDs WDK device installations
- device IDs WDK device installations
- hardware IDs WDK device installations
- compatible IDs WDK device installations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Identifiers for Secure Digital (SD) Devices


When the SD bus driver detects an SD device in the host controller socket, it examines the device configuration of the card to construct a device and hardware IDs for the device and its functions. For SD combination cards and multifunction SDIO devices, the bus driver creates a PDO and a hardware ID for each respective function.

Because the internal configuration of an SD memory device is significantly different from that of an SDIO device, the SD bus driver uses two different hardware ID formats, one for SD memory devices and another for SDIO devices.

### <a href="" id="sd-device-ids"></a> SD device ids

The device ID of an SD memory device uses the following format:

SD\\VID_v(2)&OID_o(4)&PID_p(0-5)&REV_n(1).m(1)

Where:

-   *v(2)* is a two-digit hexadecimal ID assigned by the SD Card Association (SDA) that identifies the card's manufacturer.

-   *o(4)* is a four-digit hexadecimal ID, also assigned by the SDA, that identifies the card's original equipment manufacturer (OEM) and/or the card contents.

-   *p(0-5)* is a vendor-supplied ASCII string, of 0 to 5 five characters, that indicates the product name, and n(1).m(1) is a two digit, vendor-supplied, revision number, with a decimal between the two digits (for example, 6.2).

The device ID of an SDIO device uses the following format:

SD\\VID_v(4)&PID_p(4)

Where:

-   *v(4)* is a four-digit hexadecimal vendor code assigned by PCMCIA and JEIDA.

-   *p(4)* is the four-digit hexadecimal product and/or revision number that the vendor assigns to the device.

The SD bus driver extracts the vendor and product codes from the CISTPL_MANFID tuple in the device's Card Information Structure (CIS) area.

### <a href="" id="sd-hardware-ids"></a> SD hardware IDs

For SD memory devices, the bus driver supplies two hardware IDs: one that is identical to the device ID, and another that is the same as the device ID, but without the revision information. The ID with revision information uses the following format:

SD\\VID_v(2)&OID_o(4)&PID_p(0-5)

Where, as with the device ID:

-   *v(2)* is a two-digit hexadecimal ID assigned by the SD Card Association (SDA) that identifies the card's manufacturer.

-   *o(4)* is a four-digit hexadecimal ID, also assigned by the SDA, that identifies the card's original equipment manufacturer (OEM) and/or the card contents.

-   *p(0-5)* is a vendor-supplied ASCII string, of 0 to 5 five characters, that indicates the product name.

For SDIO devices, the SD bus driver supplies a single hardware ID that is identical to the device ID.

### <a href="" id="sd-compatible-ids"></a> SD compatible IDs

In addition to device and hardware IDs, the SD bus driver generates a compatible ID under certain circumstances.

For SD memory devices, the bus driver always generates the following compatible ID:

SD\\CLASS_STORAGE

For SDIO devices, the SD bus driver generates the following compatible ID, provided the value in the function basic register (FBR) is not zero:

SD\\CLASS_c(2)

where *c(2)* is the two-digit hexadecimal device interface code.

 

 





