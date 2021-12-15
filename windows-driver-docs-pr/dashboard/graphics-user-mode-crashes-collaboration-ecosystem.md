---
title: Crashes in communication and collaboration apps (ecosystem)
description: The measure aggregates telemetry from a 7-day sliding window a ratio of crashes in communication and collaboration applications, caused by the graphics drivers, over total runtime in years (Ecosystem)
ms.topic: article
ms.date: 09/03/2021
---

# Crashes in communication and collaboration apps (ecosystem)

## Description

This measure counts the number of crashes in display drivers that happen in the context of communication and collaboration applications and calculates the runtime of such applications on all machines that have the updated driver. The measure then normalizes the crash count by cumulative application runtime in years (HOART - hit over application runtime)

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

This is the ecosystem counterpart of [Crashes in communication and collaboration apps normalized by usage <= baseline goal](./graphics-user-mode-crashes-collaboration-standard.md) measure.

## Measure attributes

| Attribute | Value |
|--|--|
| **Audience** | Ecosystem |
| **Time period** | 7-day sliding window |
| **Measurement criteria** | Aggregation of communication and collaboration application runtime in Years |
| **Minimum population** | 10,000 hours of communication and collaboration application runtime |
| **Passing criteria** | <= 1 crash per Year of cumulative runtime |
| **Measure ID** | 25912731 |

## Calculation

The measure aggregates telemetry from a 7-day sliding window into the ratio of crashes in Microsoft Edge Chromium, caused by the graphics drivers, over total runtime in years

Total Edge Chromium crashes = Count(Edge Chromium crashes on machines that have the driver)

Total Edge Chromium runtime = Sum(Edge Chromium runtime for each machine that has the driver)

Runtime in years = Total Edge Chromium runtime∗60 (minute)∗ 60 (hour)∗24 (day)∗365 (year)

### Final Calculation

Crashes in Edge Chromium normalized by usage = total Edge Chromium crashes / runtime in years
