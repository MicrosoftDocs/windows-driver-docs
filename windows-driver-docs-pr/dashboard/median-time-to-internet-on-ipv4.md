---
title: Median Time to Internet on IPv4
description: The measure aggregates telemetry from a 7-day sliding window into a median time it takes for a device to obtain internet connectivity after ethernet detection.
ms.date: 10/20/2005
ms.topic: concept-article
---

# Median Time to Internet on IPv4

Reliable internet connectivity is essential for modern computing, especially in enterprise and managed environments where Ethernet is the preferred connection type. The Median Time to Internet on IPv4 measure helps assess how quickly devices establish internet access after detecting a wired network. By tracking this timing across devices, Microsoft can identify performance trends, detect regressions, and guide improvements in driver behavior and network stack responsiveness.

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
