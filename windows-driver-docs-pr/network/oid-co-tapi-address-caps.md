---
title: OID_CO_TAPI_ADDRESS_CAPS
description: This topic describes the OID_CO_TAPI_ADDRESS_CAPS object identifier (OID).
ms.assetid: c0e44c1b-89d1-4c50-a1fc-8322bb1d00c2
keywords:
- OID_CO_TAPI_ADDRESS_CAPS
ms.date: 11/03/2017
ms.localizationpriority: medium
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

