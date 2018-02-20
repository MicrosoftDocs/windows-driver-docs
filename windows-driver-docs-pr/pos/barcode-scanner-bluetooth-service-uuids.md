---
title: Barcode scanner Bluetooth service UUIDs
description: This topic describes UUIDs for use with the Bluetooth Service Discovery Protocol (SDP) for barcode scanners.
ms.assetid: '354654EC-95C8-4BE9-83D3-0926A1E71221'
ms.author: windowsdriverdev
ms.date: 02/14/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Barcode scanner Bluetooth service UUIDs

This topic describes UUIDs for use with the Bluetooth Service Discovery Protocol (SDP) for barcode scanners.

## Bluetooth barcode scanner UUIDs

The following UUIDs are used to identify services provided by Bluetooth barcode scanners during discovery.

### SSI service UUID

The following UUID identifies the SSI service for a Bluetooth barcode scanner. Devices that expose this UUID during Bluetooth discovery will be recognized as barcode scanners that the in-box driver supports.

``` syntax
DEFINE_GUID(BarcodeScannerSimpleSerialInterfaceServiceClass_UUID, 
0xA1220169, 0xE854, 0x473E, 0x9C, 0xB5, 0x87, 0x3A, 0xCB, 0xDF, 0x1F, 0x13)
```

### Reserved for future use

The following UUID is not supported in Windows 10, version 1703, but is reserved for future use with ISCP.

``` syntax
DEFINE_GUID(BarcodeScannerIntermecScannerCommunicationProtocolServiceClass_UUID, 
0xccb06baf, 0xdca9, 0x483f, 0x84, 0xd9, 0x36, 0x23, 0x24, 0xce, 0xd, 0x97)
```

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bpos\pos%5D:%20Barcode%20scanner%20Bluetooth%20service%20UUIDs%20%20RELEASE:%20%282/14/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




