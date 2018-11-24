---
title: OID_CO_TAPI_LINE_CAPS
description: This topic describes the OID_CO_TAPI_LINE_CAPS object identifier (OID).
ms.assetid: 82c2bcb4-fb58-4e14-b1d4-2bcc0c4fcd1d
keywords:
- OID_CO_TAPI_LINE_CAPS
ms.date: 11/03/2017
ms.localizationpriority: medium
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

