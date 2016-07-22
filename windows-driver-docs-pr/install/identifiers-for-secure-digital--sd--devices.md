---
title: Identifiers for Secure Digital (SD) Devices
description: Identifiers for Secure Digital (SD) Devices
ms.assetid: d5e112b7-29ed-4950-858c-81fe0d19a902
keywords: ["device identification strings WDK , SD devices", "identification strings WDK device , SD devices", "identifiers WDK device , SD devices", "SD device IDs WDK device installations", "Secure Digital device IDs WDK device installations", "device IDs WDK device installations", "hardware IDs WDK device installations", "compatible IDs WDK device installations"]
---

# Identifiers for Secure Digital (SD) Devices


When the SD bus driver detects an SD device in the host controller socket, it examines the device configuration of the card to construct a device and hardware IDs for the device and its functions. For SD combination cards and multifunction SDIO devices, the bus driver creates a PDO and a hardware ID for each respective function.

Because the internal configuration of an SD memory device is significantly different from that of an SDIO device, the SD bus driver uses two different hardware ID formats, one for SD memory devices and another for SDIO devices.

### <a href="" id="sd-device-ids"></a> SD device ids

The device ID of an SD memory device uses the following format:

SD\\VID\_v(2)&OID\_o(4)&PID\_p(0-5)&REV\_n(1).m(1)

Where:

-   *v(2)* is a two-digit hexadecimal ID assigned by the SD Card Association (SDA) that identifies the card's manufacturer.

-   *o(4)* is a four-digit hexadecimal ID, also assigned by the SDA, that identifies the card's original equipment manufacturer (OEM) and/or the card contents.

-   *p(0-5)* is a vendor-supplied ASCII string, of 0 to 5 five characters, that indicates the product name, and n(1).m(1) is a two digit, vendor-supplied, revision number, with a decimal between the two digits (for example, 6.2).

The device ID of an SDIO device uses the following format:

SD\\VID\_v(4)&PID\_p(4)

Where:

-   *v(4)* is a four-digit hexadecimal vendor code assigned by PCMCIA and JEIDA.

-   *p(4)* is the four-digit hexadecimal product and/or revision number that the vendor assigns to the device.

The SD bus driver extracts the vendor and product codes from the CISTPL\_MANFID tuple in the device's Card Information Structure (CIS) area.

### <a href="" id="sd-hardware-ids"></a> SD hardware IDs

For SD memory devices, the bus driver supplies two hardware IDs: one that is identical to the device ID, and another that is the same as the device ID, but without the revision information. The ID with revision information uses the following format:

SD\\VID\_v(2)&OID\_o(4)&PID\_p(0-5)

Where, as with the device ID:

-   *v(2)* is a two-digit hexadecimal ID assigned by the SD Card Association (SDA) that identifies the card's manufacturer.

-   *o(4)* is a four-digit hexadecimal ID, also assigned by the SDA, that identifies the card's original equipment manufacturer (OEM) and/or the card contents.

-   *p(0-5)* is a vendor-supplied ASCII string, of 0 to 5 five characters, that indicates the product name.

For SDIO devices, the SD bus driver supplies a single hardware ID that is identical to the device ID.

### <a href="" id="sd-compatible-ids"></a> SD compatible IDs

In addition to device and hardware IDs, the SD bus driver generates a compatible ID under certain circumstances.

For SD memory devices, the bus driver always generates the following compatible ID:

SD\\CLASS\_STORAGE

For SDIO devices, the SD bus driver generates the following compatible ID, provided the value in the function basic register (FBR) is not zero:

SD\\CLASS\_c(2)

where *c(2)* is the two-digit hexadecimal device interface code.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Identifiers%20for%20Secure%20Digital%20%28SD%29%20Devices%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




