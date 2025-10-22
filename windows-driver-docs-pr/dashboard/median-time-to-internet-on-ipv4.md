---
title: Median Time to Internet on IPv4
description: The measure aggregates telemetry from a 7-day sliding window into a median time it takes for a device to obtain internet connectivity after ethernet detection.
ms.date: 10/20/2005
ms.topic: concept-article
---

# Median Time to Internet on IPv4

## Description

Users want to consistently connect to the Internet via Ethernet within a reasonable time. This measure calculates median time it takes for a device to obtain internet connectivity after ethernet detection.

## Measure attributes

| Attribute | Value |
|--|--|
| **Audience** | Standard |
| **Time period** | 7 days |
| **Machine vs. Instance** | Instance |
| **Minimum instances** | 100 instances |
| **Passing criteria** | Median (P50) <= 4 seconds |
| **Measure ID** | 55883582 |

## Calculation

This measure determines the time it takes from Ethernet detection to achieve Internet gain. Specifically, it measures the time from DHCP MediaConnected to NCSI CapabilityChange telemetry events. The measure calculates median time taken for internet connectivity through ethernet.
