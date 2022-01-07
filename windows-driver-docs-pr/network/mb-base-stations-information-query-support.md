---
title: MB base stations information query support
description: MB base stations information query support
keywords:
- MB base stations information query, Mobile Broadband base stations information query
ms.date: 08/14/2017
---

# MB base stations information query support

## Overview

The base stations information query interface is used to provide location based services with cellular base station information, such as *Base Station ID*, *Time Advance*, and other parameters that can be used to compute the geographical position of the mobile subscriber. The information gathered pertains to the cellular base station currently serving the subscriber, as well as neighboring cellular base stations. 

This topic defines the base stations information query interface for Windows, as the MBIM 1.0 specification does not provide this information through any existing CIDs. This interface is available in Windows 10, version 1709 and later. 

Serving and neighbor cell parameters are retrieved via Query/Response operations. A notification is also defined in this topic to indicate that the location of the device within the cellular network has changed.

## <a name="mbim_cid_base_stations_info"></a>MBIM_CID_BASE_STATIONS_INFO

This command retrieves information about the serving and neighbor cells known to the modem.

Service: **MBB_UUID_BASIC_CONNECT_EXTENSIONS**

Service UUID: **3d01dcc5-fef5-4d05-0d3a-bef7058e9aaf**

| CID | Command code | Minimum OS version |
| --- | --- | --- |
| MBIM_CID_BASE_STATIONS_INFO | 11 | Windows 10, version 1709 |

### Parameters

| Type | Set | Query | Notification |
| --- | --- | --- | --- |
| Command | Not applicable | MBIM_BASE_STATIONS_INFO_REQ | Not applicable |
| Response | Not applicable | MBIM_BASE_STATIONS_INFO | Not applicable |

### Query

The InformationBuffer of MBIM_COMMAND_MSG contains an MBIM_BASE_STATIONS_INFO_REQ struture. The InformationBuffer of MBIM_COMMAND_DONE contains an MBIM_BASE_STATIONS_INFO structure.

#### <a name="mbim_base_stations_info_req"></a>MBIM_BASE_STATIONS_INFO_REQ

The MBIM_BASE_STATIONS_INFO_REQ structure shall be used in the InformationBuffer for queries. It is used to configure aspects of the cell information, such as the maximum number of neighbor cell measurements, to send in response. 

| Offset | Size | Field | Type | Description |
| --- | --- | --- | --- | --- |
| 0 | 4 | MaxGSMCount | SIZE | The maximum number of entries of GSM neighboring cells returned in the GSM network measurement reports of [MBIM_GSM_NMR](#mbim_gsm_nmr). Default capacity is 15. |
| 4 | 4 | MaxUMTSCount | SIZE | The maximum number of entries of UMTS neighboring cells returned in the UMTS measured results list in [MBIM_UMTS_MRL](#mbim_umts_mrl). Default capacity is 15. |
| 8 | 4 | MaxTDSCDMACount | SIZE | The maximum number of entries of TDSCDMA neighboring cells returned in the TDSCDMA measured results list in [MBIM_TDSCDMA_MRL](#mbim_tdscdma_mrl). Default capacity is 15. |
| 12 | 4 | MaxLTECount | SIZE | The maximum number of entries of LTE neighboring cells returned in the LTE measured results list of [MBIM_LTE_MRL](#mbim_lte_mrl). Default capacity is 15. |
| 16 | 4 | MaxCDMACount | SIZE | The maximum number of entries of CDMA cells returned in the CDMA measured results list in [MBIM_CDMA_MRL](#mbim_cdma_mrl). This list includes both serving and neighboring cells. Default capacity is 12. |

### Set

Not applicable.

### Response

The MBIM_BASE_STATIONS_INFO structure shall be used in the InformationBuffer of MBIM_COMMAND_DONE for responses.

#### <a name="mbim_base_stations_info"></a>MBIM_BASE_STATIONS_INFO

The MBIM_BASE_STATIONS_INFO structure contains information about both serving and neighboring base stations.

| Offset | Size | Field | Type | Description |
| --- | --- | --- | --- | --- |
| 0 | 4 | SystemType | MBIM_DATA_CLASS | Indicates the system type (or types) for which serving cell information is valid. This member is a bitmask of one or more system types as defined in the MBIM_DATA_CLASS. |
| 4 | 4 | GSMServingCellOffset | OFFSET | The offset in bytes, calculated from the beginning of this structure, to the buffer containing the GSM serving cell information. This member can be NULL when the technology of the serving cell is not GSM. |
| 8 | 4 | GSMServingCellSize | SIZE(0-44) | The size, in bytes, used for [MBIM_GSM_SERVING_CELL_INFO](#mbim_gsm_serving_cell_info). |
| 12 | 4 | UMTSServingCellOffset | OFFSET | The offset in bytes, calculated from the beginning of this structure, to the buffer containing the UMTS serving cell information. This member can be NULL when the technology of serving cell is not UMTS. |
| 16 | 4 | UMTSServingCellSize | SIZE(0-60) | The size, in bytes, used for [MBIM_UMTS_SERVING_CELL_INFO](#mbim_umts_serving_cell_info). |
| 20 | 4 | TDSCDMAServingCellOffset | OFFSET | The offset in bytes, calculated from the beginning of this structure, to the buffer containing the TDSCDMA serving cell information. This member can be NULL when the technology of serving cell is not TDSCDMA. |
| 24 | 4 | TDSCDMAServingCellSize | SIZE(0-48) | The size, in bytes, used for [MBIM_TDSCDMA_SERVING_CELL_INFO](#mbim_tdscdma_serving_cell_info). |
| 28 | 4 | LTEServingCellOffset | OFFSET | The offset in bytes, calculated from the beginning of this structure, to the buffer containing the LTE serving cell information. This member can be NULL when the technology of serving cell is not LTE. |
| 32 | 4 | LTEServingCellSize | SIZE(0-48) | The size, in bytes, used for [MBIM_LTE_SERVING_CELL_INFO](#mbim_lte_serving_cell_info). |
| 36 | 4 | GSMNmrOffset | OFFSET | The offset in bytes, calculated from the beginning of this structure, to the buffer containing the GSM Network Measurement report. This member can be NULL when no GSM neighboring network is returned in the measurement report. |
| 40 | 4 | GSMNmrSize | SIZE | The total size, in bytes, of the buffer containing the GSM Network Measurement report in the format of [MBIM_GSM_NMR](#mbim_gsm_nmr). |
| 44 | 4 | UMTSMrlOffset | OFFSET | The offset in bytes, calculated from the beginning of this structure, to the buffer containing UMTS measured results list. This member can be NULL when no UMTS neighboring network is returned in the measurement report. |
| 48 | 4 | UMTSMrlSize | SIZE | The total size, in bytes, of the buffer containing the UMTS measured results list in the format of [MBIM_UMTS_MRL](#mbim_umts_mrl). |
| 52 | 4 | TDSCDMAMrlOffset | OFFSET | The offset in bytes, calculated from the beginning of this structure, to the buffer containing TDSCDMA measured results list. This member can be NULL when no TDSCDMA neighboring network is returned in the measurement report. |
| 56 | 4 | TDSCDMAMrlSize | SIZE | The total size, in bytes, of the buffer containing the TDSCDMA measured results list in the format of [MBIM_TDSCDMA_MRL](#mbim_tdscdma_mrl). |
| 60 | 4 | LTEMrlOffset | OFFSET | The offset in bytes, calculated from the beginning of this structure, to the buffer containing the LTE measured results list. This member can be NULL when no LTE neighboring network is returned in the measurement report. |
| 64 | 4 | LTEMrlSize | SIZE | The total size, in bytes, of the buffer containing the LTE measured results list in the format of [MBIM_LTE_MRL](#mbim_lte_mrl). |
| 68 | 4 | CDMAMrlOffset | OFFSET | The offset in bytes, calculated from the beginning of this structure, to the buffer containing CDMA measured results list. This member can be NULL when no CDMA neighboring network is returned in the measurement report. |
| 72 | 4 | CDMAMrlSize | SIZE | The total size, in bytes, of the buffer containing the CDMA measured results list in the format of [MBIM_CDMA_MRL](#mbim_cdma_mrl). |
| 76 |   | DataBuffer | DATABUFFER | The data buffer containing *GSMServingCell*, *UMTSServingCell*, *TDSCDMAServingCell*, *LTEServingCell*, *GSMNmr*, *UMTSMrl*, *TDSCDMAMrl*, *LTEMrl*, and *CDMAMrl*. |

#### GSM cell data structures

##### <a name="mbim_gsm_serving_cell_info"></a>MBIM_GSM_SERVING_CELL_INFO

The MBIM_GSM_SERVING_CELL_INFO structure contains information about the GSM serving cell.

| Offset | Size | Field | Type | Description |
| --- | --- | --- | --- | --- |
| 0 | 4 | ProviderIdOffset | OFFSET | The offset in bytes, calculated from the beginning of this structure, to a numeric (0-9) string called *ProviderId* that represents the network provider identity. This string is a concatenation of a three-digit Mobile Country Code (MCC) and a two or three-digit Mobile Network Code (MNC). This member can be NULL when no *ProviderId* information is returned. |
| 4 | 4 | ProviderIdSize | SIZE(0-12) | The size used for *ProviderId*. |
| 8 | 4 | LocationAreaCode | UINT32 | The Location Area Code (0-65535). Use 0xFFFFFFFF when this information is not available. |
| 12 | 4 | CellID | UINT32 | The Cell ID (0-65535). Use 0xFFFFFFFF when this information is not available. |
| 16 | 4 | TimingAdvance | UINT32 | The Timing Advance (0-255) in bit periods, where a bit period is 48/13µs. Use 0xFFFFFFFF when this information is not available. |
| 20 | 4 | ARFCN | UINT32 | The Absolute Radio Frequency Channel Number of the serving cell (0-1023). Use 0xFFFFFFFF when this information is not available. |
| 24 | 4 | BaseStationId | UINT32 | The Base Station ID - the base station color code and the network identity code. Use 0xFFFFFFFF when this information is not available. |
| 28 | 4 | RxLevel | UINT32 | The received signal strength of the serving cell (0-63), where <p>`X = 0, if RSS < -110 dBm`</p><p>`X = 63, if RSS > -47 dBm`</p><p>`X = integer [RSS + 110], if -110 <= RSS <= -47`</p> Use 0xFFFFFFFF when this information is not available. |
| 32 |   | DataBuffer | DATABUFFER | The data buffer containing *ProviderId*. |

##### <a name="mbim_gsm_nmr"></a>MBIM_GSM_NMR

The MBIM_GSM_NMR structure contains the network measurement report (NMR) of neighboring GSM cells.

| Offset | Size | Field | Type | Description |
| --- | --- | --- | --- | --- |
| 0 | 4 | ElementCount (EC) | UINT32 | The count of NMR entries following this element. |
| 4 |   | DataBuffer | DATABUFFER | The array of NMR records, each specified as an [MBIM_GSM_NMR_INFO](#mbim_gsm_nmr_info) structure. |

##### <a name="mbim_gsm_nmr_info"></a>MBIM_GSM_NMR_INFO

The MBIM_GSM_NMR_INFO structure contains information about a neighboring GSM cell.

| Offset | Size | Field | Type | Description |
| --- | --- | --- | --- | --- |
| 0 | 4 | ProviderIdOffset | OFFSET | The offset in bytes, calculated from the beginning of this structure, to a numeric (0-9) string called *ProviderId* that represents the network provider identity. This string is a concatenation of a three-digit Mobile Country Code (MCC) and a two or three-digit Mobile Network Code (MNC). This member can be NULL when no *ProviderId* information is returned. |
| 4 | 4 | ProviderIdSize | SIZE(0-12) | The size used for *ProviderId*. |
| 8 | 4 | LocationAreaCode | UINT32 | The Location Area Code (0-65535). Use 0xFFFFFFFF when this information is not available. |
| 12 | 4 | CellID | UINT32 | The Cell ID (0-65535). Use 0xFFFFFFFF when this information is not available. |
| 16 | 4 | ARFCN | UINT32 | The Absolute Radio Frequency Channel Number of the serving cell (0-1023). Use 0xFFFFFFFF when this information is not available. |
| 20 | 4 | BaseStationId | UINT32 | The radio base station ID of the serving cell (0-63). Use 0xFFFFFFFF when this information is not available. |
| 24 | 4 | RxLevel | UINT32 | The received signal strength of the serving cell (0-63), where <p>`X = 0, if RSS < -110 dBm`</p><p>`X = 63, if RSS > -47 dBm`</p><p>`X = integer [RSS + 110], if -110 <= RSS <= -47`</p> Use 0xFFFFFFFF when this information is not available. |
| 28 |   | DataBuffer | DATABUFFER | The data buffer containing *ProviderId*. |

#### UMTS cell data structures

##### <a name="mbim_umts_serving_cell_info"></a>MBIM_UMTS_SERVING_CELL_INFO

The MBIM_UMTS_SERVING_CELL_INFO structure contains information about the UMTS serving cell.

| Offset | Size | Field | Type | Description |
| --- | --- | --- | --- | --- |
| 0 | 4 | ProviderIdOffset | OFFSET | The offset in bytes, calculated from the beginning of this structure, to a numeric (0-9) string called *ProviderId* that represents the network provider identity. This string is a concatenation of a three-digit Mobile Country Code (MCC) and a two or three-digit Mobile Network Code (MNC). This member can be NULL when no *ProviderId* information is returned. |
| 4 | 4 | ProviderIdSize | SIZE(0-12) | The size used for *ProviderId*. |
| 8 | 4 | LocationAreaCode | UINT32 | The Location Area Code (0-65535). Use 0xFFFFFFFF when this information is not available. |
| 12 | 4 | CellID | UINT32 | The Cell ID (0-268435455). Use 0xFFFFFFFF when this information is not available. |
| 16 | 4 | FrequencyInfoUL | UINT32 | The Frequency Info Uplink (0-16383). Use 0xFFFFFFFF when this information is not available. |
| 20 | 4 | FrequencyInfoDL | UINT32 | The Frequency Info Downlink (0-16383). Use 0xFFFFFFFF when this information is not available. |
| 24 | 4 | FrequencyInfoNT | UINT32 | The Frequency Info for TDD (0-16383). Use 0xFFFFFFFF when this information is not available. |
| 28 | 4 | UARFCN | UINT32 | The UTRA Absolute Radio Frequency Channel Number for the serving cell (0-16383). Use 0xFFFFFFFF when this information is not available. |
| 32 | 4 | PrimaryScramblingCode | UINT32 | The Primary Scrambling Code of the serving cell (0-511). Use 0xFFFFFFFF when this information is not available. |
| 36 | 4 | RSCP | INT32 | The Received Signal Code Power of  the serving cell. The range is -120 to -25, in units of 1dBm. Use 0 when this information is not available. |
| 40 | 4 | ECNO | INT32 | The signal to noise ratio of the serving cell; the ratio of the received energy per PN chip for the CPICH to the total received. The range is -50 to 0, in units of 1dBm. Use 1 when this information is not available. |
| 44 | 4 | PathLoss | UINT32 | The path loss of the serving cell (46-173). Use 0xFFFFFFFF when this information is not available. |
| 48 |   | DataBuffer | DATABUFFER | The data buffer containing *ProviderId*. |

##### <a name="mbim_umts_mrl"></a>MBIM_UMTS_MRL

The MBIM_UMTS_MRL structure contains the measured results list (MRL) of neighboring UMTS cells.

| Offset | Size | Field | Type | Description |
| --- | --- | --- | --- | --- |
| 0 | 4 | ElementCount (EC) | UINT32 | The count of MRL entries following this element. |
| 4 |   | DataBuffer | DATABUFFER | The array of MRL records, each specified as an [MBIM_UMTS_MRL_INFO](#mbim_gsm_nmr_info) structure. |

##### <a name="mbim_umts_mrl_info"></a>MBIM_UMTS_MRL_INFO

The MBIM_UMTS_MRL_INFO structure contains information about a neighboring UMTS cell.

| Offset | Size | Field | Type | Description |
| --- | --- | --- | --- | --- |
| 0 | 4 | ProviderIdOffset | OFFSET | The offset in bytes, calculated from the beginning of this structure, to a numeric (0-9) string called *ProviderId* that represents the network provider identity. This string is a concatenation of a three-digit Mobile Country Code (MCC) and a two or three-digit Mobile Network Code (MNC). This member can be NULL when no *ProviderId* information is returned. |
| 4 | 4 | ProviderIdSize | SIZE(0-12) | The size used for *ProviderId*. |
| 8 | 4 | LocationAreaCode | UINT32 | The Location Area Code (0-65535). Use 0xFFFFFFFF when this information is not available. |
| 12 | 4 | CellID | UINT32 | The Cell ID (0-268435455). Use 0xFFFFFFFF when this information is not available. |
| 16 | 4 | UARFCN | UINT32 | The UTRA Absolute Radio Frequency Channel Number for the serving cell (0-16383). Use 0xFFFFFFFF when this information is not available. |
| 20 | 4 | PrimaryScramblingCode | UINT32 | The Primary Scrambling Code of the serving cell (0-511). Use 0xFFFFFFFF when this information is not available. |
| 24 | 4 | RSCP | INT32 | The Received Signal Code Power of  the serving cell. The range is -120 to -25, in units of 1dBm. Use 0 when this information is not available. |
| 28 | 4 | ECNO | INT32 | The signal to noise ratio of the serving cell; the ratio of the received energy per PN chip for the CPICH to the total received. The range is -50 to 0, in units of 1dBm. Use 1 when this information is not available. |
| 32 | 4 | PathLoss | UINT32 | The path loss of the serving cell (46-173). Use 0xFFFFFFFF when this information is not available. |
| 36 |   | DataBuffer | DATABUFFER | The data buffer containing *ProviderId*. |

#### TDSCDMA cell data structures

##### <a name="mbim_tdscdma_serving_cell_info"></a>MBIM_TDSCDMA_SERVING_CELL_INFO

The MBIM_TDSCDMA_SERVING_CELL_INFO structure contains information about the TDSCDMA serving cell.

| Offset | Size | Field | Type | Description |
| --- | --- | --- | --- | --- |
| 0 | 4 | ProviderIdOffset | OFFSET | The offset in bytes, calculated from the beginning of this structure, to a numeric (0-9) string called *ProviderId* that represents the network provider identity. This string is a concatenation of a three-digit Mobile Country Code (MCC) and a two or three-digit Mobile Network Code (MNC). This member can be NULL when no *ProviderId* information is returned. |
| 4 | 4 | ProviderIdSize | SIZE(0-12) | The size used for *ProviderId*. |
| 8 | 4 | LocationAreaCode | UINT32 | The Location Area Code (0-65535). Use 0xFFFFFFFF when this information is not available. |
| 12 | 4 | CellID | UINT32 | The Cell ID (0-268435455). Use 0xFFFFFFFF when this information is not available. |
| 16 | 4 | UARFCN | UINT32 | The UTRA Absolute Radio Frequency Channel Number for the serving cell (0-16383). Use 0xFFFFFFFF when this information is not available. |
| 20 | 4 | CellParameterID | UINT32 | The Cell parameter ID (0-127). Use 0xFFFFFFFF when this information is not available. |
| 24 | 4 | TimingAdvance | UINT32 | The Timing Advance (0-1023). This member is the same value for all timeslots. Use 0xFFFFFFFF when this information is not available. |
| 28 | 4 | RSCP | INT32 | The Received Signal Code Power of  the serving cell. The range is -120 to -25, in units of 1dBm in Q8 L3 filtered. Use 0xFFFFFFFF when this information is not available. |
| 32 | 4 | PathLoss | UINT32 | The path loss of the serving cell (46-158). Use 0xFFFFFFFF when this information is not available. |
| 36 |   | DataBuffer | DATABUFFER | The data buffer containing *ProviderId*. |

##### <a name="mbim_tdscdma_mrl"></a>MBIM_TDSCDMA_MRL

The MBIM_TDSCDMA_MRL structure contains the measured results list (MRL) of neighboring TDSCDMA cells.

| Offset | Size | Field | Type | Description |
| --- | --- | --- | --- | --- |
| 0 | 4 | ElementCount (EC) | UINT32 | The count of MRL entries following this element. |
| 4 |   | DataBuffer | DATABUFFER | The array of MRL records, each specified as an [MBIM_TDSCDMA_MRL_INFO](#mbim_tdscdma_mrl_info) structure. |

##### <a name="mbim_tdscdma_mrl_info"></a>MBIM_TDSCDMA_MRL_INFO

The MBIM_TDSCDMA_MRL_INFO structure contains information about a neighboring TDSCDMA cell.

| Offset | Size | Field | Type | Description |
| --- | --- | --- | --- | --- |
| 0 | 4 | ProviderIdOffset | OFFSET | The offset in bytes, calculated from the beginning of this structure, to a numeric (0-9) string called *ProviderId* that represents the network provider identity. This string is a concatenation of a three-digit Mobile Country Code (MCC) and a two or three-digit Mobile Network Code (MNC). This member can be NULL when no *ProviderId* information is returned. |
| 4 | 4 | ProviderIdSize | SIZE(0-12) | The size used for *ProviderId*. |
| 8 | 4 | LocationAreaCode | UINT32 | The Location Area Code (0-65535). Use 0xFFFFFFFF when this information is not available. |
| 12 | 4 | CellID | UINT32 | The Cell ID (0-268435455). Use 0xFFFFFFFF when this information is not available. |
| 16 | 4 | UARFCN | UINT32 | The UTRA Absolute Radio Frequency Channel Number for the serving cell (0-16383). Use 0xFFFFFFFF when this information is not available. |
| 20 | 4 | CellParameterID | UINT32 | The Cell parameter ID (0-127). Use 0xFFFFFFFF when this information is not available. |
| 24 | 4 | TimingAdvance | UINT32 | The Timing Advance (0-1023). This member is the same value for all timeslots. Use 0xFFFFFFFF when this information is not available. |
| 28 | 4 | RSCP | INT32 | The Received Signal Code Power of  the serving cell. The range is -120 to -25, in units of 1dBm in Q8 L3 filtered. Use 0xFFFFFFFF when this information is not available. |
| 32 | 4 | PathLoss | UINT32 | The path loss of the serving cell (46-158). Use 0xFFFFFFFF when this information is not available. |
| 36 |   | DataBuffer | DATABUFFER | The data buffer containing *ProviderId*. |

#### LTE cell data structures

##### <a name="mbim_lte_serving_cell_info"></a>MBIM_LTE_SERVING_CELL_INFO

The MBIM_LTE_SERVING_CELL_INFO structure contains information about the LTE serving cell.

| Offset | Size | Field | Type | Description |
| --- | --- | --- | --- | --- |
| 0 | 4 | ProviderIdOffset | OFFSET | The offset in bytes, calculated from the beginning of this structure, to a numeric (0-9) string called *ProviderId* that represents the network provider identity. This string is a concatenation of a three-digit Mobile Country Code (MCC) and a two or three-digit Mobile Network Code (MNC). This member can be NULL when no *ProviderId* information is returned. |
| 4 | 4 | ProviderIdSize | SIZE(0-12) | The size used for *ProviderId*. |
| 8 | 4 | CellID | UINT32 | The Cell ID (0-268435455). Use 0xFFFFFFFF when this information is not available. |
| 12 | 4 | EARFCN | UINT32 | The Radio Frequency Channel Number of the serving cell (0-65535). Use 0xFFFFFFFF when this information is not available. |
| 16 | 4 | PhysicalCellID | UINT32 | The Physical Cell ID (0-503). Use 0xFFFFFFFF when this information is not available. |
| 20 | 4 | TAC | UINT32 | The Tracking Area Code (0-65535). Use 0xFFFFFFFF when this information is not available. |
| 24 | 4 | RSRP | INT32 | The Average Reference Signal Received Power. The range is -140 to -44, in units of 1dBm. Use 0xFFFFFFFF when this information is not available. |
| 28 | 4 | RSRQ | INT32 | The Average Reference Signal Received Quality. The range is -20 to -3, in units of 1dBm. Use 0xFFFFFFFF when this information is not available. |
| 32 | 4 | TimingAdvance | UINT32 | The Timing Advance (0-255). Use 0xFFFFFFFF when this information is not available. |
| 36 |   | DataBuffer | DATABUFFER | The data buffer containing *ProviderId*. |

##### <a name="mbim_lte_mrl"></a>MBIM_LTE_MRL

The MBIM_LTE_MRL structure contains the measured results list (MRL) of neighboring LTE cells.

| Offset | Size | Field | Type | Description |
| --- | --- | --- | --- | --- |
| 0 | 4 | ElementCount (EC) | UINT32 | The count of MRL entries following this element. |
| 4 |   | DataBuffer | DATABUFFER | The array of MRL records, each specified as an [MBIM_LTE_MRL_INFO](#mbim_lte_mrl_info) structure. |

##### <a name="mbim_lte_mrl_info"></a>MBIM_LTE_MRL_INFO

The MBIM_LTE_MRL_INFO structure contains information about a neighboring LTE cell.

| Offset | Size | Field | Type | Description |
| --- | --- | --- | --- | --- |
| 0 | 4 | ProviderIdOffset | OFFSET | The offset in bytes, calculated from the beginning of this structure, to a numeric (0-9) string called *ProviderId* that represents the network provider identity. This string is a concatenation of a three-digit Mobile Country Code (MCC) and a two or three-digit Mobile Network Code (MNC). This member can be NULL when no *ProviderId* information is returned. |
| 4 | 4 | ProviderIdSize | SIZE(0-12) | The size used for *ProviderId*. |
| 8 | 4 | CellID | UINT32 | The Cell ID (0-268435455). Use 0xFFFFFFFF when this information is not available. |
| 12 | 4 | EARFCN | UINT32 | The Radio Frequency Channel Number of the serving cell (0-65535). Use 0xFFFFFFFF when this information is not available. |
| 16 | 4 | PhysicalCellID | UINT32 | The Physical Cell ID (0-503). Use 0xFFFFFFFF when this information is not available. |
| 20 | 4 | TAC | UINT32 | The Tracking Area Code (0-65535). Use 0xFFFFFFFF when this information is not available. |
| 24 | 4 | RSRP | INT32 | The Average Reference Signal Received Power. The range is -140 to -44, in units of 1dBm. Use 0xFFFFFFFF when this information is not available. |
| 28 | 4 | RSRQ | INT32 | The Average Reference Signal Received Quality. The range is -20 to -3, in units of 1dBm. Use 0xFFFFFFFF when this information is not available. |
| 32 |   | DataBuffer | DATABUFFER | The data buffer containing *ProviderId*. |

#### CDMA cell data structures

##### <a name="mbim_cdma_mrl"></a>MBIM_CDMA_MRL

The MBIM_CDMA_MRL structure contains the measured results list (MRL) of both serving and neighboring CDMA cells.

| Offset | Size | Field | Type | Description |
| --- | --- | --- | --- | --- |
| 0 | 4 | ElementCount (EC) | UINT32 | The count of MRL entries following this element. |
| 4 |   | DataBuffer | DATABUFFER | The array of MRL records, each specified as an [MBIM_CDMA_MRL_INFO](#mbim_cdma_mrl_info) structure. |

##### <a name="mbim_cdma_mrl_info"></a>MBIM_CDMA_MRL_INFO

The MBIM_CDMA_MRL_INFO data structure is designed for the CDMA2000 network type. There can be more than one CDMA2000 serving cell at the same time. Both serving cells and neighboring cells will be returned in the same list. The **ServingCellFlag** field indicates whether a cell is a serving cell or not.

| Offset | Size | Field | Type | Description |
| --- | --- | --- | --- | --- |
| 0 | 4 | ServingCellFlag | UINT32 | Indicates whether this is a serving cell. A value of 1 indicates a serving cell, while a value of 0 indicates a neighboring cell. There may be more than one serving cell at a time (notably while in a call). |
| 4 | 4 | NID | UINT32 | The Network ID (0-65535). Use 0xFFFFFFFF when this information is not available. |
| 8 | 4 | SID | UINT32 | The System ID (0-32767). Use 0xFFFFFFFF when this information is not available. |
| 12 | 4 | BaseStationId | UINT32 | The Base Station ID (0-65535). Use 0xFFFFFFFF when this information is not available. |
| 16 | 4 | BaseLatitude | UINT32 | The Base Station Latitude (0-4194303). This is encoded in units of 0.25 seconds, expressed in two’s complement representation within the low 22 bits of the DWORD. As a signed value, North latitudes are positive. Use 0xFFFFFFFF when this information is not available. |
| 20 | 4 | BaseLongitude | UINT32 | The Base Station Longitude (0-8388607). This is encoded in units of 0.25 seconds, expressed in two’s complement representation within the low 23 bits of the DWORD. As a signed value, East longitudes are positive. Use 0xFFFFFFFF when this information is not available. |
| 24 | 4 | RefPN | UINT32 | The Base Station PN Number (0-511). Use 0xFFFFFFFF when this information is not available. |
| 28 | 4 | GPSSeconds | UINT32 | The GPS seconds, or the time at which this arrived from the base station. Use 0xFFFFFFFF when this information is not available. |
| 32 | 4 | PilotStrength | UINT32 | The Signal strength of the pilot (0-63). Use 0xFFFFFFFF when this information is not available. |

### Unsolicited Event

Not applicable.

### Status codes

This CID uses Generic Status Codes (see Use of Status Codes in Section 9.4.5 of [the public USB MBIM standard](https://www.usb.org/document-library/mobile-broadband-interface-model-v10-errata-1-and-adopters-agreement)).

## <a name="mbim_cid_location_info_status"></a>MBIM_CID_LOCATION_INFO_STATUS

This CID retrieves the status of the cellular information which indicates the location of the device. It may also be used to deliver an unsolicited notification when the location information changes.

Service: **MBB_UUID_BASIC_CONNECT_EXTENSIONS**

Service UUID: **3d01dcc5-fef5-4d05-0d3a-bef7058e9aaf**

| CID | Command code | Minimum OS version |
| --- | --- | --- |
| MBIM_CID_LOCATION_INFO_STATUS | 12 | Windows 10, version 1709 |

> [!NOTE]
> MBIM_CID_LOCATION_INFO_STATUS is defined starting in Windows 10, version 1709, but is not currently supported by the OS. A modem can send this command as a notification, but the OS does not currently handle it.

### Parameters

| Type | Set | Query | Notification |
| --- | --- | --- | --- |
| Command | Not applicable | Not applicable | Not applicable |
| Response | Not appliable | MBIM_LOCATION_INFO | MBIM_LOCATION_INFO |

### Query

The InformationBuffer of the MBIM_COMMAND_MSG is not used. The InformationBuffer of the MBIM_COMMAND_DONE contains an [MBIM_LOCATION_INFO](#mbim_location_info) structure.

### Set

Not applicable.

### Response

#### <a name="mbim_location_info"></a>MBIM_LOCATION_INFO

| Offset | Size | Field | Type | Description |
| --- | --- | --- | --- | --- |
| 0 | 4 | LocationAreaCode | UINT32 | The GSM/UMTS area code of the current location. Return 0xFFFFFFFF when the current system type is not applicable. |
| 4 | 4 | TrackingAreaCode | UINT32 | The LTE tracking area code of the current location. Return 0xFFFFFFFF when the current system type is not applicable. |
| 8 | 4 | CellID | UINT32 | The ID of the cellular tower. Return 0xFFFFFFFF when *CellID* is not available. |

### Unsolicited Events

The event InformationBuffer contains an MBIM_LOCATION_INFO structure.

This event is sent if the value of *Location Area Code*/*Tracking Area Code* changes to a valid value. This event is not sent when *CellID* changes or when *Location Area Code*/*Tracking Area Code* becomes invalid.

### Status codes

This CID uses Generic Status Codes (see Use of Status Codes in Section 9.4.5 of [the public USB MBIM standard](https://www.usb.org/document-library/mobile-broadband-interface-model-v10-errata-1-and-adopters-agreement)).

## <a name="oid_wwan_base_stations_info"></a>OID_WWAN_BASE_STATIONS_INFO

The NDIS equivalent for MBIM_CID_BASE_STATIONS_INFO is [OID_WWAN_BASE_STATIONS_INFO](oid-wwan-base-stations-info.md).

