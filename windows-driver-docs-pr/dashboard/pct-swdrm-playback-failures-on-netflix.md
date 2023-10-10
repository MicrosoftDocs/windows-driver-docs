---
title: Percent of SWDRM playback failures on Netflix
description: The measure aggregates telemetry from a 90-day sliding window into a percent of SWDRM playback errors in video services
ms.topic: article
ms.date: 12/20/2019
---

# Percent of SWDRM playback failures on Netflix

## Description

Software Digital Rights Management (SWDRM) is a feature that enable the content distributor to control how the content is used. This feature protects digital keys – like private keys and content keys – and decrypted compressed & uncompressed videos. A SWDRM failure causes the user to be unable playback videos on certain services, like Netflix.  Drivers whose session failure rate is less than or equal to 1%, pass. Those drivers with session failure rates higher, fail.

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Ecosystem|
|**Time period**|90-day sliding window|
|**Measurement criteria**|Aggregation of session instances|
|**Minimum instances**|25 devices|
|**Passing criteria**|Driver session failure rate less than or equal to 2.0|
|**Measure ID**| 44233392|

## Calculation

1.	Inputs: 90 days of SWDRM playback results, from Media Foundation telemetry.  This telemetry tells Microsoft whether a DRM video playback attempt resulted in an error (playback failure) or not (playback success). 
2.	The following filters are used to produce a clean and trustworthy dataset for measurement: 
    *	Retail builds only, plus latest insider OS (filtered in)
        *	Removing the vnext++ OS removes potential instability from the OS
    *	Netflix app and Netflix in Edge only (filtered in)
        *	Removing other services removes potential instability from other services 
    *	pre-production devices (filtered out)
        *	removes potentially invalid device configurations 
    *	Devices with only a single GPU (filtered out)
        *	Ensures we are only measuring results each IHV separately. 
3.	Additionally, outlying devices are identified and filtered out based on the following metrics.  This removes devices that could skew results (positively or negatively) in the final dataset used for measurement.  Devices are filtered out if the metric result for that device is within the specified percentile criteria: 
    *	Session count per device over the 90-day period: >= 95th percentile
    *	Number of days with sessions over the 90-day period: >= 97.5th percentile
    *	Average number of sessions per day, for days with sessions, over the 90-day period: >= 97.5th percentile
    *	The failure rate for all sessions on the device over the 90-day period: >= 95th percentile


### Final calculation

*FailureRate = 100.0 * Count(Failed Sessions) / Count(Total Sessions)*
