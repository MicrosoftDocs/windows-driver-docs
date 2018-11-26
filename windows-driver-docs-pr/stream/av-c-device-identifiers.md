---
title: AV/C Device Identifiers
description: AV/C Device Identifiers
ms.assetid: c2d108c7-5ea9-42c1-92d7-5ba90f2f4232
keywords:
- AV/C WDK , identifiers
- identifiers WDK AV/C
- device IDs WDK AV/C
- Avc.sys function driver WDK , identifiers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# AV/C Device Identifiers





When a user connects an AV/C device to the computer, *Avc.sys* enumerates the active subunits on the device and generates the device identifier (ID) strings for them. There is a device identifier for each active subunit in an AV/C device. If there are no active subunits in an AV/C device, then *Avc.sys* generates a device identifier for the AV/C device itself.

The format for device identifier fields for peer subunits is:

**AVC\\*Vendor*&*Model*&*SubunitType*&*SubunitID***

The format for device identifier fields for virtual subunits is:

**VAVC\\*Vendor*&*Model*&*SubunitType*&*SubunitID***

In fields where numbers are used, the numbers are converted to hexadecimal, and alpha characters are converted to uppercase. There are no leading zeros. The device identifier specified in the INF file for the driver must match this format. All numeric fields in hardware identifiers and compatible identifiers are tagged as follows (with exceptions as noted):

-   ***Vendor***: **VEN\_** (unless vendor text is available)

-   ***Model***: **MOD\_** (unless model text is available)

-   ***SubunitType***: **TYP\_**

-   ***SubunitID***: **ID\_**

*Avc.sys* creates a device object for each active subunit that is present on an external AV/C device. An IEEE 1394 bus reset is triggered whenever an AV/C device is added to or removed from the IEEE 1394 bus. *Avc.sys* then re-enumerates the active subunits on all connected AV/C devices. The re-enumeration allows the device to reconfigure itself to add or remove subunits without requiring Windows to reload *Avc.sys* every time the AV/C device's operating mode is switched. For example, this functionality applies when a DV camcorder is switched between camera mode and VTR mode. Consequently, subunit drivers are loaded and unloaded only as their corresponding active subunits are added and removed.

*Avc.sys* cannot distinguish between multiple subunits of the same ***SubunitType***, so adding and removing these subunits loads and unloads the corresponding subunit driver with the highest ***SubunitID***.

Each subunit's device object has one or two hardware identifiers and multiple compatible identifiers. A vendor must supply one or more of these hardware or compatible identifiers, described below in the INF file for their subunit driver. Windows uses these device identifiers to locate suitable drivers to load for each subunit the first time the device is connected to the computer. You can examine the Microsoft-supplied *61883.inf*, *Msdv.inf* and *Mstape.inf* files for examples of hardware and compatible device identifiers for AV/C devices. For more information about implementing INF files, see [INF File Sections and Directives](https://msdn.microsoft.com/library/windows/hardware/ff547433).

The individual elements of the device identifier string are as follows:

<a href="" id="vendor"></a>***Vendor***  
If vendor name text is present in the IEEE 1394 Configuration ROM's Unit Capabilities root directory, then the vendor name text is used in the ***Vendor*** field. For example:

**AVC\\Microsoft&*Model*&*SubunitType*&*SubunitID***

Otherwise, the vendor's unique number (as assigned by the IEEE 1394 Trade Association) is used in the ***Vendor*** field. In the following example, "50F2" is Microsoft's 1394TA vendor number:

**AVC\\VEN\_50F2&*Model*&*SubunitType*&*SubunitID***

If the vendor name text is not present, then the numeric value is obtained from the Module\_Vendor\_ID entry in the IEEE 1394 Configuration ROM's root directory. The Command and Status Register (CSR) Architecture Key for this immediate entry is 0316 (hexadecimal), and the remaining 24 bits are the numeric Module\_Vendor\_ID entry.

<a href="" id="model"></a>***Model***  
If the model name text is present in the IEEE 1394 Configuration ROM's Unit Capabilities, then the model name text is used in the ***Model*** field. For example:

**AVC\\Microsoft&DVCamcorder&*SubunitType*&*SubunitID***

Otherwise, the model number is used in the ***Model*** field. For example:

**AVC\\Microsoft&MOD\_0&*SubunitType*&*SubunitID***

The model text from the 1394 Configuration ROM unit directory is used, giving precedence to the unit directory entries. The order of preference is as follows:

1.  The numeric identifier from the unit directory.

2.  The model text from the root directory.

3.  The model identifier from the root directory.

<a href="" id="subunittype"></a>***SubunitType***  
If available, the ***SubunitType*** field is extracted from the subunit address and converted to a string of hexadecimal values for each byte. There are multiple bytes only if the subunit type has been extended. Typically, the initial byte is extracted from the five most significant bits of the address byte, as described in section 5.3.3 of the *AV/C Digital Interface Command Set General Specification, Rev 3.0*.

For example: **AVC\\VEN\_50F2&MOD\_0&TYP\_4&*SubunitID***

For a list of subunit types that *Avc.sys* supports and their corresponding numeric values, see [**AvcSubunitType**](https://msdn.microsoft.com/library/windows/hardware/ff554137).

<a href="" id="subunitid"></a>***SubunitID***  
If the ***SubunitType*** field is available, the ***SubunitID*** field also is available. When *Avc.sys* queries the AV/C device for its subunit information, the device responds with the count of the subunits for each type. This zero-based count is used to create a device identifier for each subunit. The subunit address specification also allows for the ***SubunitID*** field to be extended, but this aspect is hidden from the subunit driver (and from you, the author of the INF file). The zero-based instance number is used in all cases. For example, if the ***SubunitID*** field is extended to support 270 subunits, the 270th subunit has a subunit identifier of 10D (269 decimal). For example:

**AVC\\Microsoft&MOD\_0&TYP\_4&ID\_10D**

For AV/C units that do not provide a ***SubunitType*** or ***SubunitID***, the device identifier string then consists of only the ***Vendor*** and ***Model*** fields, with no trailing ampersand (&).

 

 




