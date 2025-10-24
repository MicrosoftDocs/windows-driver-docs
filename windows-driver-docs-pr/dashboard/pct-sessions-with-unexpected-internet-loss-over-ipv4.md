---
title: Percentage of Sessions with unexpected Internet loss over IPv4
description: The measure aggregates telemetry from a seven-day sliding window into a percentage of instances where there are unexpected disconnects
ms.date: 10/20/2005
ms.topic: concept-article
---

# Percentage of Sessions with unexpected Internet loss over IPv4

## Description

Once a device successfully establishes a IPv4 and connects to Internet, the user should expect a stable connection with little to no Internet loss.

## Measure attributes

| Attribute | Value |
|--|--|
| **Audience** | Standard |
| **Time period** | 7 days |
| **Machine vs. Instance** | Instance |
| **Minimum instances** | 100 instances |
| **Passing criteria** | <= 3% of instances end up with unexpected disconnects |
| **Measure ID** | 55883614 |

## Calculation

This measure calculates the percentage of instances, aggregated per device, that have at least one unexpected Internet loss. Internet loss occurs after Internet connectivity is established,
when the Network Connectivity Status Indicator (NCSI) CapabilityChange event is fired during a Dynamic Host Configuration Protocol (DHCP) connectivity session and the previous capability was Internet.
