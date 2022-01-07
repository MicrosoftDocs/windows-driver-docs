---
title: Percent of YouTube video playback failures in Microsoft Edge and Internet Explorer
description: The measure aggregates telemetry from a 7-day sliding window into a percent of YouTube playback errors in Microsoft Edge or Internet Explorer
ms.topic: article
ms.date: 05/20/2019
---

# Percent of YouTube video playback failures in Microsoft Edge and Internet Explorer

## Description

When users watch YouTube videos with Microsoft Edge or Internet Explorer, their graphics components process video stream from the Web and display the rendered video on the screen. This measure monitors how often YouTube videos fail to playback in Microsoft Edge; if the user encounters a playback failure, they will be unable to load and watch the video.

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Standard |
|**Time period**|7-day sliding window|
|**Measurement criteria**|Aggregation of instances|
|**Minimum instances**|50 YouTube playbacks|
|**Passing criteria**|<= 1% of YouTube video elements have a \<video>.error property|
|**Measure ID**|6195478|

## Calculation

1. The measure aggregates telemetry from a 7-day sliding window into a **percent of YouTube playback errors in Microsoft Edge or Internet Explorer**.
2. *Session = single instance of loading a YouTube media resource into an HTML5 \<video> element*

   a. A single machine can have multiple sessions.

3. Playback failures = count(YouTube \<video>.error elements encountered in Microsoft Edge or Internet Explorer)

### Final calculation

*Percent of Microsoft Edge or Internet Explorer YouTube HTML5 playback failures = Playback failures / count(sessions)*
