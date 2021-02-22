---
title: Number of user mode crashes in Microsoft Edge Chromium normalized by usage <= Baseline goal
description: The measure aggregates telemetry from a 7-day sliding window a ratio of crashes in Microsoft Edge Chromium, caused by the graphics drivers, over total runtime in years
ms.topic: article
ms.date: 05/11/2020
ms.localizationpriority: medium
---

# Number of user mode crashes in Microsoft Edge Chromium normalized by usage <= Baseline goal

## Description

When users are browsing the internet with Edge Chromium, their graphics components will process visual data from the Web and display the rendered view on the user’s screen. This measure is monitoring how often Edge Chromium crashes due to graphics driver, in relation to the Edge Chromium runtime on all devices with the driver. If Edge Chromium crashes, the user must wait for the application to recover before being able to use it again.  

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Devices targeted by the driver|
|**Time period**|7-day sliding window|
|**Measurement criteria**|Aggregation of instances|
|**Minimum population**|30,000 hours of Microsoft Edge Chromium runtime|
|**Passing criteria**|<= 1 crash per year|
|**Measure ID**|25481659|

## Calculation

The measure aggregates telemetry from a 7-day sliding window into the Ratio of Crashes in Microsoft Edge Chromium, caused by the graphics drivers, over total runtime in years

Total Edge Chromium Crashes=Count(Edge Chromium crashes on machines that have the driver)

Total Edge Chromium Runtime=Sum(Edge Chromium runtime for each machine that has the driver)

Runtime in Years=Total Edge Chromium Runtime∗60 (minute)∗ 60 (hour)∗24 (day)∗365 (year)

### Final Calculation

Crashes in Edge Chromium Normalized by Usage=Total Edge Chromium Crashes / Runtime in Years
