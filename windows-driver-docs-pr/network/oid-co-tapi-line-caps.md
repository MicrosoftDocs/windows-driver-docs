---
title: OID_CO_TAPI_LINE_CAPS
author: windows-driver-content
description: This topic describes the OID_CO_TAPI_LINE_CAPS object identifier (OID).
ms.assetid: 82c2bcb4-fb58-4e14-b1d4-2bcc0c4fcd1d
keywords:
- OID_CO_TAPI_LINE_CAPS
ms.author: windowsdriverdev
ms.date: 11/03/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# OID_CO_TAPI_LINE_CAPS

The OID_CO_TAPI_LINE_CAPS OID requests a call manager or an integrated miniport call manager (MCM) driver to return the telephony capabilities for a specified line. This OID also requests the call manager or MCM driver to indicate whether addresses on this line have dissimilar telephony capabilities.

This request uses a CO_TAPI_LINE_CAPS structure, defined as follows, to query the telephony capabilities of a specified line:

```c++
typedef struct _CO_TAPI_LINE_CAPS {
    IN  ULONG           ulLineID;
    OUT ULONG           ulFlags;
    OUT LINE_DEV_CAPS   LineDevCaps;
} CO_TAPI_LINE_CAPS, *PCO_TAPI_LINE_CAPS;
``` 

The members of this structure contain the following information:

**ulLineID**  
Specifies the line for which telephony capabilities should be returned. **ulLineID** is a zero-based identifier.

**ulFlags**  
If the line supports multiple addresses that have dissimilar telephony capabilities, the call manager or MCM driver sets the CO_TAPI_FLAG_PER_ADDRESS_CAPS bit in ulFlags; otherwise, the call manager or MCM driver clears this bit. All undefined bits are reserved and must be set to 0.

**LineDevCaps**  
Specifies the telephony capabilities of a line, formatted as a LINE_DEV_CAPS structure. For more information about this structure, see the Microsoft Windows SDK and the ndistapi.h header file.

## Remarks

After querying the telephony capabilities of a call manager's or MCM driver's device with [OID_CO_TAPI_CM_CAPS](oid-co-tapi-cm-caps.md), a connection-oriented client queries the telephony capabilities of the line(s) supported by the device.

- If all lines supported by the device have the same line capabilities and all the addresses on these lines have the same address capabilities, the client queries OID_CO_TAPI_LINE_CAPS once to obtain the line capabilities of the device. In this case, the line capabilities returned by the call manager or MCM driver apply to all the lines supported by the device.
- If the device supports multiple lines with dissimilar capabilities, however, and/or if addresses on these lines have dissimilar address capabilities, the client queries OID_CO_TAPI_LINE_CAPS once for each line supported by the device to obtain the capabilities of each line.

The **ulFlags** setting determines how many times the client subsequently queries the capabilities of the address(es) on the line:

- If the line supports only one address, or if the line supports multiple addresses that have the same address capabilities, the client queries OID_CO_TAPI_ADDRESS_CAPS once.
- If the line supports multiple addresses that have dissimilar capabilities, the client must query OID_CO_TAPI_ADDRESS_CAPS once for each address on the line.

## Requirements

| | |
| --- | --- |
| Version | Windows Vista and later |
| Header | Ntddndis.h (include Ndis.h) |

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WWAN_DEVICE_CAPS_EX%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")