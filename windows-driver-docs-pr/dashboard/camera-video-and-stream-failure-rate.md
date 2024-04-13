---
title: Percent of Camera video and stream failures
description: The measure aggregates telemetry from a 7-day sliding window into a percentage of instances where a camera device failed to use the video and streaming feature
ms.topic: article
ms.date: 05/20/2019
---

# Percent of Camera video and stream failures

## Description

To capture a camera’s video stream, the machine must continuously store the machines perspective into a video file. If the video and streaming feature fails, the user will not be able to capture the camera’s perspective and can lose video that has not been saved.

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Standard|
|**Time period**|7 day sliding window|
|**Measurement criteria**|Aggregation of instances|
|**Minimum population**|10 instances|
|**Passing criteria**|<=10% of Video and Streaming Instances result in a failure|
|**Measure ID**|16999057|

## Calculation

1. The measure aggregates telemetry from a 7-day sliding window into a **percentage of instances where a camera device failed to use the video and streaming feature**.

   a. A single device can have multiple Video & Streaming Instances counted by the measure.

2. Types of Instances:

   a. *Successful video and streaming event = 0% failure*  

```cpp
MFCaptureEngineOnEvent (MF_CAPTURE_ENGINE_RECORD_STARTED)
```

   b. *Failed video and streaming event = 100% failure*

```cpp
i. MFCaptureEngineOnEvent (MF_CAPTURE_ENGINE_ERROR)
ii. MFCaptureEngineOnEvent (MF_CAPTURE_ENGINE_RECORD_STOPPED)
iii. MFCaptureEngineSessionStop
iv. OnEvent_RecordStop_Failure
v. Timed Out
```

### Final calculation

*Camera video and stream failure rate = average(all instances)*
