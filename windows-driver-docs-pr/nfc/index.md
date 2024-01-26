---
title: NFC Design Guide
description: Windows exposes a rich set of experiences using NFC technology.
ms.assetid: 26BFE25A-AC46-4634-8330-990DB447E55A
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
- smart card
- smartcard
ms.date: 01/11/2024
ms.topic: article
---

# Near field communications (NFC) design guide

Windows exposes a rich set of experiences using NFC technology including:

- [Wi-Fi Direct pairing](wi-fi-direct-paring-implementation.md) - Peripheral devices can participate in *Tap and Setup* and *Tap and Reconnect* use cases.
- [Near field proximity](nfp-design-guide.md) – Provides a common surface for Windows to use NFP capabilities.
- [Smart card support](design-guide-smart-card.md) – Allows callers to the NFC device driver to perform low level smart card operations on NFC contactless smart cards.
- [NFC power management](nfc-power-management.md) - NFC drivers intelligently manage the power state of the device.

To enable NFC support, Microsoft relies on IHVs to provide device drivers that implement the device driver interface (DDI) defined in these topics. Use the User-Mode Driver Framework (UMDF) 2.0 to write NFC drivers for Windows.

## Related topics

- [Getting Started with UMDF](../wdf/getting-started-with-umdf-version-2.md)
- [NFC device driver interface (DDI) reference](/windows-hardware/drivers/ddi/index)
