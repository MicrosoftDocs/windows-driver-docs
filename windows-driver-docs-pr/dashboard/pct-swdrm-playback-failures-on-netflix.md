---
title: Percent of SWDRM playback failures on Netflix
description: The measure aggregates telemetry from a 7-day sliding window into a percent of SWDRM playback errors in Netflix
ms.topic: article
ms.date: 05/20/2019
ms.localizationpriority: medium
---

# Percent of SWDRM playback failures on Netflix

## Description

Software Digital Rights Management (SWDRM) is a feature that enable the content distributor to control how the content is used. This feature protects digital keys – like private keys and content keys – and decrypted compressed & uncompressed videos. A SWDRM failure causes the user to be unable playback videos on certain services, like Netflix.

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Ecosystem|
|**Time period**|7-day sliding window|
|**Measurement criteria**|Aggregation of instances|
|**Minimum instances**|200 Netflix playbacks|
|**Passing criteria**|<= 1% of Netflix playbacks have a SWDRM failure|
|**Measure ID**|19170139|

## Calculation

1. The measure aggregates telemetry from a 7-day sliding window into a **percent of SWDRM playback errors in Netflix**.

   a. *Playback failure= \<video>.error element is populated on Netflix Videos*

2. *Netflix SWDRM playback failures = count(playback failures)*
3. *Total Netflix videos = count(\<video> elements on Netflix)*

### Final calculation

*Percent of SWDRM Netflix playback errors = Netflix SWDRM playback failures / Total Netflix videos*
