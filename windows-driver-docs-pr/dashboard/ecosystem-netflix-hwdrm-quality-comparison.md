---
title: Ecosystem Netflix HWDRM Quality Comparison
description: The measure aggregates telemetry from a 90 day sliding window into a binary value (0 or 1), indicating if the driver performance is within 2 standard deviations of the aggregate performance of all drivers from the same IHV in the retail market
ms.topic: article
ms.date: 12/20/2019
---

# Ecosystem Netflix HWDRM Quality Comparison

## Description

Hardware Digital Rights Management (HWDRM) is a feature that enables secure playback of High Definition and Ultra High Definition content on multiple device platforms. This feature protects digital keys – like private keys and content keys – and compressed & uncompressed video and audio. A HWDRM failure causes the user to be unable to playback videos on video streaming services, such as Netflix. Drivers whose session failure rate is less than or equal to 2%, pass. Those drivers with session failure rates higher, fail.

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Ecosystem|
|**Time period**|90-day sliding window|
|**Measurement criteria**|Aggregation of session instances|
|**Minimum population**|500 sessions|
|**Passing criteria**|Driver session failure rate less than or equal to 2.0|
|**Measure ID**|v1. 19170127 (Legacy), v2. 44233379|

## Calculation

1.	Inputs: 90 days of HWDRM playback results, from Media Foundation telemetry.  This telemetry tells Microsoft whether a DRM video playback attempt resulted in an error (playback failure) or not (playback success). 
2.	The following filters are used to produce a clean and trustworthy dataset for measurement: 
	*	Retail builds only, plus latest insider OS (filtered in)
		*	Removing the vnext++ OS removes potential instability from the OS
	*	Netflix app and Netflix in Edge only (filtered in)
		*	Removing other services removes potential instability from other services that are working on adopting HWDRM
	*	pre-production devices (filtered out)
		*	removes potentially invalid device configurations 
	*	Devices with only a single GPU (filtered out)
		*	Ensures we are only measuring results each IHV separately. 
	*	Sessions that resulted in expected error codes are filtered out.  Expected error codes are those that are by-design and are very unlikely to be attributed to an OS or driver bug.  These are reviewed quarterly. Many error codes may be expected but are accommodated for by setting the pass/fail threshold at 2% rather than being filtered out.  This allows us to monitor the rates of those error codes within the threshold. 
3.	Additionally, outlying devices are identified and filtered out based on the following metrics.  This removes devices that could skew results (positively or negatively) in the final dataset used for measurement.  Devices are filtered out if the metric result for that device is within the specified percentile criteria: 
	*	Session count per device over the 90-day period: >= 95th percentile
	*	Number of days with sessions over the 90-day period: >= 97.5th percentile
	*	Average number of sessions per day, for days with sessions, over the 90-day period: >= 97.5th percentile
	*	The failure rate for all sessions on the device over the 90-day period: >= 95th percentile

### Final Calculation
*FailureRate = 100.0 * Count(Failed Sessions) / Count(Total Sessions)*
