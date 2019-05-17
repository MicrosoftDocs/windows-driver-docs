---
title: Percent of machines with video HWDRM failures
description: The measure aggregates telemetry from a 7-day sliding window into a percent of machines with an HWDRM video playback failure
ms.topic: article
ms.date: 05/20/2019
ms.author: paslote
author: parkeratmicrosoft
ms.localizationpriority: medium
---

# Percent of machines with video HWDRM failures

## Description

Hardware Digital Rights Management (HWDRM) is a feature that enables secure playback of High Definition and Ultra High Definition content on multiple device platforms. This feature protects key material (private keys, content keys, and others), and decrypted, compressed, and uncompressed videos. An HWDRM failure causes the user to be unable playback videos on certain services, like Netflix.

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Standard HWID/CHID targeting|
|**Time period**|7-day sliding window|
|**Measurement criteria**|Aggregation of instances|
|**Minimum instances**|300|
|**Passing criteria**|<= 5% of machines have HWDRM failures|
|**Measure ID**|16236389|

## Calculation

1. The measure aggregates telemetry from a 7-day sliding window into a **percent of machines with an HWDRM video playback failure**.

   a. *Playback failure = \<video>.error element is populated on HTML5 videos*

2. *WDRM playback failures = count(playback failures)*
3. *Total machines = count(machines that initiated a HWDRM playback)*

### Final calculation

*Percent of machines with HWDRM playback failures = HWDRM playback failures / total machines*
