---
title: UDDP Audio - Percent of machines with at least one APO disablement in past seven days
description: When Audio APOs crash at least 10 times consecutively, the Audio service disables the APO's further usage in order for the suer to have an error free sound experience. This may result in our Audio Crash measure failing for some time on the driver submission and then start to pass again when the APO causing the issue in that driver submission gets disabled. This measure keeps track of the APO disablements in the past 7 days compared to the devices using audio in that day (Audio Client Initialize event)
ms.topic: article
ms.date: 01/19/2023
---

# Percent of machines with at least one APO disablement in past 7 days

## Description

When Audio APOs crash at least 10 times consecutively, the Audio service disables the APO's further usage in order for the suer to have an error free sound experience. This may result in our Audio Crash measure failing for some time on the driver submission and then start to pass again when the APO causing the issue in that driver submission gets disabled. This measure keeps track of the APO disablements in the past 7 days compared to the devices using audio in that day (Audio Client Initialize event).
## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Windows machiens that have an audio APO|
|**Time period**|Each day's failure rate includes APO disablements from the past 7 days|
|**Machine vs. Instance**|Machine|
|**Passing criteria**|<=0.1 % of machines have an APO disablement in the past 7 days|
|**Measure IDs**|41929221|

## Calculation

Every day:
1. We collect all APO disablements from the EndpointCharacteristics.SystemEffectAPOsDisabled event from past 7 days. We join with DeviceGraph.AudioProcessingObjectInfo information on DeviceId and EndpointInstanceId to get module information on all the composite effect modules (stream, mode, endpoint, etc) in the devices.
2. We count the number of devices that have experienced Audio Client Init events in that day (used sound).
3. We express that as a percentage of all devices that experienced APO disablements for past 7 days each day.