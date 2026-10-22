---
title: Configurability
description: This topic discuses extensibility points available to the NFC client driver, enabling the client driver to configure the parameters of many of its operations.
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
ms.date: 01/11/2024
ms.topic: concept-article
---

# Configurability

In addition to extensibility points available to the NFC client driver, the NFC CX also enables the client driver to configure the parameters of many of its operations. The following configurations can be customized by the NFC client driver.

- Driver Flags
- RF Discovery Configuration
- LLCP Configuration

## Driver Flags

The NFC CX enables the NFC client driver to provide **driver flags** to configure the run-time implementation of the class extension. These flags enable the NFC CX to implement certain standard NCI operations slightly differently, due to different firmware implementations and ambiguities in the NCI specification.

## RF Discovery Configuration

The NFC client driver sets the RF discovery configuration through the **NfcCxSetRfDiscoveryConfig** method. Set the RF discovery configuration during initialization after calling **NfcCxDeviceInitialize**. Otherwise, an error is returned.

## LLCP Configuration

The NFC client driver sets the LLCP configuration through the **NfcCxSetLlcpConfig** method provided by the NFC CX. Set the LLCP configuration during initialization after **NfcCxDeviceInitialize**. Otherwise, an error is returned.

## Related topics

- [NFC device driver interface (DDI) overview](/windows-hardware/drivers/ddi/_nfpdrivers)
- [NFC class extension (CX) design guide](/windows-hardware/drivers/nfc/nfc-class-extension-)
