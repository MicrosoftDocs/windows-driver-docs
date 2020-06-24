---
title: Number of user mode crashes in Communication and Collaboration Applications normalized by usage <= Baseline goal
description: The measure aggregates telemetry from a 7-day sliding window a ratio of crashes in Communication and Collaboration Applications, caused by the graphics drivers, over total runtime in years
ms.topic: article
ms.date: 05/11/2020
ms.localizationpriority: medium
---

# Number of user mode crashes in Communication and Collaboration Applications normalized by usage <= Baseline goal

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

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Devices targeted by the driver|
|**Time period**|7-day sliding window|
|**Measurement criteria**|Aggregation of Communication and Collaboration Application runtime in Years|
|**Minimum population**|10,000 hours of Communication and Collaboration Application runtime|
|**Passing criteria**|<= 1 crash per Year of cumulative runtime|
|**Measure ID**|25912714|

## Calculation

Ratio of Crashes in Communication and Collaboration Applications, caused by the graphics drivers, over total runtime in years

Total Crashes in Communication and Collaboration Applications= Count(Crashes in Communication and Collaboration Applications on machines that have the driver)

Total Communication and Collaboration Applications Runtime= Sum(Runtime of Communication and Collaboration Applications, for each machine that has the driver)

Runtime in Years=Total Runtime of Communication and Collaboration Applications∗60 (minute)∗ 60 (hour)∗24 (day)∗365 (year)

### Final Calculation

Crashes in Communication and Collaboration Applications normalized by usage in years=Total Crashes in Communication and Collaboration Applications / Runtime in Years
