---
title: OID_CO_TAPI_TRANSLATE_TAPI_SAP
description: This topic describes the OID_CO_TAPI_TRANSLATE_TAPI_SAP object identifier (OID).
ms.assetid: 701a1d02-8528-4b61-adbb-97c817194ac7
keywords:
- OID_CO_TAPI_TRANSLATE_TAPI_SAP
ms.date: 11/03/2017
ms.localizationpriority: medium
---

# OID_CO_TAPI_TRANSLATE_TAPI_SAP

The OID_CO_TAPI_TRANSLATE_TAPI_SAP OID requests a call manager or integrated MCM driver to prepare one or more SAPs from TAPI call parameters. The client that queries this OID uses an NDIS SAP returned by the call manager or MCM driver as an input (formatted as a [CO_SAP](https://msdn.microsoft.com/library/windows/hardware/ff545392) structure) to [NdisClRegisterSap](https://msdn.microsoft.com/library/windows/hardware/ff561648), which the client calls to register a SAP on which to receive incoming calls.

This request uses a CO_TAPI_TRANSLATE_SAP structure, which is defined as follows:

```c++
typedef struct _CO_TAPI_TRANSLATE_SAP {
    IN  ULONG               ulLineID;
    IN  ULONG               ulAddressID;
    IN  ULONG               ulMediaModes;
    IN  ULONG               Reserved;
    OUT ULONG               NumberOfSaps;
    OUT NDIS_VAR_DATA_DESC  NdisSapParams[1];
} CO_AF_TAPI_SAP, *PCO_AF_TAPI_SAP;
```

The members of this structure contain the following information:

**ulLineID**  
Specifies a zero-based line identifier.

**ulAddressID**  
Specifies a zero-based address identifier on the line specified by **ulLineID**.

**ulMediaModes**  
Specifies the media mode of the information stream of calls that the client is interested in, as one or more of the following LINEMEDIAMODE_constants: 

- **LINEMEDIAMODE_UNKNOWN**  
A media stream exists but its mode is currently unknown and may become known later. This corresponds to a call with an unclassified media type. In typical analog telephony environments, the media mode of an incoming call may be unknown until after the call has been answered and the media stream has been filtered to make a determination. 

    If the **LINEMEDIAMODE_UNKNOWN** flag is set, other media flags can also be set. This signifies that the media is unknown but that it is likely to be one of the other indicated media modes.

- **LINEMEDIAMODE_INTERACTIVEVOICE**  
The presence of voice energy on the call, and the call is treated as an interactive call with humans on both ends.

- **LINEMEDIAMODE_AUTOMATEDVOICE**  
The presence of voice energy on the call, and the voice is locally handled by an automated application.

- **LINEMEDIAMODE_DATAMODEM**  
A data modem session on the call.

- **LINEMEDIAMODE_G3FAX**  
A group 3 fax is being sent or received over the call.

- **LINEMEDIAMODE_G4FAX**  
A group 4 fax is being sent or received over the call.

- **LINEMEDIAMODE_TDD**  
A TDD (telecommunication device for the deaf) session on the call.

- **LINEMEDIAMODE_DIGITALDATA**  
Digital data is being sent or received over the call.

- **LINEMEDIAMODE_TELETEX**  
A teletex session on the call. (Teletex is one of the telematic services.)

- **LINEMEDIAMODE_VIDEOTEX**  
A videotex session on the call. (Videotex is one the telematic services.)

- **LINEMEDIAMODE_TELEX**  
A telex session on the call. (Telex is one of the telematic services.)

- **LINEMEDIAMODE_MIXED**  
A mixed session on the call. (Mixed is one of the ISDN telematic services.)

- **LINEMEDIAMODE_ADSI**  
An ADSI (Analog Display Service Interfaces) session on the call.

- **LINEMEDIAMODE_VOICEVIEW**  
The media mode of the call is VoiceView.

**Reserved**  
This is reserved. The client must set this field to 0.

**NumberOfSaps**  
Specifies the number of [NDIS_VAR_DATA_DESC](https://msdn.microsoft.com/library/windows/hardware/ff559020) structures contained in the buffer at **NdisSapParams**.

**NdisSapParams**  
Specifies a variable-length array that contains one or more NDIS_VAR_DATA_DESC structures. Each NDIS_VAR_DATA_DESC structure contains an offset to, as well as the length of, a [CO_SAP](https://msdn.microsoft.com/library/windows/hardware/ff545392) structure. Each CO_SAP structure specifies a service access point (SAP) on which a connection-oriented client can receive incoming calls.

## Requirements

| | |
| --- | --- |
| Version | Windows Vista and later |
| Header | Ntddndis.h (include Ndis.h) |

