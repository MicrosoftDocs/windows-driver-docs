---
title: Success rate of Fingerprint Sign-in Experience
description: The measure tracks the user experience of logging in with a fingerpring sensor.
ms.topic: article
ms.date: 03/13/2020
---
 
# Success rate of Fingerprint Sign-in Experience

## Description 

When a user has enrolled in Windows Hello fingerprint a credential provider will enumerate on the lock screen to capture the user’s fingerprint gesture. If the user touches their sensor, a sample will be collected, and it will be compared with the fingerprint templates enrolled on the device. If the there are three attempts in an unlock session where the collected sample does not match an enrolled template, then fingerprint is temporarily locked out until the user unlocks with a different credential. If the biometric sensor fails the user will also be blocked from using it to unlock. 

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Retail and Insider|
|**Time period**|7 days sliding window|
|**Measurement criteria**|Aggregation of machines|
|**Minimum instances**|50|
|**Passing criteria**|>= 90%|
|**Measure ID**|19554065|

## Calculation

1. This measure aggregates telemetry from a 7-day sliding window.
2. A success rate for fingerprint sign-in experience is calculated per-machine in the window.
    1. If a user on the device has enrolled fingerprint, every unlock session generates an event from the fingerprint credential provider with a result. 
    2. Sessions with specific benign results are filtered. The following cases are filtered out:
        1. NoFPEnrollments – The user that signed in did not have a fingerprint enrolled.
        2. BUMissingNoEnrollments – No fingerprint sensors are enumerated by the biometric framework and the user has no fingerprint enrollments. 
        3. BioDeviceNotAttached – No FP sensors are attached to the machine. This is for the case of external, removable sensors.
        4. NoFPLogonAttempts – User did not attempt to sign in with fingerprint and used another credential provider to log on.
        5. TriedFPUsedOtherProvider – User attempted fingerprint but used another credential provider to log in. The user did not lock out the fingerprint credential provider.
    3. The number of success sessions is divided by the total remaining sessions. 
3. An average is calculated across the success rate all machines.

## Final Calculation
Fingerprint logon success rate = average(all instances)
