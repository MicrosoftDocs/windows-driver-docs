---
title: MB 5G data class support
description: MB 5G data class support
ms.assetid: 16531A63-76EC-4722-8817-FA8DB3B2B82F
keywords:
- MB 5G data class support, Mobile Broadband 5G data class support
ms.date: 03/22/2019
ms.localizationpriority: medium
---

# MB 5G data class support

## Terminology

This topic uses the following terms:

| Term | Definition |
| --- | --- |
| NR | New Radio. NR is the term used in 3GPP when referring to 5G. |
| MBB | Mobile broadband. |
| NGC | Next Generation Core. The core of 5G. |
| DC | Dual Connectivity. The network can support both LTE and 5G NR, including dual connectivity with which devices have simultaneous connections to LTE and NR. |
| SA | Standalone. The device can set up a call on 5G. |
| NSA | Non-standalone. The device sets up a call on LTE and adds a new 5G carrier for data traffic. |
| gNR | A node that supports NR as well as connectivity to NGC. |

## Overview

Windows 10, version 1903 is the first Windows release to support 5G mobile broadband drivers for IHV partners. The name *5G* is friendly name for New Radio (NR), which was introduced in the [3GPP Release 15 specification](http://www.3gpp.org/release-15). Comprehensive specifications on the NR air interface, radio access network (RAN) technology and interface, basic network slicing concepts, and other aspects of NR are defined in the [3GPP TS 38.xx series of specifications](http://www.3gpp.org/DynaReport/38-series.htm). These specifications form the foundation for the wider ecosystem to prepare for the first phase of end-to-end 5G deployment around the world in 2019.

NR is a comprehensive set of standards that provide true long-term evolution to existing 4th-generation LTE technologies, covering everything from narrowband to ultra-broadband, and from nominal-latency to ultra-reliable/low-latency communications. As a technology, 5G is expected to develop over a decade-long time frame. This topic describes the first steps for Windows support of 5G in Windows 10, version 1903, starting with 5G enhanced mobile broadband (eMBB).

## Windows 5G architectural considerations



## MBIM Extensions release 2.0

## MBIM service and CID values

| Service name | UUID | UUID value |
| --- | --- | --- |
| Microsoft Basic IP Connectivity Extensions | UUID_BASIC_CONNECT_EXTENSIONS | 3D01DCC5-FEF5-4D05-9D3A-BEF7058E9AAF |

## MBIM_CID_VERSION

## MBIM_CID_MS_DEVICE_CAPS_V2

## MBIM_CID_REGISTER_STATE

## MBIM_CID_PACKET_SERVICE

## MBIM_CID_SIGNAL_STATE