---
title: NFP device identifiers
description: NFP device identifiers
ms.assetid: B387D3F8-A9A7-47F0-B5E3-8437581947E4
---

# NFP device identifiers


The following are the device identifiers for NFP device drivers:

-   Device Interface Class
    -   GUID\_DEVINTERFACE\_NFP
    -   "{FB3842CD-9E2A-4F83-8FCC-4B0761139AE9}"
-   Device Class GUID
    -   “{5630831C-06C9-4856-B327-F5D32586E060}”
-   Device Class
    -   “Proximity”
    -   This is an OS-defined Device Class starting with Windows 8. Drivers that expose this interface must match this Device Class.
-   DEVPKEY\_NFP\_Capabilities
    -   0xFB3842CD, 0x9E2A, 0x4F83, 0x8F, 0xCC, 0x4B, 0x07, 0x61, 0x13, 0x9A, 0xE9, 0x02

If the device is advertised as NFC, the driver MUST populate DEVPKEY\_NFP\_Capabilities on the exposed GUID\_DEVINTERFACE\_NFP interface with a DEVPROP\_TYPE\_STRING\_LIST property containing one entry: “StandardNfc”.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnfpdrivers\nfpdrivers%5D:%20NFP%20device%20identifiers%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




