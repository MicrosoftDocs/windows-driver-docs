---
title: OID_CO_TAPI_GET_CALL_DIAGNOSTICS
author: windows-driver-content
description: This topic describes the OID_CO_TAPI_GET_CALL_DIAGNOSTICS object identifier (OID).
ms.assetid: 5b0b1a96-9d66-4ee3-9b9a-3341ca3a4b5c
keywords:
- OID_CO_TAPI_GET_CALL_DIAGNOSTICS
ms.author: windowsdriverdev
ms.date: 11/03/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# OID_CO_TAPI_GET_CALL_DIAGNOSTICS

The OID_CO_TAPI_GET_CALL_DIAGNOSTICS OID requests a call manager or MCM driver to return diagnostic information about a failed call or a call torn down by the remote TAPI party.

This request uses a CO_TAPI_CALL_DIAGNOSTICS structure, which is defined as follows:

```c++
typedef struct _CO_TAPI_CALL_DIAGNOSTICS {
    OUT ULONG               ulOrigin;
    OUT ULONG               ulReason;
    OUT NDIS_VAR_DATA_DESC  DiagInfo;
} CO_TAPI_CALL_DIAGNOSTICS, *PCO_TAPI_CALL_DIAGNOSTICS;
```

**ulOrigin**  
Specifies the origination of the call as one of the following LINECALLORIGIN_ constants: 

- **LINECALLORIGIN_OUTBOUND**  
The call is an outgoing call.

- **LINECALLORIGIN_INTERNAL**  
The call is incoming and originated internally (on the same PBX, for example).

- **LINECALLORIGIN_EXTERNAL** 
The call is incoming and originated externally.

- **LINECALLORIGIN_UNKNOWN**  
The call is incoming. Its origin is currently unknown but may become known later.

- **LINECALLORIGIN_UNAVAIL**  
The call is incoming. Its origin is not available and will never be known.

- **LINECALLORIGIN_CONFERENCE**  
The call handle is for a conference call--that is, for the application's connection to the conference bridge in the switch.

**ulReason**  
Specifies the reason for the call as one of the following LINECALLREASON_ constants: 

- **LINECALLREASON_DIRECT**  
The call is direct.

- **LINECALLREASON_FWDBUSY**  
The call was forwarded from a busy extension.

- **LINECALLREASON_FWDNOANSWER**  
The call was forwarded after some number of rings from an unanswered extension.

- **LINECALLREASON_FWDUNCOND**  
The call was forwarded unconditionally from another number.

- **LINECALLREASON_PICKUP**  
The call was picked up from another extension.

- **LINECALLREASON_UNPARK**  
The call was retrieved as a parked call.

- **LINECALLREASON_REDIRECT**  
The call was redirected to this station.

- **LINECALLREASON_CALLCOMPLETION**  
The call was the result of a call completion request.

- **LINECALLREASON_TRANSFER**  
The call was transferred from another number. Party identifier information may indicate who the caller is and from where the call was transferred.

- **LINECALLREASON_REMINDER**  
The call is a reminder (or "recall") that the user has a call parked or on hold for a potentially long time.

- **LINECALLREASON_UNKNOWN**  
The reason for the call is currently unknown but may become known later.

- **LINECALLREASON_UNAVAIL**  
The reason for the call is unavailable and cannot become known later.

**DiagInfo**  
Specifies an [NDIS_VAR_DATA_DESC](https://msdn.microsoft.com/library/windows/hardware/ff559020) structure that contains an offset to, as well as the length of, optional diagnostic information supplied by the call manager or MCM driver. The content and format of the diagnostic information is driver-determined.

## Requirements

| | |
| --- | --- |
| Version | Windows Vista and later |
| Header | Ntddndis.h (include Ndis.h) |

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WWAN_DEVICE_CAPS_EX%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")