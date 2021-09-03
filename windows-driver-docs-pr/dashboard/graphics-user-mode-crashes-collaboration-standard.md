---
title: Crashes in communication and collaboration apps normalized by usage <= baseline goal
description: The measure aggregates telemetry from a 7-day sliding window a ratio of crashes in communication and collaboration applications, caused by the graphics drivers, over total runtime in years
ms.topic: article
ms.date: 09/02/2021
ms.localizationpriority: medium
---

# Crashes in communication and collaboration apps normalized by usage <= baseline goal

## Description

This measure is counting the number of crashes in display drivers that happen in the context of the communication and collaboration applications and calculating the runtime of such applications on all machines that have the updated driver. The measure then normalizes the crash count by cumulative application runtime in years (HOART - hit over application runtime)

Examples of communication and collaboration applications considered for this measure:

* MICROSOFT.SKYPEAPP
* DISCORD.EXE
* SKYPE.EXE
* TEAMVIEWER.EXE
* LYNC.EXE
* WECHAT.EXE
* QQ.EXE
* SLACK.EXE
* KAKAOTALK.EXE
* ZOOM.EXE
* ZOOM
* WHATSAPP.EXE
* LINE.EXE
* YOUCAMSERVICE.EXE
* TELEGRAM.EXE
* VIBER.EXE
* MICROSOFT.SKYPEROOMSYSTEM

## Measure attributes

| Attribute | Value |
|--|--|
| **Audience** | Devices targeted by the driver |
| **Time period** | 7-day sliding window |
| **Measurement criteria** | Aggregation of communication and collaboration application runtime in years |
| **Minimum population** | 10,000 hours of communication and collaboration application runtime |
| **Passing criteria** | <= 1 crash per Year of cumulative runtime |
| **Measure ID** | 25912714 |

## Calculation

Ratio of crashes in communication and collaboration applications, caused by the graphics drivers, over total runtime in years

Total crashes in communication and collaboration applications = Count(crashes in communication and collaboration applications on machines that have the driver)

Total communication and collaboration applications runtime = Sum(runtime of communication and collaboration applications, for each machine that has the driver)

Runtime in years = total runtime of communication and collaboration applications ∗ 60 (minute) ∗ 60 (hour) ∗ 24 (day) ∗ 365 (year)

### Final Calculation

Crashes in communication and collaboration applications normalized by usage in years = total crashes in communication and collaboration applications / runtime in years
