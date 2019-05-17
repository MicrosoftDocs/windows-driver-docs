---
title: Percent of HWDRM playback failures on Netflix
description: The measure aggregates telemetry from a 7-day sliding window into a percent of HWDRM playback errors in Netflix
ms.topic: article
ms.date: 05/20/2019
ms.author: paslote
author: parkeratmicrosoft
ms.localizationpriority: medium
---

# Percent of HWDRM playback failures on Netflix

## Description

Hardware Digital Rights Management (HWDRM) is a feature that enable secure playback of High Definition and Ultra High Definition content on multiple device platforms. This feature protects digital keys – like private keys and content keys – and decrypted compressed & uncompressed videos. An HWDRM failure causes the user to be unable playback videos on certain services, such as Netflix.

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Ecosystem|
|**Time period**|7-day sliding window|
|**Measurement criteria**|Aggregation of instances|
|**Minimum instances**|200 Netflix playbacks|
|**Passing criteria**|<= 2% of Netflix playbacks have a HWDRM failure|
|**Measure ID**|19170127|

## Calculation

1. The measure aggregates telemetry from a 7-day sliding window into a **percent of HWDRM playback errors in Netflix**.

   a. *Playback failure = \<video>.error element is populated on Netflix videos*
2. *Netflix HWDRM playback failures = count(playback failures)*
3. *Total Netflix videos = count(\<video> elements on Netflix)*

### Final calculation

*Percent of HWDRM Netflix playback errors = Netflix HWDRM playback failures / total Netflix videos*
