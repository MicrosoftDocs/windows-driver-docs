---
title: Autoconfiguration in an IHV Driver
description: Autoconfiguration in an IHV Driver
ms.assetid: 81febae0-6fab-4226-9e98-7705d606caf4
keywords:
- IHV driver autoconfiguration WDK printer
- autoconfiguration WDK printer , IHV drivers
- printer autoconfiguration WDK printer , IHV drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Autoconfiguration in an IHV Driver


A standalone IHV driver that supports autoconfiguration must meet the following requirements:

1.  Follow the Microsoft [bidi communications schema](https://msdn.microsoft.com/library/windows/hardware/ff545175) and the [bidi communication interfaces](https://msdn.microsoft.com/library/windows/hardware/ff545163) described in the Windows SDK documentation.

2.  Support the PRINTER\_EVENT\_CONFIGURATION\_UPDATE printer event in the [**DrvPrinterEvent**](https://msdn.microsoft.com/library/windows/hardware/ff548564) function.

3.  Be aware of the bidi notification schema's ability to understand received notifications. See [Bidi Communications Schema](bidirectional-communication-schema.md).

**Note**  It is not necessary to create a standalone driver in order to provide support for autoconfiguration. You can, instead, write a GPD or PPD file that takes advantage of one of the Microsoft printer class drivers. For details, see [In-box Support for Autoconfiguration](in-box-support-for-autoconfiguration.md).

 

 

 




