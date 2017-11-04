---
title: OID_CO_TAPI_CM_CAPS
author: windows-driver-content
description: This topic describes the OID_CO_TAPI_CM_CAPS object identifier (OID).
ms.assetid: c0e44c1b-89d1-4c50-a1fc-8322bb1d00c2
keywords:
- OID_CO_TAPI_CM_CAPS
ms.author: windowsdriverdev
ms.date: 11/03/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WWAN_DEVICE_CAPS_EX%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")