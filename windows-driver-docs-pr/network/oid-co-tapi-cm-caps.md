---
title: OID_CO_TAPI_CM_CAPS
description: This topic describes the OID_CO_TAPI_CM_CAPS object identifier (OID).
ms.assetid: c0e44c1b-89d1-4c50-a1fc-8322bb1d00c2
keywords:
- OID_CO_TAPI_CM_CAPS
ms.date: 11/03/2017
ms.localizationpriority: medium
---

# OID_CO_TAPI_CM_CAPS

The OID_CO_TAPI_CM_CAPS OID requests a call manager or an integrated miniport call manager (MCM) driver to return the number of lines supported by its device (the device for which it provides call management services). This OID also requests the call manager or MCM driver to indicate whether these lines have dissimilar line capabilities.

This request uses a CO_TAPI_CM_CAPS structure, which is defined as follows:

```c++
typedef struct _CO_TAPI_CM_CAPS {
    OUT ULONG   ulCoTapiVersion;
    OUT ULONG   ulNumLines;
    OUT ULONG   ulFlags;
} CO_TAPI_CM_CAPS, *PCO_TAPI_CM_CAPS;
``` 

The members of this structure contain the following information:

**ulCoTapiVersion**  
Specifies the TAPI version supported by the call manager or MCM driver. The call manager or MCM driver should set this to CO_TAPI_VERSION.

**ulNumLines**  
Specifies the number of lines supported by the device.

**ulFlags**  
If the device supports multiple lines that have dissimilar line capabilities or if the addresses on any of these lines have dissimilar address capabilities, the call manager or MCM driver sets the CO_TAPI_FLAG_PER_LINE_CAPS bit in **ulFlags**; otherwise, the call manager or MCM driver clears this bit. All undefined bits are reserved for future use and must be set to 0.

## Remarks

A connection-oriented client uses the information returned from this OID to determine how it will query the line capabilities of the call manager's or MCM driver's device with [OID_CO_TAPI_LINE_CAPS](oid-co-tapi-line-caps.md).

## Requirements

| | |
| --- | --- |
| Version | Windows Vista and later |
| Header | Ntddndis.h (include Ndis.h) |

