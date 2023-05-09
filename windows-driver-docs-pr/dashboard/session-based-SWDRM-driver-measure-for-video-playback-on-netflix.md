---
title: Session based SWDRM Driver measure for Video playback on Netflix 
description: This session-based Software DRM Driver measure is used to capture the percentage of sessions that have an error during video playback on Netflix while using software DRM.
ms.topic: article
ms.date: 01/19/2023
---

#  Percentage of devices with SWDRM playback that triggered the Catalog reload event

## Description

This session-based Software DRM Driver measure is used to capture the percentage of sessions that have an error during video playback on Netflix while using software DRM. DRM (Digital Rights Management) techniques (Software or Hardware) are used during Video Playback on windows devices. More information about DRM can be found at Digital Rights Management - Windows drivers | Microsoft Docs.

More information about DRM can be found at [Digital Rights Management - Windows drivers | Microsoft Docs](/windows-hardware/drivers/audio/digital-rights-management).

## Measure attributes

| Attribute | Value |
|--|--|
| **Audience** | This session-based Software DRM Driver measure is used to capture the percentage of sessions that have an error during video playback on Netflix while using software DRM. |
| **Time period** | Daily |
| **Measurement criteria** | Percent of sessions with errors |
| **Minimum population** | 500 sessions |
| **Passing criteria** | >=99% of sessions do not have any errors during playback|
| **Measure ID** | 43952495 |

## Calculation

1. The measure is computed daily. Each row corresponds to a device and provides information about the session failure percentage (metric value) and the session count (instance count).
2. This information is then directly input to Mission control after leveraging the graphics BYOD modules which adds additional GPU related columns.