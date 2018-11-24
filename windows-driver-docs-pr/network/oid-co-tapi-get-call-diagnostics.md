---
title: OID_CO_TAPI_GET_CALL_DIAGNOSTICS
description: This topic describes the OID_CO_TAPI_GET_CALL_DIAGNOSTICS object identifier (OID).
ms.assetid: 5b0b1a96-9d66-4ee3-9b9a-3341ca3a4b5c
keywords:
- OID_CO_TAPI_GET_CALL_DIAGNOSTICS
ms.date: 11/03/2017
ms.localizationpriority: medium
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

