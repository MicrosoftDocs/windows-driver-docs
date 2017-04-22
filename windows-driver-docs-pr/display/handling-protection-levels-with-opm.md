---
title: Handling Protection Levels with OPM
description: Handling Protection Levels with OPM
ms.assetid: 2d3e5d07-8d6f-44fb-985a-96990538ed29
keywords:
- protection levels WDK display , types of
- protection levels WDK display , ACP
- protection levels WDK display , Analog Copy Protection
- protection levels WDK display , CGMS-A
- protection levels WDK display , Content Generation Management System Analog
- protection levels WDK display , High-bandwidth Digital Content Protection
- protection levels WDK display , HDCP
- protection levels WDK display , DisplayPort Content Protection
- protection levels WDK display , DPCP
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Handling Protection Levels with OPM


Each output protection type (for example, Analog Copy Protection (ACP), [Content Generation Management System Analog (CGMS-A)](cgms-a-standards.md), High-bandwidth Digital Content Protection (HDCP), and DisplayPort Content Protection (DPCP)) has protection levels associated with it. For more information about ACP, see the [Rovi (formerly Macrovision)](http://go.microsoft.com/fwlink/p/?linkid=71273) website. For more information about HDCP, see the [HDCP Specification Revision 1.1](http://go.microsoft.com/fwlink/p/?linkid=38728). For more information about DisplayPort, see the [DisplayPort](http://go.microsoft.com/fwlink/p/?linkid=71382) Web article.

A graphics adapter is not required to support any output protection types. However, a graphics adapter must accurately report the protection types that it supports for each of the graphics adapter's outputs and the currently set protection level for each output.

ACP and CGMS-A protect analog TV signals. Currently, OPM can use ACP and CGMS-A to protect signals from composite outputs, S-Video outputs, or component outputs. For information about the various ACP and CGMS-A protection levels, see the [**DXGKMDT\_OPM\_ACP\_PROTECTION\_LEVEL**](https://msdn.microsoft.com/library/windows/hardware/ff560834) and [**DXGKMDT\_OPM\_CGMSA**](https://msdn.microsoft.com/library/windows/hardware/ff560846) enumerations.

HDCP protects digital video signals. Currently, OPM can use HDCP to protect data from Digital Video Interface (DVI) and High-Definition Multimedia Interface (HDMI) connector outputs. For information about the HDCP protection levels, see the [**DXGKMDT\_OPM\_HDCP\_PROTECTION\_LEVEL**](https://msdn.microsoft.com/library/windows/hardware/ff560878) enumeration.

DPCP protects digital video signals from DisplayPort output connectors.

The following sections describe the precedence that is placed on protection levels if more than one protected output is created for a particular physical output connector and the algorithm for determining a physical output connector's protection level:

[Assigning Precedence to Protection Levels](assigning-precedence-to-protection-levels.md)

[Determining the Protection Level for a Physical Output](determining-the-protection-level-for-a-physical-output.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Handling%20Protection%20Levels%20with%20OPM%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




