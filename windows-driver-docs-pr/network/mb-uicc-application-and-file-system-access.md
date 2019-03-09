---
title: MB UICC application and file system access
description: MB UICC application and file system access
ms.assetid: 9A9BFCCE-2481-412F-AEBB-9919F6916224
keywords:
- MB UICC application and file system access, Mobile Broadband UICC application and file system access
ms.date: 03/07/2019
ms.localizationpriority: medium
---

# MB UICC application and file system access

## Overview

This topic specifies an extension to the Mobile Broadband Interface Model (MBIM) interface to permit accessing UICC smart card application and file systems. This extension to MBIM exposes logical access to the UICC's [ETSI TS 102 221 technical specification](https://go.microsoft.com/fwlink/p/?linkid=864594)-compliant applications and filesystems, and is supported in Windows 10, version 1903 and later.

## Detailed design - UICC access and security

The UICC provides a file system and supports a set of applications that can run concurrently. These include the USIM for UMTS, CSIM for CDMA, and ISIM for IMS. The SIM is a legacy portion of the UICC that can be modeled as one of these applications (for GSM).

The following diagram from section 8.1 of the [ETSI TS 102 221 technical specification](https://go.microsoft.com/fwlink/p/?linkid=864594) shows an example card application structure.

![An example UICC application structure](images/mb-uicc-application-structure.png "An example UICC application structure.")

The UICC file system can be regarded as a forest of directory trees. The legacy SIM tree is rooted at a Master File (MF) and contains up to two levels of subdirectories (Dedicated Files, or DFs) containing Elemental Files (EFs) that hold various types of information. The SIM defines DFs under the MF, one of which - DFTelecom - contains information common to multiple access types such as the common phone book. Additional applications are effectively implemented as separate trees, each rooted in its own Application Directory File (ADF). Each ADF is identified by an application identifier that can be up to 128 bits long. A file under the card root (EFDir under the MF in the diagram) contains the application names and corresponding identifiers. Within a tree (the MF or an ADF), DFs and EFs might be identified by a path of file IDs, where a file ID is a 16-bit integer.

## Benefits for MBIM functions

With this extension, Windows provides the following benefits for MBIM functions:

- A new set of application and file system CIDs that are part of the same low-level UICC access service previously available with [low-level UICC access](mb-low-level-uicc-access.md), but with no dependencies on existing APDU-based access CIDs.
    - The new set of application and file system CIDs do not rely on any of the existing low-level UICC access CIDs such as MBIM_CID_MS_UICC_ATR or MBIM_CID_UICC_OPEN_CHANNEL. The two sets of CIDs are considered as two different communication channels between the ME and UICC, and can work in parallel.
- The ability to get a list of all applications on the UICC.
    - Each application is associated with a full application ID, application name, and PIN info.
    - MBIM functions can get the currently selected application.
- GET STATUS on a file.
    - The file is specified with an application ID and a file path relative to the application ID.
    - If no application ID is specified, file paths that begin with *3F00* are assumed to be legacy pseudo applications under the root master file, and file paths that begin with *7FFF* are assumed to be the currently selected application.
    - Key properties include the file type (EF/DF/ADF), file structure (transparent, cyclic, linear, and BER-TLV), accessibility, and PIN info.
- READ or WRITE to a file.
    - The file is specified with an application ID and a file path relative to the application ID.
    - If no application ID is specified, file paths that begin with *3F00* are assumed to be legacy pseudo applications under the root master file, and file paths that begin with *7FFF* are assumed to be the currently selected application.
    - All valid UICC file structures (transparent, cyclic, linear, and BER-TLV) are supported.
- Extending PIN operations to a per-application basis. Additional PIN types beyond PIN1 are supported.
- Implementing the retrieval of GID1 and PNN through new APIs.
- HLK tests for testing the generic UICC APIs and GID1/PNN support.

## MBIM service and CID values

| Service name | UUID | UUID value |
| --- | --- | --- |
| Microsoft Low-Level UICC Access | UUID_MS_UICC_LOW_LEVEL | C2F6588E-F037-4BC9-8665-F4D44BD09367 |
| Microsoft Basic IP Connectivity Extensions | UUID_BASIC_CONNECT_EXTENSIONS | 3D01DCC5-FEF5-4D05-9D3A-BEF7058E9AAF |

The following table specifies the UUID and command code for each CID, as well as whether the CID supports Set, Query, or Event (notification) requests. See each CID’s individual section within this topic for more info about its parameters, data structures, and notifications. 

| CID | UUID | Command code | Set | Query | Notify |
| --- | --- | --- | --- | --- | --- |
| MBIM_CID_MS_UICC_APP_LIST | UUID_MS_UICC_LOW_LEVEL | 7 | N | Y | N |
| MBIM_CID_MS_UICC_FILE_STATUS | UUID_MS_UICC_LOW_LEVEL | 8 | N | Y | N |
| MBIM_CID_MS_UICC_ACCESS_BINARY | UUID_MS_UICC_LOW_LEVEL | 9 | Y | Y | N |
| MBIM_CID_MS_UICC_ACCESS_RECORD | UUID_MS_UICC_LOW_LEVEL | 10 | Y | Y | N |
| MBIM_CID_MS_PIN_EX | UUID_BASIC_CONNECT_EXTENSIONS | 15 | Y | Y | N |

## MBIM_CID_MS_UICC_APP_LIST

This CID retrieves a list of applications in a UICC and information about them. When the UICC in the modem is fully initialized and ready to register with the mobile operator, a UICC application must be selected for registration and a query with this CID should return the selected application in the **ActiveAppIndex** field in the MBIM_UICC_APP_LIST structure used in response.

### Parameters

|  | Set | Query | Notification |
| --- | --- | --- | --- |
| Command | Not applicable | Empty | Not applicable |
| Response | Not applicable | MBIM_UICC_APP_LIST | Not applicable |

### Query

The InformationBuffer of MBIM_COMMAND_MSG is empty.

### Set

Not applicable.

### Response

The InformationBuffer in MBIM_COMMAND_DONE contains the following MBIM_UICC_APP_LIST structure.

#### MBIM_UICC_APP_LIST (version 1)

| Offset | Size | Field | Type | Description |
| --- | --- | --- | --- | --- |
| 0 | 4 | Version | UINT32 | The version number of the structure that follows. This field must be set to **1** for version 1 of this structure. |
| 4 | 4 | AppCount | UINT32 | The number of UICC application **MBIM_UICC_APP_INFO** structures being returned in this response. |
| 8 | 4 | ActiveAppIndex | UINT32(0..NumApp - 1) | The index of the application selected by the modem for registration with the mobile network. This field must be between **0** and the **AppCount - 1**. It indexes to the array of applications returned by this response. If no application is selected for registration, this field contains **0xFFFFFFFF**. |
| 12 | 4 | AppListOffset | OFFSET | The offset, in bytes, calculated from the beginning of this structure to the buffer containing the app list. |
| 16 | 4 | AppListSize | SIZE(0..AppCount * 312) | The size of the app list data, in bytes. |
| 20 | AppListSize | DataBuffer | DATABUFFER | An array of **AppCount** * **MBIM_UICC_APP_INFO** structures. |

#### MBIM_UICC_APP_INFO

| Offset | Size | Field | Type | Description |
| --- | --- | --- | --- | --- |
| 0 | 4 | AppType | MBIM_UICC_APP_TYPE | The type of the UICC application. |
| 4 | 4 | AppIdSize | SIZE(0..16) | The size of the application ID, in bytes, as defined in section 8.3 of the [ETSI TS 102 221 technical specification](https://go.microsoft.com/fwlink/p/?linkid=864594). This field is set to zero for the **MBIMUiccAppTypeMf**, **MBIMUiccAppTypeMfSIM**, or **MBIMUiccAppTypeMfRUIM** app types. |
| 8 | 16 | AppId | Byte array | The application ID. Only the first **AppIdSize** bytes are meaningful. If the application ID is longer than **MBIM_MAXLENGTH_APPID** bytes, then AppIdSize specifies the actual length but only the first **MBIM_MAXLENGTH_APPID** bytes are in this field. This field is valid only when **AppType** is not **MBIMUiccAppTypeMf**, **MBIMUiccAppTypeMfSIM**, or **MBIMUiccAppTypeMfRUIM**. |
| 24 | 4 | AppNameLength | SIZE(0..256) | The length, in characters, of the application name. |
| 28 | 256 | AppName | ASCII character array | A UTF-8 string specifying the name of the application. The length of this field is specified by **AppNameLength**. If the length is greater than or equal to **MBIM_MAXLENGTH_APPNAME** bytes, this field contains the first **MBIM_MAXLENGTH_APPNAME - 1** bytes of the name. The string is always null-terminated. |
| 284 | 4 | NumPins | SIZE(0..8) | The number of application PIN references. In other words, the numbef of elements of **PinRef** that are valid. Applications on a virtual R-UIM have no PIN references. |
| 288 | 8 | PinRef | Byte array | A byte array specifying the application PIN references for this application (keys for PIN1 and possibly UPIN), as defined in section 9.4.2 of the [ETSI TS 102 221 technical specification](https://go.microsoft.com/fwlink/p/?linkid=864594). In the case of a single-verification card, or an MBB driver and/or modem that does not support different application keys for different applications, this field must be **0x01**. |

#### MBIM_UICC_APP_TYPE

| Type | Value | Description |
| --- | --- | --- |
| MBIMUiccAppTypeUnknown | 0 | Unknown type. |
| MBIMUiccAppTypeMf | 1 | Legacy SIM directories rooted at the MF. |
| MBIMUiccAppTypeMfSIM | 2 | Legacy SIM directories rooted at the DF_GSM. |
| MBIMUiccAppTypeMfRUIM | 3 | Legacy SIM directories rooted at the DF_CDMA. |
| MBIMUiccAppTypeUSIM | 4 | USIM application. |
| MBIMUiccAppTypeCSIM | 5 | CSIM applicaton. |
| MBIMUiccAppTypeISIM | 6 | ISIM application. |

#### Constants

The following constants are defined for MBIM_CID_MS_UICC_APP_LIST.

`const int MBIM_MAXLENGTH_APPID = 16`  
`const int MBIM_MAXLENGTH_APPNAME = 256`  
`const int MBIM_MAXNUM_PINREF = 8`  

### Unsolicited Events

Not applicable.

### Status Codes

The following status codes are applicable:

| Status code | Description |
| --- | --- |
| MBIM_STATUS_SUCCESS | Basic MBIM status as defined for all commands. |
| MBIM_STATUS_BUSY | Basic MBIM status as defined for all commands. |
| MBIM_STATUS_FAILURE | Basic MBIM status as defined for all commands. |
| MBIM_STATUS_NO_DEVICE_SUPPORT | Basic MBIM status as defined for all commands. |
| MBIM_STATUS_SIM_NOT_INSERTED | Unable to perform the UICC operation because the UICC is missing. |
| MBIM_STATUS_BAD_SIM | Unable to perform the UICC operation because the UICC is in an error state. |
| MBIM_STATUS_NOT_INITIALIZED | Unable to perform the UICC operation because the UICC is not yet fully initialized. |

## 

### Parameters

|  | Set | Query | Notification |
| --- | --- | --- | --- |
| Command | Not applicable | Not applicable | Not applicable |
| Response | Not applicable | Not applicable | Not applicable |

### Query

### Set

### Response

### Unsolicited Events

### Status Codes

## 

### Parameters

|  | Set | Query | Notification |
| --- | --- | --- | --- |
| Command | Not applicable | Not applicable | Not applicable |
| Response | Not applicable | Not applicable | Not applicable |

### Query

### Set

### Response

### Unsolicited Events

### Status Codes

## 

### Parameters

|  | Set | Query | Notification |
| --- | --- | --- | --- |
| Command | Not applicable | Not applicable | Not applicable |
| Response | Not applicable | Not applicable | Not applicable |

### Query

### Set

### Response

### Unsolicited Events

### Status Codes

## 

### Parameters

|  | Set | Query | Notification |
| --- | --- | --- | --- |
| Command | Not applicable | Not applicable | Not applicable |
| Response | Not applicable | Not applicable | Not applicable |

### Query

### Set

### Response

### Unsolicited Events

### Status Codes