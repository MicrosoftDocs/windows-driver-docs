---
title: Number of user mode crashes in Communication and Collaboration Applications normalized by usage <= Baseline goal (Ecosystem)
description: The measure aggregates telemetry from a 7-day sliding window a ratio of crashes in Communication and Collaboration Applications, caused by the graphics drivers, over total runtime in years (Ecosystem)
ms.topic: article
ms.date: 05/11/2020
ms.localizationpriority: medium
---

# Number of user mode crashes in Communication and Collaboration Applications normalized by usage <= Baseline goal (Ecosystem)

## Description

This measure is counting the number of crashes in Display Drivers that happen in the context of the Communication and Collaboration Applications and calculating the runtime of such applications on all machines that have the updated driver. The measure then normalizes the crash count by cumulative application runtime in years (HOART - hit over application runtime)

Examples of Communication and Collaboration applications considered for this measure:

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

This is the ecosystem counterpart of [Number of user mode crashes in Communication and Collaboration applications normalized by usage <= Baseline goal](./graphics-user-mode-crashes-collaboration-standard.md) measure.

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Ecosystem|
|**Time period**|7-day sliding window|
|**Measurement criteria**|Aggregation of Communication and Collaboration Application runtime in Years|
|**Minimum population**|10,000 hours of Communication and Collaboration Application runtime|
|**Passing criteria**|<= 1 crash per Year of cumulative runtime|
|**Measure ID**|25912731|

## Calculation

The measure aggregates telemetry from a 7-day sliding window into the Ratio of Crashes in Microsoft Edge Chromium, caused by the graphics drivers, over total runtime in years

Total Edge Chromium Crashes=Count(Edge Chromium crashes on machines that have the driver)

Total Edge Chromium Runtime=Sum(Edge Chromium runtime for each machine that has the driver)

Runtime in Years=Total Edge Chromium Runtime∗60 (minute)∗ 60 (hour)∗24 (day)∗365 (year)

### Final Calculation

Crashes in Edge Chromium Normalized by Usage=Total Edge Chromium Crashes / Runtime in Years
