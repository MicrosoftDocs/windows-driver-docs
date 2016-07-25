---
title: Identifiers for IDE Devices
description: Identifiers for IDE Devices
ms.assetid: b1624eb9-afa7-49ce-9db1-b0eab466ddcd
keywords: ["device identification strings WDK , IDE devices", "identification strings WDK device , IDE devices", "identifiers WDK device , IDE devices", "IDE device identifiers WDK device installations", "device IDs WDK device installations", "hardware IDs WDK device installations", "compatible IDs WDK device installations", "integrated device electronics identifiers WDK device installations"]
---

# Identifiers for IDE Devices


## <a href="" id="ddk-identifiers-for-ide-devices-dg"></a>


Identifiers for integrated device electronics (IDE) devices resemble SCSI identifiers. The device ID format is as follows:

IDE\\t\*v(40)r(8)

Where:

-   *t\** is a device-type code of variable length.

-   *v(40)* is a string that contains the vendor name, an underscore, vendor's product name, and enough underscores to bring the total to 40 characters.

-   *r(8)* is an 8-character revision number.

There are three hardware IDs, in addition to the device ID:

IDE\\v(40)r(8)

IDE\\t\*v(40)

V(40)r(8)

As in the SCSI case, there is only one compatible ID, a generic type name similar to the standard SCSI type names supplied by the SCSI Port driver, but having only eleven entries instead of eighteen. The generic device-type names for IDE devices are as follows:

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">IDE Type Code</th>
<th align="left">Device Type</th>
<th align="left">Generic Type</th>
<th align="left">Peripheral ID</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>DIRECT_ACCESS_DEVICE (0)</p></td>
<td align="left"><p>Disk</p></td>
<td align="left"><p>GenDisk</p></td>
<td align="left"><p>DiskPeripheral</p></td>
</tr>
<tr class="even">
<td align="left"><p>SEQUENTIAL_ACCESS_DEVICE (1)</p></td>
<td align="left"><p>Sequential</p></td>
<td align="left"><p>GenSequential</p></td>
<td align="left"><p>TapePeripheral</p></td>
</tr>
<tr class="odd">
<td align="left"><p>PRINTER_DEVICE (2)</p></td>
<td align="left"><p>Printer</p></td>
<td align="left"><p>GenPrinter</p></td>
<td align="left"><p>PrinterPeripheral</p></td>
</tr>
<tr class="even">
<td align="left"><p>PROCESSOR_DEVICE (3)</p></td>
<td align="left"><p>Processor</p></td>
<td align="left"><p>GenProcessor</p></td>
<td align="left"><p>OtherPeripheral</p></td>
</tr>
<tr class="odd">
<td align="left"><p>WRITE_ONCE_READ_MULTIPLE_DEVICE (4)</p></td>
<td align="left"><p>Worm</p></td>
<td align="left"><p>GenWorm</p></td>
<td align="left"><p>WormPeripheral</p></td>
</tr>
<tr class="even">
<td align="left"><p>READ_ONLY_DIRECT_ACCESS_DEVICE (5)</p></td>
<td align="left"><p>CdRom</p></td>
<td align="left"><p>GenCdRom</p></td>
<td align="left"><p>CdRomPeripheral</p></td>
</tr>
<tr class="odd">
<td align="left"><p>SCANNER_DEVICE (6)</p></td>
<td align="left"><p>Scanner</p></td>
<td align="left"><p>GenScanner</p></td>
<td align="left"><p>ScannerPeripheral</p></td>
</tr>
<tr class="even">
<td align="left"><p>OPTICAL_DEVICE (7)</p></td>
<td align="left"><p>Optical</p></td>
<td align="left"><p>GenOptical</p></td>
<td align="left"><p>OpticalDiskPeripheral</p></td>
</tr>
<tr class="odd">
<td align="left"><p>MEDIUM_CHANGER (8)</p></td>
<td align="left"><p>Changer</p></td>
<td align="left"><p>GenChanger</p></td>
<td align="left"><p>MediumChangerPeripheral</p></td>
</tr>
<tr class="even">
<td align="left"><p>COMMUNICATION_DEVICE (9)</p></td>
<td align="left"><p>Net</p></td>
<td align="left"><p>GenNet</p></td>
<td align="left"><p>CommunicationsPeripheral</p></td>
</tr>
<tr class="odd">
<td align="left"><p>10</p></td>
<td align="left"><p>Other</p></td>
<td align="left"><p>GenOther</p></td>
<td align="left"><p>OtherPeripheral</p></td>
</tr>
</tbody>
</table>

 

For IDE changer devices, the generic type name is **GenChanger** instead of **ScsiChanger** and for communication devices the generic type name is **GenNet** instead of **ScsiNet**. The SCSI Port driver returns no generic name at all for sequential access and "processor" devices, whereas the IDE bus driver returns **GenSequential** and **GenProcessor**. Also, the IDE bus driver returns only ten generic types, whereas the SCSI Port driver currently returns eighteen. In other respects, the generic names returned by the IDE bus driver are the same as those returned by the SCSI Port driver.

The compatible ID for an IDE tape drive is as follows:

GenSequential

In the special case of an LS-120 device, the IDE bus driver returns the following compatible ID:

GenSFloppy

The following shows the kind of identifiers that can be generated for an IDE hard disk drive:

IDE\\DiskMaxtor\_91000D8\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_SASX1B18

IDE\\Maxtor\_91000D8\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_SASX1B18

IDE\\DiskMaxtor\_91000D8\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Maxtor\_91000D8\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_SASX1B18

GenDisk

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Identifiers%20for%20IDE%20Devices%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




