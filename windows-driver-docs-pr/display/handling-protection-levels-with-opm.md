---
title: Handling Protection Levels with OPM
description: Handling Protection Levels with OPM
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
ms.date: 04/20/2017
---

# Handling Protection Levels with OPM

Each output protection type (for example, [Analog Copy Protection (ACP)](https://business.tivo.com/services/acp-technology), [Content Generation Management System Analog (CGMS-A)](cgms-a-standards.md), [High-bandwidth Digital Content Protection (HDCP)](https://www.digital-cp.com/hdcp-specifications), and [DisplayPort](https://go.microsoft.com/fwlink/p/?linkid=71382) Content Protection (DPCP)) has protection levels associated with it.

A graphics adapter is not required to support any output protection types. However, a graphics adapter must accurately report the protection types that it supports for each of the graphics adapter's outputs and the currently set protection level for each output.

ACP and CGMS-A protect analog TV signals. Currently, OPM can use ACP and CGMS-A to protect signals from composite outputs, S-Video outputs, or component outputs. For information about the various ACP and CGMS-A protection levels, see the [**DXGKMDT_OPM_ACP_PROTECTION_LEVEL**](/windows-hardware/drivers/ddi/d3dkmdt/ne-d3dkmdt-_dxgkmdt_opm_acp_protection_level) and [**DXGKMDT_OPM_CGMSA**](/windows-hardware/drivers/ddi/d3dkmdt/ne-d3dkmdt-_dxgkmdt_opm_cgmsa) enumerations.

HDCP protects digital video signals. Currently, OPM can use HDCP to protect data from Digital Video Interface (DVI) and High-Definition Multimedia Interface (HDMI) connector outputs. For information about the HDCP protection levels, see the [**DXGKMDT_OPM_HDCP_PROTECTION_LEVEL**](/windows-hardware/drivers/ddi/d3dkmdt/ne-d3dkmdt-_dxgkmdt_opm_hdcp_protection_level) enumeration.

DPCP protects digital video signals from DisplayPort output connectors.

The following sections describe the precedence that is placed on protection levels if more than one protected output is created for a particular physical output connector and the algorithm for determining a physical output connector's protection level:

[Assigning Precedence to Protection Levels](assigning-precedence-to-protection-levels.md)

[Determining the Protection Level for a Physical Output](determining-the-protection-level-for-a-physical-output.md)
