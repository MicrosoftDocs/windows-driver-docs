---
title: Percent of Camera preview failures
description: The measure aggregates telemetry from a 7-day sliding window into a percentage of instances where a camera device failed to use the preview feature
ms.topic: article
ms.date: 05/20/2019
---

# Percent of Camera preview failures

## Description

When attempting to capture an image, the device previews the image that is about to be captured. If the preview feature fails, the user will be unable to see the camera’s perspective and might not be able to capture an image to save as a photo.

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Standard|
|**Time period**|7 day sliding window|
|**Measurement criteria**|Aggregation of instances|
|**Minimum population**|10 instances|
|**Passing criteria**|<=8 % of preview Instances result in a failure|
|**Measure ID**|16998893|

## Calculation

1. The measure aggregates telemetry from a 7-day sliding window into a **percentage of instances where a camera device failed to use the preview feature**.

   a. A single device can have multiple preview instances counted by the measure.

2. Types of Instances:

   a. *Successful preview event = 0% failure*

```cpp
MFCaptureEngineOnEvent (MF_CAPTURE_ENGINE_PREVIEW_STARTED) HRESULT == 0
MFCaptureEnginePreviewSinkFirstFrame (MF_CAPTURE_ENGINE_PREVIEW_STARTED)
```

   b. *Failed preview event = 100% failure*

```cpp
MFCaptureEngineOnEvent (MF_CAPTURE_ENGINE_PREVIEW_STARTED) HRESULT != 0
```

**OR** a successful preview event followed by:

```cpp
MFCaptureEngineOnEvent (MF_CAPTURE_ENGINE_ERROR)
MFCaptureEngineOnEvent (MF_CAPTURE_ENGINE_PREVIEW_STOPPED) > 1000ms
MFCaptureEngineOnEvent (MF_CAPTURE_ENGINE_PREVIEW_STARTED) HRESULT != 0
```

### Final calculation

*Camera preview failure rate = average(all instances)*
