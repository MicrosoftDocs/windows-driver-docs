---
title: OID_CO_TAPI_ADDRESS_CAPS
author: windows-driver-content
description: This topic describes the OID_CO_TAPI_ADDRESS_CAPS object identifier (OID).
ms.assetid: c0e44c1b-89d1-4c50-a1fc-8322bb1d00c2
keywords:
- OID_CO_TAPI_ADDRESS_CAPS
ms.author: windowsdriverdev
ms.date: 11/03/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# OID_CO_TAPI_ADDRESS_CAPS

The OID_CO_TAPI_ADDRESS_CAPS OID requests a call manager or an integrated miniport call manager (MCM) driver to return the telephony capabilities for a specified address on a specified line.

This request uses a CO_TAPI_ADDRESS_CAPS structure, which is defined as follows:

```c++
typedef struct _CO_TAPI_ADDRESS_CAPS {
    IN  ULONG               ulLineID;
    IN  ULONG               ulAddressID;
    OUT ULONG               ulFlags;
    OUT LINE_ADDRESS_CAPS   LineAddressCaps;
} CO_TAPI_ADDRESS_CAPS, *PCO_TAPI_ADDRESS_CAPS;
``` 

The members of this structure contain the following information:

**ulLineID**  
Specifies the zero-based line identifier of the line on which the given address is located.

**ulAddressID**  
Specifies the zero-based address identifier on the line for which capabilities should be returned.

**ulFlags**  
These flags are reserved.

**LineAddressCaps**  
Specifies the telephony capabilities of an address, formatted as a LINE_ADDRESS_CAPS structure. For more information about this structure, see the Microsoft Windows SDK and the ndistapi.h header file.

## Remarks

After querying the line capabilities of a call manager's or MCM driver's device with [OID_CO_TAPI_LINE_CAPS](oid-co-tapi-line-caps.md), a connection-oriented client queries the capabilities of the address(es) for each line as follows:

- If the previous query of OID_CO_TAPI_LINE_CAPS indicated that the line supports only one address or that all addresses on the line have the same address capabilities, the client queries OID_CO_TAPI_ADDRESS_CAPS once to determine the capabilities of all the addresses on the line. In this case, the address capabilities returned by the call manager or MCM driver apply to all addresses on the line.

- If a line supports multiple addresses that have dissimilar capabilities, the client queries OID_CO_TAPI_ADDRESS_CAPS once for each address on the line. In this case, the address capabilities returned by the call manager or MCM driver apply to a specified address on a specified line.

The call manager or MCM driver returns the address capabilities for a specified address in **LineAddressCaps**.

## Requirements

| | |
| --- | --- |
| Version | Windows Vista and later |
| Header | Ntddndis.h (include Ndis.h) |

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WWAN_DEVICE_CAPS_EX%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")