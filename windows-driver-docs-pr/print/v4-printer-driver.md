---
title: V4 Printer Driver
description: The v4 printer driver model addresses known issues with the version 3 driver model to improve the experience that users have with their printers.
ms.date: 10/30/2025
ms.topic: concept-article
#customer intent: As a hardware developer, I need to understand the v4 printer driver model and how it differs from previous models.
---

# V4 printer driver

[!include[Print Support Apps](../includes/print-support-apps.md)]

The v4 printer driver model is a refinement of the existing v3 printer driver model. Its design improves driver development, reduces IT management costs, and supports new scenarios. The v4 print driver model continues to support many familiar technologies like [XPSDrv](xpsdrv-printer-driver.md), [GPD](introduction-to-gpd-files.md), [PPD](pscript-minidrivers.md), [Autoconfiguration](printer-autoconfiguration.md), and [Bidi](bidirectional-communication.md). The v4 print driver model also supports several new extensibility points.

The v4 print driver model is optimized for several new scenarios:

- Windows 8 scenarios

  Universal Windows Platform (UWP) apps present new design considerations regarding UI behavior and security context. A printer driver model was needed that would provide deeply integrated support for this new environment. The v4 print driver model provides the only way for printer manufacturers to provide customized Print Preferences experiences or Printer Notification experiences in UWP apps.

- Printer sharing

  Printer sharing is a key value proposition item for Windows servers. The v4 printer driver model makes sharing easier and more efficient by eliminating the need to manage drivers across processor architectures.

- Ease of driver development

  The v4 driver supports existing development efforts from the version 3 printer driver model and from the XPSDrv architecture. The v4 driver is easier to develop and test.

> [!NOTE]
> To help to better explain some of the concepts in this section, a fictional company called Fabrikam is used.

## High-level architecture

The following architecture diagram is a high-level representation of a v4 print driver. Except for the rendering filters and user interface applications, Microsoft implements all the other functional blocks in the diagram.

:::image type="content" source="images/v4driverarch.png" alt-text="Diagram shows a high level representation of v4 print driver.":::

V4 print drivers rely heavily on data files and JavaScript for extensibility. The blue boxes represent existing files that were used in the v3 driver model. The green boxes represent new places to plug in.

## In this section

| Article | Description |
|---|---|
| [V4 printer driver rendering](v4-driver-rendering.md) | Provides information about v4 printer driver rendering. |
| [V4 printer driver configuration](v4-driver-configuration-architecture.md) | Provides information about v4 printer driver configuration. |
| [V4 printer driver setup](v4-driver-setup.md) | Provides information about v4 printer driver setup. |
| [V4 printer driver user interfaces](v4-printer-driver-user-interfaces.md) | Provides information about v4 printer driver user interfaces. |
| [V4 printer driver connectivity](v4-driver-connectivity-architecture.md) | Provides information about v4 printer driver connectivity. |
| [Build a v4 printer driver](building-a-basic-v4-printer-driver.md) | Provides information about how to build a v4 printer driver in Visual Studio. |

## Related content

- [Print DDI reference](/windows-hardware/drivers/ddi/_print/)
