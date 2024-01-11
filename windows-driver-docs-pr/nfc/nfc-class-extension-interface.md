---
title: NFC Class Extension Interface
description: The NFC CX interface is based on the UMDF class extension model.
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
ms.date: 01/11/2024
---

# NFC class extension interface

The NFC CX interface is based on the UMDF class extension model. The NFC CX interface enables the NFC client to offload the class implementation to the Microsoft-provided class extension that implements the NFC CX interface, while allowing the client driver to perform transport-specific initialization and I/O handling, as well as serve as the host for all vendor-specific functionality required for the NFC controller.

The NFC CX interface includes the following methods:

- [**NfcCxDeviceInitConfig**](/windows-hardware/drivers/ddi/nfccx/nf-nfccx-nfccxdeviceinitconfig)
- [**NfcCxDeviceInitialize**](/windows-hardware/drivers/ddi/nfccx/nf-nfccx-nfccxdeviceinitialize)
- [**NfcCxDeviceDeinitialize**](/windows-hardware/drivers/ddi/nfccx/nf-nfccx-nfccxdevicedeinitialize)
- [**NfcCxHardwareEvent**](/windows-hardware/drivers/ddi/nfccx/nf-nfccx-nfccxhardwareevent)
- [**NfcCxNciReadNotification**](/windows-hardware/drivers/ddi/nfccx/nf-nfccx-nfccxncireadnotification)
- [**NfcCxSetRfDiscoveryConfig**](/windows-hardware/drivers/ddi/nfccx/nf-nfccx-nfccxsetrfdiscoveryconfig)
- [**NfcCxSetLlcpConfig**](/windows-hardware/drivers/ddi/nfccx/nf-nfccx-nfccxsetllcpconfig)
- [**NfcCxRegisterSequenceHandler**](/windows-hardware/drivers/ddi/nfccx/nf-nfccx-nfccxregistersequencehandler)
- [**NfcCxUnRegisterSequenceHandler**](/windows-hardware/drivers/ddi/nfccx/nf-nfccx-nfccxunregistersequencehandler)

## Related topics

- [NFC device driver interface (DDI) overview](/windows-hardware/drivers/ddi/index)
- [NFC class extension (CX) reference](/windows-hardware/drivers/ddi/index)
