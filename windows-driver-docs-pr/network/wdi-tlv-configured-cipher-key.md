---
title: WDI_TLV_CONFIGURED_CIPHER_KEY
description: WDI_TLV_CONFIGURED_CIPHER_KEY is a TLV that contains a list of configured ciphers to be set in OID_WDI_GET_PM_PROTOCOL_OFFLOAD.
ms.date: 05/07/2021
keywords:
 - WDI_TLV_CONFIGURED_CIPHER_KEY Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI_TLV_CONFIGURED_CIPHER_KEY

WDI_TLV_CONFIGURED_CIPHER_KEY is a TLV that contains a list of configured ciphers to be set in [OID_WDI_GET_PM_PROTOCOL_OFFLOAD](oid-wdi-get-pm-protocol-offload.md). Drivers must return any GTK or iGTK keys that are currently configured. This TLV is a value of the [WDI_TLV_PM_PROTOCOL_OFFLOAD_80211RSN_REKEY](wdi-tlv-pm-protocol-offload-80211rsn-rekey.md) TLV.

## TLV Type

0x147

## Length

The size (in bytes) of the following values.

## Values

| Type | Description |
| --- | --- |
| [WDI_CIPHER_KEY_TYPE](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_cipher_key_type) | The type of key being returned. |
| [WDI_CIPHER_ALGORITHM](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_cipher_algorithm) | Specifies the cipher algorithm that uses this key. |
| [WDI_TLV_CIPHER_KEY_GCMP_256_KEY](wdi-tlv-cipher-key-gcmp-256-key.md) | Contains GCMP_256 cipher algorithm key data. This is only present if the cipher algorithm is WDI\_CIPHER\_ALGO\_GCMP\_256. |
| UINT8\[6\] | The initial 48-bit value of the Packet Number (PN), which is used for replay protection. Optional if **CipherAlgorithm** is **WDI_CIPHER_ALGO_WEP40**, **WDI_CIPHER_ALGO_WEP104**, or **WDI_CIPHER_ALGO_WEP**. |
| TLV<LIST\<UINT8>> | Present if and only if **CipherAlgorithm** is **WDI_CIPHER_ALGO_CCMP**. Contains CCMP cipher algorithm key data. |
| TLV<LIST\<UINT8>> | Present if and only if **CipherAlgorithm** is **WDI_CIPHER_ALGO_GCMP**. Contains GCMP cipher algorithm key data. |
| [WDI_TLV_CIPHER_KEY_TKIP_INFO](wdi-tlv-cipher-key-tkip-info.md) | Present if and only if **CipherAlgorithm** is **WDI_CIPHER_ALGO_TKIP**. |
| [WDI_TLV_CIPHER_KEY_BIP_GMAC_256_KEY](wdi-tlv-cipher-key-bip-gmac-256-key.md) | Present ony if cipher algorithm is WDI\_CIPHER\_ALGO\_BIP\_GMAC\_256. |
| TLV<LIST\<UINT8>> | Present if and only if **CipherAlgorithm** is **WDI_CIPHER_ALGO_BIP**. |
| TLV<LIST\<UINT8>> | Present if and only if **CipherAlgorithm** is **WDI_CIPHER_ALGO_WEP40**, **WDI_CIPHER_ALGO_WEP104**, or **WDI_CIPHER_ALGO_WEP**. |
| TLV<LIST\<UINT8>> | Present if and only if **CipherAlgorithm** is in the range of **WDI_CIPHER_ALGO_IHV_START** to **WDI_CIPHER_ALGO_IHV_END**. |

## Requirements

| &nbsp; | &nbsp; |
| ------ | ------ |
| **Minimum supported client** | Windows 10, version 2004 |
| **Minimum supported server** | Windows Server 2016 |
| **Header** | Wditypes.hpp |
