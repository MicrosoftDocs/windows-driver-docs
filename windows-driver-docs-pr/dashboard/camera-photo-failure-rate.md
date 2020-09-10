---
title: Percent of Camera photo capture failures
description: The measure aggregates telemetry from a 7-day sliding window in a percentage of instances where a camera device failed to use the photo feature
ms.topic: article
ms.date: 05/20/2019
ms.localizationpriority: medium
---

# Percent of Camera photo capture failures

## Description

To capture the camera’s preview into memory, the user can take a photo and store it on their machine. If the photo-taking process fails, the user will not be able to capture the desired image.

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Standard|
|**Time period**|7 day sliding window|
|**Measurement criteria**|Aggregation of instances|
|**Minimum population**|10 instances|
|**Passing criteria**|<=5% of photo taking Instances result in a failure|
|**Measure ID**|16998997|

## Calculation

1. The measure aggregates telemetry from a 7-day sliding window in a **percentage of instances where a camera device failed to use the photo feature**.

     a. A single device can have multiple Photo Instances counted by the measure

2. Types of Instance

   a. *Successful photo event = 0% failure*

```cpp
i. MFCaptureEngineOnEvent (MF_CAPTURE_ENGINE_PHOTO_TAKEN)

ii. MFCaptureEngineOnEvent (MF_CAPTURE_ENGINE_PHOTO_SEQUENCE_STARTED)
```

b. Failed photo event = 100% failure

```cpp
i. MFCaptureEngineOnEvent (MF_CAPTURE_ENGINE_PHOTO_TAKEN) HRESULT !=0

ii. MFCaptureEngineOnEvent (MF_CAPTURE_ENGINE_PHOTO_SEQUENCE_STARTED) HRESULT !=0

iii. Timed Out
```

### Final calculation

*Camera photo failure rate = average (all instances)*
