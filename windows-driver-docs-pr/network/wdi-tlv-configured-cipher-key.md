---
title: WDI_TLV_CONFIGURED_CIPHER_KEY
description: WDI_TLV_CONFIGURED_CIPHER_KEY is a TLV that contains a list of configured ciphers to be set in OID_WDI_GET_PM_PROTOCOL_OFFLOAD.
ms.assetid: 8C7C77F7-FF62-485C-94C4-EE0F1E57D771
ms.date: 04/02/2018
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
| [WDI_CIPHER_KEY_TYPE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wditypes/ne-wditypes-_wdi_cipher_key_type) | The type of key being returned. |
| [WDI_CIPHER_ALGORITHM](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wditypes/ne-wditypes-_wdi_cipher_algorithm) | Specifies the cipher algorithm that uses this key. |
| UINT8\[6\] | The initial 48-bit value of the Packet Number (PN), which is used for replay protection. Optional if **CipherAlgorithm** is **WDI_CIPHER_ALGO_WEP40**, **WDI_CIPHER_ALGO_WEP104**, or **WDI_CIPHER_ALGO_WEP**. |
| TLV<LIST\<UINT8>> | Present if and only if **CipherAlgorithm** is **WDI_CIPHER_ALGO_CCMP**. Contains CCMP cipher algorithm key data. |
| TLV<LIST\<UINT8>> | Present if and only if **CipherAlgorithm** is **WDI_CIPHER_ALGO_GCMP**. Contains GCMP cipher algorithm key data. |
| [WDI_TLV_CIPHER_KEY_TKIP_INFO](wdi-tlv-cipher-key-tkip-info.md) | Present if and only if **CipherAlgorithm** is **WDI_CIPHER_ALGO_TKIP**. |
| TLV<LIST\<UINT8>> | Present if and only if **CipherAlgorithm** is **WDI_CIPHER_ALGO_BIP**. |
| TLV<LIST\<UINT8>> | Present if and only if **CipherAlgorithm** is **WDI_CIPHER_ALGO_WEP40**, **WDI_CIPHER_ALGO_WEP104**, or **WDI_CIPHER_ALGO_WEP**. |
| TLV<LIST\<UINT8>> | Present if and only if **CipherAlgorithm** is in the range of **WDI_CIPHER_ALGO_IHV_START** to **WDI_CIPHER_ALGO_IHV_END**. |
 

## Requirements

| | |
| --- | --- |
| Minimum supported client | Windows 10, version 1803 |
| Minimum supported server | Windows Server 2016 |
| Header | Wditypes.hpp |
