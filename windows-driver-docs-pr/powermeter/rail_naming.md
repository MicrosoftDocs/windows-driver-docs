---
title: Naming convention for EMI rails 
description: Naming convention for EMI rails 
keywords:
- Energy Metering , interface
- Energy Meter Interface WDK
- PMI WDK Energy Meter
ms.date: 10/14/2021
---

# Integrating EMI data into E3

Energy Estimation Engine (E3) attributes energy to software applications. If the device has data expressed through the EMI interface and matches the rail naming taxonomy, E3 will preferentially use that data over its software estimated model.

## Rail to component mapping

| EMI Rail Name        | Component |
|----------------------|-----------|
| CPU or CPU_*         | cpu       |
| STORAGE or STORAGE_* | disk      |
| WIFI or WIFI_*       | network   |
| MBB or MBB_*         | mbb       |
| DISPLAY or DISPLAY_* | display   |
| GPU or GPU_*         | soc       |

## How the rails are mapped to E3 component energy

If the Emi rail name matches the name in the map above, the measurement from that rail and only that rail will be used for the E3 component energy.  

If there is not an exact match to the name but matches that start being with “rail name_”, the sum of these rails will be used for the component.

## Example of exact match

GPU, GPU_TOP, and GPU_BOTTOM are available.
Only GPU will be used for E3 Soc energy

## Example without exact match

WIFI_BLUETOOTH and WIFI_WIFI are available.
The sum of WIFI_BLUETOOTH and WIFI_WIFI will be used for E3 Network energy.
