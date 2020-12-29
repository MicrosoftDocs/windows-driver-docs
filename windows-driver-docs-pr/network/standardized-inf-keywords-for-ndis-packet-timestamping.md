---
title: Standardized INF keywords for NDIS packet timestamping
description: Standardized INF keywords for NDIS packet timestamping
ms.date: 12/31/2020
ms.localizationpriority: medium
---

# Standardized INF Keywords for NDIS Selective Suspend


The following standardized INF keywords are defined to enable, disable, and configure parameters for NDIS selective suspend on a miniport driver:

[**\*PtpHardwareTimestamp** INF keyword](#ptphardwaretimestamp-inf-keyword)

[**\*SoftwareTimestamp** INF keyword](#softwaretimestamp-inf-keyword)


For more information about standardized INF keywords, see [Standardized INF Keywords for Network Devices](standardized-inf-keywords-for-network-devices.md).

## \*PtpHardwareTimestamp INF keyword



|SubkeyName|ParamDesc|Value|EnumDesc|
|--- |--- |--- |--- |
|***PtpHardwareTimestamp**|PTP Hardware Timestamp|0 (Default)|Disabled|
|||1|Enabled|

## \*SoftwareTimestamp INF keyword

|SubkeyName|ParamDesc|Value|EnumDesc|
|--- |--- |--- |--- |
|***SoftwareTimestamp**|Software Timestamp|0 (Default)|Disabled|
|||1|**RxAll**: This enum value corresponds to the miniport driver capability to generate software timestamps for all packets during Rx.|
|||2|**TxAll**: This enum value corresponds to the miniport driver capability to generate software timestamps for all packets during Tx.|
|||3|**RxAll & TxAll**: This enum value corresponds to the miniport driver capability to generate software timestamps for all packets during Rx and Tx.|
|||4|**TaggedTx**: This enum value corresponds to the miniport driver capability to generate software timestamps for a specific Tx packet when indicated to do so by the operating system.|
|||5|**RxAll & TaggedTx**: This enum value corresponds to the miniport driver capability to generate software timestamps for all packets during Rx and for a specific Tx packet when indicated to do so by the operating system.|