---
title: V4 printer driver
description: The v4 printer driver model was designed to address known issues with the version 3 driver model, and thus improve the quality of the experience that users have with their printers.
ms.date: 10/20/2022
---

# V4 printer driver

The v4 printer driver model is a refinement of the existing v3 printer driver model. It's designed to improve driver development, reduce IT management costs, and support new scenarios. The v4 print driver model continues to support many familiar technologies like [XPSDrv](xpsdrv-printer-driver.md), [GPD](introduction-to-gpd-files.md), [PPD](pscript-minidrivers.md), [Autoconfiguration](printer-autoconfiguration.md), and [Bidi](bidirectional-communication.md). The v4 print driver model also supports several new extensibility points.

The v4 print driver model is also optimized for several new scenarios:

- Windows 8 scenarios

    UWP apps present new design considerations regarding UI behavior and security context. So a printer driver model was needed that would provide deeply integrated support for this new environment. The v4 print driver model provides the only way for printer manufacturers to provide customized Print Preferences experiences or Printer Notification experiences in UWP apps.

- Printer sharing

    Printer sharing is a key value proposition item for Windows servers. The v4 printer driver model was designed to make sharing easier and more efficient by eliminating the need to manage drivers across processor architectures.

- Ease of driver development

    The v4 driver supports existing development efforts from the version 3 printer driver model and from the XPSDrv architecture. And also, the v4 driver is easier to develop and test.

> [!NOTE]
> To help to better explain some of the concepts in this section, a fictional company called Fabrikam is used.

## High-level Architecture

The following architecture diagram is a high-level representation of a v4 print driver. Except for the rendering filters and user interface applications, all the other functional blocks in the diagram are implemented by Microsoft. V4 print drivers rely heavily on data files and JavaScript for extensibility. The blue boxes represent existing files that were used in the v3 driver model, and the green boxes represent new places to plug in.

![high level representation of v4 print driver.](images/v4driverarch.png)

## In this section

| Article | Description |
|---|---|
| [V4 printer driver rendering](v4-driver-rendering.md) | Provides information about v4 printer driver rendering. |
| [V4 printer driver configuration](v4-driver-configuration.md) | Provides information about v4 printer driver configuration. |
| [V4 printer driver setup](v4-driver-setup.md) | Provides information about v4 printer driver setup. |
| [V4 printer driver user interfaces](v4-printer-driver-user-interfaces.md) | Provides information about v4 printer driver user interfaces. |
| [V4 printer driver connectivity](v4-printer-driver-connectivity.md) | Provides information about v4 printer driver connectivity. |
| [Build a v4 printer driver in Visual Studio](build-a-v4-print-driver-in-visual-studio.md) | Provides information about how to build a v4 printer driver in Visual Studio. |

## Related sections

[Print DDI reference](/windows-hardware/drivers/ddi/_print)
