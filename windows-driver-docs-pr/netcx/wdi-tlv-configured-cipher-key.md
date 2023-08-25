---
title: WDI_TLV_CONFIGURED_CIPHER_KEY
ms.topic: reference
description: WDI_TLV_CONFIGURED_CIPHER_KEY is a WiFiCx TLV that contains a list of configured ciphers to be set in OID_WDI_GET_PM_PROTOCOL_OFFLOAD.
ms.date: 08/23/2023
---

# WDI_TLV_CONFIGURED_CIPHER_KEY

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]

WDI_TLV_CONFIGURED_CIPHER_KEY is a TLV that contains a list of configured ciphers to be set in [OID_WDI_GET_PM_PROTOCOL_OFFLOAD](oid-wdi-get-pm-protocol-offload.md). Drivers must return any GTK or iGTK keys that are currently configured. This TLV is a value of the [WDI_TLV_PM_PROTOCOL_OFFLOAD_80211RSN_REKEY](wdi-tlv-pm-protocol-offload-80211rsn-rekey.md) TLV.

## TLV Type

0x147

## Length

The size (in bytes) of the following values.

## Values

| Type | Multiple TLV instances allowed | Optional | Description |
| --- | --- | --- | --- |
| [WDI_CIPHER_KEY_TYPE](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_cipher_key_type) | | | The type of key being returned. |
| [WDI_CIPHER_ALGORITHM](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_cipher_algorithm) | | |Specifies the cipher algorithm that uses this key. |
| [WDI_TLV_CIPHER_KEY_RECEIVE_SEQUENCE_COUNT](wdi-tlv-cipher-key-receive-sequence-count.md) | | | The initial 48-bit value of the Packet Number (PN), which is used for replay protection. Optional if **CipherAlgorithm** is **WDI_CIPHER_ALGO_WEP40**, **WDI_CIPHER_ALGO_WEP104**, or **WDI_CIPHER_ALGO_WEP**. |
| [WDI_TLV_CIPHER_KEY_CCMP_KEY](wdi-tlv-cipher-key-ccmp-key.md) | | X |Present if and only if **CipherAlgorithm** is **WDI_CIPHER_ALGO_CCMP**. Contains CCMP cipher algorithm key data. |
| [WDI_TLV_CIPHER_KEY_GCMP_KEY](wdi-tlv-cipher-key-gcmp-key.md) |  | X |Present if and only if **CipherAlgorithm** is **WDI_CIPHER_ALGO_GCMP**. Contains GCMP cipher algorithm key data. |
| [WDI_TLV_CIPHER_KEY_TKIP_INFO](wdi-tlv-cipher-key-tkip-info.md) |  | X |Present if and only if **CipherAlgorithm** is **WDI_CIPHER_ALGO_TKIP**. |
| [WDI_TLV_CIPHER_KEY_BIP_KEY](wdi-tlv-cipher-key-bip-key.md) |  | X |Present if and only if **CipherAlgorithm** is **WDI_CIPHER_ALGO_BIP**. |
| [WDI_TLV_CIPHER_KEY_WEP_KEY](wdi-tlv-cipher-key-wep-key.md) |  | X |Present if and only if **CipherAlgorithm** is **WDI_CIPHER_ALGO_WEP40**, **WDI_CIPHER_ALGO_WEP104**, or **WDI_CIPHER_ALGO_WEP**. |
| [WDI_TLV_CIPHER_KEY_IHV_KEY](wdi-tlv-cipher-key-ihv-key.md) |  | X |Present if and only if **CipherAlgorithm** is in the range of **WDI_CIPHER_ALGO_IHV_START** to **WDI_CIPHER_ALGO_IHV_END**. |
| [WDI_TLV_CIPHER_KEY_GCMP_256_KEY](wdi-tlv-cipher-key-gcmp-256-key.md) |  | X |Contains GCMP_256 cipher algorithm key data. This is only present if the cipher algorithm is **WDI\_CIPHER\_ALGO\_GCMP\_256**. |
| [WDI_TLV_CIPHER_KEY_BIP_GMAC_256_KEY](wdi-tlv-cipher-key-bip-gmac-256-key.md) |  | X |Present ony if cipher algorithm is **WDI\_CIPHER\_ALGO\_BIP\_GMAC\_256**. |
| [WDI_TLV_LINK_ID](wdi-tlv-link-id.md) | | X | Specifies the AP's link Id. This will be present when setting or querying the link-specific keys on a multi-link connection. |

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|
