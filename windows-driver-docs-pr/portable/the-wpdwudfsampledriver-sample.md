---
Description: The WpdWudfSampleDriver Sample
title: The WpdWudfSampleDriver Sample
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# The WpdWudfSampleDriver Sample


This section of the WPD driver documentation describes a comprehensive sample driver, WpdWudfSampleDriver, that is included with the Windows Driver Kit (WDK).

The comprehensive WPD sample driver (WpdWudfSampleDriver) demonstrates virtually all aspects of the Microsoft Windows Portable Devides (WPD) device driver interface (DDI). This driver is built as a normal User-Mode Driver Framework (UMDF) driver that also processes the WPD command set. Although this driver does not interact with actual hardware, it simulates communicating with a device that supports phone contacts, pictures, music, and video.

This driver was written in the simplest way to demonstrate concepts. Therefore, the sample driver might perform operations or be structured in a way that are inefficient in a production driver. Additionally, this sample does not use real hardware. Instead, it simulates a device by using data structures in memory. Therefore, the driver might be implemented in a way that is unrealistic for production hardware.

Some of the tasks that are accomplished by the WpdWudfSampleDriver are written for the advanced Windows Portable Devices (WPD) driver developer. These tasks are described in topics later in this section.

## <span id="related_topics"></span>Related topics


[The WPD Driver Samples](the-wpd-driver-samples.md)

 

 





