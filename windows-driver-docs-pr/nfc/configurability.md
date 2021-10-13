---
title: Configurability
description: This topic discuses extensibility points available to the NFC client driver, enabling the client driver to configure the parameters of many of its operations.
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Configurability


In addition to extensibility points available to the NFC client driver, the NFC CX also enables the client driver to configure the parameters of many of its operations. The following configurations can be customized by the NFC client driver.

-   Driver Flags
-   RF Discovery Configuration
-   LLCP Configuration

## Driver Flags


The NFC CX allows the NFC client driver to provide [**driver flags**](/windows-hardware/drivers/ddi/nfccx/ne-nfccx-_nfc_cx_driver_flags) to configure the run-time implementation of the class extension. These flags allow the NFC CX to implement certain standard NCI operation slightly differently, due to different firmware implementations due to ambiguities in the NCI specification.

## RF Discovery Configuration


The RF discovery configuration can be set by the NFC client driver through the [**NfcCxSetRfDiscoveryConfig**](/windows-hardware/drivers/ddi/nfccx/nf-nfccx-nfccxsetrfdiscoveryconfig) method. The RF discovery configuration should be done during initialization after calling [**NfcCxDeviceInitialize**](/windows-hardware/drivers/ddi/nfccx/nf-nfccx-nfccxdeviceinitialize), otherwise an error is returned.

## LLCP Configuration


The LLCP configuration can be set by the NFC client driver through the [**NfcCxSetLlcpConfig**](/windows-hardware/drivers/ddi/nfccx/nf-nfccx-nfccxsetllcpconfig) method provided by the NFC CX. The LLCP configuration should be done during initialization after [**NfcCxDeviceInitialize**](/windows-hardware/drivers/ddi/nfccx/nf-nfccx-nfccxdeviceinitialize), otherwise an error is returned.

 

 
## Related topics
[NFC device driver interface (DDI) overview](/windows-hardware/drivers/ddi/index)  
[NFC class extension (CX) reference](/windows-hardware/drivers/ddi/index)
