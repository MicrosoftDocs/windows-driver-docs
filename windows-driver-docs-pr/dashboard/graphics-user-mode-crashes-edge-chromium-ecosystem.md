---
title: User mode crashes in Microsoft Edge Chromium normalized by usage <= baseline goal (ecosystem)
description: The measure aggregates telemetry from a 7-day sliding window a ratio of crashes in Microsoft Edge Chromium, caused by the graphics drivers, over total runtime in years (ecosystem)
ms.topic: article
ms.date: 09/02/2021
ms.localizationpriority: medium
---

# User mode crashes in Microsoft Edge Chromium normalized by usage <= baseline goal (ecosystem)

## Description

When users are browsing the internet with Edge Chromium, their graphics components will process visual data from the Web and display the rendered view on the user's screen. This measure is monitoring how often Edge Chromium crashes due to graphics driver, in relation to the Edge Chromium runtime on all devices with the driver. If Edge Chromium crashes, the user must wait for the application to recover before being able to use it again.  

This is the ecosystem counterpart of [User mode crashes in Microsoft Edge Chromium normalized by usage <= baseline goal](./graphics-user-mode-crashes-edge-chromium-standard.md) measure.

## Measure attributes

| Attribute | Value |
|--|--|
| **Audience** | Ecosystem |
| **Time period** | 7-day sliding window |
| **Measurement criteria** | Aggregation of instances |
| **Minimum population** | 30,000 hours of Microsoft Edge Chromium runtime |
| **Passing criteria** | <= 1 crash per year |
| **Measure ID** | 25389120 |

## Calculation

The measure aggregates telemetry from a 7-day sliding window into the ratio of crashes in Microsoft Edge Chromium, caused by the graphics drivers, over total runtime in years

Total Edge Chromium crashes = Count(Edge Chromium crashes on machines that have the driver)

Total Edge Chromium runtime = Sum(Edge Chromium runtime for each machine that has the driver)

Runtime in years = total Edge Chromium runtime ∗ 60 (minute) ∗ 60 (hour) ∗ 24 (day) ∗ 365 (year)

### Final Calculation

Crashes in Edge Chromium normalized by usage = total Edge Chromium crashes / runtime in years
