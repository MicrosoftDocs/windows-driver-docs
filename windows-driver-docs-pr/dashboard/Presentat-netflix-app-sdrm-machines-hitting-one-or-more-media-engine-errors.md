---
title: PresentAt - Netflix app (Software Digital Rights Management) % of machines hitting one or more media engine errors
description: % of machines using Present AT that hit one or more media engine errors during video playback on the Netflix app, which supports Software Digital Rights Management (SWDRM). This measure monitors media engine errors that arise for driver versions using Present AT on Netflix app. 

ms.topic: article
ms.date: 07/15/2022
---

#  Percent of machines using PresentAt on Netflix app (Software Digital Rights Management) that hit one or more media engine errors

## Description

During a user's session, a machine hits one or more media engine errors during video playback on the Netflix app, which supports Software Digital Rights Management (SWDRM). This measure monitors media engine errors that arise for driver versions using Present AT on Netflix app.

Examples of media engine errors can be found here: [Errors Online: Error lookup](windowsinternalservices.azurewebsites.net)



## Measure attributes

| Attribute | Value |
|--|--|
| **Audience** | Machines with a WDDM 3.1+ graphics driver that supports displayables, which is a feature in Direct 3D 11  [D3D11_FEATURE enumeration (d3d11.h)](https://docs.microsoft.com/en-us/windows/win32/api/d3d11/ne-d3d11-d3d11_feature) - Win32 apps, and is running the Netflix app. |
| **Time period** | 7-day sliding window |
| **Measurement criteria** | Percent of machines |
| **Minimum population** | 100 machines |
| **Passing criteria** | <=2% of devices hit a playback error|
| **Measure ID** | 39664000 |

## Calculation

1. The measure aggregates telemetry from a 7-day sliding window into a percentage of machines that have 1 or more media engine errors while using the Netflix app with Present AT
2. Failure machines = count(machines with 1 or more video playback errors using Netflix app with Present AT)
3. Total machines = count(machines using Netflix app with Present AT)
4. Final calculation = Failure machines / Total machines
