---
title: Near-field communication (NFC) device drivers in Windows 10
description: This topic summarizes the new features and improvements for near-field communication (NFC) device drivers in Windows 10.
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
ms.date: 03/28/2022
---

# Near-field communication (NFC) device drivers in Windows 10

This topic summarizes the new features and improvements for near-field communication (NFC) device drivers in Windows 10.

- The NFC device driver model has converged for both desktop and mobile devices to create a universal NFC device driver model. Hardware partners can now build a single driver that can run on all Windows device platforms.

- The [NFC class extension (CX)](/windows-hardware/drivers/nfc/nfc-class-extension-) implements the Windows-defined device driver interfaces to interact with the NFC controller, secure elements, and remote RF endpoints.

- An in-box NFC radio manager has been added to take care of managing airplane mode for NFC. Do not package IHV-supplied NFC radio managers with NFC drivers (as was done in earlier versions of Windows). Installing an IHV-supplied NFC radio manager alongside the Windows 10 NFC radio manager will cause conflicts between those software components.

## Related topics

- [NFC device driver interface (DDI) reference](/windows-hardware/drivers/ddi/_nfpdrivers/)
