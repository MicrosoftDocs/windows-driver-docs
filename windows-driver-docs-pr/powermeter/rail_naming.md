---
title:Naming convention for EMI rails 
description: Naming convention for EMI rails 
keywords:
- Energy Metering , interface
- Energy Meter Interface WDK
- PMI WDK Energy Meter
ms.date: 10/14/2021
ms.localizationpriority: medium
---

# Naming convention for EMI rails 


The Energy Estimation Engine (E3) will override the software model for components with EMI rails, if they match a pre-defined naming convention.   

## Rail to Component mapping

| EMI Rail Name | Component |
|--|--|
| CPU | cpu | STORAGE | disk | WIFI | network | MBB | mbb | DISPLAY | display | GPU | Soc* |

* Gpu energy is mis-labeled as “Soc” component energy in E3.

## How the rails are mapped to E3 component energy

If the Emi rail name matches the name in the map above, the measurement from that rail and only that rail will be used for the E3 component energy.  

If there is not an exact match to the name but matches that start being with “rail name_”, the sum of these rails will be used for the component. 

## Example of exact match

GPU, GPU_TOP, and GPU_BOTTOM are available.
Only GPU will be used for E3 Soc energy

## Example without exact match

WIFI_BLUETOOTH and WIFI_WIFI are available.
The sum of WIFI_BLUETOOTH and WIFI_WIFI will be used for E3 Network energy.

## Tip

The output of “powercfg /srumutil” has a column that indicates which components used EMI rails

 


