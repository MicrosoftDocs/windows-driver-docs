---
title: CGMS-A Standards
description: CGMS-A Standards
ms.date: 04/20/2017
---

# CGMS-A Standards

The Copy Generation Management System - Analog (CGMS-A) is a copy protection system for analog video signals. Various countries and regions use different versions of CGMS-A. A hardware vendor must ensure that their display miniport driver supports the appropriate CGMS-A version.

For example, a driver for a graphics adapter to be used in Japan should probably support the Association of Radio Industries and Businesses (ARIB) TR-B15 standard, which is the operational guideline for digital satellite broadcasting. However, a driver for a graphics adapter to be used in the United States should support the International Electrotechnical Commission (IEC) 61880 standard or the Consumer Electronics Association (CEA) CEA-608-B standard. The standard that a graphics adapter's display miniport driver supports depends on the type of signal that the adapter transmits.

The following list describes various standards that define CGMS-A. Redistribution control is defined only in the CEA-805-A standard.

- **CEA-805-A**
  - Data on Component Video Interfaces
  - Defines how CGMS-A and redistribution control information should be encoded in an analog 480p, 720p, or 1080i signal that is transmitted from a component video output (Y/Pb/Pr output).
  - This standard is published by the [Consumer Electronics Association (CEA)](https://www.standardsportal.org/usa_en/sdo/cea.aspx).

- **CEA-608-B and EIA-608-B**
  - Line 21 Data Services
  - Defines how CGMS-A information should be encoded in a 480i signal that is transmitted from an RF, composite, or S-Video output.
  - This standard is published by CEA and [Electronic Components Industry Association](https://go.microsoft.com/fwlink/p/?linkid=71278) (ECIA).

- **EN 300 294 V1.3.2 (1998-04)**
  - Television systems; 625-line television - Wide Screen Signaling (WSS)
  - Defines how CGMS-A should be encoded in a 576i Phase Alternation Line (PAL) or Sequential Color with Memory (SECAM) signal.
  - This standard is published by the [European Telecommunications Standards Institute](https://go.microsoft.com/fwlink/p/?linkid=26364) (ETSI).

- **IEC - 61880 - First edition - Video systems (525/60)**  
  - Video and accompanied data using the vertical blanking interval - Analog interface
  - A method of encoding CGMS-A information in a 480i video signal that is transmitted from an analog or digital video output.
  - This method is published by [International Electrotechnical Commission](https://go.microsoft.com/fwlink/p/?linkid=8732) (IEC).

- **IEC - 61880-2 - First edition - Video systems (525/60)**
  - Video and accompanied data using the vertical blanking interval - Analog interface - Part 2: 525 progressive scan system
  - A method of encoding CGMS-A information in a 480p video signal that is transmitted from an analog or digital video output.

- **IEC - 62375 - Video systems (625/50 progressive)**
  - Video and accompanied data using the vertical blanking interval - Analog interface
  - A method of encoding CGMS-A information in a 576p video signal that is transmitted from an analog or digital video output.

- **ARIB TR-B15**
  - Operational Guideline for Digital Satellite Broadcasting
  - Defines how CGMS-A information should be encoded in an analog 480i, 480p, 720p, or 1080i signal that is transmitted from a video output.
  - This standard applies only to Japan.
  - This standard is published by the [Association of Radio Industries and Businesses](https://go.microsoft.com/fwlink/p/?linkid=71283) (ARIB).
