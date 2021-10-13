---
title: Barcode scanner Bluetooth service UUIDs
description: This topic describes UUIDs for use with the Bluetooth Service Discovery Protocol (SDP) for barcode scanners.
ms.date: 02/14/2018
ms.localizationpriority: medium
---

# Barcode scanner Bluetooth service UUIDs

This topic describes UUIDs for use with the Bluetooth Service Discovery Protocol (SDP) for barcode scanners.

## Bluetooth barcode scanner UUIDs

The following UUIDs are used to identify services provided by Bluetooth barcode scanners during discovery.

### SSI service UUID

The following UUID identifies the SSI service for a Bluetooth barcode scanner. Devices that expose this UUID during Bluetooth discovery will be recognized as barcode scanners that the in-box driver supports.

```cpp
DEFINE_GUID(BarcodeScannerSimpleSerialInterfaceServiceClass_UUID, 
0xA1220169, 0xE854, 0x473E, 0x9C, 0xB5, 0x87, 0x3A, 0xCB, 0xDF, 0x1F, 0x13)
```

### Reserved for future use

The following UUID is not supported in Windows 10, version 1703, but is reserved for future use with ISCP.

```cpp
DEFINE_GUID(BarcodeScannerIntermecScannerCommunicationProtocolServiceClass_UUID, 
0xccb06baf, 0xdca9, 0x483f, 0x84, 0xd9, 0x36, 0x23, 0x24, 0xce, 0xd, 0x97)
```





