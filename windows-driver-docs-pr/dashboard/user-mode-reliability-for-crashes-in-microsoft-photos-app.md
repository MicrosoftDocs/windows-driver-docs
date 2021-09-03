---
title: Reliability for crashes in Microsoft Photos app less than or equal to the baseline goal (ecosystem)
description: Learn about the measure that counts the number of display driver crashes in the Microsoft Photos app, then normalizes the total runtime to years.
ms.topic: article
ms.date: 09/02/2021
ms.localizationpriority: medium
---

# Reliability for crashes in Microsoft Photos app less than or equal to the baseline goal (ecosystem)

## Description

This measure counts the number of crashes in display drivers that happen in the context of the Microsoft Photos application and calculates the runtime of Microsoft Photos on all machines that have the updated driver. The measure then normalizes the total runtime to years, indicating the number of crashes a user would experience if they used Microsoft Photos for a year.

## Measure attributes

| Attribute | Value |
|--|--|
| **Audience** | Ecosystem |
| **Time period** | 7-day sliding window |
| **Measurement criteria** | Aggregation of instances |
| **Minimum instances** | 10,000 hours of Microsoft Photos runtime |
| **Passing criteria** | <= 1.5 crashes per year of runtime |
| **Measure ID** | 20240794 |

## Calculation

1. The measure aggregates telemetry from a 7-day sliding window into a ratio of crashes in Microsoft Photos, caused by the graphics drivers, over total runtime in years.
1. Total crashes in Microsoft Photos app = count(crashes in Microsoft Photos on machines that have the driver)
1. Total Microsoft Photos runtime = sum(runtime of Microsoft Photos, for each machine that has the driver)
1. Runtime in years = total runtime of Microsoft Photos \* 60 (minute) \* 60 (hour) \* 24 (day) \* 365 (year)

### Final calculation

Crashes in Microsoft Photos normalized by usage in years = total crashes in Microsoft Photos / runtime in years
